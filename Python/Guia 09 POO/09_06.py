class Persona:
    
    def __init__(self, nombre: str):
        self._nombre: str = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.getter
    def nombre(self):
        if self._nombre == "":
            print("No tengo nombre")
        else:
            print(f"Mi nombre es {self._nombre}")
    
    @nombre.setter
    def nombre(self, valor: str):
        if valor.strip() == "":
            raise ValueError("Nombre vacío")
        self._nombre = valor
        print("Tengo nuevo nombre")

    @nombre.deleter
    def nombre(self):
        print("Has borrado mi nombre")
        self._nombre = ""


p1 = Persona("Noelia")
print(p1.nombre)
p1.nombre = "Otro Nombre"
print(p1.nombre)
del p1.nombre
print(p1.nombre)
p1.nombre = " "

