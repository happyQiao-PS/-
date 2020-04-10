# 寻找登录的post地址

- 1 在form表单中寻找action对应的url地址
  - post的数据是input标签中name的值作为键，真正的用户名密码作为值的字典，post的url地址就是action对应的地址。
- 2 抓包获取相应的url以及数据
  - chrome浏览器勾选pressive log选项就可以保证数据不会因为页面改变而改变了
  - 寻找post数据，确定参数
    - 参数不会变，直接使用，比如密码不是动态加密的时候。
    - 参数会变
      - 参数在当前的响应中
      - 通过js生成



### 定位需要的js

- 选择会触发js事件的按钮，点击event listener,找到js的位置。
- 通过chrome中的search all file来搜索url中的关键字。
- 通过添加断点的方式来自己试一试就好了！