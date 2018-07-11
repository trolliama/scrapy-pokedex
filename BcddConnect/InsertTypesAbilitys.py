import mysql.connector as pymysql


CONFIG = {'user': 'root',
          'password': 'cdc121022',
          'host': 'localhost',
          'database': 'pokedex'}


def insert_types(tipo):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    add_type = "INSERT INTO tipos(tipo) VALUES(%s)"

    cursor.execute(add_type, (tipo))
    con.commit()

    cursor.close()
    con.close()


def insert_ability(ability):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    add_ability = "INSERT INTO habilidades(nome_habilidade) VALUES(%s)"

    cursor.execute(add_ability, (ability))
    con.commit()

    cursor.close()
    con.close()


