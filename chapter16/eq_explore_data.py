import plotly.express as px
import json
mag=[]
lat=[]
lon=[]

with open('d.geojson', 'r', encoding='utf-8') as f:
    data=json.load(f)
    print(type(data),type(data['features']), type(data['metadata']['count']))
    #count의 데이터는 ""가 없으므로 int로 읽힌다(json의 특징)
    #딕셔너리 안의 딕셔너리 / 딕셔너리 안의 리스트를 읽는 방법 익히기
    #features가 리스트 이므로 for문으로 새로운 리스트에 추가한다.
    for feature in data['features']:
        mag.append(feature['properties']['mag'])
        # print(mag ,type(feature['properties']['mag']))
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])
        # print(lat)
        # print(lon)
title='Global Earth quakes'
fig=px.scatter_geo(lat=lat, lon=lon, size=mag, title=title)
fig.show()
#---------------------------------------------------------
#pip install plotly-express 설치해 줌