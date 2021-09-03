#-*- coding = utf-8 -*-
#@Time : 2021/9/2 11:32
#@Author : ghan
#@File : spider.py


"""collections已经被弃用，并在3.8中停止工作,使用collections.abc可代替"""
from  collections.abc import  Iterable
from collections.abc import Iterator
import time

"""使用普通的类，无法实现迭代"""

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self,name):
        self.names.append(name)


    """用iter可，报错"""
    def __iter__(self):
        """如果想要一个对象成为一个可迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            #若是长度大于，则停止
            raise  StopIteration

classmate = Classmate()
classmate.add("zql")
classmate.add("wx")
classmate.add("wpz")

# print("判断classmate是否可以是迭代的对象：",isinstance(classmate,Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是迭代器：",isinstance(classmate_iterator,Iterator))
# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)