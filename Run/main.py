# -*- coding: utf-8 -*-

import sys
from multiprocessing import Process

sys.path.append('.')
sys.path.append('..')

from Api.ProxyApi import run as ProxyApiRun
from Schedule.ProxyValidSchedule import run as ValidRun
from Schedule.ProxyRefreshSchedule import run as RefreshRun


def run():
    p_list = list()  # 生成一个列表对象
    p1 = Process(target=ProxyApiRun, name='ProxyApiRun')  # 代理api进程
    p_list.append(p1)
    p2 = Process(target=ValidRun, name='ValidRun')  # 有效 进程
    p_list.append(p2)
    p3 = Process(target=RefreshRun, name='RefreshRun')  # 刷新进程
    p_list.append(p3)

    for p in p_list:
        p.daemon = True
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()
