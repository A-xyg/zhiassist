"""
配置读取与校验
所有模块统一从get_settings()读配置,禁止在业务代码里硬编码连接串或密钥
"""
from functools import lru_cache #缓存装饰器:让get_settings只读一次.venv
from pydantic import Field #Field用于给字段加约束与说明
from pydantic_settings import BaseSettings,SettingsConfigDict
#配置基类

class Settings(BaseSettings):
#应用配置:从.env读取,启动时即校验类型与必填项
#model_config 告诉 pydatic-settings 去哪读配置
    model_config =SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra = "ignore",
)

#应用名 ：默认值，不在.env里也能跑
app_name:str = "zhiassist"
# 日志级别 ：限制只能是这四个值之一，写错启动就报错(这就是[校验])
log_level:str = Field(default="INFO",pattern="^(DEBUG|INFO|WARNING|ERROR)$")

#数据库连接串：无默认值 ==> .env里必须提供，否则启动报错
mysql_dsn:str
#Redis 地址：同上，必填
redis_url:str

#LLM配置
llm_base_url:str ="https://api.example.com/v1"
llm_api_key:str =""
llm_model_primary:str ="placeholder-model"
