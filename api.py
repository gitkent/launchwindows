import requests
import getpass
import json
from operator import itemgetter
from pprint import pprint
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

import getCityID
import getScore

class launchwindows(Resource):
  def get(self, city=None):
    api_key = "2558ecc8196f8701fac72635245a8b09"
    cityID = getCityID.getCityID(city)

    if city is None:
      d = []
      i = 0
      while i < len(cityID): ## for each city in cities
        url = "https://api.openweathermap.org/data/2.5/forecast?id={ct}&appid={key}&units=metric".format(ct=cityID[i], key=api_key)
        res = requests.get(url)
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
        i += 1

      ordered_data = sorted(d, key=itemgetter('score')) 
      result = {'launchWindows': [ordered_data[:5]]}

    else:
      url = "https://api.openweathermap.org/data/2.5/forecast?id={ct}&appid={key}&units=metric".format(ct=cityID, key=api_key)
      res = requests.get(url)
      data = res.json()

      city_name = data['city']['name']
      weather_list = data['list']

      d = []
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

      ordered_data = sorted(d, key=itemgetter('score')) 
      result = {'launchWindows': [ordered_data[:5]]}

    return jsonify(result)

app = Flask(__name__)
api = Api(app)
app.add_url_rule('/launchwindows',
                view_func=launchwindows.as_view('all'),
                methods = ['GET'])

app.add_url_rule('/launchwindows/<city>',
                view_func=launchwindows.as_view('city'),
                methods = ['GET'])

if __name__ == '__main__':
  app.run(port='5002',debug=True)