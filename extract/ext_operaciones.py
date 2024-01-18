
import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_operaciones():
    try:
        filename = './csvs/operaciones.csv'
        operaciones = pd.read_csv(filename)
        return operaciones

    except:
        traceback.print_exc()

    finally:
        pass
