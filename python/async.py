#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   async.py
@Time    :   2024/04/16 10:27:17
@Author  :   yangguoli 
@Desc    :   None
'''

import asyncio


async def func1():
    print(f'func 1 is running')
    await asyncio.sleep(2)
    print(f'func 1 is completed')
    return "func1"
    

async def func2():
    print(f'func 2 is running')
    print(f'func 2 is completed')
    return "func2"
    
async def main():
    print("main子协程开始执行")
    task_list = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2())
    ]
    await asyncio.wait(task_list)
    print("main子协程执行结束")


# if __name__ == '__main__':
#     asyncio.run(main())
if __name__ == '__main__':
    # 获取多个异步任务的返回结果
    loop = asyncio.get_event_loop()
    task_list = [
        loop.create_task(func1()),
        loop.create_task(func2())
    ]
    wait_tasks = asyncio.wait(task_list)
    loop.run_until_complete(wait_tasks)
    for task in task_list:
        print(task.result())
    
    



    