import traceback
from util.db_connection import Db_Connection
import pandas as pd

def transformar_fechas ():

    try:
        type = 'mysql'
        host = '10.10.10.2'
        port = '3306'
        user = 'dwh'
        pwd = 'elcaro_4U'
        db = 'staging'

        con_db = Db_Connection(type, host, port, user, pwd, db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception(f"El tipo de base de datos {type} no es válido")
        elif ses_db == -2:
            raise Exception("Error al establecer la conexión de pruebas")        
        
        sql_stmt = "SELECT FechaEmision, SUBSTRING(FechaEmision, 7, 4) AS Anio, SUBSTRING(FechaEmision, 4, 2) AS Mes, SUBSTRING(FechaEmision, 1,2 ) AS Dia FROM staging_operaciones;"
        tra_fecha = pd.read_sql(sql_stmt, ses_db)
        
        return tra_fecha

    except:
        traceback.print_exc()
    finally:
        pass
