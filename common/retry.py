"""重试退避:用 tenacity防止瞬态故障导致整个任务失败。"""
from tenacity import(  #导入tenacity的核心构件
    retry,             #装饰器本体
    stop_after_attempt,#停止条件:最多试N次
    wait_exponential,  #等待策略:指数退避(1s,2s,4s···)
    retry_if_exception_type, #只重试指定异常类型
    before_sleep_log,        #每次重试前打日志
)
import logging

logger = logging.getLogger('zhiassist.retry')

#定义一个可重试的网络异常(示例;真实场景用requests.ConnectionError等)
class TransientError(Exception):
    """瞬态错误:重试可能成功"""

#组合成一个可复用的装饰器
retry_on_transient = retry(
    stop=stop_after_attempt(3),#最多8次
    wait=wait_exponential(multiplier=1,min=1,max=8),#等1s->2s->4s上限8s
    retry=retry_if_exception_type(TransientError),#只对TransientError重试，别乱重试
    before_sleep=before_sleep_log(logger,logging.WARNING),#重试前打警告日志
    reraise=True, #3次都失败就抛出原异常，不包装
)


@retry_on_transient
def flaky_call(should_fail_times:int) -> str:
    """演示用:前N次抛异常,之后成功
    
    参数：
        should_fail_times:前几次调用故意失败。
    返回：
        成功时返回字符串。
    """
    global _call_count
    _call_count += 1
    if _call_count <= should_fail_times:
        raise TransientError(f"第{_call_count}次调用失败")
    return f"第{_call_count}次调用成功"

_call_count = 0 #模块级计数器,仅用于演示