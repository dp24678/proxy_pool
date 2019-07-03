# -*- coding: utf-8 -*-


from Util.utilClass import LazyProperty
from Config.setting import *


class ConfigGetter(object):
    """
    get config
    """

    def __init__(self):
        pass

    @LazyProperty
    def db_type(self):
        return DATABASES.get("default", {}).get("TYPE", "SSDB")

    @LazyProperty
    def db_name(self):
        return DATABASES.get("default", {}).get("NAME", "proxy")

    @LazyProperty
    def db_host(self):
        return DATABASES.get("default", {}).get("HOST", "127.0.0.1")

    @LazyProperty
    def db_port(self):
        return DATABASES.get("default", {}).get("PORT", 8080)

    @LazyProperty
    def db_password(self):
        return DATABASES.get("default", {}).get("PASSWORD", "")

    @LazyProperty
    def proxy_getter_functions(self):
        """
        代理IP 获取函数
        :return: 注册的所有 代理IP获取函数名（列表）
        """
        return PROXY_GETTER

    @LazyProperty
    def host_ip(self):
        return SERVER_API.get("HOST", "127.0.0.1")

    @LazyProperty
    def host_port(self):
        return SERVER_API.get("PORT", 5010)


config = ConfigGetter()

if __name__ == '__main__':
    print(config.db_type)
    print(config.db_name)
    print(config.db_host)
    print(config.db_port)
    print(config.proxy_getter_functions)
    print(config.host_ip)
    print(config.host_port)
    print(config.db_password)
