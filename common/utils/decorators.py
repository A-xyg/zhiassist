"""
手写装饰器:理解装饰器原理(tenacity就是这类思想的成熟实现)
"""
import time   #计时
from functools import wraps #保留原函数的元信息(名字、文档字符串)
from ..logs import get_logger #复用日志;俩个点=上一级common /目录(logs.py在那)

logger = get_logger("decorators")


def timer(func):
    """计时装饰器:打印函数耗时,不改函数内部逻辑"""
    @wraps(func)   #保留原函数名,便于调试与测试
    def wrapper(*args,**kwargs):
        start = time.perf_counter()     #高精度计时起点
        try:
            return func(*args,**kwargs)  #调用原函数,参数原样透传
        finally:
            cost = time.perf_counter() - start  #无论成功失败都计时
            logger.info("%s耗时%.4f秒",func.__name__,cost)
    return wrapper

def log_call(func):
    """日志装饰器:记录函数名与参数"""
    @wraps(func)
    def  wrapper(*args,**kwargs):
        logger.info("调用%s args=%s kwargs=%s",func.__name__,kwargs)
        return func(*args,**kwargs)
    return wrapper