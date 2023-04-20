from typing import Any

import articulos
import usuario


def main():
    TITULO: str = "NEGOCIO"
    OPCIONES: dict[str, dict[str, Any]]

    OPCIONES = {
        "1": {"etiqueta": "articulos", "accion": articulos.menu.main},
        "2": {"etiqueta": "* Clientes"},
        "3": {"etiqueta": "* Ventas"},
        "x": {"etiqueta": "Salir", "acción": False},
    }
    usuario.menu.principal(TITULO, OPCIONES)
    

if __name__ == "__main__":
    main()