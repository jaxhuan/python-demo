a = sorted(['jax', 'haha', 'amazing', 'create'], key=str.lower, reverse=True)
print(a)

table_score = [('bob', 75), ('amada', 92), ('bart', 66), ('lisa', 88)]

print(table_score)


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


print('name:', sorted(table_score, key=by_name))
print('score:', sorted(table_score, key=by_score))

L = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))
print(L)
