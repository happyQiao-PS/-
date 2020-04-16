# from time import sleep
# import json
#
#
# class A:
#     def __init__(self,num):
#         self.num = num
#
# a = A(1)
# a1 = json.dumps(a)
# print(type(a))
# print("------------转换中-------------")
# sleep(3)
# print("------------转换完毕------------")
# print(eval(a1))

import re

from 我的python函数库.parse_url import Parse_url

if __name__ == '__main__':
    url="https://www.douban.com/search?source=suggest&q=新冠肺炎"
    p = Parse_url()
    ret = p.parse(url)
    with open("./data.html","w",encoding="utf-8")as f:
        f.write(ret)