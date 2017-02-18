import re

import requests

i = 1
while i < 47:
    i = i + 1
    url = 'http://www.gamersky.com/handbook/201611/836206_'
    url = url + str(i)
    url = url  + '.shtml'

    print(url)

    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    html = reponse.text
    #print(html)

    rex = 'src="http://img1.gamersky.com/image2016/11/20161118.*?jpg'
    srclist = re.findall(rex , html , re.I)

    for src in srclist:
        src = src.replace('src="' , "")
        #print(src)

        r = requests.get(src)
        'http://img1.gamersky.com/image2016/11/20161118_xdj_187_7/gamersky_020small_040_20161118144956.jpg'
        img_name = src[len('http://img1.gamersky.com/image2016/11/20161118_xdj_187_7/') : ]
        img_name = 'some2/' + img_name
        with open(img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

    #print(len(srclist))
    #print(srclist)

