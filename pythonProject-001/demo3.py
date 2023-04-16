# import requests
# from playwright.sync_api import sync_playwright
# dic1 = ((('测试一号'), ('测试二号'), ('测试三号')))
# print(type(dic1))
# dic2 = {"ceshiyihao":"ceshierhao ", "ceshinshanh0o":"ceshisihao "}
# print(type(dic2))
# dic3 = [1,2,3]
# print(type(dic3))
# dic3.remove(2)
# print(dic3)
# dic3.append(9)
# print(dic3)
# dic3.clear()
# print(dic3)

import  requests
# respose = requests.get("https://wwww.baidu.com")
# print(respose.status_code)
# print(respose.url)
# print(respose.headers)
# print(respose.cookies)
# print(respose.text)
# print(respose.content)
data = {"word":"hello"}
response = requests.post("http://httpbin.org/post", data=data)
print(response.content)