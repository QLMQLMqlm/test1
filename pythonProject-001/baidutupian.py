import json
import uuid

import requests

if __name__ == '__main__':
    word = input('请输入爬取的关键字：')
    page_num = int(input("请输入要爬取的页数："))

    urls = [
        f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7629181675624716186&ipn=rj&ct=201326592&is=&fp=result&fr=&word={word}"
        f"&queryWord={word}=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc"
        f"=&nc=1&expermode=&nojc=&isAsync=&pn={30 * (i + 1)}&rn=30&gsm=3c&1681818018511= "
        for i in range(page_num)
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 "
                      "Edg/112.0.1722.46 "
    }

    for url in urls:
        # 做请求的时候是json数据的话使用text
        # 做请求的时候是二进制的是使用content
        res = requests.get(url, headers=headers).text

        for item in json.loads(res)['data']:
            img_url = item.get('thumbURL', '')
            # 如果图片地址找不到，后面不需要执行
            if img_url == '':
                continue

            img_date = requests.get(img_url, headers=headers).content
            # file1 = 'D:\\study\\pic'
            with open(f"pic/{uuid.uuid4()}.jpg", 'wb') as f:
                f.write(img_date)
