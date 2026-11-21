"""统一日志:控制台+文件双输出,按天轮转。"""
import logging #python标准日志模块
from logging.handlers import TimedRotatingFileHandler #按时间轮转的处理器
from pathlib import Path   #跨平台路径处理


def setup_logging(level:str = "INFO",log_dir:str ="logs") -> logging.Logger:
    """初始化应用日志,返回根logger
    
    参数：
        level:日志级别(DEBUG|INFO|WARNING|ERROR)
        log_dir:日志文件存放目录,相当于当前工作目录
    返回:
        配置好的 logging.Logger对象
    异常:
        无显示异常;目录不存在时自动创建。
    """
    logger = logging.getLogger("zhiassist") #应用专属logger,不污染根logger
    logger.setLevel(level)   #设置最低级别
    logger.handlers.clear()  #防止重复调用时叠加多个handler

    fmt =logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"
    ) #格式： 时间 | 级别 |模块名 | 消息

    console =logging.StreamHandler()  #控制台输出
    console.setFormatter(fmt)
    logger.addHandler(console)

    Path(log_dir).mkdir(parents=True,exist_ok=True) #目录不存在就建，存在不报错
    file_handler = TimedRotatingFileHandler(
        Path(log_dir) / "app.log",
        when = "midnight",  #每天零点轮换
        backupCount=7, #保留7天
        encoding="utf-8", #中文日志不乱码
    )
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger

def get_logger(name:str) -> logging.Logger:
    """ 按模块名取子logger,如get_logger('db')>"""
    return logging.getLogger(f"zhiassist.{name}")
