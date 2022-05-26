import controller_dml as dml
import controller_ddl as ddl
import controller_read_file as crf


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    database = "log_data_prueba"
    ddl.create_db(database)
    ddl.create_table(database, "log")
    dml.insert_log(database,crf.read_file())
    #dml.select_log(database)
