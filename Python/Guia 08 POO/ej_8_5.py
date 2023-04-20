"""Manos A La Obra - Ejercicio 05"""
class Persona:
    def __init__(self, nombres: str, apellidos: str):
        self.nombres: str = nombres
        self.apellidos: str = apellidos
    
    def nombre_completo(self) -> str:
        return f"{self.apellidos}, {self.nombres}"
    
class Cliente:
    def __init__(self, nombres: str, apellidos: str, celular: str):
        #Composición 
        self.persona = Persona(nombres, apellidos)
        self.celular: str = celular

    def nombre_completo(self) -> str:
        return f"{self.nombres.upper()}, {self.apellidos.upper()}"

    def saludar(self) -> str:
        return f"¡Hola {self.nombres}!"
    
class Usuario:
    #Agregación
    def __init__(self, cliente: Cliente):
        self.cliente: Cliente = cliente
        self.contraseña: str = self.generar_contraseña()

    def generar_contraseña(self) -> str:
        return f"{self.cliente.persona.nombres[:5]}{self.cliente.celular[-2:]}"


def main():
    p = Persona("Alguien", "De por ahí")
    print(p.nombre_completo())

    c = Cliente("Otro", "Apellido", "1234")
    print(c.persona.nombres, c.persona.apellidos, c.celular)

    u = Usuario(c)
    print(u.contraseña)

if __name__ == "__main__":
    main()