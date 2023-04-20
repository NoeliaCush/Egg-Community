"""
Crea una clase Producto con las siguientes características:
Atributos de instancia:
código: int
nombre: str
precio: float
stock: int (no es obligatorio. Valor predeterminado: 0)
Crea al menos 3 instancias de clases y muestra sus datos.

"""
from typing import Optional

class Administrador:
    contraseña: str = "admin"

    def verificar_contraseña(self) -> bool:
        entrada = input("Ingrese una contraña")
        if entrada == Administrador.contraseña:
            print("Contraseña correcta, podes acceder")
            return True
        else:
            print("Contraseña incorrecta, no podes acceder")
            return False

class Producto(Administrador):

    impuestos: float = 1.15
    lista_productos: list = []

    def __init__(self, codigo: int, nombre: str, precio: float,stock: Optional[int] = 0):
        self.codigo: int = codigo
        self.nombre: str = nombre
        self.precio: float = self.precio_final(precio)
        self.stock: Optional[int] = stock

    def __str__(self) -> str:
        return f"{self.codigo}, {self.nombre}, {self.precio}, {self.stock}"   

    def precio_final(self, precio: float) -> float:
        return precio * Producto.impuestos
    
    def comprar(self, cantidad:int):
        if not self.verificar_contraseña:
            print("No se puede acceder")
        else:
            if self in Producto.lista_productos:
                if self.stock: 
                    self.stock = self.stock + cantidad
            else:
                if self.stock:
                    self.stock = self.stock + cantidad
                    Producto.lista_productos.append(self)
   
    def vender(self, cantidad:int):
        if self in Producto.lista_productos:
            if self.stock:
                self.stock = self.stock - cantidad 
                if cantidad > self.stock:
                    print("No se puede vender mas del stock del producto")
                elif self.stock - cantidad == 0:
                    print("Se vendió la totalidad del producto")
                    Producto.lista_productos.remove(self)
        else:
            print("El producto que desea vender no se encuentra en la lista de productos")

    def listar_productos(self):
        Producto.lista_productos.append(self)

    def mostrar_productos(self):
        for p in Producto.lista_productos:
            if isinstance(p, Libro):
                print(f"{p.autor}, {p.isbn}")
            elif isinstance(p, Café):
                print(f"{p.descripción},{p.proveedor}")
            else:
                print(p)

class Libro(Producto):
    def __init__(self, autor: str, isbn: int,
                 codigo: int, nombre: str, precio: float, stock: Optional[int] = 0):
        super().__init__(codigo, nombre, precio, stock)
        self.autor: str = autor
        self.isbn: int = isbn

class Café(Producto):
    def __init__(self, descripción: str, proveedor: str,
                codigo: int, nombre: str, precio: float, stock: Optional[int] = 0):
        super().__init__(codigo, nombre, precio, stock)
        self.descripción: str = descripción
        self.proveedor: str = proveedor

if __name__ == "__main__":
    producto_1 = Producto(1, "Mate", 100.10, 20)
    print(producto_1)
    producto_1.listar_productos

    libro_1 = Libro("Autor", 1234, 50, "Nombre", 20.20, 5)
    libro_1.comprar(5)
    libro_1.mostrar_productos()


    

