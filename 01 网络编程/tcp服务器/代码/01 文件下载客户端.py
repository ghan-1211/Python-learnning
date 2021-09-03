#-*- coding = utf-8 -*-
#@Time : 2021/8/26 14:41
#@Author : ghan
#@File : spider.py


import socket


def main():
    # 1、创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2、绑定一个本地ip和port
    ip = input("请输入服务器的ip地址：")
    port = int(input("请输入服务器的端口号："))

    #3、链接服务器
    tcp_socket.connect((ip,port))

    #4、获取下载的文件名字
    file_name = input("请输入一个下载的文件名：")
    #5、将文件名字发送到服务器
    tcp_socket.send(file_name.encode("utf-8"))

    #6、接收文件中的数据
    recv_data = tcp_socket.recv(1024)
    # file = open('new_' + file_name,'wb')

    if recv_data:
        # 7、若是有数据，则保存接收到的数据到一个文件中
        with open("[新]" + file_name, "wb") as f:
            f.write(recv_data)

    #8、关闭套接字
    tcp_socket.close()


    # had_write_len = 0
    #
    # while True:
    #     data = tcp_socket.recv(4096)
    #     if data:
    #         file.write(data)
    #         had_write_len += len(data)
    #     else:
    #         file.close()
    #
    #         if had_write_len > 0:
    #             print("文件传输完成！")
    #         else:
    #             print("服务器没有这文件")
    #             os.remove("new_" + file_name)
    #
    #         tcp_socket.close()
    #         break

if __name__ == '__main__':
    main()