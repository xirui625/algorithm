#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   字典高并发操作.py
@Time    :   2024/04/16 10:01:30
@Author  :   yangguoli 
@Desc    :   None
'''

# import asyncio

# async def modify_dict(lock, my_dict, key, value):
#     async with lock:
#         my_dict[key] = value
#         print(f"Modified dict: {my_dict}")

# async def main():
#     my_dict = {}
#     lock = asyncio.Lock()

#     tasks = []
#     for i in range(5):
#         task = asyncio.create_task(modify_dict(lock, my_dict, f'key_{i}', f'value_{i}'))
#         tasks.append(task)

#     await asyncio.gather(*tasks)

# asyncio.run(main())]

import asyncio
from concurrent.futures import ThreadPoolExecutor

async def fetch_value(key):
    # 模拟获取值的过程，这里可以替换成你的实际逻辑
    await asyncio.sleep(1)  # 模拟耗时操作
    return f"value_{key}"

def modify_dict(lock, my_dict, key):
    async def _modify_dict():
        value = await fetch_value(key)
        async with lock:
            my_dict[key] = value
            print(f"Modified dict: {my_dict}")

    return _modify_dict

async def main():
    my_dict = {}
    lock = asyncio.Lock()

    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()

        tasks = []
        for i in range(5):
            task = loop.run_in_executor(executor, modify_dict(lock, my_dict, f'key_{i}'))
            tasks.append(task)

        await asyncio.gather(*tasks)

asyncio.run(main())



