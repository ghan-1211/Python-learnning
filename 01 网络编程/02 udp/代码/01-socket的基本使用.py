#-*- coding = utf-8 -*-
#@Time : 2021/8/22 21:12
#@Author : ghan
#@File : spider.py

import socket

def main():
    # 创建一个udp套接字
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #可以使用套接字收发数据
    s.sendto(b"0817",("192.168.8.19",8080))
    #关闭套接字
    s.close()

if __name__ == '__main__':
    main()