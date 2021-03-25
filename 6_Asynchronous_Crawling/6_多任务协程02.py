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
    response = requests.get(url=url)

    # aiohttp:基于异步网络请求的模块

    print(response.text)
    print('Done.........:', url)


tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时： ', time.time() - start)
