from flask import Flask, request
from flask_restful import Resource, Api

class launchwindows(Resource):
    result = getWeather()
    return result

api.add_resource(launchwindows, '/launchwindows')

if __name__ == '__main__':
     app.run(port='5002')