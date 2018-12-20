import requests

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_ZIP_code_prefixes').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,"lxml")



table = soup.find('table',{})

city_state = table.findAll('a')

cities = []

for c in city_state:
    print (c.get('title'))
