from 我的python函数库.parse_url import Parse_url

url = "http://10.29.222.226/eportal/InterFace.do?method=login"
data = {
    "userId": "ITS201606",
    "password": "201606",
    "service": "教学办公",
    "queryString": "wlanuserip%3D21e5a285e987a386514ab6f278a50723%26wlanacname%3Dd9d75cbe58ced701%26ssid%3D%26nasip%3D4c9ff00a9f7b29f8e3c32f9c523bdd73%26snmpagentip%3D%26mac%3D51f59c7b500d416934940041cd20a273%26t%3Dwireless-v2%26url%3D49c3499ef4d35403bab2ea466f597e6ca01ef10e502434aa3a03ff9a24d8966c5361ea9578d54a36%26apmac%3D%26nasid%3Dd9d75cbe58ced701%26vid%3D720febab39ae288a%26port%3D4f3e0f99fed4ac11%26nasportid%3D60733b29adccb934a74b04290c3ee976e9b526c28130ec4bd154c844dcd0c2816986857cb61f695d",
    "operatorPwd": "",
    "operatorUserId": "",
    "validcode": ""
}
p = Parse_url()
ret = p.parse(url, method="post", data=data)
print(ret)
