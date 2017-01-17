
import re
from time import sleep

import requests


webbase = 'http://www.ubiaoqing.com/hot/'


def getbqb(img_url , imagename):

    basepath = 'bqb3/'
    img_name = basepath + imagename
    r = requests.get(img_url)
    with open(img_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)

def anasrc(alltext):
    regu = '<img.*>'

    imagelist = re.findall(regu , alltext ,  re.I)
    for image in imagelist:
        src = ''
        text = ''
        reg = 'http://ubq.*jpg\"'
        srcL = re.findall(reg , image , re.I)
        for sr in srcL:
            src = sr[:len(sr) - 1]
        reg = 'alt=\".*\" '
        textL = re.findall(reg , image , re.I)
        for te in textL:
            text = te[5:len(te) - 2]
            text = text + '.jpg'

        if(len(src) > 10):
            getbqb(src , text)


    for image in imagelist:
        src = ''
        text = ''
        reg = 'http://ubq.*gif\"'
        srcL = re.findall(reg , image , re.I)
        for sr in srcL:
            src = sr[:len(sr) - 1]
       # print(src)
        reg = 'alt=\".*\" '
        textL = re.findall(reg , image , re.I)
        for te in textL:
            text = te[5:len(te) - 2]
            text = text + '.gif'
        if (len(src) > 10):
            getbqb(src, text)


def main():
    index = 59

    while index < 100:
        print('当前是   ' + str(index) + '  页')
        index = index + 1
        weburl = webbase + str(index)
        r = requests.get(weburl)
        anasrc(r.text)
        sleep(5)


if __name__ == '__main__':
    main()