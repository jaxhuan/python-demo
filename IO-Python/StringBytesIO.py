from io import StringIO, BytesIO

# 在内存中写StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')
print(f.getvalue())

# 读取
f = StringIO('Hello world!!\nhahhahahha\nin fact,i\'m ok')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())  # strip()去掉后面的\n不然输出隔一行

# BytesIO
b = BytesIO()
b.write('中文'.encode('utf-8'))
b.getvalue()

b = BytesIO(b'\xe4')
print(b.read())
