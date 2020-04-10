# requests模块使用基础

## 发送简单的请求

- 需求，通过requests向百度首页发出请求，获取百度首页的数据

    `response = requests.get(url)`

### response的常用方法

    - response.text
    - response.content
    - response.status_code
    - response.request.headers
    - response.headers

## 发送带header的请求

- 为什么需要带上header？

  - 模拟浏览器，欺骗服务器，获取和浏览器一致的内容

  - header的形式：字典

  headers = {'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/54.0.1840.99 Safari/537.36'}

  - 用法：requests.get(url,headers=headers)

## 发送带参数的请求

- 什么叫做请求带参数

  - 例子1:<http://www.wokan.com/tutrial/server/2019/02/25/>
  
  - 例子2:<http://www.baidu.com/s?wd=iphone&c=b>

- 参数的形式：字典

    `kw = {"wd":"长城"}`

- 用法：`request.get(url,params=kw)`
