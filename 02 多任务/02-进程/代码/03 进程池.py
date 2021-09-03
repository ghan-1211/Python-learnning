#-*- coding = utf-8 -*-
#@Time : 2021/9/1 16:44
#@Author : ghan
#@File : spider.py


from multiprocessing import Pool
import time,os,random


def worker(msg):
    t_start = time.time()
    print("%s 开始执行，进程号为%d" % (msg,os.getid()))
    # random.random()随机生成0-1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕！耗时%0.2f" % (t_stop-t_start))


# 定义一个进程池，最大进程数3
po = Pool(3)
for i in range(0,10):
    # Pool().apply_async(要调用的目标，(传递给目标的参数元组))
    # 每次循环将会空闲出来的子进程去调用目标
    po.apply_async(worker,(i,))


print("----start----")
po.close()
po.join()
print("----end----")