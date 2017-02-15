# ThreadLocal为了解决一个线程内各个函数之间传递参数丑陋的问题(常用于：为每个
# 线程绑定数据库链接，http请求等等)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# 没用ThreadLocal之前,缺点：每调用一层函数都得传参，丑+麻烦

def process_stu(name):
    stu = Student(name)
    do_task1(stu)
    do_task2(stu)


def do_task1(stu):
    # 此处stu是局部变量，每个线程都有一个，所以不会互相影响
    do_sub_task1(stu)
    pass


def do_task2(stu):
    do_sub_task1(stu)
    pass


def do_sub_task1(stu):
    pass


import threading

# 创建全局ThreadLocal对象++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
local_school = threading.local()


def process_student():
    # 获取当前线程的student
    std = local_school.student
    print('Hello,%s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('jax',), name='jax_thread')
t2 = threading.Thread(target=process_thread, args=('yinsi',), name='yinsi_thread')
t1.start()
t2.start()
t1.join()
t2.join()
