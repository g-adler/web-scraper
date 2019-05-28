#! /usr/bin/python3
import requests
import urllib.request
from Product import Product
from bs4 import BeautifulSoup
import json

def getData():

    products = []
    url = 'https://nerdstore.com.br/categoria/especiais/game-of-thrones/'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('Erro na busca de Informações: ' + str(response.status_code))

    items = BeautifulSoup(response.text, 'html.parser')

    for item in items.find_all('li', 'product'):
        name = item.h2.string
        price = item.span.get('data-gtm4wp_product_price')
        img = item.img.get('src')
        product = Product(name, price, img)
        products.append(product)
    if not products:
        raise Execption('Erro na formação do Array')
    return products

def loadJson():

    products = getData()
    json_list = json.dumps([object.__dict__ for object in products])
    return json_list

loadJson()
