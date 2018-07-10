from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
from scrapy.GenerateUrl import generate_second_url

DATA_POKE = []


class Pokemon:
    def __init__(self, poke_id, html):
        self.poke_id = poke_id
        self.main(html)

    def main(self, html):
        for tr in html.find_all('tr', limit=806):
            if tr.td['data-sort-value'] != str(self.poke_id):
                continue

            url_2 = self.collect_data_tbpokemons(tr)
            print(self.poke_id)
            self.id_evol = self.collect_idevolucao(url_2)
            print(self.id_evol)

            """
            collect_data_tbtype_weaknes(url_cod_site2)
            collect_data_tbtype(url_cod_site2)
            collect_data_tbcategoria_tbhabilidades(url_cod_site2)
            collect_data_tbsexo(url_cod_site2)
            """

            self.poke_id += 1


    def collect_data_tbpokemons(self, tr):
        """Essa func tem como objetivo retirar dados do primeiro e segundo site
        1-
            -Id do pokémon
            -Nome
            -HP
            -Ataque
            -Defesa
            -Sp Ataque
            -Sp Defesa
            -Speed
        2-
            -Altura
            -Peso
            -descrição
            """

        def collect_desc(url):
            div = url.find('div', class_='version-descriptions active')
            DATA_POKE.append(div.p.string)

        def collect_altura_peso(url):

            div_code = url.find('div', class_='column-7')

            for li in div_code.find_all('li', limit=2):
                data = li.find('span', class_='attribute-value')
                DATA_POKE.append(data.string.split()[0])

        for td in tr.find_all('td')[1:]:
            classe_valor = td['class'][0]
            if classe_valor not in ('cell-icon', 'cell-total'):  # O atributo da tag 'cell-total' não me interessa
                data = td.string if not td.small else td.small.string
                DATA_POKE.append(data)

        url_code_site2 = generate_second_url(DATA_POKE[0])

        collect_altura_peso(url_code_site2)
        collect_desc(url_code_site2)

        print('Dados do pokémon {} coletado com sucesso!!'.format(DATA_POKE[0]))

        self.name, self.hp, self.atk, self.defesa,\
            self.spDefesa, self.spAtk, self.speed, self.altura,\
            self.peso, self.desc = DATA_POKE

        DATA_POKE.clear()

        return url_code_site2 # é retornado o atributo Nome


    def collect_idevolucao(self, url_code):
        div_classe = 'column-12 push-1 dog-ear-bl'
        url_code = url_code.find('div', class_=div_classe)

        li = url_code.find('li', class_='last')

        id_evol = li.find('span').string.strip()
        print('ev: ', id_evol[3:])
        if int(id_evol[3: ]) - self.poke_id > 0:
            id_evolucao = self.poke_id + 1

            print("Id da evolução do pokémon coletado com sucesso!")
            return str(id_evolucao)


if __name__ == '__main__':

    try:
        print('Tentando conexão...')
        req = Request('https://pokemondb.net/pokedex/all', headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(urlopen(req).read(), 'html.parser').find('tbody')

        print('Conexão feita com sucesso!\nIniciando coleta de dados...')

    except Exception as e:
        print('Falha na conexão: ', e)

    poke = Pokemon(1, html)

