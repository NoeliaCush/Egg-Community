"""Manos A  La Obra 01"""
class Estudiante:
    #variable de clase
    nombre_escuela = "HomeSchooling"

    #método de instancia: constructor
    def __init__(self, nombre, edad):
        #variable de instancia
        self.nombre = nombre
        self.edad = edad

    #método de instancia
    def mostrar(self):
        # accede a las variablesde instancia y a la vez a la variable de clase
        print("Estudiante: ", self.nombre, self.edad, Estudiante.nombre_escuela)

    #método de instancia
    def cambiar_edad(self, nueva_edad):
        #modifica la variable de instancia
        self.edad = nueva_edad

    #método de clase
    @classmethod
    def modificar_nombre_escuela(cls, nuevo_nombre):
        #modifica la variable de clase
        cls.nombre_escuela = nuevo_nombre

if __name__ == "__main__":
    #crea la instancia estudiante
    estudiante_1 = Estudiante("Noelia", 24)

    #invoca mostrar
    estudiante_1.mostrar()

    #modifica la edad
    estudiante_1.cambiar_edad(25)

    #modifica el nombre de la escuela
    estudiante_1.modificar_nombre_escuela("EGGCommunity")

    #invoca mostrar
    estudiante_1.mostrar()