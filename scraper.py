#! /usr/bin/python3
import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://nerdstore.com.br/categoria/especiais/game-of-thrones/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for product in soup.find_all('li', 'product'):
    print('---------------------------------------------------------')
    print(product.h2.string)
    print('---------------------------------------------------------')
    print(product.img.get('src'))
    print('---------------------------------------------------------')
    print(product.span.get('data-gtm4wp_product_price'))
