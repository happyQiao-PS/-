import requests

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36"}

# proxies = {
#     "http":"http://120.36.3.109:3128",
#     "https":"https://120.36.3.109:3128"
# }

url = "http://www.baidu.com"

session = requests.session()

response = session.get(url=url,headers=headers)

print(response.status_code)

print(response.cookies)