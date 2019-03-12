import requests
import getpass
import json
from operator import itemgetter
from pprint import pprint

import getCityID
import getScore

#api_key = getpass.getpass(prompt="Enter API Key: ")
api_key = "2558ecc8196f8701fac72635245a8b09"
#city = input("Enter city: ")
city = 'Mel'
cityID = getCityID.getCityID(city)

if isinstance(cityID, list):
  print("List")
  i = 0
  while i < len(cityID):
    url = "https://api.openweathermap.org/data/2.5/forecast?id={ct}&appid={key}&units=metric".format(ct=cityID[i], key=api_key)
    res = requests.get(url)
    data = res.json()

    city_name = data['city']['name']
    weather_list = data['list']
    json_dict = {}
    data = []

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
      data.append(tmp_dict)
      index += 1
      
    i += 1

    ordered_data = sorted(data, key=itemgetter('score')) 
    json_dict["launchWindows"] = ordered_data[:5]

    n = json.dumps(json_dict, indent=2)
    o = json.loads(n)
    pprint(o)

elif isinstance(cityID, str):
  print("String")
  url = "https://api.openweathermap.org/data/2.5/forecast?id={ct}&appid={key}&units=metric".format(ct=cityID, key=api_key)
  res = requests.get(url)
  data = res.json()

  city_name = data['city']['name']
  weather_list = data['list']

  json_dict = {}
  data = []

  index = 0
  while index < len(weather_list):
    #for key in weather_list[index]:
      temp = weather_list[index]['main']['temp']
      speed = weather_list[index]['wind']['speed']
      direction = weather_list[index]['wind']['deg']
      datetime = weather_list[index]['dt_txt']
      score = getScore.getScore(temp,speed,direction)
      
      tmp_dict = {}
      tmp_dict["location"] = city_name
      tmp_dict["datetime"] = datetime
      tmp_dict["score"] = score
      data.append(tmp_dict)
      index += 1

  ordered_data = sorted(data, key=itemgetter('score')) 
  json_dict["launchWindows"] = ordered_data[:5]

  n = json.dumps(json_dict, indent=2)
  o = json.loads(n)

  pprint(o)