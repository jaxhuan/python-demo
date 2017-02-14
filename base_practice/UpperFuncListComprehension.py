# 列表生成式(生成列表)

a = [x * x for x in range(1, 11)]

print(a)

a = [x * x for x in range(1, 11) if x > 5]

print(a)

# 双层循环创建list

a = [m + n for m in 'ABC' for n in 'XYZ']

print(a)

# 两个参数生成list
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a = [k + '=' + str(v) for k, v in dic.items()]
print(a)

# 应用：列出当前目录下所有文件和目录名称
import os

all_src = [d for d in os.listdir('.')]
print('this folder cotains src:', all_src)

L = ['Jax', 'Hello', 'OK', 'hi', 20, 'hahhahah']

print([s.lower() for s in L if isinstance(s, str)])
