from 我的python函数库.parse_url import Parse_url
import json

class XinglangSplier:

    def __init__(self,url):
        self.url = url

    def setProxies(self,proxies=None):
        self.proxies = proxies

    def get_news_box(self):
        parse_url = Parse_url()
        response_str = parse_url.parse(self.url)
        response_dict = json.loads(response_str)
        return response_dict["data"]["cards"]  # 返回了一个列表嵌套了多个字典的数据形式

    def parse_news_list(self,news_box_list,num=10):
        url_list = []
        print(len(news_box_list))
        for news_item in news_box_list:
            if num == 0:break
            num = num - 1
            url_list.append(news_item["scheme"])
        return url_list

    def run(self,num):
        '''
            #目标是爬去新浪新闻手机端的数据
            1，爬去url获取相关的数据并且存入一个字典
            2，从字典里面取出新闻的详细url并且再次发送请求获取响应
            3，把响应的数据保存为一个文本数据保存在本地，需要几个就保存几个
        '''
        news_box_list = self.get_news_box()
        url_list = self.parse_news_list(news_box_list,num=5)
        # print(url_list)
        # print("长度是:%s" % str(len(url_list)))

if __name__ == '__main__':
    url = "https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0"
    x = XinglangSplier(url)
    x.run(1)
    # with open("数据的提取方法/新浪微博/news/hello.json","w",encoding="utf-8")as f:
    #     json.dump(data,f,ensure_ascii=False,indent=2)