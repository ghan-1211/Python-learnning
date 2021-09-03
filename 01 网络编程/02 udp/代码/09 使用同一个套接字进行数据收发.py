#-*- coding = utf-8 -*-
#@Time : 2021/8/23 16:01
#@Author : ghan
#@File : spider.py

import  socket

def main():

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #获取对方的ip/port
    dest_ip= input("请输入对方的ip：")
    dest_port = int(input("请输入对方的port："))

    #从键盘获取数据
    send_data = input("请输入发送数据：")
    #encode编码
    #s.sendto(send_data.encode("utf-8"),("192.168.8.19",8080))
    s.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))

    #接收会送过来的数据
    recv_data = s.recvfrom(1024)
    #套接字是一个可以同时收发数据
    print(recv_data)

    s.close();

if __name__ == '__main__':
    main()
