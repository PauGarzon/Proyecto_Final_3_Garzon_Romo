import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_clientes():
    try:
        filename = './csvs/clientes.csv'
        clientes = pd.read_csv(filename)
        return clientes

    except:
        traceback.print_exc()

    finally:
        pass
