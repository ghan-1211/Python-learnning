#-*- coding = utf-8 -*-
#@Time : 2021/8/26 16:32
#@Author : ghan
#@File : spider.py


import socket

def read_file_data(file_name):
    try:
        file = open(file_name,'rb')
    except Exception as e:
        print('文件不存在！')
    else:
        file_data = file.read()
        file.close()

        return file_data

#创建一个服务器套接字
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind绑定一个端口
server_socket.bind(("",9999))

#将套接字设置为监听模式
server_socket.listen(128)

while True:
    client_socket,client_addr = server_socket.accept()
    print("接收来自%s的文件下载请求"% str(client_addr))

    #接收文件名称，读取本地文件数据
    file_name = client_socket.recv(4096)

    file_data = read_file_data(file_name)
    if file_data:
        client_socket.send(file_data)

    client_socket.close()

server_socket.close()