# pickle python中用来序列化对象的接口

import pickle
import json

d = dict(name='jax', age=25, sex=1)

# pickle.dumps()把一个对象转换成二进制
with open('/home/jax/桌面/demo.txt', 'wb') as file:
    print(pickle.dumps(d))
    pickle.dump(d, file)

with open('/home/jax/桌面/demo.txt', 'rb') as file:
    print(pickle.load(file))

print(json.dumps(d))
print(json.loads(json.dumps(d)))


# json和class
class User(object):
    def __init__(self, name='jax', score=0):
        self._name = name
        self._score = score

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score


def dic2user(d):
    return User(d['_name'], d['_score'])


def user2dic(u):
    return {'_name': u.name, '_score': u.score}


user = User()

user_json = json.dumps(user, default=user2dic)
user_json = json.dumps(user, default=lambda obj: obj.__dict__)
# 此处两个作用相等，都是把user转换成dic
# 一般当类里面没有声明__slots__时，class的__dict__属性就是一个dict，用来存储实例变量,但
# 当声明__slots__后，不能用第二种

print(user_json)
print(json.loads(user_json, object_hook=dic2user))
