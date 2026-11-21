"""
数据库会话管理:SQLAIchemy 2.x engine + 上下文管理。
"""
from sqlalchemy import create_engine #创建数据库连接池
from sqlalchemy.orm import sessionmaker,Session #会话工厂与类型
from contextlib import contextmanager #自定义上下文管理器
from common.config import get_settings #从配置读连接串

settings = get_settings()           #启动时读一次配置

engine = create_engine(
    settings.mysql_dsn,         #形如mysql+pymysql://user:pwd@host:3306/db
    pool_pre_ping=True,         #每次取连接先ping,避免使用已断开的连接
    echo=False,                 #True会打印所有SQL,调试时打开
)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)


@contextmanager
def get_session() ->Session:
    """
    上下文管理器:进with开会 话,出with自动提交/回滚/关闭
    
    用法:
        with get_session() as db:
        db.add(obj)
    """
    db = SessionLocal() #新建会话
    try:
        yield db        #把会话交给调用方
        db.commit()     #正常退出:提交事务
    except Exception:
        db.rollback()       #异常:回滚,避免脏数据
        raise               #异常继续向上抛,不吞掉
    finally:
        db.close()          #无论成功失败都关闭连接

