import requests
from bs4 import BeautifulSoup

class PageParser(object):
   def __init__(self, url):
       self.url = url

   def temperature(self):
       response = requests.get(self.url)
       soup = BeautifulSoup(response.text, 'html.parser')
       tag_selected = soup.select('.today-temp')
       print(tag_selected[0].text)

weather = PageParser("https://sinoptik.ua/погода-киев")
weather.temperature()