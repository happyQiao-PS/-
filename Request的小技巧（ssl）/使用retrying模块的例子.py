# from retrying import retry
# from time import sleep
#
# @retry(stop_max_attempt_number=4,wait_fixed=None)
# def runing():
#     print("尝试中！！！")
#     assert 1+1==1
#
# if __name__ == '__main__':
#     runing()
import json
import requests
import pprint

url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
response = requests.get(url,headers=headers)
ret = response.content.decode("utf-8")
ret1 = json.loads(ret)
with open("index.json","w",encoding="utf-8")as f:
    json.dump(ret1,f,ensure_ascii=False,indent=2)
