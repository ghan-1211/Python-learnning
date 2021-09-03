#-*- coding = utf-8 -*-
#@Time : 2021/8/27 16:15
#@Author : ghan
#@File : spider.py


import threading
import time


class MyTread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm" + self.name + '@' + str(i)#name属性中保存的是当前线程的名字
            print(msg)
if __name__ == '__main__':
    t = MyTread()
    t.start()