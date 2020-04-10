import requests
import sys
from lxml import etree

class FanyiSpider:
    def __init__(self):
        self.url = "http://m.youdao.com/translate"
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36"}
        self.data = {
            "inputtext":None,
            "type":"AUTO"
        }
    def __str__(self):
        return "请输入需要翻译的参数！"

    def postData(self):
        response = requests.post(url=self.url,headers=self.headers,data=self.data)
        return response.content.decode("utf-8")

    def parseData(self,html):
        htmlData = etree.HTML(html)
        data = htmlData.xpath('//*[@id="translateResult"]/li')
        return data

    def run(self,text=None):
        if text:
            self.data["inputtext"] = text
        else:return
        data = self.postData()
        word = self.parseData(data)
        list_text = [w.text for w in word]
        print(list_text[0])

if __name__ == '__main__':
    fanyi = FanyiSpider()
    try:
        text = sys.argv[1]
        if text:
            fanyi.run(text=text)
    except:
        print(fanyi)
