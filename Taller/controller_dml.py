import sqlite3 as sql


def insert_log(db, lista):
    connect = sql.connect(db)
    cursor = connect.cursor()
    query = "INSERT INTO log (fecha,tipo_mensaje,archivo,linea) VALUES (?, ?, ?, ?)"
    cursor.executemany(query,lista)
    connect.commit()
    connect.close()

def select_log(db):
    connect = sql.connect(db)
    cursor = connect.cursor()
    query = "SELECT * FROM log"
    cursor.execute(query)
    for row in cursor:
        print(str(row[0])+" - "+str(row[1])+" - "+str(row[2])+" - "+str(row[3])+" - "+str(row[4]))
    connect.close()


