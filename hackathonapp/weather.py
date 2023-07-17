from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
from django.template.loader import render_to_string
from django.http import HttpResponse


def crawl_weather_data():

    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = bs(html.text,'html.parser')

    
    # 온도 출력
    tempdata1 = soup.find('div',{'class':'temperature_text'})
    tempdata2 = tempdata1.findAll('strong')
    first_element = tempdata2[0]
    temperature = first_element.text.split()[1]  
    temperature = temperature.replace('온도', '') 

    #print("현재 온도 : " + temperature)

    # 습도 출력
    humidata1 = soup.find('div',{'class':'temperature_info'})
    humidata2 = humidata1.findAll('div', {'class':'sort'})
    if len(humidata2) == 4:
        second_element = humidata2[2]
    else:
        second_element = humidata2[1]
    humi = second_element.text.split()[1]  
    humi = humi.replace('습도', '') 
    #print("현재 습도 : " + humi)

    # 날씨 텍스트 출력
    weatdata1 = humidata1.findAll('span')
    third_element = weatdata1[2].text
    #print("현재 날씨 : " + third_element)

    # 체감온도 출력
    realtemp = humidata2[0].text.split()[1] 
    realtemp = realtemp.replace('체감', '') 
    #print("체감 온도 : " +  realtemp)

    # 자외선 출력
    UVdata1 = soup.find('div',{'class':'report_card_wrap'})
    UVdata2 = UVdata1.findAll('span')
    UVdata3 = UVdata2[2].text
    # print("자외선    : " + UVdata3)

    return temperature, humi, realtemp, third_element, UVdata3

