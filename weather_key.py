import os
import requests
from datetime import datetime
import pprint

key = os.environ.get('w_key')

url = 'http://api.openweathermap.org/data/2.5/forecast'


def main():
    location = get_location_city_country()
    weather_data, error =  get_current_weather(location, key)
    if error:
        print('Location not found.')
    else:
        current_temp = get_tempreture(weather_data)
        print(f'The current temperature is {current_temp} C')


def get_location_city_country():
    city, country = '',''
    while len(city) == 0:
        city = input('Please enter the city: ').strip()

    while len(country) !=2 or not country.isalpha():
        country = input('Enter the 2 letter country code: ')
        location = f'{city}, {country}'
    return location
def get_tempreture(weather_temp):
    list_of_forecasts = data['list']
    for forecast in list_of_forecasts:

        temp = forecast['main'] ['temp']
        timestamp = forecast['dt_txt']
        forecast_date = datetime.fromtimestamp(timestamp)
        print (f'At {forecast_date} the temperature will be {temp} C')

def get_weather_description(weather_description):
    
    try:
        temp = weather_data['weather']['description']
        return temp
    except KeyError:
        print('This data is not in the format expected')
        return 'Unknown'

def get_wind_speed(wind_speed):
    
    try:
        temp = weather_data['wind']['speed']
        return temp
    except KeyError:
        print('This data is not in the format expected')

        return 'Unknown'

def get_current_weather(location, key):
    
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key }
        res = requests.get(url, params=query)
        res.raise_for_status()
        data = res.json()
        return data, None
    except Exception as ex:
        print(ex)
       # print(response.text)
        return None, ex


if __name__ == "__main__":
    main()

