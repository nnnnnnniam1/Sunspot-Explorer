# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
import requests
import json
from PyNaver import NaverCloudPlatform

city = "Seoul"
apiKey = "55aa6ff0030ca82f0dadf00ab53d20fd"
lang = 'kr'
units = 'metric'
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
data = json.loads(result.text)


# print(data)
#
# # 지역 : name
# print(data["name"],"의 날씨입니다.")
# # 자세한 날씨 : weather - description
# print("날씨는 ",data["weather"][0]["description"],"입니다.")
# # 현재 온도 : main - temp
# print("현재 온도는 ",data["main"]["temp"],"입니다.")
# # 체감 온도 : main - feels_like
# print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
# # 최저 기온 : main - temp_min
# print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# # 최고 기온 : main - temp_max
# print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# # 습도 : main - humidity
# print("습도는 ",data["main"]["humidity"],"입니다.")
# # 기압 : main - pressure
# print("기압은 ",data["main"]["pressure"],"입니다.")
# # 풍향 : wind - deg
# print("풍향은 ",data["wind"]["deg"],"입니다.")
# # 풍속 : wind - speed
# print("풍속은 ",data["wind"]["speed"],"입니다.")

client_id = "xehpem1fza"
client_secret = "U9P5H440l8RhmLyyb41d0CTzgnyX73H4XAwhDRYX"

query = "서울특별시 강남구 강남대로 310"
endpoint = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
url = f"{endpoint}?query={query}&X-NCP-APIGW-API-KEY-ID={client_id}&X-NCP-APIGW-API-KEY={client_secret}"

res = requests.get(url)
# print(res.json())


ipstack_key = "8630ab0fb1ab374d7f232587551bd4ae"
send_url = 'http://api.ipstack.com/check?access_key=' + ipstack_key
r = requests.get(send_url)
j = json.loads(r.text)
# print(j)

lon = j['longitude']
lat = j['latitude']
print(lon, lat)

lon_lat_api = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(lon_lat_api)
data = json.loads(result.text)

print(data["weather"][0])

print(data)
# 자세한 날씨 : weather - description
print("날씨는 ",data["weather"][0]["description"],"입니다.")
# 현재 온도 : main - temp
print("현재 온도는 ",data["main"]["temp"],"입니다.")
# 체감 온도 : main - feels_like
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# 습도 : main - humidity
print("습도는 ",data["main"]["humidity"],"입니다.")
# 기압 : main - pressure
print("기압은 ",data["main"]["pressure"],"입니다.")
# 풍향 : wind - deg
print("풍향은 ",data["wind"]["deg"],"입니다.")
# 풍속 : wind - speed
print("풍속은 ",data["wind"]["speed"],"입니다.")


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


# print(mapData["results"]["area2"]["name"])
# print(mapData["results"]["area3"]["name"])


# client_id = "xehpem1fza"
# client_secret = "U9P5H440l8RhmLyyb41d0CTzgnyX73H4XAwhDRYX"
# api = NaverCloudPlatform(client_id, client_secret)
#
#
# coords = str(str(lon) + "," + str(lat))
# print(coords)
# res = api.reverse_geocoding(coords)
# print(res.json())




