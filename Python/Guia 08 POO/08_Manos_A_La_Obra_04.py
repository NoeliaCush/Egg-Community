"""Manos A La Obra - Ejercicio 04"""

class Persona:
    def __init__(self, nombres: str, apellidos: str):
        self.nombres: str = nombres
        self.apellidos: str = apellidos
    
    def nombre_completo(self) -> str:
        return f"{self.apellidos}, {self.nombres}"

"""
1. Crea una nueva clase Lugar, que tenga como atributo de clase "estado"
que será de tipo bool, tendrá por valor predeterminado True. Además,
crea atributos de instancia (requeridos) "localidad": str y "distancia":
float.
"""
class Lugar():
    def __init__(self, localidad: str, distancia: float, estado: bool = True):
        self.estado: bool = estado
        self.localidad: str = localidad
        self.distancia: float = distancia

"""
2. Crea una nueva clase llamada Saldo, que tenga como atributo de
instancia (requerido) "balance": float, cuyo valor predeterminado sea 0.
"""
class Saldo():
    def __init__(self, balance: float = 0.0):
        self.balance: float = balance

#3. Cliente heredará de Persona, Lugar y Saldo
class Cliente(Persona, Lugar, Saldo):
    def __init__(self, nombres: str, apellidos: str, celular: str,
                 localidad: str, distancia: float, estado: bool,
                 balance: float):
        Persona.__init__(self, nombres, apellidos)
        Lugar.__init__(self, localidad, distancia, estado)
        Saldo.__init__(self, balance)
        self.celular: str = celular

    def nombre_completo(self) -> str:
        return f"{self.nombres.upper()}, {self.apellidos.upper()}"

    def saludar(self) -> str:
        return f"¡Hola {self.nombres}!"
    
    def datos(self) -> None:
        print(f"{self.nombre_completo().upper()}: "
              f"Vive en {self.localidad} "
              f"(dista de aquí {self.distancia}km)"
              f"Tiene en su cuenta ${self.balance}")

class Usuario(Cliente):

    def __init__(self, nombres: str, apellidos: str, celular: str):
        super().__init__(nombres, apellidos, celular)
        self.contraseña: str = self.generar_contraseña()

    def generar_contraseña(self) -> str:
        return f"{self.nombres[:5]}{self.celular[-2:]}"
    
if __name__ == "__main__":
    cliente_1 = Cliente("Noelia", "Cruz", "156022623", "Ushuaia", 0, True, 2000)
    cliente_1.datos()

    