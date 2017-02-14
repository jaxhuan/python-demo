class Fruit(object):
    def eat(self):
        print('eating fruit...')


class Apple(Fruit):
    def eat(self):
        print('eating apple')


class Lemon(Fruit):
    pass


def EatFruit(fruit):
    fruit.eat()


def getType(object):
    print(type(object))


apple = Apple()
lemon = Lemon()

EatFruit(apple)
EatFruit(lemon)

getType(apple)
getType(lemon)

import types

print(type(getType) == types.BuiltinFunctionType)

print(dir(apple))

# 判断对象是否有某个参数
hasattr(apple, 'name')
# 添加参数
setattr(apple, 'name', 'Apple')
print(getattr(apple, 'name', 'Fruit'))
print(apple.name)
