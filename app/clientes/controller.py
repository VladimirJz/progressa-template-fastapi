from fastapi import APIRouter, Depends, HTTPException

from app.clientes.dependencies import get_cliente_services
from .services import ClienteServices
from core.session import get_db_connection


router = APIRouter(
    prefix="/clientes",
    tags=["API de Clientes"]
)



# @router.get("/{id}")
# def get_datos_cliente(id:int=0):
#     cliente_servicio = ClienteServices(get_db_connection())
#     resultado = cliente_servicio.consulta_cliente_por_id(cliente_id=id)
    
#     return resultado

@router.get("/{id}")
def get_datos_cliente(id:int=0, cliente_servicio:ClienteServices=Depends(get_cliente_services)):
    resultado = cliente_servicio.consulta_cliente_por_id(cliente_id=id)
   
    return resultado
    
    
