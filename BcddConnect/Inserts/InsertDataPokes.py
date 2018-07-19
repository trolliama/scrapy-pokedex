import mysql.connector as pymysql


CONFIG = {'user': 'root',
          'password': 'cdc121022',
          'host': 'localhost',
          'database': 'pokedex'}


def insert_pokes(data):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    data = tuple(map(lambda x: str(x) if x else x, data))
    
    add_pokes = "INSERT INTO pokemons(\
            id, nome, vida, ataque, defesa,\
            ataqueSp, defesaSp, velocidade,\
            descricao, altura, peso, id_categoria,\
            id_evolucao)\
            values (%s, %s, %s, %s, %s,\
            %s, %s, %s, %s, %s, %s,\
             %s, %s)"

    print(len(data))
    print(data)
    cursor.execute(add_pokes, data)
    con.commit()
    print('Adicionado dados do pokémon')

    cursor.close()
    con.close()


    