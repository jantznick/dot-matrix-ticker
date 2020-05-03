import requests
import os
from dotenv import load_dotenv
load_dotenv()

weatherApiKey = os.environ["WEATHERAPIKEY"]
weatherZip = os.environ["WEATHERZIP"]

openWeatherApiKey = weatherApiKey
zipCode = weatherZip
currentWeatherEndpoint = f'https://api.openweathermap.org/data/2.5/weather?zip={zipCode},us&appid={openWeatherApiKey}'
forecastEndpoint = f'https://pro.openweathermap.org/data/2.5/forecast/hourly?zip={zipCode},us&appid={openWeatherApiKey}'


def get_tempAndDescription():
	r = requests.get(currentWeatherEndpoint)
	# k > f = 9/5(K - 273.15) + 32
	kTemp = r.json()['main']['temp']
	fTemp = 9 / 5 * (kTemp - 273.15) + 32
	return (round(fTemp, 2), r.json()['weather'][0]['description'])
