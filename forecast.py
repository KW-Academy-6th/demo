import requests
def forecast():
    from datetime import datetime,timedelta
    # 실제함수
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")#원하는 문자열형식으로
    # print forecast data
    import json
    # def forecast():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    key = 'TwoMG6Z71zy+QFydVUxVupQLdYSXX/1qg63Da6n4bf4z69mofJAZCe3byVt2j66m/CFRtqizSwYDG7obG/Y5FQ=='
    todaydate=datetime.today().strftime("%Y%m%d") # 오늘 날짜를 불러오기위한 함수
    params = {
        'serviceKey': key,
        'pageNo': '1',
        'numOfRows': '1000',
        'dataType': 'JSON',
        'base_date': yesterday,
        'base_time': '2300', #그전날11시 기준예보으로 
        'nx': '60',#서울 기준 
        'ny': '127'

    }

    # 수정한다 
    response = requests.get(url, params=params)

    json_data = response.json()
    RAIN=[]# 시간당 비가 오는 횟수 저장
    forecastdata=[]
    #예측날짜는오늘로 
    for item in json_data['response']['body']['items']['item']:
        #일 최고온도 하나씩
        if item['fcstDate']==todaydate and item["category"] == "TMX" :
            forecastdata.append(("TMX"+item['fcstValue']))
        #일 최저온도 하나씩
        if item['fcstDate']==todaydate and item["category"] == "TMN" :
            forecastdata.append(("TMN"+item['fcstValue']))
    #     현재온도 시간별
        if item['fcstDate']==todaydate and item["category"] == "TMP" and item['fcstTime']=='0800':
            forecastdata.append(("TMP"+item['fcstValue']))

    #     습도 시간별
        if item['fcstDate']==todaydate and item["category"] == "REH"and item['fcstTime']=='1100':
            forecastdata.append(("REH"+item['fcstValue']))
    #     강수형태 시간별
        if item['fcstDate']==todaydate and item["category"] == "PTY"and item['fcstTime']=='1100':

            forecastdata.append(("PTY"+item['fcstValue']))
    #     강수확률 60 넘는게 있으면 비온다 1 비 안온다0
        if item['fcstDate']==todaydate and item["category"] == "POP":
            if int(item['fcstValue'])>=60: #반복문 돌면서 비가 오는 시간대를 전부체크
                RAIN.append(1)#
    #비오는시간이 6시간이상이면  비온다 1 비 안온다0
    if RAIN.count(1)>=6:
        forecastdata.append(1)
    else:
        forecastdata.append(0)
    #         print((item["fcstValue"]))<class 'str'>
    return forecastdata
print(forecast())