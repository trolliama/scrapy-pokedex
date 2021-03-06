from urllib.request import urlopen,Request, urlretrieve
from bs4 import BeautifulSoup
from os import mkdir
from scrapy import GenerateUrl



DIRNAME = './imagensPokemon'

def cria_dir():
    """Criação do diretório onde será baixada as imagens,
    se já existir simplesmente é avisado que o download está começando."""

    try:
        mkdir(DIRNAME)
    except FileExistsError:
        print('Diretório existente, fazendo download de imagens...')

def download_image(url, id):
    """Função para o download das imagens do pokemon.
    Especifique a partir de qual pokémon você deseja baixar as imagens 
    informando seu id.
    """
    for tr in url.find_all('tr', limit=917):
        td = tr.find('td', class_='cell-num cell-fixed')  #  Alguns pokémons com a tag 'small' na primeira tag 'td'
        
        if td['data-sort-value'] != str(id):       #  são pokémons que ja passaram, no entanto com um estilo diferente,
            continue                               #  estes não nos interessam e por isso é verificado se o ip ja foi repetido.
            
        td = tr.find('td',class_='cell-name')
        poke_name = td.a.string

        url = GenerateUrl(poke_name).generate()
        div_imagem = url.find('div', class_='profile-images')
        link_imagem = div_imagem.find('img')['src']

        pathArq = DIRNAME + '/' + str(id) + '.png'

        urlretrieve(link_imagem, pathArq)
        id += 1  # Adiciona mais um para o id do próximo pokémon

        print('Imagem do %s foi baixada' % poke_name)


if __name__ == '__main__':
    try:
        req = Request('https://pokemondb.net/pokedex/all', headers={'User-Agent': 'Mozilla/5.0'})
        url_cod = BeautifulSoup(urlopen(req).read(), 'html.parser').find('tbody')
    except Exception as e:
        print('Conexão falhada: ', e)

    else:
        print('conexão feita com sucesso!')
        cria_dir()
        download_image(url_cod, int(input("Qual id do pokémon inicial? ")))
