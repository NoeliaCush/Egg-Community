import os

archivo = "mi_ruta.txt"
RUTA = os.getcwd()

def crear_archivo():
    if os.path.isfile(archivo):
        print(f"El archivo {archivo} ya existe.")
    else:
        with open(archivo, "w") as f:
            print(f"Se creó el archivo {archivo}")

def escribir(linea):
    with open(archivo, "a") as f:
        f.write(str(linea) + "\n" )

def leer():
    with open(archivo, "r") as f:
        datos = f.readlines()
        for indice, línea in enumerate(datos, start= 1):
            print(indice, línea, end= "")

def main():
    crear_archivo()
    escribir(RUTA)
    escribir(archivo)
    leer()

if __name__ == "__main__":
    main()