#-*- coding = utf-8 -*-
#@Time : 2021/8/23 16:01
#@Author : ghan
#@File : spider.py

import  socket

def main():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 从键盘获取数据
        send_data = input("请输入发送数据：")

        #如果输出的数据时exit，则退出程序
        if send_data == 'exit':
            break

        # encode编码
        s.sendto(send_data.encode("utf-8"), ("192.168.8.19", 8080))

    s.close();


if __name__ == '__main__':
    main()
