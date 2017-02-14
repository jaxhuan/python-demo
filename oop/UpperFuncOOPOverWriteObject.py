# 定制一个自己的类，通过复写Object方法

class User(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'User : %s' % self.name


user = User('jax')
print(user)
