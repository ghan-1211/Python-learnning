#-*- coding = utf-8 -*-
#@Time : 2021/9/2 21:18
#@Author : ghan
#@File : spider.py


def create_num(all_num):
    print("****1******")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        """方式1"""
        #print(a)
        print("****2******")
        yield a #在函数中只要包含yield，就不是函数，而是一个生成器的模板
        a, b = b, a + b
        print("****3******")
        current_num += 1
        print("****4******")

#如果在调用create_num的时候，发现这函数有yield，那么不调用函数，而是创建一个生成器对象
obj = create_num(10) #创建生成器对象
obj2 = create_num(2)

ret = next(obj) #生成器执行
print("obj:",ret)
ret = next(obj) #生成器执行
print("obj",ret)



ret1 = next(obj2)
print("obj2",ret1)
ret1 = next(obj2)
print("obj2",ret1)

# for num in obj:
#     print(num)