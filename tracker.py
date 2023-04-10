import requests
from bs4 import BeautifulSoup
import json

scrap_params = [
        {'store': 'dia', 
         'url': 'https://diaonline.supermercadosdia.com.ar/bebida-energizante-monster-energy-mango-loco-473-ml-282433/p',
         'parent': 'span.vtex-product-price-1-x-currencyContainer',
         'child': 'span.vtex-product-price-1-x-currencyInteger'},

        {'store': 'disco', 
         'url':  'https://www.disco.com.ar/bebida-energizante-monster-mango-loco-473-ml/p'},

        {'store': 'carrefour', 
         'url':  'https://www.carrefour.com.ar/bebida-energizante-monster-mango-loco-473-ml-655265/p',
         'parent': 'span.lyracons-carrefourarg-product-price-1-x-currencyContainer',
         'child': 'span.lyracons-carrefourarg-product-price-1-x-currencyInteger'}
         ]


def scraper():
    for n in scrap_params:
        store = n['store']
        url = n['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        if store == 'disco':
            #Exception because this website doesn't show price in plain text on html.parser
            soup = soup.find("script", {"type": "application/ld+json"})
            data = json.loads(soup.text)
            price_text = data["offers"]["lowPrice"]
        else:
            price_int = soup.select_one(f"{n['parent']} > {n['child']}")
            price_text = price_int.text
        print(f'Monster Mango en {store} cuesta {price_text}.')

if __name__ == '__main__':
    scraper()
