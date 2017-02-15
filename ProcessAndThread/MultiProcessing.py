import os

# # linux中,fork()代表复制当前进程来生成一个子进程,一次调用，返回两次，一次在子进程返回，结果总是0，一次在父进程中返回，返回子进程的id
# print('Process %s start...' % os.getpid())
#
# pid = os.fork()
#
# if pid == 0:
#     print('child processing:%s,parent process:%s' % (os.getpid(), os.getppid()))
# else:
#     print('parent processing:%s,and i create a child process:%s' % (os.getpid(), pid))

# python中的跨平台多进程(上面的fork()只能在linux和mac中调用，windows上并没有fork)

from multiprocessing import Process, Pool, Queue


# 子进程要做的事
def do_something(name, count):
    print('Child process is start,name=>%s,id=>%s,count=>%d' % (name, os.getpid(), count))


#
# # 1.创建一个子进程
# if __name__ == '__main__':
#     print('running on process:%s' % os.getpid())
#     p = Process(target=do_something, args=('jax_process', 20))
#     p.start()
#     p.join()  # 设定子进程执行完毕以后再下一步，相当于进程间的同步
#     print('child process is over,come back parent process:%s' % os.getpid())

# # 2.创建进程池
# if __name__ == '__main__':
#     print('running on process:%s' % os.getpid())
#     p = Pool(3)  # 此处3表示该进程池中最多执行的进程数，此处为3,意思是：先执行前三个进程，执行完以后再执行后面的，以此类推
#     for i in range(10):
#         p.apply_async(do_something, args=('jax_process' + str(i), 20))
#     print('wait child process done...')
#     p.close()
#     p.join()
#     print('child process done')


# 进程间通信Queue,Pipes

import time, random


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ('A', 'B', 'C'):
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue...' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()  # pr里面死循环，强行终止

# 运行外部进程并控制输入输出

# import subprocess
#
# print('$ nslookup www.python.org')
# nslookup = subprocess.call(['nslookup', 'www.baidu.com'])
# print('Exit code:', nslookup)
