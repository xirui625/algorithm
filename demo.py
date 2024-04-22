#!/usr/bin/env python 
#-*- coding: UTF-8 -*-
# @Time    : 2022/4/27 下午6:53
# @Author  : yangguoli
# @File    : demo.py
# @Software: PyCharm


# import collections

# if __name__ == '__main__':
#     # nums = [-1,0,1,2,-1,-4]
#     # nums_dict = collections.Counter(nums)
#     # print(nums_dict)
#     # n = list(filter(lambda a: a < 0, nums_dict))
#     # print(n)
#     # p = list(filter(lambda a: a >= 0, nums_dict))
#     # print(p)
#     j = -1
#     if j in (0, -1):
#         print(111)
# import threading
# import asyncio

# async def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     await asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())

# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
    
    
# async def async_generator():
#     for i in range(5):
#         await asyncio.sleep(1)
#         yield i

# async def main():
#     async for item in async_generator():
#         print(item)


# asyncio.run(main())

        
