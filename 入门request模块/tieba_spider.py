import requests
import time

class Tieba_spider:
    def __init__(self,search_name):
        self.search_name = search_name
        self.url = "https://tieba.baidu.com/f?kw="+search_name+"&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

    def generate_url_list(self,generate_num):
        generate_list = []
        for i in range(generate_num):
            generate_list.append(self.url.format(i*50))
        return generate_list

    def parse_url(self,url):
        response = requests.get(url=url,headers=self.headers)
        time.sleep(0.1)
        return response.content.decode("utf-8")

    def save(self,html_code,index):
        filename = self.generate_filename(index)
        with open(filename,"w",encoding="utf-8") as f:
            f.write(html_code)
            print(filename+"下载完毕")

    def generate_filename(self,index):
        filename = "./tiebaFile/{}的第{}页.html".format(self.search_name,index)
        return filename

    def analysis_url(self,generate_list):
        for generate_item in generate_list:
            html_code = self.parse_url(generate_item)
            self.save(html_code=html_code,index=generate_list.index(generate_item)+1)

    def run(self,num=1000):
        '''
            1.需要实现自动生成1000页的对应的url的列表
            2.使用这些url对数据进行请求，并且获取数据的解码格式
            3.保存好这些数据，每一页保存为一个.html文件，提示尽可能完善
        '''
        generate_list = self.generate_url_list(generate_num=num)
        self.analysis_url(generate_list=generate_list)


if __name__ == '__main__':
    search_name = input("请输入您想要下载的内容名称:").strip()
    num = input("请输入您需要下载的页数:").strip()
    spider = Tieba_spider(search_name)
    spider.run(int(num))