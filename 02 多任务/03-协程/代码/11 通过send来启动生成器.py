#-*- coding = utf-8 -*-
#@Time : 2021/9/2 21:18
#@Author : ghan
#@File : spider.py


def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        """方式1"""
        #print(a)
        yield a #在函数中只要包含yield，就不是函数，而是一个生成器的模板
        a, b = b, a + b
        current_num += 1
    return  "ok..."

obj = create_num(20) #创建生成器对象

while True:
    try:
        ret = next(obj)  # 生成器执行
        print(ret)
    except Exception as ret:
        print(ret.value)
        break


# for num in obj:
#     print(num)