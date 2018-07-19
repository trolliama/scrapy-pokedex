import mysql.connector as pymysql


CONFIG = {'user': 'root',
          'password': 'cdc121022',
          'host': 'localhost',
          'database': 'pokedex'}

def queryCategoria(categoria):
    con = pymysql.connect(**CONFIG)
    cursor = con.cursor()

    sql = "SELECT id from categorias where categoria=%s"
    cursor.execute(sql, (categoria,))
    result = cursor.fetchone()
    
    cursor.close()
    con.close()

    print(type(result),"tipo resultdo")
    return result