import requests
from flask import Flask, request, redirect, render_template, url_for
city = None
app = Flask(__name__)


def weather_forecast(city_name, url):
    api_key = '8d10261be2d0b5bfa9ca599de17be895'
    url = url.format(city_name, api_key)
    try:
        response = requests.get(url)
        json_data = response.json()
        if response.status_code == 200:
            main = json_data['main']
            return {"City": city, "Temperature": f"{main['temp']} C", 'Pressure': f"{main['pressure']} hpa",
                    'Humidity': f"{main['humidity']}%"}
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f'Error {e}')


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/city", methods=['POST'])
def _city():
    global city
    city = request.form["city_name"]
    return redirect(url_for("weather"))


@app.route('/weather')
def weather():
    data = weather_forecast(city, 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric')
    return render_template('weather.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
