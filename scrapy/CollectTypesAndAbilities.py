from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
from BcddConnect.InsertTypes import insert_types

if __name__ == '__main__':
    urls = {'https://pokemondb.net/ability', 'https://pokemondb.net/type'}

    for url in urls:
        reqs = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_code = BeautifulSoup(urlopen(reqs).read(), 'html.parser').find('tbody')

        data = [link_data.string for link_data in html_code.find_all('a')]
        print(data)