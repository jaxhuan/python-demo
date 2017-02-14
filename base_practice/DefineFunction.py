def power(x):
    return x * x


# 适用于参数的个数可变的情况
def sum(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum)
    return sum


sum()
sum(1, 2)
numbers = [1, 2, 3]
sum(*numbers)


# 关键词参数
def person(name, age, **kwargs):
    print('name:', name, 'age:', age, 'other:', kwargs)
    if 'city' in kwargs:
        print('has city:', kwargs['city'])
    else:
        print('no city')
        pass


# 只允许传入city,sex等关键词,调用时可以不传入city
def user(name, pwd, *, city='sh', sex):
    print('name:', name, 'pwd:', pwd, city, sex)


others = {'like': 'girl', 'sex': 'male'}
person('xiao chao', 24, **others)
person('jax', 25, birth='19931109', city='sh')
person('xiao red', 19)
person('xiao green', 18, like='play')


# 总结，func(*args,**kw)中,args接收的是一个list或者tuple，kw接收的是一个map对象

# 递归函数

# 计算阶乘(计算过大的数字会导致栈溢出，解决方案:尾递归)暂时没搞懂
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(5))
print(fact(1000))
