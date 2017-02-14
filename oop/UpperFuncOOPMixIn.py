# 多重继承(java通过implent interface来实现多重继承，而python则原生支持多重继承)


class Animal(object):
    pass


class RunnableMixIn(object):
    def run(self):
        print('something is running...')


class FlyableMixIn(object):
    def fly(self):
        print('something is flying')


class Dog(Animal, RunnableMixIn):
    pass


class Cat(Animal, FlyableMixIn):
    def fly(self):
        print('this cat is flying,because he is black.')


dog = Dog()
cat = Cat()

dog.run()
cat.fly()
