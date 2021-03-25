import asyncio
import time

async def request(url):
    print('Downloading: ', url)

    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    #time.sleep(2)是基于同步模块的。
    #在asyncio中遇到阻塞操作必须进行手动挂起，即使用await来封装asyncio.sleep
    await asyncio.sleep(2)

    print('   Done    :', url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.google.com',
    'www.sogou.com'
]

#任务列表：存放多个任务对象
tasks=[]
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-start)