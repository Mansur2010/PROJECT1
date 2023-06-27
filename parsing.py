import requests
from bs4 import BeautifulSoup

ASUS = "https://www.olx.kz/d/obyavlenie/asus-rog-strix-g15-g531gt-IDnYMvy.html"
ACER = "https://www.olx.kz/d/obyavlenie/noutbuk-acer-v-otlichnom-sostoyanii-s-garantiey-IDnZ7Ew.html"
LENOVO = "https://www.olx.kz/d/obyavlenie/noutbuk-lenovo-g50-70-IDnZ41I.html"

hello = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def get_olx_data1(url):
    full_page = requests.get(url, headers=hello)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.find('h1', {'class': 'css-1soizd2'})
    result = []
    if convert:
        result.append(convert.text)
    else:
        result.append('no data')
    return result

def get_olx_data2(url):
    full_page = requests.get(url, headers=hello)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.find('h3', {'class': 'css-ddweki'})
    result = []
    if convert:
        result.append(convert.text)
    else:
        result.append('no data')
    return result

def get_olx_data3(url):
    full_page = requests.get(url, headers=hello)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.find('div', {'class': 'css-bgzo2k er34gjf0'})
    result = []
    if convert:
        result.append(convert.text)
    else:
        result.append('no data')
    return result



print(get_olx_data1(ASUS))
print(get_olx_data2(ASUS))
print(get_olx_data3(ASUS))

print(get_olx_data1(ACER))
print(get_olx_data2(ACER))
print(get_olx_data3(ACER))

print(get_olx_data1(LENOVO))
print(get_olx_data2(LENOVO))
print(get_olx_data3(LENOVO))
