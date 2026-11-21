"""
数据模型示例:会话表(第7章Agent长期记忆的基础)
"""
from sqlalchemy import String,Text,Integer  #列类型
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column #2.x声明式基类
from datetime import datetime,timezone

class Base(DeclarativeBase):
    """所有模型的基类,统一建表元数据"""
    pass


class SessionRecord(Base):
    """一次对话会话的记录"""

    __tablename__ = "session_records"       #表名

    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    session_id:Mapped[str] = mapped_column(String(64),index=True)   #索引:按会话查的快
    role:Mapped[str] = mapped_column(String(16))      #user /assistant
    content:Mapped[str] = mapped_column(Text)       #正文,Text支持长文本
    created_at:Mapped[datetime] = mapped_column(default=lambda:datetime.now(timezone.utc))
     