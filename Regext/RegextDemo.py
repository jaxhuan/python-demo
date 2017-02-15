from collections import Iterable
import re

# 常规使用 *任意字符,+多个字符(至少一个),?不知道有没有字符，
regext = r'^\d{3}\s*\-\s*\d{3,8}$'

if re.match(regext, '010-1236546549'):
    print('match')
else:
    print('failed')

result = re.split(r'[\s\,\;]+', 'a,b;,c   d')

print(result)

# group
m = re.match(r'^([\d]{4})-(\d{7})$', '0359-4793098')
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 判断时间(hh:mm:ss)

regext = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0-5]{0,1}[0-9])\:([0-5]{0,1}[0-9])'

re_time = re.compile(regext)

m = re_time.match('19:09:36')
print(m.groups())
