import socket

# AF_INET表示ip v4,SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 链接服务器
s.connect(('www.sina.com.cn', 80))

# 发送请求
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

# 接收数据
buffer = []

while True:
    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

recieve_data = b''.join(buffer)

s.close()

# 输出header，保存网页内容到文件
header, content = recieve_data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('demo.html', 'wb') as f:
    f.write(content)
