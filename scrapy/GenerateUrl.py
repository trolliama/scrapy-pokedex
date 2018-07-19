from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
from scrapy.DescritorPokeName import PokeName

class GenerateUrl():
    poke_name = PokeName() # Descritor

    def __init__(self, poke_name):
        self.poke_name = poke_name

    def generate(self):
        """Função para gerar a url do segundo site usado para extrair os dados"""
        print(self.poke_name)
        try:
            reqs = Request('https://www.pokemon.com/br/pokedex/' + self.poke_name.lower(), headers={'User-Agent': 'Mozilla/5.0'})
            url = BeautifulSoup(urlopen(reqs).read(), 'html.parser')

            print("segunda url criada!")
        except Exception as e:
            print('Falha na criação da segunda url: ', e)
            return None

        return url
"""
def main():
    url2 = GenerateUrl('Nidoran♂').generate()
    url2 = GenerateUrl('Nidoran♀').generate()

main()"""