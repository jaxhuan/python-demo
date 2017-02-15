# namedtuple 自定义特殊的tuple,指定的名字和元素名
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 3)

print(p, 'p is a Point?', isinstance(p, Point), 'p is a tuple?', isinstance(p, tuple))
print(p.x)
print(p.y)

# ex
Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle_black = Circle(1, 1, 1)

# deque list查询很快，但插入和删除慢，deque是为了实现搞笑插入和删除的双向列表，适用于队列和栈:

from collections import deque

de = deque([1, 2, 3])
de.append(4)
de.appendleft(5)
print(de)
de.pop()
de.popleft()
print(de)

# ddict 返回默认值的dic
from collections import defaultdict

dic = defaultdict(lambda: 'none')
print(dic['jax'])

# 计数器
from collections import Counter

c = Counter()
for ch in 'python programming':
    c[ch] = c[ch] + 1
print(c)
