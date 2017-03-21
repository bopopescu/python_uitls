import os
import re
from time import sleep

import requests

def getbqb(img_url , imagename , index):
    index = (int) (index / 10)
    index = 'bqb/bqb' + str(index)

    try:
        os.mkdir(index)
    except Exception :
        pass

    basepath = str(index) + '/'
    img_name = basepath + imagename

    try:
        r = requests.get(img_url)
        with open(img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
    except Exception :
        print('index:  ' + index + '   img_url: ' + img_url + '  is bad url')


def checkparentname(html):
    # print (html)

    par = re.findall('"#df0000"><b>.*?</b>' , html)
    if len(par) > 0:
        par = par[0]
        par = par[len('"#df0000"><b>'):len(par) - len('</b>')]
        return par
    else :
        return '未分类'



def genImagepager(name , url):
    print(name, url)
    parentname = '未分类'
    if '福利' in name:
        parentname = '福利'
    elif '精选游戏' in name:
        parentname = '精选游戏'
    elif '手机' in name:
        parentname = '手机'



    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    html = reponse.text

    parentname = checkparentname(html)

    # print(html)

    imagetList = re.findall('http://www.gamersky.com/showimage/id_gamersky.shtml\?http.*?"' , html)
    for image in imagetList:
        print(image)






def getImagePageconter(name , url):
    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    html = reponse.text
    print (url)

    pageCount = re.findall('class="page_css.*下一页' , html.replace('\n' , ''))
    # print (pageCount)
    pageCountlist = re.findall('http.*?shtml' , pageCount[0])
    index = 0
    # while index < 1:
    while index < len(pageCountlist) - 1:
        # print (paœgeCountlist[index])
        genImagepager(name , pageCountlist[index])
        index = index + 1



def main():
    webbase = 'http://db2.gamersky.com/LabelJsonpAjax.aspx?jsondata={%22type%22:%22updatenodelabel%22,%22isCache%22:true,%22cacheTime%22:60,%22nodeId%22:%2220117%22,%22isNodeId%22:%22true%22,%22page%22:'
    index = 0
    # while index < 22:
    while index < 22:
        index = index + 1
        _webbase = webbase + str(index) + '}'
        # print (_webbase)

        reponse = requests.get(_webbase)
        reponse.encoding = 'utf-8'
        html = reponse.text

        # print(html)


        liList = re.findall('<div class.*?</div>' , html)

        for li in liList:
            if 'img' in li:
                addressList = re.findall('http://.*?.shtml' , li)
                addressList = addressList[0]
                # print (addressList)
                name  = re.findall('alt=\".*?\"' , li.replace('\\' , ''))
                name = name[0]
                name = name[len('alt="') : len(name) - 1]
                # print (name)
                getImagePageconter(name ,addressList)


    # print (html)



if __name__ == '__main__':
    # main()
    getImagePageconter('每周壁纸精选：形容美丽有三宝 颜好、腰软、身材棒' , 'http://www.gamersky.com/ent/201703/881616.shtml')