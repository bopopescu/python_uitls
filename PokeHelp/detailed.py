import requests
import re

def show(list):
    for li in list:
        print(li)

def find(pm):
    print(pm)

    date = []

    reponse = requests.get(pm[3])
    html = reponse.text
    html = html.replace('\n' , '')

    #print(html)

    rex = '获得方式.*?</table>'
    placeList = re.findall(rex , html , re.I)
    #print(placeList)
    placeList = placeList[1]

    #print(placeList)
    rex = '<tr.*?</tr>'
    _placeList = re.findall(rex , placeList , re.I)
    del _placeList[0]
    _placeList.pop()
    #show(_placeList)




    for place in _placeList:
        v = []
        #print(place)
        v1 = []
        v2 = []
        #print(place)
        rexPlace = '<td.*?</td>'
        ver = re.findall(rexPlace , place , re.I)
        #print(ver[0])
        _ve = re.findall('>.*?<' , ver[0] , re.I)

        _v1 =''
        for ve in _ve:
            if len(ve) > 5:
                ve = ve.replace('&#160;' , '')
                ve = ve.replace('>', '')
                ve = ve.replace('<', '')
                _v1 = _v1 + ve + '/'
        _v1 = _v1[:-1]
        #v1.append(_v1)

        _v3 = ''
        place = re.findall('title.*?</a>', ver[1])
        #print(ve , place)
        if len(place) < 1:
            #v2.append('无可捕捉地')
            _v3 = '无可捕捉地'
        else:
            for _place in place:
                v3 = []
                #print(_place)
                pl = re.findall('>.*?<' , _place , re.I)
                pl = pl[0]
                pl = pl.replace('>' , '')
                pl = pl.replace('<' , '')
                #v3.append(pl)
                _v3 = _v3 + pl + ' '

                #v2.append(v3)
            _v3 = _v3[:-1]
            #v2.append(_v3)
                    #print(v1, _place)

        fang = ''
        fin = re.findall('>.*?<' , ver[2])
        for fi in fin:
            #print(fi)
            fi = fi.replace('>' , '')
            fi = fi.replace('<', '')
            fi = fi.replace('', '')
            if len(fi) > 1 :
                fang = fang + fi + '/'
                #print(v1, fi)
        fang = fang[:-1]


        #print(ver[3])
        bz = re.findall('>.*?<' , ver[3])
        bei = ''
        if len(bei) == 0:
            bei = '无'
        else:
            for b in bz:
                b = b.replace(' ','')
                b = b.replace('>', '')
                b = b.replace('<', '')
                b = b.replace('*', '')
                bei = bei + b
            pd = re.findall('譯名請求', bei)
            if len(pd) > 0:
                bei = '无'


        #print(bei)


        v.append(_v1)
        v.append(_v3)
        v.append(fang)
        v.append(bei)

        date.append(v)



    show(date)






#find([1, '001', '妙蛙种子', 'https://wiki.52poke.com/wiki/%E7%83%88%E9%9B%80'])
find([1, '001', '妙蛙种子', 'https://wiki.52poke.com/wiki/妙蛙种子'])