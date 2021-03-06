from scrapy.CollectIndependentTables.coletor import getCategorias
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from BcddConnect.InsertsTables import insert_category


if __name__ == '__main__':
    url = 'https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_category'

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_code = BeautifulSoup(urlopen(req).read(), 'html.parser').find('table', class_='sortable')

    for categoria in getCategorias(html_code):
        insert_category(categoria)
