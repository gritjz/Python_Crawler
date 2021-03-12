import asyncio

async def request(url):
    print('Requesting: ', url)
    print('Done      : ', url)
    #return 用于绑定回调
    return url

#async修饰的韩式，调用之后返回的一个协程对象
#下面几种方式调用async时，都会绑定c
c = request('www.baidu.com')



# #创建一个事件循环对象
# loop = asyncio.get_event_loop()
# #将协程对象注册到loop中。启动loop
# loop.run_until_complete(c)

# #task的使用
# loop = asyncio.get_event_loop()
# #基于loop创建一个task对象
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# #future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

#绑定回调
def callback_func(task):
    #result返回的就是任务对象中封装的协程对象对应函数的返回值，即上面requests中return的url
    print(task.result())

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)