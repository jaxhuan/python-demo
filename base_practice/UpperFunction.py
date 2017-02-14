# 切片(应用，string是一个特殊的list,因此，可以通过切片来操作string==java中的substring)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 取前L中J到K的元素
def getJ2K(J, K, L):
    result = []
    for i in range(len(L)):
        if i >= J and i <= K:
            result.append(L[i])
        else:
            continue
    return result


# 复制L
L[:]
L.copy()

# 使用系统方法(取L中前5个元素)
print(L[0:5])
# 1,2,3,4,5

# 取前6个元素，每隔两个取一次
print(L[0:6:2])
# result is 1,3,5?

# 取前7个元素
print(L[:7])

# 取所有元素，每隔3个取一次
print(L[::3])

# 取最后2个元素
print(L[-2:])

# 取最后一个元素
print(L[-1:])
