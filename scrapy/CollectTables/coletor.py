from urllib.request import Request,urlopen
from bs4 import BeautifulSoup


def getHtmlTypesAbilitys(URLS):
    for url in URLS.keys():
        reqs = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_code = BeautifulSoup(urlopen(reqs).read(), 'html.parser').find('tbody')

        getDadosTypesAbilitys(html_code, url, URLS)


def getDadosTypesAbilitys(html, url, URLS):
    for link_data in html.find_all('a'):
        URLS[url](str(link_data.string))


def getCategorias(html_code):
    categorias = set()

    for tr in html_code.find_all('tr'):
        try:
            tr['style']
        except KeyError:
            td = tr.find_all('td', limit=4)[-1]
            if td.find('span'):
                print(1)
                categoria = td.find('span').string

            else:
                categoria = td.string.replace('Pokémon', '')

            categorias.add(categoria.strip())
    return categorias


