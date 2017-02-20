import re
import requests


i = 0
#f = open('some1/file.txt', 'a')

while i < 73:

    i = i + 1
    url = 'http://bbs.tianya.cn/post-16-627945-'
    url = url + str(i) + '.shtml'

    print(url)

    reponse = requests.get(url)
    html = reponse.text

    html = html.replace('\r' , ' ')
    html = html.replace('\n' , ' ')
    html = html.replace('\t' , ' ')

    rex = '<div class="atl-item.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>'
    atl_item_list = re.findall(rex , html , re.I)

    for atl_item in atl_item_list:

        page = atl_item
        rex_name = 'host=\".*?\"'
        host = re.findall(rex_name , page , re.I)

        if host[0] == 'host="老夜"':
            rex_bbs_content = '<div class="bbs-content">.*</div>'
            bbs_content = re.findall(rex_bbs_content, page, re.I)
            bbs_content = bbs_content[0].replace('<div class="bbs-content">' , '')
            bbs_content = bbs_content.replace('\u3000\u3000', '')
            bbs_content = bbs_content.replace('<br>', '\n')
            bbs_content = bbs_content.replace('</div>', '')
            bbs_content = bbs_content.replace(' ', '')

            print(bbs_content)

            #f.write(bbs_content)


#f.close()