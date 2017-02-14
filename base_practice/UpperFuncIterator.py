# 迭代器(iterator)

# 判断一个对象是否是iterator
from collections import Iterator, Iterable

is_iterator = isinstance((x for x in range(10)), Iterator)
print(is_iterator)

is_iterator = isinstance([], Iterator)
print(is_iterator)

print(isinstance({}, Iterator))
print(isinstance('jax', Iterator))

print('is iterable')

print(isinstance((x for x in range(10)), Iterable))

print(isinstance([], Iterable))

# 转换为Iterator对象
print(isinstance(iter([]), Iterator))

# Iterable和Iterator的区别在于:Iterable表示这个对象可以迭代(进行for each循环),而
# Iterator则表示这个对象室一个流，可以用过next()获取下一个数据，直到stop

# Iterable 相当于为某些特定对象提供遍历(迭代)的功能，
# 而Iterator则用于生成惰性计算的对象，因此Iterator适用于表示特别大的对象，如全体自然数，因为Iterator只有在需要的时候才会计算。
