#-*- coding = utf-8 -*-
#@Time : 2021/8/27 11:18
#@Author : ghan
#@File : spider.py


import time


def sing():
    """唱歌5s"""
    for i in range(5):
        print("----十年人间--------")
        time.sleep(1)


def dance():
    """跳舞5s"""
    for i in range(5):
        print("----正在跳舞--------")
        time.sleep(1)


def main():
    sing()
    dance()

if __name__ == "__main__":
    main()