# Request深入

### 发送POST请求



- 用法
  - response = request.post("http://www.baidu.com/",data=data,headers=headers)
  - data是一个字典类型的数据

### 代理

- 反向代理：浏览器-->nginx-->服务器

  - 明确服务器的ip地址

- 正向代理：浏览器-->代理服务器-->Google服务器

  - 不知道服务器的具体地址

- 代理这个东西其实专门用来帮助我们访问的，加入目标服务器对你的ip设置了限制，那么也就意味着你自己是不可以访问的，但是别的机器可以呀！所以你让那个机器作为一个代理服务器，为你发送请求并且给你目标服务器的响应。典型的一个例子就是翻墙这个操作！很重要的！

- 用法：

  - `request.get("http://www.baidu.com",proxies=proxies)`

  - proxies的形式：字典

    ```python
    proxies = {
        "http":"http://12.34.56.128:9920",
        "https":"https://12.34.56.128:9920",
    }
    ```

- 使用代理ip的注意事项

  - 1.检查ip的可用性
    - 可以使用request添加超时参数来判断ip地址的质量
    - 在线代理ip检测网站(百度即可)
  - 2.准备一堆的ip地址，组成ip地址池，随机选择ip地址来使用
  - 3.如何选择代理ip，让使用次数比较少的ip地址被使用的可能性更大
    - {"ip":"http://"+ip,"times":0}
    - [{},{},{},{}]，对这个ip的列表按照使用次数来排序，选择使用次数较少的ip地址，从中随机选择一个。



### cookie和session的区别：

- cookie数据存放在客户的浏览器上，session数据存放在服务器上。
- cookie不是很安全，别人可以分析存放在本地的cookie并且进行cookie欺骗。
- session会在一定时间内保存在服务器上，当访问增多时，会比较占用你服务器的性能。
- 单个cookie保存的数据不能超过4k，很多浏览器都限制一个站点最多保存20个cookie。



- 带上cookie,session的好处
  - 可以请求到登录之后的页面
- 带上cookie,session的弊端
  - 一套cookie和session往往和一个用户对应
  - 请求太快或者请求次数太多，容易被服务器识别成为爬虫
- 因此不需要cookie的时候，尽量不要使用
  - 但是为了获取登录之后的页面，我们必须发送带有cookies的请求。



### 携带cookie进行请求

- 携带一堆的cookie进行请求，把cookie组成cookie池。 

### 处理cookies,sessions请求

- requests提供了一个叫做session类，来实现客户端和服务器端的回话保持

- 使用方法：

  - 实例化一个session对象

  - 让session发送get或者post请求

    ```python
    session = requests.session()
    response = session.get(url,headers)
    ```

  - 请求登录之后的网站的思路，使用requests携带的session进行操作

    - 实例化session
    - 先使用session发送请求，登录对网站，把cookie保存在session中
    - 在使用session请求登陆之后才能访问的网站，session能够自动的携带登录成功时保存在其中的cookie进行请求。

- 不发送post请求，使用cookie获取登录后的页面

  - cookie过期时间很长的网站
  - cookie过期时间之前能够拿到所有的数据，比较麻烦
  - 配合其他的程序一起使用，其他程序专门获取cookie，当前程序专门请求页面

- cookies参数的两种添加方式

  ```python
  headers = {
      "User-Agent":"xxx",
      "Cookie":"xxx"
  }
  response = requests.get(url=url,headers=headers)
  	#或者换成
  cookies = {xxxxxx}
  	#必须是一个字典，并且里面的数据全部都是键值对形式的数据才可以通过运算
      
      #字符串cookie转换成可以使用的字典形式的经典代码 ----> 字典推导式
      cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
  
  response = requests.get(url=url,headers=headers,cookies=cookies)
  	
  	#不过需要注意
  session = requests.session()
  response = session.post(xxx)
  	#这里session会自动保存cookie，下一次再要请求的时候直接用session请求就可以自带cookie相关的登录信息并且提交上去了
  ```

  