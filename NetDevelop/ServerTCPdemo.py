import socket, threading, time

# 创建基于ipv4和tcp协议的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听地址和接口(127.0.0.1)表示本地,7788为测试端口，小于1024的端口需要super user权限才可以绑定
s.bind(('127.0.0.1', 7788))

# 开始监听,5表示等待连接的最大数量
s.listen(5)
print('server has listen,Waiting for connection...')


# 接收到连接所做的处理
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程处理这个连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


