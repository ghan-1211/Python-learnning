#-*- coding = utf-8 -*-
#@Time : 2021/8/25 21:25
#@Author : ghan
#@File : spider.py

import socket


def main():
    #1、创建tcp套接字  dgram-udp  stream-tcp
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2、链接服务器
    # tcp_socket.connect("192.168.22.1",8080)
    server_ip = input("请输入要链接的服务器的ip：")
    server_port = int(input("请输入要链接的服务器的port："))
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)
    #3、发送数据/接收欧数据
    sen_data = input("请输入要发送的数据：")
    tcp_socket.send(sen_data.encode('utf-8'))
    #4、关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()