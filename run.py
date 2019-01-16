import requests
from bs4 import BeautifulSoup

page = "https://sinoptik.ua/погода-киев"

class sinoptik():
    def weather(self):
        response = requests.get(page)
        site = BeautifulSoup(response.text, "html.parser")
        temper = site.select('.today-temp')
        weather_now = temper[0].text
        print(weather_now)
        return weather_now

temperature = sinoptik()
temperature.weather()