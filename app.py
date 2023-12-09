# -*- coding: utf-8 -*-

from flask import Flask, render_template,request,jsonify
from datetime import datetime
import requests
import json

app = Flask(__name__)

#위도경도 정보 가져오기
ipstack_key = "8630ab0fb1ab374d7f232587551bd4ae"
send_url = 'http://api.ipstack.com/check?access_key=' + ipstack_key
r = requests.get(send_url)
j = json.loads(r.text)

lon = j['longitude']
lat = j['latitude']

# 날씨 데이터 가져오기 - OpenWeatherMap API Key
apiKey = "55aa6ff0030ca82f0dadf00ab53d20fd"
lang = 'kr'
units = 'metric'
lon_lat_api = f"hhttp://api.openweathermap.org/geo/1.0/reverse?lat={lat}8&lon={lon}&appid={apiKey}&lang={lang}&units={units}"



# OpenWeatherMap API 키
apiKey = "55aa6ff0030ca82f0dadf00ab53d20fd"
lang = 'kr'
units = 'metric'

lon_lat_api = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(lon_lat_api)
data = json.loads(result.text)

# 위도경도로 위치 찾기 - naveropenapi
client_id = "xehpem1fza"
client_secret = "U9P5H440l8RhmLyyb41d0CTzgnyX73H4XAwhDRYX"
coords = str(lon) + "," + str(lat)
output = "json"
orders = "addr"
endpoint = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
addrURL = f"https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?coords={lon},{lat}&orders={orders}&output={output}&X-NCP-APIGW-API-KEY-ID={client_id}&X-NCP-APIGW-API-KEY={client_secret}"

# 헤더
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret
}
# 요청
res = requests.get(addrURL)
mapData = res.json()
print(mapData)

# print(mapData["results"])
# print(mapData["results"][0]["region"])
area = mapData["results"][0]["region"]
print(area)
print(area["area1"]["name"])
print(area["area2"]["name"])
print(area["area3"]["name"])

def recommend_places(weather):
    # 현재 날짜 가져오기
    current_date = datetime.now().month

    # 날씨에 따라 객관적인 장소를 추천하는 함수
    if weather in ["Thunderstorm", "Drizzle", "Rain"]:
        return ["영화관", "쇼핑몰", "레스토랑"]
    elif weather == "Snow":
        # 12월에서 2월 사이에는 추가적인 눈썰매장, 아이스링크장, 스키장을 추천
        if 12 <= current_date <= 2:
            return ["눈썰매장", "아이스링크장", "스키장"]
        else:
            return ["실내 스포츠 시설", "실내 수영장", "실내 망원경 체험장"]
    elif weather in ["Mist", "Smoke", "Haze", "Dust", "Fog"]:
        return ["차 한잔의 여유", "도서관", "예술 전시관"]
    elif weather in ["Sand", "Ash", "Squall", "Tornado"]:
        return ["안전한 실내 활동", "도서관", "예술 전시관"]
    elif weather == "Clear":
        # 여름인 경우에는 7월부터 8월까지 수영장을 추가로 추천
        if 7 <= current_date <= 8:
            return ["공원", "산책로", "수영장"]
        else:
            return ["공원", "산책로"]
    elif weather == "Clouds":
        return ["미술관", "도서관", "카페"]
    else:
        return ["놀러갈 장소 추천이 없습니다."]



@app.route('/')
def index():
    return render_template('index.html', weather_data=data, area_data=area)

@app.route('/recommend-places')
def recommend_places_endpoint():
    # 날씨에 따라 장소 추천
    current_weather = request.args.get('weather')

    recommended_places = recommend_places(current_weather)

    # 결과를 JSON 형식으로 반환
    return jsonify(recommended_places)


if __name__ == '__main__':
    app.run(debug=True)

