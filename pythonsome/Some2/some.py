import re

import requests
#
# html = requests.get("http://chuansong.me/ideatech/")
# print html.text
#
#

url = 'http://www.runoob.com/w3cnote_genre/joke/page/2'

reponse = requests.get(url)
html = reponse.text
print (html)

html = html.replace('\n' , '')
list = re.findall('<div class="archive-list-item">.*?</i></h2>' , html )

print(list)