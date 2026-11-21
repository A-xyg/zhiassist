"""建表脚本:幂等,重复执行不报错"""
from common.db.base import engine   #数据库连接
from common.db.models import Base   #模型元数据


def main() -> None:
    Base.metadata.create_all(bind=engine)
    print("表已创建:",list(Base.metadata.tables.keys()))

if __name__ == "__&#8203;main__":
    main()

