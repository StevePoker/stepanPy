import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

html_text = get_html("https://sinoptik.ua/погода-киев")
site = BeautifulSoup(html_text, "html.parser")
temper = site.select('.today-temp')
weather = temper[0].getText()
print("In Kiev now: " + weather)
