#-*- coding = utf-8 -*-
#@Time : 2021/8/26 9:27
#@Author : ghan
#@File : spider.py


import socket
def main():
    #1、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2、bind绑定套接字
    tcp_server_socket.bind(("",7895))

    #3、listen使套接字变为被动链接
    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的客户端到来")
        # 4、accept等待客户端的链接
        # client_socket用来为客户端服务
        # tcp_server_socket就可省下来专门等待其他新客户端的的链接
        new_client_socket, client_addr = tcp_server_socket.accept()  # accept返回的是元组
        print("一个新的客户端已经到来%s" % str(client_addr))

        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)
        print("客户端送过来的请求是：%s" % recv_data.decode("utf-8"))

        # 回送客户端发送过来的请求
        new_client_socket.send("hhh".encode("utf-8"))

        # 关闭套接字
        new_client_socket.close()#当前客户端，关闭，不会再为这个客户端服务
        print("已经服务完毕！")

    #如果将监听套接字关闭了，会导致不能再次等待客户端到阿里，即xxx.accept会失败
    tcp_server_socket.close()


if __name__ == '__main__':
    main()