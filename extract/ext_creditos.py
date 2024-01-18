import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_creditos():
    try:
        filename = './csvs/creditos.csv'
        creditos = pd.read_csv(filename)
        return creditos

    except:
        traceback.print_exc()

    finally:
        pass
