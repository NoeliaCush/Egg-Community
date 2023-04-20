"""Manos A La Obra - Ejercio 03"""
#1. Agregar las anotaciones de tipo
class Persona:
    def __init__(self, nombres: str, apellidos: str):
        self.nombres: str = nombres
        self.apellidos: str = apellidos
    
    def nombre_completo(self) -> str:
        return f"{self.apellidos}, {self.nombres}"
    
class Cliente(Persona):
    def __init__(self, nombres: str, apellidos: str, celular: str):
        super().__init__(nombres, apellidos)
        self.celular: str = celular

    def nombre_completo(self) -> str:
        return f"{self.nombres.upper()}, {self.apellidos.upper()}"

    def saludar(self) -> str:
        return f"¡Hola {self.nombres}!"
    
#2. Crea una nueva clase Usuario que herede de Cliente
class Usuario(Cliente):

    def __init__(self, nombres: str, apellidos: str, celular: str):
        super().__init__(nombres, apellidos, celular)
#4. Agrega el atributo "contraseña" al método constructor de Usuario
#5. Asigna a contraseña la cadena que devuelve el método generar contraseña
        self.contraseña: str = self.generar_contraseña()

#3. Crea un nuevo método "generar_contraseña"
    def generar_contraseña(self) -> str:
        return f"{self.nombres[:5]}{self.celular[-2:]}"
    
if __name__ == "__main__":
#6. Crea una instancia de persona, muestra su nombre completo
    persona_1 = Persona(nombres="Esteban Horacio", apellidos="Acevedo Aberastain")
    print(persona_1.nombre_completo())

#7. Crea una instancia de Cliente, muestra su nombre completo y celular.
    cliente_1 = Cliente(nombres="Liliana Roxana", apellidos="Perícoli", celular="1234")
    print(cliente_1.nombre_completo(), cliente_1.celular)

#8. Crea una instancia de Usuario, muestra su nombre completo, celular y contraseña
    usuario_1 = Usuario(nombres="Ramón", apellidos="De un lugar", celular="999")
    print(usuario_1.nombre_completo(), usuario_1.celular, usuario_1.contraseña)
    