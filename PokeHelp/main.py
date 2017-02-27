import re
import  requests

url = 'https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88'
reponse = requests.get(url)

html = reponse.text
html = html.replace('\n' , '')
#print(html)

rex = '<table class="a-c roundy eplist bgl-一般 b-一般 bw-2">.*</table>'
tbodyList = re.findall(rex , html , re.I)
#print(tbodyList[0])

rex = '<tr>.*?</tr>'
pmList = re.findall(rex , tbodyList[0] , re.I)

verIndex = 0
_pmList = []

for pm in pmList:
    #print(pm)
    _pm = []

    index = re.findall('<td colspan="4">', pm, re.I)
    if len(index) > 0:
        verIndex = verIndex + 1

    rexid = '#[0-9]*'
    id = re.findall(rexid , pm , re.I)
    if len(id) > 0:
        _id = id[0]
        _id = _id[1:]
        _pm.append(verIndex)
        _pm.append(_id)

        rexName = 'title=".*?"'
        name = re.findall(rexName , pm , re.I)
        _name = name[0]
        _name = _name[len('title="') : len(_name) - 1]
        #print(_name)
        _pm.append(_name)

        _wiki = 'https://wiki.52poke.com/wiki/' + _name

        #print(_wiki)

        _pm.append(_wiki)

        _pmList.append(_pm)

for pm in _pmList:
    from detailed import  find
    find(pm)