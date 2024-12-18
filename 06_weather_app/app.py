from flask import Flask, render_template, request
import requests


app = Flask(__name__)

API_KEY = 'token'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# curl =  "http://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=your_api_key&units=metric"



@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'  
            }
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error = f"City '{city}' not found. Please try again."
    return render_template('weather.html', weather_data=weather_data, error=error)



if __name__ == '__main__':
    app.run(debug=True)