from dataclasses import dataclass, asdict
from datetime import date, datetime
import json
import os


import locale
locale.setlocale(locale.LC_ALL, "")

@dataclass
class Cliente:
    dni: str
    apellidos: str
    nombres: str
    nacimiento: date

def cliente_crear() -> Cliente | None:
    try:
        dni = input("DNI: ")
        apellidos = input("Apellidos: ")
        nombres = input("Nombres: ")
        fecha = input("Fecha de nacimiento (dd mm aaaa): ")
        nacimiento = datetime.strptime(fecha, "%d %m %Y").date()
        if nacimiento > datetime.now().date():
            raise Exception("Nacimiento mayor a la fecha actual")
    except Exception as e:
        print("ERROR", e)
        return None
    else:
        cliente = Cliente(dni, apellidos, nombres, nacimiento)
        return cliente
    
def cliente_guardar(cliente: Cliente):
    lista_clientes: list[dict[str, str]] = []
    if os.path.isfile("archivo.json"):
        with open("archivo.json", "r") as f:
            try:
                lista_clientes = json.load(f)
            except ValueError as e:
                print(e)
    with open("archivo.json", "w") as f:
        datos = asdict(cliente)
        lista_clientes.append(datos)
        json.dump(lista_clientes, f, indent=4, default=str)

    #datos = asdict(cliente)
    #with open("prueba.txt", "a") as archivo:
    #   for valor in datos.values():
    #        archivo.write(f"{valor}, ")
    #  archivo.write(datetime.now().strftime("creado: %A %d%B/Y %H:%M:%S \n" ))

    
def main():
    for numero in range(1,4):
        print("Cliente", numero)
        nuevo_cliente = cliente_crear()
        if nuevo_cliente:
            pass


if __name__ == "__main__":
    main()
    

