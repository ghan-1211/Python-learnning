#-*- coding = utf-8 -*-
#@Time : 2021/8/27 9:37
#@Author : ghan
#@File : spider.py


import socket


def main():
    # 1、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2、绑定一个本地ip和port
    tcp_server_socket.bind(("",9860))

    tcp_server_socket.listen(128)
    #3、链接客户端
    new_client_socket,client_addr = tcp_server_socket.accept()

    #接收客端发送过来的，要下载的文件名
    file_name = new_client_socket.recv(1024)
    print("客户端（%s）需要下载文件是： %s " % (str(client_addr),file_name))

    #发送文件的数据给客户端
    # new_client_socket.send("ljing1211".encode("utf-8"))
    new_client_socket.send("ljing1211".encode("utf-8"))

    #关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()
if __name__ == '__main__':
    main()