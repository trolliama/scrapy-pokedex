from scrapy.DataCollectPokemon import Pokemon
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

if __name__ == '__main__':

    try:
        print('Tentando conexão...')
        req = Request('https://pokemondb.net/pokedex/all', headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(urlopen(req).read(), 'html.parser').find('tbody')

        print('Conexão feita com sucesso!\nIniciando coleta de dados...')
        
    except Exception as e:
        print('Falha na conexão: ', e)

    finally:

        poke_id = 1
        for tr in html.find_all('tr', limit=806):
            poke = Pokemon(poke_id)

            if tr.td['data-sort-value'] != str(poke_id):
                continue

            url_2 = poke.collect_data_tbpokemons(tr)
            poke.collect_idevolucao(url_2)
            
            poke()

            Pokemon.callFuncs(url_2, poke_id)

            poke_id += 1