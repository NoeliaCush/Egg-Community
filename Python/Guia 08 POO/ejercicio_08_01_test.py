from ejercicio_08_01 import  Producto, Libro, Café

def test_Producto():
    producto = Producto(codigo= 1234, nombre= "Nombre", precio=10.10, stock=1)
    assert producto.codigo == 1234
    assert producto.nombre == "Nombre"
    assert producto.precio == 11.614999999999998
    assert producto.stock == 1

def test_Libro():
    libro = Libro(autor="Autor", isbn= 123, codigo=6, nombre= "Nombre", precio= 20.20, stock= 5)
    assert libro.autor == "Autor"
    assert libro.isbn == 123
    assert libro.codigo == 6
    assert libro.nombre == "Nombre"
    assert libro.precio == 23.229999999999997
    assert libro.stock == 5

def test_Café():
    cafe = Café(descripción= "Cafe", proveedor= "Proveedor", codigo= 1, nombre= "Nombre", precio= 10, stock=5)
    assert cafe.descripción == "Cafe"
    assert cafe.proveedor == "Proveedor"
    assert cafe.codigo == 1
    assert cafe.nombre == "Nombre"
    assert cafe.precio == 11.5
    assert cafe.stock == 5