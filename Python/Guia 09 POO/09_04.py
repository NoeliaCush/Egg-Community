class Producto:
    def __init__(self, nombre: str, cantidad: int) -> None:
        self.nombre: str = nombre
        self.cantidad: int = cantidad

    def __contains__(self, nombre):
        if self.nombre == nombre:
            return True     

p1 = Producto(nombre="Teclado", cantidad= 3)
p2 = Producto(nombre= "Mouse", cantidad= 4)

print("Teclado" in p1)
print("Teclado" in p2)


