from bs4 import BeautifulSoup
import requests

OLX ='https://www.olx.kz/'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

def get_olx_data1(url):
    full_page = requests.get(url, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("h6", {"class": "16v5mdi"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('NO DATA...')
    return result

def get_olx_data2(url):
    full_page = requests.get(url, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("p", {"class": "10bogli"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('NO DATA...')
    return result

def get_olx_data3(url):
    full_page = requests.get(url, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "3lkihg"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('NO DATA...')
    return result
print(get_olx_data1(OLX))
print(get_olx_data2(OLX))
print(get_olx_data3(OLX))
