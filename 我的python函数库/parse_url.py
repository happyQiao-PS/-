import requests

class Parse_url:
    def __init__(self):
        self.headers = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        self.proxies = {}

    def _parse(self,url,headers,method,verify,data):
        response = None
        if method=="GET":
            response = requests.get(url,headers=headers or self.headers,verify=verify)
        elif method.upper()=="POST":
            response = requests.post(url,headers=headers or self.headers,data=data,verify=verify)
        return response

    def parse(self,url=None,headers=None,verify=True,method="GET",conversion=True,data=None):
        try:
            if url is not None and conversion:
                return self._parse(url,headers,method,verify,data).content.decode("utf-8")
            elif not conversion:
                return self._parse(url,headers,verify)
        except Exception as e:
            raise e