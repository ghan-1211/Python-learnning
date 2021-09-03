#-*- coding = utf-8 -*-
#@Time : 2021/8/27 10:05
#@Author : ghan
#@File : spider.py


import socket


def send_file_2_client(new_client_socket,client_addr):

    #1、接收客端发送过来的，要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端（%s）需要下载文件是： %s " % (str(client_addr),file_name))

    file_content = None
    #2、打开文件，读取数据
    try:
        f = open(file_name,'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)


    #3、若是有文件，则发送文件的数据给客户端
    if file_content:
        # new_client_socket.send("ljing1211".encode("utf-8"))
        new_client_socket.send(file_content)


def main():
    # 1、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2、绑定一个本地ip和port
    tcp_server_socket.bind(("",9860))
    # 3、链接客户端
    tcp_server_socket.listen(128)#128和操作系统有关系

    while True:
        # 4、等待客户端的链接
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 5、调用发送文件函数，完成为客户端服务
        send_file_2_client(new_client_socket, client_addr)

        # 关闭套接字
        new_client_socket.close()

    tcp_server_socket.close()

if __name__ == '__main__':
    main()