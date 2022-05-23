import controller_dml as dml
import controller_ddl as ddl


if __name__ == '__test__':
    ddl.create_db("log_data_prueba")
    ddl.create_table("log_data_prueba", "log")
    dml.insertLog("log_data_prueba", "2021-02-22","INFO","id.trabajoya.equis",20)

