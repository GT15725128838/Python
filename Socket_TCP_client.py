import socket

# 创建套接字
Tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立tc连接
Tcp_client_socket.connect(("192.168.31.247", 7878))

# 发送数据
Tcp_client_socket.send("hello,world".encode('utf-8'))

# 关闭套接字
Tcp_client_socket.close()