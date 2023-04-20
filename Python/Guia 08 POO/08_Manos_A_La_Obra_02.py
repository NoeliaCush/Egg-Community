"""Manos A La Obra - Ejercicio 02"""

from typing import Optional

class Persona:
    """Clase que maneja datos de los vecinos"""

    vecindario: str = "Buenos Vecinos"
#Agrega una variable de clase
    localidad: str 

#Se agrega la variable de instancia requerida
    def __init__(self, nombre:str, sexo: str, edad: int,
                 profesión: Optional[str] = None ) -> None:
        self.nombre: str = nombre
        self.sexo: str = sexo
        self.profesión: Optional[str] = profesión
        self.edad: int= edad
    
    def trabajo(self) -> str:
        if self.profesión:
            mensaje = f"{self.nombre} trabaja como {self.profesión}"
        else:
            mensaje = f"{self.nombre} no está trabajando"
        return mensaje

if __name__ == "__main__":
#Crea 3 instancias de persona
    persona_1 = Persona(nombre= "Noelia", sexo= "mujer", edad= 24)
    persona_2 = Persona(nombre="Ines", sexo="mujer", edad= 58)
    persona_3 = Persona(nombre="Luis", sexo="hombre", edad= 64)

#Modifica la edad de una de las instancias

    persona_1.edad= 25
    print(persona_1.edad)

#Modifica la variable de clase
    Persona.localidad = "Ushuaia"
    print(persona_1.localidad)
    print(persona_2.localidad)
    print(persona_3.localidad)
    print(Persona.localidad)

#Desde una instancia muestra "vecindario" y "localidad"}
    print(persona_1.vecindario)
    print(persona_1.localidad)

#Guarda los objetos en una lista "Personas", iterala y muestra todas las edades
    personas = [persona_1, persona_2, persona_3]
    for persona in personas:
        print(persona.edad)



