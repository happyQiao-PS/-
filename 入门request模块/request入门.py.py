import requests

url = "http://www.baidu.com/s"

url_sogou = "https://www.sogou.com/web"

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

params = {
    "wd":"新型冠状病毒"
}

params_sogou = {
    "query" : "新型冠状病毒"
}

#response = requests.get(url=url,headers=headers,params=params)

response = requests.get(url=url_sogou,headers=headers,params=params_sogou)

print(response.status_code)

print(response.content.decode())

#response Url :https://www.sogou.com/web?query=%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92
print(response.request.url)

print("------------------------------------------------------------------------------------------------")
print()
print()


#另外一种不得不学习胡python字符串拼接胡方式
print("hi:{}".format("hello world"))


url_sogou_split = "https://www.sogou.com/web?query={}".format("新型冠状病毒")

response = requests.get(url=url_sogou_split,headers=headers)

print(response.status_code)

print(response.request.url)