import requests
from bs4 import BeautifulSoup

class PageParser(object):
   def __init__(self):
       self.url = "https://sinoptik.ua/погода-киев"

   def temperature(self):
       response = requests.get(self.url)
       soup = BeautifulSoup(response.text, 'html.parser')
       tag_selected = soup.select('.today-temp')
       return tag_selected[0].text

weather = PageParser()

if __name__ == '__main__':
    temperature = weather.temperature()
    print('Kyiv: %s' % temperature)