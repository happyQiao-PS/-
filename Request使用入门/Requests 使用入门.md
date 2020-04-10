# Requests 使用入门

### requests中解决编码的方法

- r.content.decode()
- r.content.decode("gbk")
- r.text

### Response.text和response.content的区别



- response.text
  - 类型：str
  - 解码类型：根据HTTP头部对响应的编码做出有根具的推测，推测文本的编码
  - 如何修改编码方式：`response.encoding='gbk'`
- response.content
  - 类型：bytes
  - 解码类型：没有指定
  - 如何修改编码方式：`response.content.decode("utf-8")`
- 推荐使用response.content.decode()的方式获取响应的html页面