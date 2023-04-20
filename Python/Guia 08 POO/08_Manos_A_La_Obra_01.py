"""Manos A La Obra  - Ejercicio 1"""
from typing import Optional

class Persona:
    """Clase que maneja datos de los vecinos"""
#Se agrega la variable compartida vecindario
    vecindario: str = "Buenos Vecinos"

    def __init__(self, nombre:str, sexo: str,
                 profesión: Optional[str] = None) -> None:
        self.nombre: str = nombre
        self.sexo: str = sexo
        self.profesión: Optional[str] = profesión
    
    def trabajo(self) -> str:
        if self.profesión:
            mensaje = f"{self.nombre} trabaja como {self.profesión}"
        else:
            mensaje = f"{self.nombre} no está trabajando"
        return mensaje

if __name__ == "__main__":
#Crea el objeto persona_1 como instancia de persona con un nombre, sexo y profesiónm    
    persona_1 = Persona(nombre= "Luis",
                    sexo= "hombre",
                    profesión="transportista")

#Crea el objeto persona_2 con un nombre, sexo pero sin una profesión
    persona_2 = Persona(nombre= "Noelia",
                    sexo="mujer")

#Imprime todas las variables de instancia
    print(f"{persona_1.nombre}, {persona_1.sexo}, {persona_1.profesión}")
    print(f"{persona_2.nombre}, {persona_2.sexo}")

#Llama al método trabajo, guardando la devolución en una variable y mostrar el mensaje
    trabajo_1 = persona_1.trabajo()
    print(trabajo_1)

    trabajo_2 = persona_2.trabajo()
    print(trabajo_2)

#Se muestra la varibale compartida
    print(persona_1.vecindario)
    print(persona_2.vecindario)
    print(Persona.vecindario)

#Cambia la variable compartida desde la clase Persona
    Persona.vecindario = "Nuevo Barrio"
    print(persona_1.vecindario)
    print(persona_2.vecindario)
    print(Persona.vecindario)

#Cambia la variable compartida pero solo para el objeto persona_1
    persona_1.vecindario = "La Costa"
    print(persona_1.vecindario)
    print(persona_2.vecindario)
    print(Persona.vecindario)

#Ver variables de instancia de cada objeto
    print(persona_1.__dict__)
    print(persona_2.__dict__)

#La función isinstance permite ver si una intancia pertenece a una clase
    print(isinstance(12, int))
    print(isinstance(12, float))
    print(isinstance(persona_1, Persona))





