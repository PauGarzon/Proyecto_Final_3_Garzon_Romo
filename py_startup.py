import traceback
from extract.ext_clientes import extraer_clientes
from extract.per_staging import persistir_staging
from extract.ext_creditos import extraer_creditos
from extract.ext_nacionalidad import extraer_nacionalidad
from extract.ext_operaciones import extraer_operaciones
from extract.aux_parroquia import extraer_parroquia

from transform.tra_domicilio import transformar_domicilio
from transform.tra_clientes import transformar_clientes
from transform.tra_fechas import transformar_fechas
from transform.tra_credito import transformar_credito

#from sor.sor_cliente import sor_clientes
from sor.sor_credito import extract_and_loadCr
from sor.sor_domicilio import extract_and_load
from sor.sor_fecha import extract_and_loadF
from sor.sor_cliente import extract_and_loadCl


try:

    #cli = extraer_clientes()
    #print(cli)
    #persistir_staging(cli,'staging_clientes')

    #creditos = extraer_creditos()
    #persistir_staging(creditos,'staging_creditos')

    #nacionalidad=extraer_nacionalidad()
    #persistir_staging(nacionalidad,'staging_nacionalidad')
    
    #operaciones=extraer_operaciones()
    #persistir_staging(operaciones,'staging_operaciones')
    
    #parroquia=extraer_parroquia()
    #persistir_staging(parroquia,'staging_parroquiaResidencia')



    #tra_cli = transformar_clientes()
    #persistir_staging(tra_cli,'tra_Cliente')

    #tra_fecha = transformar_fechas()
    #persistir_staging(tra_fecha,'tra_Fecha')

    #tra_domi = transformar_domicilio()
    #persistir_staging(tra_domi,'tra_Domicilio')

    #tra_cred = transformar_credito()
    #persistir_staging(tra_cred,'tra_credito')



    #extract_and_loadCl()
    #extract_and_loadF()
    #extract_and_load()
    #extract_and_loadCr()

except:
    traceback.print_exc()

finally:
    pass


