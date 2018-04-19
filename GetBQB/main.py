# coding: utf-8

import os
import re
from time import sleep

import requests


webbase = 'http://www.youbiaoqing.com/hot/'


def getbqb(img_url , imagename , index):
    # index = (int) (index / 10)
    # index = 'bqb/bqb' + str(index)
    index = 'bqb/bqb'

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

def anasrc(alltext , index):
    alltext = alltext.replace('\t' , '')
    alltext = alltext.replace('\r' , '')
    alltext = alltext.replace('\n' , '')
    alltext = alltext.replace(' ' , '')
    print alltext
  #  print('in anasrc')
    regu = 'blank"><img.*?>'

    imagelist = re.findall(regu , alltext ,  re.I)

    # imageurl = imageurl[0]
    for image in imagelist:
        imageurl = re.findall('http://img.*?\.jpg', image)
        try:
            imageurl = imageurl[0]
            # print 'imageurl: ' + imageurl
            name = re.findall('alt=".*?"' , image )
            name = name[0]
            name = name.replace('alt="' , '')
            name = name.replace('"' , '')
            name = name.replace(' ' , '')
            name = name + '.jpg'


            if (u'可爱' in name or  u'萌' in name) and u'tf' not in name:
                print name
                getbqb(imageurl , name , index)
        except Exception:
            pass

    #print('out anasrc')



def main():
    index = 0
    #max 5866
    # while index < 2:
    while True:
        print('is  ' + str(index) + '  page')
        index = index + 1
        weburl = webbase + str(index)
        print weburl
        r = requests.get(weburl)
        # print r.text
        anasrc(r.text , index)
       # sleep(5)


if __name__ == '__main__':
    main()
