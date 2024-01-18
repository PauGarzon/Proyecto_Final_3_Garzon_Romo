import traceback
from util.db_connection import Db_Connection
import pandas as pd
 
def extract_and_load():
    try:
        # Configuración para la base de datos de staging
        type_staging = 'mysql'
        host_staging = '10.10.10.2'
        port_staging = '3306'
        user_staging = 'dwh'
        pwd_staging = 'elcaro_4U'
        db_staging = 'staging'
 
        # Configuración para la base de datos sor
        type_sor = 'mysql'
        host_sor = '10.10.10.2'
        port_sor = '3306'
        user_sor = 'dwh'
        pwd_sor = 'elcaro_4U'
        db_sor = 'sor'
 
        # Conexión a la base de datos de staging
        con_db_staging = Db_Connection(type_staging, host_staging, port_staging, user_staging, pwd_staging, db_staging)
        ses_db_staging = con_db_staging.start()
 
        # Verificación de la conexión
        if ses_db_staging == -1:
            raise Exception(f"El tipo de base de datos {type_staging} no es válido")
        elif ses_db_staging == -2:
            raise Exception("Error al establecer la conexión de pruebas")
 
        # Consulta SQL para seleccionar datos de la tabla tra_Domicilio en staging
        sql_stmt = "SELECT * FROM tra_Domicilio;"
        sor_dom = pd.read_sql(sql_stmt, ses_db_staging)
 
        # Conexión a la base de datos sor
        con_db_sor = Db_Connection(type_sor, host_sor, port_sor, user_sor, pwd_sor, db_sor)
        ses_db_sor = con_db_sor.start()
 
        # Verificación de la conexión
        if ses_db_sor == -1:
            raise Exception(f"El tipo de base de datos {type_sor} no es válido")
        elif ses_db_sor == -2:
            raise Exception("Error al establecer la conexión de pruebas")
 
        # Inserción de los datos en la tabla correspondiente en sor
        sor_dom.to_sql(name='sor_Domicilio', con=ses_db_sor, if_exists='replace', index=False)
 
    except:
        traceback.print_exc()
    
 
# Llamar a la función para realizar la extracción y carga de datos
extract_and_load()