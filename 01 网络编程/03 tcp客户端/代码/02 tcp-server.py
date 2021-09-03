#-*- coding = utf-8 -*-
#@Time : 2021/8/26 9:27
#@Author : ghan
#@File : spider.py


import socket
def main():
    #1、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2、bind绑定套接字
    tcp_server_socket.bind(("",7890))

    #3、listen使套接字变为被动链接
    tcp_server_socket.listen(128)

    print("***1****")
    #4、accept等待客户端的链接
    #client_socket用来为客户端服务
    #tcp_server_socket就可省下来专门等待其他新客户端的的链接
    new_client_socket,client_addr = tcp_server_socket.accept()#accept返回的是元组
    print("***2****")

    print(client_addr)

    #接收客户端发送过来的请求
    recv_data = new_client_socket.recv(1024)
    print(recv_data)

    #回送客户端发送过来的请求
    new_client_socket.send("hhh".encode("utf-8"))

    #关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()

if __name__ == '__main__':
    main()