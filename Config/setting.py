# -*- coding: utf-8 -*-


# 数据库配置
from os import getenv


class ConfigError(BaseException):
    pass


DB_TYPE = getenv('db_type', 'SSDB')

if DB_TYPE == 'SSDB':
    DB_HOST = getenv('ssdb_host', '127.0.0.1')
    DB_PORT = getenv('ssdb_port', '6379')
elif DB_TYPE == 'MONGODB':
    DB_HOST = getenv('mongodb_host', '127.0.0.1')
    DB_PORT = getenv('mongodb_host', '27017')
else:
    raise ConfigError('Unknown database type, your environment variable `db_type` should be one of SSDB/MONGODB.')

DATABASES = {
    "default": {
        "TYPE": "SSDB",  # 如果使用SSDB或redis数据库，均配置为SSDB
        "HOST": "127.0.0.1",  # db host
        "PORT": 6379,     # db port
        "NAME": "proxy",  # 默认配置
        "PASSWORD": ""    # db password

    }
}

# 注册代理 获取函数

PROXY_GETTER = [
    "freeProxyFirst",      # 这里是启用的代理抓取函数名，可在ProxyGetter/getFreeProxy.py 扩展
    # "freeProxySecond",
    "freeProxyThird",
    "freeProxyFourth",
    "freeProxyFifth",
    "freeProxySixth"
    "freeProxySeventh",
    # "freeProxyEight",
    # "freeProxyNinth",
    "freeProxyTen",
    "freeProxyEleven",
    "freeProxyTwelve",
    # foreign website, outside the wall
    # "freeProxyWallFirst",
    # "freeProxyWallSecond",
    # "freeProxyWallThird"
]

# 配置 API服务
SERVER_API = {
    "HOST": "0.0.0.0",  # 监听ip, 0.0.0.0 监听所有IP
    "PORT": 5010        # 监听端口
}
