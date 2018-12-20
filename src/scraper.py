import requests
import re
import csv

url = 'https://en.wikipedia.org/wiki/List_of_ZIP_code_prefixes'
# url = 'https://pe.usps.com/Archive/HTML/DMMArchive20050106/print/L002.htm'
website_url = requests.get(url).text

from bs4 import BeautifulSoup




soup = BeautifulSoup(website_url, "lxml")
table = soup.findAll('table')

def hasNumbers(input):
    return any(char.isdigit() for char in input)

def cleaner(string):
    s = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,†*]", "", string)
    return s

def write_to_csv(l):
    with open("../dev-docker/SQL/output.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(["zipcode","city_state"])
        for item in l:
            for a in item:
                writer.writerow(a)

def build_zips(list):
    d = [x for x in list]
    zips = []
    for cnt,(v,w) in enumerate(zip(d[:-1],d[1:])):
        if hasNumbers(v)==True and hasNumbers(w)==False:
            d = v.split(' ')
            zip_unit = d[0]+'xx'
            state = cleaner(d[1])
            full = [zip_unit,w+', '+state]
            zips.append(full)
        else:
            pass
    return zips

def scraper(url):
    website_url = requests.get(url).text
    tables = soup.findAll('table')
    raw = [[i.text for i in x.findAll('b')] for x in tables]
    a = [build_zips(l) for l in raw]
    return a

write_to_csv(scraper(url))
