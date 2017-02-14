# map_demo is a dic,as same as map
map_demo = {'jax': 100, 'ming': 200}

for m in map_demo:
    print(m, map_demo[m])

# set_demo is a set,this is not can save the same 2 value
set_demo = set([1, 2, 1, 3])
set_demo.add(5)

print(set_demo)
print('diff:', set_demo.difference(set([1, 4, 6])))

t=(1,2,3)