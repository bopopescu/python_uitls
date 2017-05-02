
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


def main(questionid):

    index = 0
    _isEnd = False
    #
    # url = 'https://www.zhihu.com/api/v4/questions/%s/answers?limit=20&offset='%(questionid)
    # print(url)

    headers = {'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20' , 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}



    while not _isEnd:
        # url = 'https://www.zhihu.com/api/v4/questions/%s/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=%s'%(questionid , index)

        # url = 'https://www.zhihu.com/api/v4/questions/%s/answers?limit=20&offset=%s'%(questionid , index)

        url = 'https://www.zhihu.com/api/v4/questions/%s/answers?include=data[*].is_normal,content&limit=20&offset=%s'%(questionid , index)

        # print(url)

        index = index + 20

        reponse = requests.get(url , headers=headers)
        html = reponse.text

        print(html)

        alljson = json.loads(html)
        # print(alljson['data'])

        alldata = alljson['data']

        for data in alldata:

            pageJson = json.dumps(data)
            # print('pageJson' + pageJson)

            content = json.loads(pageJson)
            text = content['content']
            print( text )

        _isEnd = findIsEnd(html)




main(46312145)



