
import json, requests, sys
import json
import os

from flask import Flask, render_template, json, request
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    location = request.form['lname']
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&APPID=592f0e34a29fa9ac9395ecca8acfb667'
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    w = weatherData['weather']
    country = weatherData['sys']
    temp = weatherData['main']
    return 'Current weather in ' + location.capitalize() + ' - ' + country['country'] + '\ntemperature: ' + str(
        temp['temp'] - 273.15) + '\nComment: ' + w[0]['main'] + '-' + w[0]['description']


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))

    print("Starting app on port %d" % port)

app.run(debug=False, port=port, host='0.0.0.0')