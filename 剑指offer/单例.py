# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/10 17:25
import time
import threading

# 1. 使用模块，Python的模块是天然的单例模块，因为模块第一次导入，就会生成.pyc文件，当第二次导入时，就会直接加载.pyc文件，
# 不会再次执行模块代码。因此，我们只需把相关函数和数据定义在一个模块中，就可以获得一个单例对象了。


class Singleton(object):
    pass


singleton = Singleton()


# 2. 使用类


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

