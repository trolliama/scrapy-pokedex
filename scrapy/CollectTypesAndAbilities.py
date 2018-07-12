from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
from BcddConnect.InsertsTables import insert_types, insert_ability


def getHtml():
    for url in URLS.keys():
        reqs = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_code = BeautifulSoup(urlopen(reqs).read(), 'html.parser').find('tbody')

        getDados(html_code, url)


def getDados(html, url):
    for link_data in html.find_all('a'):
        URLS[url](link_data.string)


if __name__ == '__main__':
    URLS = {'https://pokemondb.net/ability': insert_ability, 'https://pokemondb.net/type': insert_types}
    getHtml()