import os
import re
from time import sleep

import requests

# def getbqb(img_url , imagename , index):
#     index = (int) (index / 10)
#     index = 'bqb/bqb' + str(index)
#
#
#
#     basepath = str(index) + '/'
#     img_name = basepath + imagename
#
#     try:
#         r = requests.get(img_url)
#         with open(img_name, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=1024):
#                 f.write(chunk)
#     except Exception :
#         print('index:  ' + index + '   img_url: ' + img_url + '  is bad url')


def saveimage(parentname, relimage):
    parentname = 'image/' + parentname

    filename = re.findall('/.*?\..*' , relimage)
    filename = filename[0]
    filename = filename.split('/')
    filename = filename[len(filename) - 1]

    filename = parentname + '/' + filename

    pd = os.path.isfile(filename)

    if pd:
        print(relimage + ' finish')
    else:
        try:
            os.mkdir(parentname)
        except Exception :
            pass

        try:
            r = requests.get(relimage)
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
        except Exception :
            print(relimage + '   error')


def checkparentname(html):
    # print (html)


    par = re.findall('"#df0000"><b>.*?</b>' , html)
    par2 = re.findall('"#df0000"><strong>.*?</strong>' , html)
    par3 = re.findall('<strong>.*?</strong>' , html)
    if len(par) > 0:
        par = par[0]
        par = par.replace('"#df0000"><b>' , '')
        par = par.replace('</b>' , '')
        return par
    elif len(par2) > 0:
        par2 = par2[0]
        par2 = par2.replace('"#df0000"><strong>', '')
        par2 = par2.replace('</strong>', '')
        return par2
    elif len(par3) > 0:
        par3 = par3[0]
        par3 = par3.replace('<strong>', '')
        par3 = par3.replace('</strong>', '')
        return par3
    else :
        return '未分类'



def genImagepager(name , url):
    # print(name, url)
    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    html = reponse.text



    # if '福利' in name:
    #     if '本周' in name:
    #         parentname = '未分类'
    #     else:
    #         parentname = '福利'
    if '精选游戏' in name:
        parentname = '精选游戏'
    elif '手机' in name:
        parentname = '手机'
    else:
        parentname = checkparentname(html)


    if parentname == 'Anime':
        parentname = '动漫'
    elif parentname == 'Nature':
        parentname = '风景'
    elif parentname == 'Women':
        parentname = '美女'
    # elif parentname == 'Minimalism':
    #     parentname = '动漫'
    elif parentname == 'Space':
        parentname = '星空'
    elif parentname == '秋：':
        parentname = '风景'
    elif parentname == '节：':
        parentname = '节日'
    elif parentname == '漫：':
        parentname = '漫画'
    elif parentname == '水：':
        parentname = '风景'
    elif parentname == '景：':
        parentname = '风景'
    elif parentname == '游：':
        parentname = '游戏'
    elif parentname == '妹：':
        parentname = '美女'

    # elif parentname == 'Anime':
    #     parentname = '动漫'

    if '福利' in parentname:
        parentname = '福利'
    if '太空' in parentname:
        parentname = '星空'
    if '你懂' in parentname:
        parentname = '福利'
    if '二次元' in parentname:
        parentname = '二次元'
    if '妹子' in parentname:
        parentname = '福利'
    if '游戏' in parentname:
        parentname = '游戏'
    if '军事' in parentname:
        parentname = '军事'
    if '硬核' in parentname:
        parentname = '军事'
    if '机甲' in parentname:
        parentname = '机甲'
    if '战争' in parentname:
        parentname = '军事'
    if '风景' in parentname:
        parentname = '风景'
    if '美少女' in parentname:
        parentname = '美女'
    if '女' in parentname:
        parentname = '美女'
    if '星空' in parentname:
        parentname = '星空'
    if '电影' in parentname:
        parentname = '影视'
    if '哲理' in parentname:
        parentname = '哲理'
    if '游戏' in parentname:
        if '4K' not in parentname:
            parentname = '游戏'




    if '：' in parentname:
        parentname = parentname[:-1]


    parentname = parentname.replace(' ' , '')
    parentname = parentname.replace('/' , '')
    parentname = parentname.replace('特辑' , '')


    if len(parentname) < 1:
        parentname = '未分类'
    print(name , parentname, url)

    # print(html)

    imagetList = re.findall('http://www.gamersky.com/showimage/id_gamersky.*?\.shtml\?http.*?"' , html)

    for image in imagetList:
        relimage = re.findall('http://img.*"' , image)
        relimage = relimage[0]
        relimage = relimage[:len(relimage) - 1]
        print(relimage)

        saveimage(parentname , relimage)





def getImagePageconter(name , url):
    url = url.replace('\n' , '')
    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    html = reponse.text
    print(url)
    # print(html)

    pageCount = re.findall('class="page_css.*下一页' , html.replace('\n' , ''))
    # print (pageCount)
    try:
        pageCountlist = re.findall('http.*?shtml' , pageCount[0])
        index = 0
        # while index < 1:
        while index < len(pageCountlist) - 1:
            # print (paœgeCountlist[index])
            genImagepager(name , pageCountlist[index])
            index = index + 1
    except Exception:
        print(url + 'is bad')

#
# baselist = []

def main():
    webbase = 'http://db2.gamersky.com/LabelJsonpAjax.aspx?jsondata={%22type%22:%22updatenodelabel%22,%22isCache%22:true,%22cacheTime%22:60,%22nodeId%22:%2220117%22,%22isNodeId%22:%22true%22,%22page%22:'
    index = 12
    # while index < 1:
    while index < 22:
        print('index =  ' + str(index) )
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
                _base = []
                addressList = re.findall('http://.*?.shtml' , li)
                addressList = addressList[0]
                # print (addressList)
                name  = re.findall('alt=\".*?\"' , li.replace('\\' , ''))
                name = name[0]
                name = name[len('alt="') : len(name) - 1]

                # with open('baseaddress.txt', 'a' , encoding = 'utf-8') as f:
                #     f.write(name)
                #     f.write('\n')
                #
                # with open('baseaddress.txt', 'a') as f:
                #     f.write(addressList)
                #     f.write('\n')

                getImagePageconter(name ,addressList)




def test():
    with open('baseaddress.txt', 'r', encoding='utf-8') as f:
        base = f.readlines()

        index = 0

        while index < len(base):
            ba = base[index]
            ba = ba.replace('\n', '')
            index = index + 1
            baad = base[index]
            ba = ba.replace('\n', '')
            # print(ba , baad)
            index = index + 1
            getImagePageconter(ba, baad)




if __name__ == '__main__':
    main()
    # baselist = ''

    # test()



    # getImagePageconter('每周壁纸精选：形容美丽有三宝 颜好、腰软、身材棒' , 'http://www.gamersky.com/ent/201703/881616.shtml')