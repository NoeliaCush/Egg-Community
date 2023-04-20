from typing import Any

import validacion


def leer_opcion(opciones: dict[str, dict[str, Any]]) -> str | None:
    opcion = input("Elige una opción: ")
    entrada_valida = validacion.validar.cadena_no_vacia(opcion)
    if entrada_valida:
        if opcion in opciones.keys():
            return opcion
        else:
            return None
    else:
        return None


def mostrar(titulo: str, opciones: dict[str, dict[str, Any]]) -> None:
    print()
    print(f" {titulo} ".center(30, "*"))
    for descriptor, descripcion in opciones.items():
        etiqueta = descripcion["etiqueta"]
        print(f"{descriptor}.{etiqueta}")
    print()


def principal(titulo: str, opciones: dict[str, dict[str, Any]]) -> None:
    while True:
        mostrar(titulo, opciones)
        try:
            opcion: str | None = leer_opcion(opciones)
        except KeyboardInterrupt:
            break
        else:
            if opcion:
                accion = opciones[opcion].get("accion", None)
                if accion == None:
                    continue
                elif accion == False:
                    return None
                else:
                    accion()
            else:
                continue
                    
            