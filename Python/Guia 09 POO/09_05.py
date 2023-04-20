class Especialidad:
    def __init__(self, nombre: str, salario: float) -> None:
        self.nombre = nombre
        self.__salario_base = salario

    def _get_salario_base(self) -> float:
        return self.__salario_base
    
class Empleado(Especialidad):
    def __init__(self, especialidad: str, salario: float, nombre: str) -> None:
        super().__init__(especialidad, salario)
        self.nombre = nombre
        self.especialidad: str = especialidad
        self.__salario: float = self._get_salario_base() * 1.25
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, valor):
        if valor > self.__salario:
            self.__salario = valor
        else:
            return ValueError
        
empleado = Empleado("Constructor", 1000, "Pepe")
print(empleado.nombre)
print(empleado.especialidad)
print(empleado.get_salario())
empleado.set_salario(2000)
print(empleado.get_salario())
empleado.set_salario(1500)
print(empleado.__dict__)
