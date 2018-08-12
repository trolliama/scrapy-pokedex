import mysql.connector as pymysql


CONFIG = {'user': 'root',
          'password': 'cdc121022',
          'host': 'localhost',
          'database': 'pokedex'}

def queryCategoria(categoria):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor(buffered=True)

    sql = "SELECT id from categorias where categoria=%s"
    cursor.execute(sql, (categoria,))
    result = cursor.fetchone()
    
    cursor.close()
    con.close()

    return result


def queryTipos(tipo):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor(buffered=True)

    sql = "SELECT id from tipos where tipo=%s"
    cursor.execute(sql, (tipo,))
    result = cursor.fetchone()
    
    cursor.close()
    con.close()
    
    return result


def queryAbilitys(habilidade):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor(buffered=True)

    sql = "SELECT id from habilidades where nome_habilidade=%s"
    cursor.execute(sql, (habilidade,))
    result = cursor.fetchone()
    
    cursor.close()
    con.close()

    return result


def querySexos(sexo):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor(buffered=True)

    sql = "SELECT id from sexos where sexo=%s"
    cursor.execute(sql, (sexo,))
    result = cursor.fetchone()
    
    cursor.close()
    con.close()

    return result




