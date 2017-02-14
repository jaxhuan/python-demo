# 列表生成式式生成列表的快捷方法，但是一下子加载列表中所有元素占用内存空间太大，所以引出列表生成器，当使用元素的时候使用生成器生成

genetator = (x * x for x in range(1, 11))

for g in genetator:
    print(g)


# 普通的斐波那契数列实现函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'ok'


fib(20)


# 生成器形式的斐波那契数列形式
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'ok'


# 获取生成的结果，但是获取不到return值
for fb in fib_g(20):
    print(fb)

# 获取返回值
fb = fib_g(6)
while True:
    try:
        print(next(fb))
    except StopIteration as e:
        print('the generator return:', e.value)
        break


# 当一个函数中有yield关键字时，则此函数是一个生成器
# 生成器类型的函数,每次调用next()时执行，遇到yield返回，再次执行时从上次返回的yield出继续执行

# practice,这里杨辉三角没想出来，心塞
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
