"""
python
错误码与异常分层:让上层能按类型捕获不同故障
"""
class AppError(Exception):
    """ 所有业务异常的基类"""

    code: str ="E0000" #默认错误码，子类覆盖
    message: str ="未知错误"

    def __init__(self,message: str | None = None) -> None:
    #允许调用时传更具体的消息,不传就用类默认
        self.message = message or self.message 
        super().__init__(f"[{self.code}] {self.message}")


class ConfigError(AppError):
    """ 配置错误:缺环境变量、环境不对等。"""

    code = "E1001"
    message = "配置错误"

class DatabaseError(AppError):
    """数据库错误:连接失败、SQL执行失败等。"""

    code = "E2001"
    message = "数据库错误"

class CacheError(AppError):
    """缓存错误:Redis 连接失败、超时等。"""

    code ="E3001"
    message = "缓存错误"