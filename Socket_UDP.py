import  socket


# 创建socket
# AF_INET 表示ip地址，也是internet互联⽹
# SOCK_DGRAM 表示使⽤udp 协议
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

send_content = "hello,world"

# 把⽂本内容转码，转成⼆进制数据
send_data = send_content.encode("utf-8")

# 发送数据
# ("192.168.31.221", 8080) 接收数据⽅ip地址和端⼝
udp_socket.sendto(send_data, ("192.168.31.221", 8080))

# 关闭数据
udp_socket.close()