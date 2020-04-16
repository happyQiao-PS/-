# Requests小技巧

1. requests.util.dict_from_cookiejar  把cookie对象转换成字典
2. 请求SSL证书验证
   - response = requests.get("https://www.12306.cn/mormhweb/",verify=False)
3. 设置超时
   - response = requests.get(url,timeout=10)
4. 配合状态码判断是否请求成功
   - assert response.status_code == 200



### 接下来就是这些例子的实际使用

```python
import requests
response = requests.get("http://www.baidu.com")
#这个时候就会在response里面自动存在一个有服务器发送过来的cookie存在！

response.cookies
#调用这个属性可以查看当前的cookie但是需要注意这个cookie看到的是一个对象

requests.utils.dict_from_cookiejar(response.cookies)
#使用requests中的dict_from_cookiejar方法可以把cookie转换成一个字典。

--------------------------------------------------------------
#加入你想要把一个json字符串转换成cookie可以使用cookiejar_from_dicts方法
requests.utils.cookirjar_from_dict({"key":"value"})
```

### 使用retrying模块来帮助重新请求失败的url地址

安装方法：`pip install retrying`

- 或者可以下载云码解压进入解压后的目录，使用`python setup.py install`

命令来安装

- `***.whl`安装方法`pip install ***.whl`就可以安装了
- retrying的具体使用方法可以参考官方文档：<https://pypi.org/project/retrying/>