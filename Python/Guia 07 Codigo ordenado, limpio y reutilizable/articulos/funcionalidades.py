from pprint import pprint

import usuario

from .datos import articulos
from .formulario import FORMULARIO


def ver()-> None:
    if articulos["articulo"]:
        pprint(articulos, sort_dicts=False)
    else:
        print("No hay artículos registrados")
    return


def agregar() -> None:
    formulario_ingresado = usuario.entrada_datos.entrada(FORMULARIO)
    if formulario_ingresado:
        articulos["articulo"].update(formulario_ingresado)
        print("Artículo agregado")
        

