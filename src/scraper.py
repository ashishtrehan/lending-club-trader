import requests

url = 'https://en.wikipedia.org/wiki/List_of_ZIP_code_prefixes'
# url = 'https://pe.usps.com/Archive/HTML/DMMArchive20050106/print/L002.htm'
website_url = requests.get(url).text

from bs4 import BeautifulSoup




soup = BeautifulSoup(website_url, "lxml")
table = soup.findAll('table')

def build_zips(list):
    d = [x for x in list if x not in ('000 ','001 ','002 ','003 ','004 ')]
    cnt = 0
    for cnt,(v,w) in enumerate(zip(d[:-1],d[1:])):
        if cnt % 2 == 0:
            print ([v,w])
        else:
            pass

def scraper(url):
    website_url = requests.get(url).text
    tables = soup.findAll('table')
    raw = [[i.text for i in x.findAll('b')] for x in tables]
    a = [build_zips(l) for l in raw]
    return a

#
# city_state = table.findAll('a')
#
# cities = []

# for c in city_state:
#     print (c.get('title'))

# zips = table.findAll('b')

# for z in zips:
#     print (z.text)

# print (soup)
print (scraper(url))
