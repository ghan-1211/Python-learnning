#-*- coding = utf-8 -*-
#@Time : 2021/9/2 20:55
#@Author : ghan
#@File : spider.py


nums = list()

a = 0
b = 1
i = 0

while i<10:
    nums.append(a)
    a, b = b, a + b
    i += 1

for num in nums:
    print(num)