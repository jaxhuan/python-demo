high = 1.75
weight = 80.5

bmi = weight / (high * high)

if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('超级胖')
    pass

for x in range(5):
    print(x)

l = ('jax', 'xiaoming', 'xiaored', 'xiaoyellow')

for name in l:
    print('Hello,%s' % name)
