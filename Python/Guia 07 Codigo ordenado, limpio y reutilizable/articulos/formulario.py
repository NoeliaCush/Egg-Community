from typing import Callable

from validacion import validar
from . import validaciones

FORMULARIO: dict[str, dict[str, str | tuple[Callable, ...]]]
FORMULARIO = {
    "id":{
        "etiqueta": "Código: ",
        "acciones": (validar.entero_natural, validaciones.codigo)},
    "nombre":{
        "etiqueta": "Nombre: ",
        "acciones": (validar.cadena_no_vacia, validaciones.nombre)},  
    "precio":{
        "etiqueta": "Precio: ",
        "acciones": (validar.real_positivo, validaciones.precio)},
    "cantidad":{
        "etiqueta": "Cantidad: ",
        "acciones": (validar.entero_natural, validaciones.cantidad)},
}