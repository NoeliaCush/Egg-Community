from dataclasses import dataclass, field

@dataclass
class Producto:
    codigo: int 
    nombre: str 
    precio: float 
    cantidad: int = 0
    precio_final: float = field(init= False)

    def __post_init__(self):
        self.precio_final = round(self.precio * 1.21, 2)

producto_1 = Producto(1, "manzana", 12.40)

print(producto_1)