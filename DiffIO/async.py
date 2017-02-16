# 协程：在一个函数中，若碰到耗时任务，那么先中断，执行其他任务，在适当时候再继续执行
# 我的理解:通过函数方法来间接实现多任务，但协程本质上在一个线程内

# 使用asyncio实现单线程的并发io操作

import asyncio
import threading


# # async表示这个要用协成来完成这个方法里的代码，await 表示后面的代码室耗时操作
# async def hello():
#     print('Hello world!%s' % threading.current_thread())
#     r = await asyncio.sleep(1)
#     print('Hello again!%s' % threading.current_thread())
#
#
# tasks = [hello(), hello()]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# 应用例子:获取sina,souhu,163首页
async def get_page(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header => %s' % (host, line.decode('utf-8').strip()))
    # ignore the body,close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [get_page(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
