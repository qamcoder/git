import requests


def weather_forecast(city_name, url):
    api_key = '8d10261be2d0b5bfa9ca599de17be895'
    url = url.format(city_name, api_key)
    try:
        response = requests.get(url)
        json_data = response.json()
        if response.status_code == 200:
            main = json_data['main']
            return {"City": city, "Temperature": f"{main['temp']} C", 'Pressure': f"{main['pressure']} hpa", 'Humidity': f"{main['humidity']}%"}

        else:
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        print(f'Error {e}')


city = 'Kotli Loharan'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

data = weather_forecast(city, url)
for key, value in data.items():
    print(f"{key}: \t{value}")
