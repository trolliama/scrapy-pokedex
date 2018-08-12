from BcddConnect.InsertDataPokes import *


class ScrapyTbNxN():

    def __init__(self, pokeid):
        self.poke_id = pokeid

    def collectSexo(self, div):
        icons = list(map(lambda x: x['class'][1], div.find_all('i'))) # vai retirar apenas os valores das classes, o retorno é um split() do valor, por isso uso o índice '1'

        if not icons:
            sexo = ['?']
        elif len(icons) > 1:
            sexo = ['M', 'F']
        else:
            sexo = ['M'] if icons[0] == 'icon_male_symbol' else ['F']
        
        insert_sexo(sexo, self.poke_id)


    def collectAbilitys(self, li):
        abilitys = []
        for span in li.find_all('span', class_='attribute-value'):
            abilitys.append(span.string)

        insert_abilitys(abilitys, self.poke_id)


    def collectTypes(self, url):
        div = url.find('div', class_='dtm-type')
        types = []

        for tag in div.find_all('a'):
            types.append(tag.string)

        insert_type(types, self.poke_id)


    def collectWeaknesses(self, url):
        div = url.find('div', class_='dtm-weaknesses')
        weaks = []

        for link in div.find_all('a'):
            weak = link['href'] # Retira o link da tag
            ind = weak.find('=') + 1 # Procura pela substring e adiciona mais um para começar a partir da primeira letra do tipo

            weaks.append(weak[ind: ].capitalize())

        insert_weaknesses(weaks, self.poke_id)