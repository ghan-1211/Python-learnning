#-*- coding = utf-8 -*-
#@Time : 2021/8/23 16:27
#@Author : ghan
#@File : spider.py

import socket
def main():
    #1、创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2、绑定一个本地信息
    localaddr = ('',7788)
    udp_socket.bind(localaddr)#必须绑定自己电脑的ip和port，其它不可
    #3、接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        #recv_data这个变量自己存储的是一个元组（接收到的数据，发送方的ip,port）
        recv_msg = recv_data[0] #存储接收的数据
        send_addr = recv_data[1]
        #4、打印接收到的数据
        # print(recv_data)
        #print("%s:%s" % (str(send_addr),recv_msg.decode('utf-8')))
        print("%s:%s" % (str(send_addr),recv_msg.decode('gbk')))
    #5、关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()