# __slots__(使用__slots__属性限制该类只能有这两个参数,__slots__只对当前类起作用，对子类不起作用，
# 除非子类也定义了__slots__，那么子类的属性限制为子类__slots__+父类__slots__)


class User(object):
    __slots__ = ('user_name', 'pass_word')


class UserVip(User):
    age = 30


user1 = User()
user1.user_name = 'jax'
user1.pass_word = '123456'

user2 = UserVip()
user2.haha = 'haha'
print(user2.haha)

print('name is %s,password is %s' % (user1.user_name, user1.pass_word))
