from parse_url import Parse_url
import re

# 首先我们这次的爬虫工作比较简单
# 这次的url遵循了restful框架规则在最后后的url中添加了一个页码地址，我们可以使用循环的方式
# 每一次请求的数据都通过正则匹配把有效的数据保存下来

class neihanduanzi(Parse_url):
    def __init__(self, url=None):
        super().__init__()
        self.url = url

    def parse_data(self, url):  # 发送请求并且处理数据
        res_html = self.parse(url=url)
        title_list = self.get_title(html_code=res_html)  # 获取标题
        article_list = self.get_article(html_code=res_html)  # 获取段子
        return title_list, article_list

    def get_title(self, html_code):
        return re.findall(r'rel=\"bookmark\" title=\"(.*?)\"', html_code)

    def get_article(self, html_code):
        return re.findall(r'</strong>(.*)?</p>', html_code)

    def generate_url(self, url=None, num=1):
        self.num = num
        self.url_list = [url % (i + 1) for i in range(num)]

    def save(self,*args,**kwargs):
        if args:
            for index,item in enumerate(args[1]):
                args[2].write(args[0][index]+"\n"+item+"\n")

    def _run(self, url, num):
        self.generate_url(url=url, num=num)
        if len(self.url_list) > 0:
            for index,url_item in enumerate(self.url_list):
                title_list, article_list = self.parse_data(url=url_item)  # 获取到数据列表了
                with open("data/内涵段子第%d.txt" %(index+1),"w+",encoding="utf-8")as f:
                    self.save(title_list,article_list,f)

    def run(self, url, num=1):
        try:
            self._run(url=url, num=num)
        except Exception as e:
            raise e


if __name__ == '__main__':
    spider = neihanduanzi()
    try:
        num = int(input("输入页数：").strip())
        spider.run(url="https://wengpa.com/duanzi/page/%d/", num=num)
    except:
        spider.run(url="https://wengpa.com/duanzi/page/%d/")
