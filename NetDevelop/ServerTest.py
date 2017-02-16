import socket

# 测试上面那个小服务器
s_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_test.connect(('127.0.0.1', 7788))
# 连接上以后，对面会发welcome
print(s_test.recv(1024).decode('utf-8'))

for data in [b'jax', b'yinsi', b'xiaoming']:
    s_test.send(data)
    print(s_test.recv(1024).decode('utf-8'))
s_test.send(b'exit')
s_test.close()
