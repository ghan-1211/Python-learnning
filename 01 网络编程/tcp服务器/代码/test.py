#-*- coding = utf-8 -*-
#@Time : 2021/8/26 15:31
#@Author : ghan
#@File : spider.py


import urllib3
class Spider:

    def loadPage(self,page):
        url = "http://www.neihan8.com/article/list_5_" + str(page)+ ".html"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        headers = {'User-Agent':user_agent}
        req = urllib3.response(url,headers = headers)

if __name__ == '__main__':
    pass