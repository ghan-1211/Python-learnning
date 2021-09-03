#-*- coding = utf-8 -*-
#@Time : 2021/8/27 14:44
#@Author : ghan
#@File : spider.py


import threading
import time


def test1():
    for i in range(5):
        print("-------test01------%d--------" % i)
        time.sleep(1)


def main():
    #在调用thread前先打印当前线程信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)#填写函数名称，而非调用

    #在调用thread之后打印
    print(threading.enumerate())

    t1.start()

    #在调用start之后打印
    print(threading.enumerate())

if __name__ == "__main__":
    main()