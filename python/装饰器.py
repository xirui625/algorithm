#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   装饰器.py
@Time    :   2024/04/14 21:01:22
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
import functools

# functools.wraps的作用
# 当你使用装饰器时，装饰器会将原始函数替换为其内部的包装函数。
# 但是，这可能会导致一些问题，因为包装函数的元数据（如函数名、文档字符串、参数列表等）不会传递给包装后的函数。
# 这可能会影响调试和文档生成等操作。

# 普通装饰器
# 这是装饰器函数，参数 func 是被装饰的函数
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('主人，我准备开始执行：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('主人，我执行完啦。')
    return wrapper

# 带参数的装饰器,

def log_with_level(level):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if level == 'info':
                print("INFO:", func.__name__, "was called")
            elif level == 'debug':
                print("DEBUG:", func.__name__, "was called")
            elif level == 'warning':
                print("WARNING:", func.__name__, "was called")
            elif level == 'error':
                print("ERROR:", func.__name__, "was called")
            elif level == 'critical':
                print("CRITICAL:", func.__name__, "was called")
            else:
                raise ValueError("Invalid log level")
                
            return func(*args, **kwargs)
        return wrapper
    return decorator