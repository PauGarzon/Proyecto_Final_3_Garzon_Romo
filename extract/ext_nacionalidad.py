
import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_nacionalidad():
    try:
        filename = './csvs/nacionalidad.csv'
        nacionalidad = pd.read_csv(filename)
        return nacionalidad

    except:
        traceback.print_exc()

    finally:
        pass
