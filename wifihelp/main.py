


import requests
import mysql.connector





def save_sql(ssid , bssid , pwd):



    conn = mysql.connector.connect(user='root', password='root', database='wifihelp')
    cursor = conn.cursor()



    cursor_search = conn.cursor()
    #sql = 'select * from image where href = \'%s\' and dateid   BETWEEN  %d and %d' % (image_url, betweendate - 5, betweendate)
    sql = 'select * from wifitable where bssid = \'%s\' '%(  bssid)
    cursor_search.execute(sql)
    statu = cursor_search.fetchall()
    if len(statu) == 0:
        cursor.execute('insert into wifitable(ssid , bssid , pwd ) values (%s,%s,%s)', [ssid, bssid , pwd])
        print(ssid, bssid , pwd)

    conn.commit()
    cursor.close()

def getpwd(url):
    roponse = requests.get(url)
    html = roponse.text
    #print(html)

    import re
    pwd = re.findall('当前密码记录.*当前密码记录' , html , re.I)
    pwd = pwd[0]
    pwd = pwd.replace('当前密码记录' , '')
    pwd = pwd[2 : len(pwd) - 4]
    #print(pwd)
    return pwd

def getwifiBase(url):
    roponse = requests.get(url)
    html = roponse.text
    html = html.replace('\r' , '')
    html = html.replace('\n', '')
    html = html.replace('\t', '')


    import re
    listother = re.findall('<div class="content-main">.*</div>' , html , re.I)

    _index = 0
    for other in listother:
        _index = _index  + 1
        ww_url = re.findall('<a.*?</a>' , other , re.I)
        for w_url in ww_url:
            xieliu = re.findall('title="已泄露"' , w_url , re.I)
            if len(xieliu) > 0:
                index = _index
                rel_url = re.findall('href=\".*?\"', w_url, re.I)
                base_url = rel_url[0][len('href="'):len(rel_url[0]) - 1]
                listwifi = re.findall('.*?/' , base_url , re.I)
                sid = listwifi[2][:len(listwifi[2]) - 1]
                bsid = listwifi[3][:len(listwifi[3]) - 1]
                real_url = 'http://www.wifi4.cn' + base_url

                pwd = getpwd(real_url)


                save_sql(sid, bsid , pwd)


    try:
        getwifiBase(real_url)
    except :
        print("getwifiBase error")





if __name__ == '__main__':
    getwifiBase('http://www.wifi4.cn/wifi/test/010101010104/')