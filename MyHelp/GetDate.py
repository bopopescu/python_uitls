
# -*- coding: utf-8 -*-

import re
import requests



def getWeaterDate():
    weather = []
    print 'getWeaterDate'
    print '获得当日天气'
    url = 'http://m.weathercn.com/index.do?language=zh-cn&id=102133'

    reponse = requests.get(url)

    html = reponse.text
    html = html.replace(' ', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')



    _weatherList = re.findall('<dl>.*?</dl>' , html)


    #print _weatherList[0]


    #获取当前天气
    temps = re.findall('<p>.*?</p>' , _weatherList[0])
    temps = temps[0]
    temps = temps.replace('<p>' , '')
    temps = temps.replace('</p>', '')
   # print temps
    weather.append(temps)


    #获取当日最高气温
    heightweather = re.findall('<strong>.*?</strong>' , _weatherList[0])
    heightweather = heightweather[0]
    heightweather = heightweather.replace('<strong>' , '')
    heightweather = heightweather.replace('</strong>' , '')
    heightweather = heightweather.replace(u'°', '')
   # print heightweather
    weather.append(heightweather)

    # 获取当日最低气温
    loweather = re.findall(u'<br><b>.*?</b>低温', _weatherList[0])
    loweather = loweather[0]
    loweather = loweather.replace('<br><b>','')
    loweather = loweather.replace(u'</b>低温', '')
    loweather = loweather.replace(u'°', '')
   # print loweather
    weather.append(loweather)

    #获取当前风力
    reponse = requests.get('http://e.weather.com.cn/d/mcy/101070201.shtml')
    reponse.encoding = 'utf-8'
    html = reponse.text
    wind = re.findall('</span><span>.*?</span></li>' , html)
    wind = wind[0]
    wind = wind.replace(u'</span><span>风力：' , '')
    wind = wind.replace('</span></li>', '')
    #print wind
    weather.append(wind)

    return weather


def getWeaterDateInHouer():
    #整点天气预报
    print '整点天气预报'

    hWeather = []

    reponse = requests.get('http://m.weathercn.com/hourly-weather-forecast.do?partner=&language=zh-cn&id=102133')

    html = reponse.text
    #print html
    html = html.replace(' ' , '')
    html = html.replace('\n', '')
    html = html.replace('\t', '')
    html = html.replace('\r', '')
    #print html
sdasd
    _hourList = re.findall('<dl>.*?</dl>' , html)
    #pdsdaarint _hourList[0]

    _weather = re.findall('</dd><dd>.*?</dd>' , _hourList[0])
    _weather = _weather[0]
    _weather = _weather.replace('</dd><dd>' , '')
    _weather = _weather.replace('</dd>', '')
    #print _weather

    hWeather.append(_weather)

    _temp = re.findall('<strong>.*?</strong>' , _hourList[0])
    _temp = _temp[0]
    _temp = _temp.replace('<strong>','')
    _temp = _temp.replace('&#176;</strong>', '')
    #print _temp

    hWeather.append(_temp)

    return hWeather

#print getWeaterDateInHouer()



# _w = getWeaterDate()
# for w in _w:
#     print w





