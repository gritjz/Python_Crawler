# 环境安装aiohttp
# 使用aiohttp中clientSession实现网络请求
import aiohttp

import asyncio
import requests
import time

urls = [
    'http://127.0.0.1:5000/AAA',
    'http://127.0.0.1:5000/BBB',
    'http://127.0.0.1:5000/CCC'
]
start = time.time()


async def get_page(url):
    print('Downloading..:', url)
    # requests.get()是基于同步的代码，无法执行异步操作
    # response = requests.get(url=url)
    # aiohttp:基于异步网络请求的模块, 用await挂起
    async with aiohttp.ClientSession() as session:
        # get(),post():
        # headers, params/data, proxy='http://ip:port'
        async with await session.get(url) as response:
            # text（）可以返回字符串形式的响应数据
            # read（）可以返回二进制形式的响应数据
            # json（）可以返回json对象
            # 在获取响应数据操作之前，一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)
    print('Done.........:', url)


tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时： ', time.time() - start)
