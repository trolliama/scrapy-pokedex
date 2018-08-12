from BcddConnect.InsertsTables import insert_types, insert_ability
from scrapy.CollectIndependentTables.coletor import getHtmlTypesAbilitys

if __name__ == '__main__':
    URLS = {'https://pokemondb.net/ability': insert_ability, 'https://pokemondb.net/type': insert_types}
    getHtmlTypesAbilitys(URLS)