# 枚举。注：我喜欢
from enum import Enum, unique

from collections import Iterable, Iterator

# 常规用法
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 派生类，自己定义value值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(isinstance(Weekday, Iterable))

for w in Weekday:
    print(w, '=>', w.value)
