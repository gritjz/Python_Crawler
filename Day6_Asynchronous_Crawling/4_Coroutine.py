import asyncio

async def request(url):
    print('Requesting: ', url)
    print('Done      : ', url)
#async修饰的韩式，调用之后返回的一个协程对象
c = request('www.baidu.com')

#创建一个事件循环对象
loop = asyncio.get_event_loop()

#将协程对象注册到loop中。启动loop
loop.run_until_complete(c)