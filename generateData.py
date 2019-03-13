import requests
import json

import getScore

def generateData(id,u,d):
  res = requests.get(u)
  data = res.json()

  city_name = data['city']['name']
  weather_list = data['list']

  index = 0
  while index < len(weather_list):
    temp = weather_list[index]['main']['temp']
    speed = weather_list[index]['wind']['speed']
    direction = weather_list[index]['wind']['deg']
    datetime = weather_list[index]['dt_txt']
    score = getScore.getScore(temp,speed,direction)
    
    tmp_dict = {}
    tmp_dict["location"] = city_name
    tmp_dict["datetime"] = datetime
    tmp_dict["score"] = score
    d.append(tmp_dict)
    index += 1

  return d