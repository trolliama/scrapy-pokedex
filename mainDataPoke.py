from scrapy.DataCollectPokemon import Pokemon
from urllib.request import urlopen,Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup


if __name__ == '__main__':

    try:
        print('Tentando conexão...')
        req = Request('https://pokemondb.net/pokedex/all', headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(urlopen(req).read(), 'html.parser').find('tbody')

        print('Conexão feita com sucesso!\nIniciando coleta de dados...')

    except HTTPError as e:
        print('Falha na conexão: ', e)

    else:
        poke_id = int(input('id do pokémon inicial: '))
        for tr in html.find_all('tr', limit=917): # Foi colocado um limite pois o segundo site em que é usado para extrair informações não tem o último pokémon do primeiro site
            poke = Pokemon(poke_id)
        
            if tr.td['data-sort-value'] == str(poke_id):
                url_2 = poke.collect_data_tbpokemons(tr)
                poke.collect_idevolucao(url_2)
                poke()
                poke.collectTypes(url_2)
                poke.collectWeaknesses(url_2)

                poke_id += 1