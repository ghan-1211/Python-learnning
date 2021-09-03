#-*- coding = utf-8 -*-
#@Time : 2021/9/2 11:32
#@Author : ghan
#@File : spider.py


from  collections import  Iterable
from collections import Iterator
import time

"""使用普通的类，无法实现迭代"""

class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)


    """用iter可，报错"""
    def __iter__(self):
        """如果想要一个对象成为一个可迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):

    def __init__(self,obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
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