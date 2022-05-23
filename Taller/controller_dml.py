import sqlite3 as sql


def insertLog(db, fecha, tipoM, archivo, linea):
    connect = sql.connect(db)
    cursor = connect.cursor()
    query = f"INSERT INTO log (fecha,tipo_mensaje,archivo,linea) VALUES ('{fecha}','{tipoM}','{archivo}',{linea})"
    cursor.execute(query)
    connect.commit()
    connect.close()

