import itertools

# count创建无限迭代器
natuals = itertools.count(1)

for i in natuals:
    print(i)
    if i == 100:
        break

# cycle无限重复一个序列(妈的，停不下来)

# cs = itertools.cycle('jax=>yinsi')
# cs = itertools.cycle(dict(a=1, b=2, c=3))
#
# for i in cs:
#     print(i)

# repeat 重复一个元素，但是可以限定次数

ns = itertools.repeat('a', 3)
for ch in ns:
    print(ns)

# takewhile()截取一段序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x < 20, natuals)

print('take while:', list(ns))

# chain 把一组迭代对象串联起来

for ch in itertools.chain('jax', 'yinsi'):
    print('chain=>', ch)

# group 挑出相邻的重复元素放一起

for key, group in itertools.groupby('AAABBBCCCCaa'):
    print(key, list(group))

for key, group in itertools.groupby('AAaABbbCcc', lambda c: c.upper()):
    print(key, list(group))
