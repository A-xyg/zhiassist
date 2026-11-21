"""
Redis 三场景:缓存/会话状态/限流计数
"""
import json         #序列化复杂对象
import redis        #redis-py客户端
from common.config import get_settings #从配置读Redis地址
from common.errors import CacheError    #统一异常

settings = get_settings()
client = redis.Redis.from_url(
    settings.redis_url,     #redis://127.0.0.1:6379/0
    decode_responses = True,    #自动把bytes解码成str,省去手动.decode()
    socket_connect_timeout = 2, #连接超时2秒,避免一直卡住
)

def cached_get(key:str,loader,ttl:int = 60):
    """
    场景1 ·缓存:先查Redis,没有再调loader并写回。

    参数:
        key:缓存键。
        loader:无参数函数,缓存命中时未用他加载数据
        ttl:过期秒数
    返回:
        缓存或加载的数据
    """
    try:
        hit = client.get(key)       #查缓存
        if hit is not None:         #命中
            return json.loads(hit)  #反序列化
        value = loader()            #未命中:加载真实数据
        client.setex(key,ttl,json.dumps(value,ensure_ascii=False))  #写入并设过期
        return value
    except redis.RedisError as exc:
        raise CacheError(f"缓存读写失败:{exc}") from exc  #转成业务异常

def set_session(session_id:str,data:dict,ttl: int = 1800) -> None:
    """场景2·会话状态:30分钟过期,用于多轮对话记忆"""
    client.setex(f"session:{session_id}",ttl,json.dumps(data,ensure_ascii=False))


def get_session(session_id:str) ->dict | None:
    """读取会话状态,不存在返回None"""
    raw = client.get(f"session:{session_id}")
    return json.loads(raw) if raw else None

def allow_request(user_id:str,limit:int = 10, window: int = 60) -> bool:
    """
    场景3·限流计数:60秒内最多limit次请求
    
    实现:INCR计数 + 首次设置EXPIRE,超过阈值返回False
    """
    key = f"ratelimit:{user_id}"
    count = client.incr(key)        #原子自增,天然线程安全
    if count == 1:                  #第一次访问才没有过期时间
        client.expire(key,window)
    return count <= limit