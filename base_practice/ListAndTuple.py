# names is a list,the list is can change
names = ['jax', 'mechile', 'hahha']
classnames = [[1, 2, 3], '1', [4], 5]

names.append('john')
names.insert(0, 'heihei')

for name in classnames:
    print('name= %s' % name)
print('names count: %d' % len(names), names)

print('last name is: %s' % names[-1])

print(names[0])

# now names is can't changed list
names = ('haha', 'hehe')

