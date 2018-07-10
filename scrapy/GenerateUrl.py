from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
from string import ascii_letters


def generate_second_url(poke_name):
    """Função para gerar a url do segundo site usado para extrair os dados"""

    def tem_caractere_ilegal(s):
        """Verificação de caractere com acentuação"""

        return any(c not in ascii_letters for c in s)

    def recreate_name(poke_name):
        """ Recria o nome do pokemon para que ele esteja de acordo com a norma DNS
        para a url dos sites. Cada Símbolo é substituido por algo diferente e por isso
        foi criado um dicionário.
        """
        dic = {'♀': '-female', '♂': '-male', "'": "", '.': '', ' ': '-', ':': '', 'é': 'e'}

        for special_chars in dic.keys():
            try:  # Tente substiruir, caso não consiga retornará um erro e tentará novamente com outro caractere
                poke_name = poke_name.replace(special_chars, dic[special_chars])
            except:
                continue
        return poke_name

    if not poke_name.isalpha() or tem_caractere_ilegal(
            poke_name):  # Verifica se o nome do pokémon vai contra as regras de DNS
        poke_name = recreate_name(poke_name)
    try:
        reqs = Request('https://www.pokemon.com/br/pokedex/' + poke_name.lower(), headers={'User-Agent': 'Mozilla/5.0'})
        url_code = BeautifulSoup(urlopen(reqs).read(), 'html.parser')

        print("segunda url criada!")
    except Exception as e:
        print('Falha na criação da segunda url: ', e)
        return None

    return url_code