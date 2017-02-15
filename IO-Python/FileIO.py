# 读取文件

# 1.必须close()
file = open('/home/jax/桌面/demo.txt', 'r')
print(file.read())
file.close()

# 2.不用close()
with open('/home/jax/桌面/demo.txt', 'r') as file:
    print(file.read())  # 读取全部内容

    for line in file.readlines():
        print(line.strip())  # 去掉末尾的\n

# 读取二进制的视频，图片文件等等
with open('demo.jpg', 'rb') as file:
    print(file.read())

# 读取非utf-8编码的文本文件,如果存在非法编码的情况，加error参数
with open('demo.html', 'r', encoding='gbk', errors='ignore') as file:
    for line in file.readlines():
        print(line)

# 写文件 注:会覆盖掉已有的
with open('/home/jax/桌面/demo.txt', 'w', encoding='utf-8') as file:
    file.write('HelloWorld,this is added by code~')

with open('/home/jax/桌面/demo.txt', 'r') as file:
    print(file.read())  # 读取全部内容
