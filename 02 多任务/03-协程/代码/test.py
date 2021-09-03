#-*- coding = utf-8 -*-
#@Time : 2021/9/2 11:29
#@Author : ghan
#@File : spider.py


"""判断是否可以迭代"""

from collections import Iterable

isinstance([11,22,33,44],Iterable)

isinstance(100,Iterable)