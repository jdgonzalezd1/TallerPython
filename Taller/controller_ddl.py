import sqlite3 as sql

def create_db():
    connect = sql.connect("log_data")
    connect.commit()
    connect.close()

def create_table():
    connect = sql.connect("log_data")
    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "log" (
            "id"	INTEGER NOT NULL,
            "fecha"	TEXT NOT NULL,
            "tipo_mensaje"	TEXT NOT NULL,
            "archivo"	TEXT NOT NULL,
            "linea"	INTEGER NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
        ) 
        """
    )
    connect.commit()
    connect.close()
