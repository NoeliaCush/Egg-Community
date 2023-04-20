from typing import Any

import usuario
from . import funcionalidades

def main():
    TITULO: str = "ARTICULOS"
    OPCIONES: dict[str, dict[str, Any]]

    OPCIONES = {
        "1": {"etiqueta": "Ver artículos ", "accion": funcionalidades.ver},
        "2": {"etiqueta": "Agregar un artículo", "accion": funcionalidades.agregar},
        "3": {"etiqueta": "* Modificar un artículo"},
        "4": {"etiqueta": "* Eliminar un artículo"},
        "x": {"etiqueta": "Salir", "acción": False},
    }
    usuario.menu.principal(TITULO, OPCIONES)