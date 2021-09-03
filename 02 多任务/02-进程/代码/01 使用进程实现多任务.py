#-*- coding = utf-8 -*-
#@Time : 2021/9/1 14:11
#@Author : ghan
#@File : spider.py


import threading
import time
import multiprocessing


def test1():
    while True:
        print("1---------")
        time.sleep(2)


def test2():
    while True:
        print("2---------")
        time.sleep(2)


def main():
    """
    这是线程
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()
    """

    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()