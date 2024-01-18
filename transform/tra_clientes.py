import traceback
from util.db_connection import Db_Connection
import pandas as pd

def transformar_clientes ():

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
        
        sql_stmt = "SELECT Identificacion, CASE WHEN Edad BETWEEN 15 AND 29 THEN '15-29' \
                    WHEN Edad BETWEEN 30 AND 44 THEN '30-44' \
                    WHEN Edad BETWEEN 45 AND 59 THEN '45-59' \
                    WHEN Edad BETWEEN 60 AND 74 THEN '60-74'\
                    WHEN Edad BETWEEN 75 AND 89 THEN '75-89' \
                    WHEN Edad BETWEEN 90 AND 104 THEN '90-104' ELSE '105+'  \
                    END AS rangoEdad, EstadoCivil,Sexo,Profesion,Nacionalidad FROM staging_clientes;"
        tra_Cliente = pd.read_sql(sql_stmt, ses_db)
        
        return tra_Cliente

    except:
        traceback.print_exc()
    finally:
        pass
