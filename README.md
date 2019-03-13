# lauchwindows
## Pre-req
### Install required Python libraries
```
pip3 install requests
pip3 install flask
pip3 install flask_restful
pip3 install flask_jsonpify
```
### Create an account from OpenWeatherMap
1. Go to https://openweathermap.org/
2. Click Sign Up and enter your details
3. Once Signed in, go to API Keys Tab
4. Obtain your API Key, keep your API Key to be used later

## Start up Launch Windows app
1. Clone to your local
    ```
    git clone https://github.com/gitkent/launchwindows.git
    ```
2. Start the app
    ```
    cd launchwindows/
    python api.py
    ```
## Access to Data
Once the app is up and running, the API URL is http://127.0.0.1:5002/launchwindows
### Default cities
By default it selects and displays the top 5 optimal Rocket launching windows based on the weather forecast for the next 5 days from Melbourne, Hobart, Perth and Darwin. Go to browser and put this URL:
```
http://127.0.0.1:5002/launchwindows?key=<your_api_key>
```
### Query by city
You can also query launch windows by city for top 5 optimal Rocket launching windows for that city. On your browser:
```
http://127.0.0.1:5002/launchwindows/Melbourne?key=<your_api_key>
http://127.0.0.1:5002/launchwindows/Perth?key=<your_api_key>
http://127.0.0.1:5002/launchwindows/Darwin?key=<your_api_key>
http://127.0.0.1:5002/launchwindows/Hobart?key=<your_api_key>
```
Enjoy!