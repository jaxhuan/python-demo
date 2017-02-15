import threading, time


# 在子线程中执行的任务
def do_back_ground():
    print('thread is running:%s' % threading.current_thread().name)


print('thread is running:%s' % threading.current_thread().name)
t_bg = threading.Thread(target=do_back_ground, name='jax child thread')
t_bg.start()
t_bg.join()
print('child thread is over,now thread is %s' % threading.current_thread().name)

# Lock(多线程同事操作一个变量，会造成变量的不确定性，所以使用线程锁来确保结果)

# 多线程导致变量balance的结果不确定:


balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('all thread is over,changed balance is: %d' % balance)

# 解决方法，使用锁(锁只有一个，同一时刻只能有一个线程持有锁，其他线程等待)

balance = 0
lock = threading.Lock()


def run_thread_with_lock(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 操作变量完成后释放锁
            lock.release()


t1 = threading.Thread(target=run_thread_with_lock, args=(5,))
t2 = threading.Thread(target=run_thread_with_lock, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Use Lock,all thread is over,changed balance is: %d' % balance)

