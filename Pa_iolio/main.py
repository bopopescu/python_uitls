


# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import re

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time ,os
import requests

def main():

    driver = webdriver.PhantomJS(executable_path="/Users/haizhi/Desktop/Little_See/Little_See/Little_See_Server/phantomjs-2.1.1-macosx/bin/phantomjs")
    #driver = webdriver.PhantomJS(executable_path="/Users/yszsyf/Desktop/android/Little_See/Little_See_Server/phantomjs-2.1.1-macosx/bin/phantomjs")
    #driver.get("http://www.qdaily.com/tags/29.html")


    index = 1
    while index <= 21:
        url = "http://bing.ioliu.cn/?p=%s"%(index)
        #print(url)
        r = requests.get(url)
        html = r.text

        s = r.text
        ss = s.replace(" ", "")
        urls = re.findall(r"href=\"http://im.*?.jpg", ss, re.I)

        _num = 1
        for i in urls:
            if _num % 2 == 1:
                print(i)
            _num = _num + 1


        index = index + 1




main()