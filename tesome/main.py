import requests , re
import time

from sendEmail import send

_ip = '0.0.0.0'


def checkip(ip):
    global _ip
    print 'old ip:' + _ip
    if _ip == ip:
        print 'meishi'
    else:
        print 'youshi'
        _ip = ip
        send(ip)

def getIp():
    try:
        reponse = requests.get('http://city.ip138.com/ip2city.asp')
        html = reponse.text
        ip = re.findall('\d+\.\d+\.\d+\.\d+' , html)
        print  ip[0]
        checkip(ip[0])
    except Exception:
        print 'error'

def main():
    global _ip
    index = 0
    while True:
        getIp()
        index = index + 1
        print index
        time.sleep(10)




main()
