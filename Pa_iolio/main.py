


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
    "http://images.ioliu.cn/bing/LondonRadiometers_ZH-CN12114654989_1920x1080.jpg"
    "g_img={url: \"/az/hprichbg/rb/LondonRadiometers_ZH-CN12114654989_1920x1080.jpg"
    url = "https://www.bing.com/"
    driver.get(url)

   # print(driver.page_source)
    text = driver.page_source

    _url = re.findall(r"g_img=.*?.jpg" , text , re.I)
    print(_url[0])
    image_url = _url[0].replace("g_img={url: \"/az/hprichbg/rb/" ,"http://images.ioliu.cn/bing/")
    print(image_url)
   # urls = re.findall(r"href=\"http://im.*?.jpg", ss, re.I)

  #  "g_img={url: "/az/hprichbg/rb/LondonRadiometers_ZH-CN12114654989_1920x1080.jpg",id:'bgDi"

    # index = 1
    # while index <= 21:
    #     url = "http://bing.ioliu.cn/?p=%s"%(index)
    #     #print(url)
    #     r = requests.get(url)
    #     html = r.text
    #
    #     s = r.text
    #     ss = s.replace(" ", "")
    #     urls = re.findall(r"href=\"http://im.*?.jpg", ss, re.I)
    #
    #     _num = 1
    #     for i in urls:
    #         if _num % 2 == 1:
    #             print(i)
    #         _num = _num + 1
    #
    #
    #     index = index + 1




main()