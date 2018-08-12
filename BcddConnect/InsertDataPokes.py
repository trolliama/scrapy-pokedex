import mysql.connector as pymysql
import BcddConnect.QueryTables as query


CONFIG = {'user': 'root',
          'password': 'cdc121022',
          'host': 'localhost',
          'database': 'pokedex'}


def insert_pokes(data):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    data = list(map(lambda x: str(x) if x else x, data)) # Só será transformado em string se o valor não for None 'if x else x'
    print(data)
    add_pokes = "INSERT INTO pokemons(\
            id, nome, vida, ataque, defesa,\
            ataqueSp, defesaSp, velocidade,\
            descricao, altura, peso, id_categoria,\
            id_evolucao)\
            values (%s, %s, %s, %s, %s,\
            %s, %s, %s, %s, %s, %s,\
             %s, %s)"
    
    try:
        cursor.execute(add_pokes, data)
    except pymysql.errors.DatabaseError as e:
        print(e)
        print("data original: ", data)
        data[8] = data[8].replace(data[1], data[1][:-1]) # Replace nome do pokémon nidoran macho e fêmea na descrição
        data[1] = data[1][:-1] # Recriar nome dos pokémons NIdoran macho e fêmea
        print('data modificada: ', data)
        cursor.execute(add_pokes, data)

    finally:
        con.commit()
        print('Adicionado dados do pokémon')

        cursor.close()
        con.close()


def insert_type(data, poke_id):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    add = "INSERT INTO pokemon_tipos(id_pokemon, id_tipo) values (%s, %s)"

    for tipo in data:
        id_tipo = query.queryTipos(str(tipo))[0]
        cursor.execute(add, (poke_id, id_tipo))

    con.commit()
    print("tipos do pokémon adicionados")

    cursor.close()
    con.close()


def insert_weaknesses(data, poke_id):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    add = "INSERT INTO pokemon_fraquezas(id_pokemon, id_tipo) values (%s, %s)"

    for weak in data:
        id_weak = query.queryTipos(str(weak))[0]
        cursor.execute(add, (poke_id, id_weak))

    con.commit()
    print("fraquezas do pokémon adicionadas")

    cursor.close()
    con.close()


def insert_sexo(data, poke_id):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    add = "INSERT INTO pokemon_sexos(id_pokemon, id_sexo) values (%s, %s)"

    for sexo in data:
        id_sexo = query.querySexos(sexo)[0]
        cursor.execute(add, (poke_id, id_sexo))

    con.commit()
    print("sexos do pokémon adicionados")

    cursor.close()
    con.close()


def insert_abilitys(data, poke_id):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    add = "INSERT INTO pokemon_habilidades(id_pokemon, id_habilidade) values (%s, %s)"

    for hab in data:
        id_hab = query.queryAbilitys(str(hab))[0]
        cursor.execute(add, (poke_id, id_hab))

    con.commit()
    print("habilidades do pokémon adicionadas")

    cursor.close()
    con.close()