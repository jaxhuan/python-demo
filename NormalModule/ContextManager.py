# 只要实现了上下文管理的对象都可以用with .. as ..:来打开,实现上下文管理通过__enter__()和__exit__()


# class User(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('user %s enter' % self.name)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print('error')
#         else:
#             print('%s end' % self.name)
#
#     def say(self):
#         print('%s is say something...' % self.name)
#
#
# with User('jax') as jax:
#     jax.say()

# 上面这样写太麻烦了
from contextlib import contextmanager


class User(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print('%s is say something...' % self.name)


@contextmanager
def create_user(name):
    print('enter user')
    user = User(name)
    yield user
    print('end user')


with create_user('jax') as jax:
    jax.say()


# contextmanager用来实现某段代码前后自动执行某段代码
@contextmanager
def tag():
    print('do something before')
    yield
    print('do something after')


with tag():
    print('main thing')

# closing 使用closing()把该对象变为上下文对象，然后就可以用with了

from contextlib import closing
from urllib.request import urlopen

with urlopen('https://www.baidu.com') as page:
    for line in page:
        print(line)

with closing('haha') as ch:
    print(ch)
