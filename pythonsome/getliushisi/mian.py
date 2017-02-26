import re

import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
response = requests.get(url='http://chuansong.me/ideatech', headers=headers)
text = response.text


print(text)
list = re.findall('http://h.chuansong.me/.*jpg' , text , re.I)
print(list)
# response = requests.get("http://www.myexception.cn/other/")
# text = response.text
# list = re.findall('(/u/cms/www).*?(.jpg|png|gif|jpeg)' , text , re.I)
# print(list)