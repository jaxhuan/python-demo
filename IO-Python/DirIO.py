# 操作文件和目录

import os
import shutil

path = os.path.join('/home/jax/桌面', 'testdir')

print(path, '==>', os.path.exists(path))

if os.path.exists(path) == False:
    os.mkdir(path)

print(path, '==>', os.path.exists(path))

# 使用join(),split()等方法可以避免操作系统的路径区别,ex:windows,C:\；linux,C:/
print(os.path.split('/home/jax/桌面/demo.txt'))

# 获取文件扩展名
print(os.path.splitext('/home/jax/桌面/demo.txt'))

# 应用

# 列出当前上所有文件夹
dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dirs)

# 列出当前目录所有的.jpg文件
files = [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.jpg']
print(files)



