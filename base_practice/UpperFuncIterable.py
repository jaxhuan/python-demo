# 迭代(便利对象==java foreach)

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for d in dic:
    print(d)

for k, v in dic.items():
    print('key:', k, 'value:', v)

for v in dic.values():
    print(v)

for s in 'jax':
    print(s)

# 判断一个对象是否可迭代
from collections import Iterable

isinstance('abc', Iterable)

isinstance(123, Iterable)

# python里面只有for each,那么怎么在循环的时候使用下标?ex for(int i=0;i<list.size();i++)

for index, value in enumerate(dic):
    print('index:', index, 'object:', value)
