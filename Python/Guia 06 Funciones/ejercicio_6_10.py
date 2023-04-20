"""
10) . A partir de la sección anterior, Colecciones de datos II, mejora el último
ejercicio usando funciones. Solamente realiza la parte de los "artículos",
pero con la siguiente estructura:
{
"artículo": {
{
"id": int,
"nombre": str,
"precio": float,
"cantidad": int
},
}
}
El "id" sería el "código del artículo", que no puede repetirse. Puedes crear
un menú y agregar funcionalidades. Emplea las mejores prácticas que
has aprendido.



from pprint import pprint

articulos={ "artículo": {}}

while True:
    respuesta = input("¿Quiere agregar un artículo? s/n: ").lower()
    if respuesta == "n":
        break
    elif respuesta == "s":
        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        datos = {"nombre": nombre, "precio": precio, "stock": stock}
        articulos["artículo"][codigo] = datos
        pprint(articulos)

"""