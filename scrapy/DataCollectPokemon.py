from scrapy.GenerateUrl import GenerateUrl
from BcddConnect.Inserts.InsertDataPokes import insert_pokes
from BcddConnect.Querys.QueryTables import queryCategoria


class Pokemon:

    def __init__(self, poke_id):
        self.poke_id = poke_id
        self.data = [poke_id]


    def __call__(self):
        insert_pokes(self.data)


    @staticmethod
    def callFuncs(url_cod_site2, poke_id):
         """
            collect_data_tbtype_weaknes(url_cod_site2)
            collect_data_tbtype(url_cod_site2)
            collect_data_tbcategoria_tbhabilidades(url_cod_site2)
            collect_data_tbsexo(url_cod_site2)
            """


    def collect_desc(self, url):
            div = url.find('div', class_='version-descriptions active')
            self.data.append(div.p.string.strip())


    def collect_altura_peso(self, url):

        div_code = url.find('div', class_='column-7')

        for li in div_code.find_all('li', limit=2):
            data = li.find('span', class_='attribute-value')
            value = data.string.split()[0]

            self.data.append(value.replace(',', '.'))


    def collect_categoria(self, url):
        li = url.find("div", class_="column-7 push-7").li
        categoria = str(li.find('span', class_='attribute-value').string)
        id_categoria = queryCategoria(categoria)[0]
        self.data.append(id_categoria)


    def collect_data_tbpokemons(self, tr):
        "Essa func tem como objetivo retirar dados do primeiro e segundo site"

        for td in tr.find_all('td')[1:]:
            classe_valor = td['class'][0]
            if classe_valor not in ('cell-icon', 'cell-total'):  # O atributo da tag 'cell-total' não me interessa
                data = td.string if not td.small else td.small.string
                self.data.append(data)

        second_url = GenerateUrl(self.data[1]).generate()

        self.collect_desc(second_url)
        self.collect_altura_peso(second_url)
        self.collect_categoria(second_url)

        print('Dados do pokémon {} coletado com sucesso!!'.format(self.data[1]))

        return second_url


    def collect_idevolucao(self, url_code):
        div_classe = 'column-12 push-1 dog-ear-bl'
        url_code = url_code.find('div', class_=div_classe)

        li = url_code.find('li', class_='last')

        id_last = li.find('span').string.strip()
        id_evolucao = None

        print('ev: ', id_last[3:])
        if int(id_last[3: ]) - self.poke_id > 0:
            id_evolucao = self.poke_id + 1

            print("Id da evolução do pokémon coletado com sucesso!")
        self.data.append(id_evolucao)


