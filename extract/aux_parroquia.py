import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_parroquia():
    try:
        filename = './csvs/parroquiaResidencia.csv'
        parroquia = pd.read_csv(filename)
        return parroquia

    except:
        traceback.print_exc()

    finally:
        pass
