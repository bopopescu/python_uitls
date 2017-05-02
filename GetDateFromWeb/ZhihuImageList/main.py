import os

import requests
import re
import json


def findIsEnd(html):
    jsondata = json.loads(html)
    str1 = jsondata['paging']
    _paging = json.dumps(str1)
    paging = json.loads(_paging)
    is_end = paging['is_end']
    return is_end


def saveimage(imagesrc, relimage):
    parentname = imagesrc
    parentname = re.findall('com/.*?_r\.(?:jpg|png)' , parentname)
    parentname = parentname[0]
    parentname = parentname.replace('com/' , '')
    parentname = parentname.replace('_r', '')

    filename = 'image/' + relimage + '/' + parentname

    # print(filename)

    pd = os.path.isfile(filename)

    if pd:
        print(relimage + 'is create')
    else:
        try:
            r = requests.get(imagesrc)
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
        except Exception :
            print(filename + 'crate error')


def createFile(filename):
    filename = 'image/' + filename
    try:
        os.mkdir(filename)
    except Exception :
        print('文件夹创建失败')



def main(questionid ):
    headers = {'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}

    _url = 'https://www.zhihu.com/api/v4/questions/%s'%(questionid)
    titleReponse = requests.get(_url , headers = headers)
    titleHtml = titleReponse.text

    titleJson = json.loads(titleHtml)
    title = titleJson['title']
    title = str(title)
    title = title.replace('？' , '')
    # print(title)


    index = 0
    _isEnd = False



    createFile(title)

    while not _isEnd:
        url = 'https://www.zhihu.com/api/v4/questions/%s/answers?include=data[*].is_normal,content&limit=20&offset=%s'%(questionid , index)

        print(url)

        index = index + 20

        reponse = requests.get(url , headers=headers)
        html = reponse.text

        # print(html)

        alljson = json.loads(html)
        # print(alljson['data'])

        alldata = alljson['data']


        for data in alldata:

            pageJson = json.dumps(data)
            # print('pageJson' + pageJson)

            content = json.loads(pageJson)
            text = content['content']
            # print( text )

            _index = True
            imageList = re.findall('data-original=\"https?://pic.*?(?:png|jpg|jpeg)', text)
            for image in imageList:
                if _index:
                    image = image.replace('data-original=\"' , '')
                    print(image)
                    saveimage(image , title)
                _index = not _index


        # _isEnd = True
        _isEnd = findIsEnd(html)




main(46312145 )



