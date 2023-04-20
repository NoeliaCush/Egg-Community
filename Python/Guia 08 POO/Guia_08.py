"""class Persona:
    def __init__(self, nombre, sexo, profesión):
        self.nombre = nombre
        self.sexo = sexo
        self.profesión = profesión
    
    def trabajo(self):
        print(f"{self.nombre} trabaja como {self.profesión}")

#Crea objeto pasando argumento POR POSICIÓN

carmen = Persona("Carmen", "mujer", "ingeniera en software")
juan = Persona("Juan", "hombre", "médico")

#Crea objeto pasando argumento POR NOMBRE
carmen = Persona(nombre= "Carmen",
                 sexo= "mujer",
                 profesión= "ingeniera en software")

juan = Persona(nombre= "Juan",
               sexo= "hombre",
               profesión= "médico")

#Invocar al objetoi con sus atribútos y métodos
print(carmen.nombre, carmen.sexo)
print(juan.nombre, juan.sexo)

carmen.trabajo()
"""

"""
class Persona:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos
    
    def nombre_completo(self):
        return f"{self.apellidos}, {self.nombres}"
    
#Clase cliente tiene TODOS los métodos de la clase Persona
class Cliente(Persona):
#Si se quiere agregar un nuevo atributo que NO está en la clase padre:
    def __init__(self, nombres, apellidos, celular):
        super().__init__(nombres, apellidos)
        self.celular = celular

#Si se quiere modificar un método heredado, se reescribe en la clase hija
    def nombre_completo(self):
        return f"{self.nombres.upper()}, {self.apellidos.upper()}"

    def saludar(self):
        return f"¡Hola {self.nombres}!"
    

persona_1 = Persona(nombres="Juan Enrique", apellidos="Jurado")
print(persona_1.nombre_completo())

cliente_1 = Cliente(nombres="Justa", apellidos="Chavez", celular="1234")
print(f"{cliente_1.nombre_completo()}, Celular: {cliente_1.celular}")
"""
"""
class Saludos:
    def bienvenida(self, nombre):
        print(f"Hola {nombre}")
    
class Preguntas:
    def preguntar(self):
        print("¿Cómo estas?")

class Persona(Saludos, Preguntas):
    def __init__(self, nombre):
        self.nombre = nombre
        self.bienvenida(self.nombre)
        self.preguntar()

p = Persona("Lucía")
"""

"""
class Persona:
    def __init__(self, nombres: str, apellidos: str):
        self.nombres: str = nombres
        self.apellidos: str = apellidos
    
    def nombre_completo(self) -> str:
        return f"{self.apellidos}, {self.nombres}"
    
class Lugar:
    def __init__(self, localidad: str, distancia: float):
        self.localidad: str = localidad
        self.distancia: float = distancia

class Cliente(Persona, Lugar):
    def __init__(self, nombres: str, apellidos: str,
                 localidad: str, distancia: float):
        #Mixin:
        Persona.__init__(self, nombres, apellidos)
        Lugar.__init__(self, localidad, distancia)
    
    def datos(self) -> None:
        print(f"{self.nombre_completo().upper()}: "
              f"Eligió la localida de {self.localidad} "
              f"(dista de aquí {self.distancia}km)")

c = Cliente("Nombre", "Apellido", "Mendoza", 2000.23)
c.datos()
"""
"""
from typing import Iterable

class Ruedas:
    def __init__(self, cantidad: int):
        self.cantidad: int = cantidad

class Autos:
    stock = 0

    def __init__(self, nombre: str, ruedas: Ruedas):
        self.nombre: str = nombre
        self.ruedas: Ruedas = ruedas
        Autos.stock += 1
        print(f"{self.nombre} tiene {self.ruedas.cantidad} ruedas")
        print(f"Cantidad de autos creados: {Autos.stock}")
        del ruedas


def fábrica_de_autos(marcas: Iterable):
    ruedas = Ruedas(cantidad=4)
    for marca in marcas:
        nuevo_auto = Autos(marca, ruedas)


marcas = ["Fiat", "Toyota", "Ford"]
fábrica_de_autos(marcas)
"""

from typing import Iterable

class Ruedas:
    def __init__(self, cantidad: int):
        self.cantidad: int = cantidad

class Autos:
    stock = 0

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.ruedas = Ruedas(cantidad=4)
        Autos.stock += 1
        print(f"{self.nombre} tiene {self.ruedas.cantidad} ruedas")
        print(f"Cantidad de autos creados: {Autos.stock}")
        


def fábrica_de_autos(marcas: Iterable):
    ruedas = Ruedas(cantidad=4)
    for marca in marcas:
        nuevo_auto = Autos(marca, ruedas)


marcas = ["Fiat", "Toyota", "Ford"]
fábrica_de_autos(marcas)