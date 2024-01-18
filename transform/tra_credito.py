import traceback
from util.db_connection import Db_Connection
import pandas as pd

def transformar_credito ():

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
        
        sql_stmt = "SELECT NumeroOperacion AS bkCredito, Destino AS Destino, Oficina AS Oficina, TipoCRedito AS TipoCRedito, Estado AS Estado From staging_creditos;"
        cre_dom = pd.read_sql(sql_stmt, ses_db)
        
        return cre_dom

    except:
        traceback.print_exc()
    finally:
        pass