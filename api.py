from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from operator import itemgetter

import getCityID
import generateData

class launchwindows(Resource):
  def get(self, city=None):
    api_key = request.args.get('key', None)
    cityIDs = getCityID.getCityID(city)

    l = []
    if isinstance(cityIDs, list):
      i = 0
      while i < len(cityIDs): ## for each city in cities
        url = "https://api.openweathermap.org/data/2.5/forecast?id={ct}&appid={key}&units=metric".format(ct=cityIDs[i], key=api_key)
        all_data = generateData.generateData(cityIDs[i],url,l)
        i += 1

      ordered_data = sorted(all_data, key=itemgetter('score')) 
      result = {'launchWindows': [ordered_data[:5]]}

    elif isinstance(cityIDs, str):
      url = "https://api.openweathermap.org/data/2.5/forecast?id={ct}&appid={key}&units=metric".format(ct=cityIDs, key=api_key)
      all_data = generateData.generateData(cityIDs,url,l)

      ordered_data = sorted(all_data, key=itemgetter('score')) 
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