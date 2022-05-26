import sqlite3 as sql
# DDL para la creación de BD SQLite
# Para probar funcionamiento de BD, usar log_data_prueba


def create_db(db):
    connect = sql.connect(db)
    connect.commit()
    connect.close()


def create_table(db,table):
    connect = sql.connect(db)
    cursor = connect.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    connect.commit()
    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS "{table}" (
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
