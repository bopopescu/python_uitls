import re

import requests


def getWeaterDate():
    print 'getWeaterDate'

    reponse = requests.get('http://i.tq121.com.cn/j/wap/hours.js?2016')
    html = reponse.text
    print html
    