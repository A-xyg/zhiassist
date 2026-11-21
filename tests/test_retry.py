"""测试重试装饰器:验证重试次数与最终结果"""
import common.retry as retry_mod #导入模块,便于重置计数器
from common.retry import flaky_call #被测函数


def test_retry_eventually_succeeds():
    """前俩次失败、第三次成功:应返回成功且不抛出异常"""
    retry_mod._call_count = 0  #重置模块级计数器
    result = flaky_call(2)      #前俩次失败
    assert "成功" in result     #断言最终成功
    assert retry_mod._call_count == 3 #断言确实调用了三次