"""
Punto 4. Crea otro archivo llamado 'prueba.py' dentro de la carpeta
'proyecto'. Copia el siguiente código:

import matematica_1
import matematica_2

sumar(3, 3)
restar(3, 1)
multiplicar(3, 3)
dividir(3, 2)
print(PI)
"""

"""
Punto 5. Ejecuta el programa. ¿Qué es lo que pasa?
    Ocurre un error porque se debe escribir el nombre del módulo 
cuando se quiera usar las funciones
"""
"""
Punto 6. Cambia el código a la siguiente forma

import matematica_1
import matematica_2

matematica_1.sumar(3, 3)
matematica_1.restar(3, 1)
matematica_2.multiplicar(3, 3)
matematica_2.dividir(3, 2)
print(matematica_1.PI)
"""

"""
Punto 7. Prueba cambiar nuevamente el código de 'prueba.py' y corrige el error:

from matematica_1 import sumar, restar, PI
from matematica_2 import multiplicar, dividir

sumar(3,3)
restar(3, 1)
multiplicar(3, 3)
dividir(3, 2)
print(PI)
"""
"""
Punto 8. Cambia nuevamente el código de 'prueba.py' e intenta ejecutar:

from matematica_1 import *
from matematica_2 import *


sumar(3,3)
restar(3, 1)
multiplicar(3, 3)
dividir(3, 2)
print(PI)
"""

"""
Punto 9.  Hay ocasiones en las que interesa, por colisión de otros nombres o para
mejorar la legibilidad, usar un nombre diferente del módulo (u objeto)
que estamos importando. Python nos ofrece esta posibilidad a través de
la sentencia 'as'. Cambia nuevamente el código de 'prueba.py':

import matematica_1 as m1
import matematica_2 as m2


m1.sumar(3,3)
m1.restar(3, 1)
m2.multiplicar(3, 3)
m2.dividir(3, 2)
print(m1.PI)
"""

""" Manos A La Obra - Ejercicio 3 """

"""
Punto 2. Modifica 'prueba.py' y trata de ejecutarlo

import matematica.matematica_1 as m1
import matematica.matematica_2 as m2


m1.sumar(3,3)
m1.restar(3, 1)
m2.multiplicar(3, 3)
m2.dividir(3, 2)
print(m1.PI)
"""

"""
Punto 4. Modifica 'prueba.py' y ejecútalo:

import matematica as mat

mat.m1.sumar(3, 3)
mat.m1.restar(3, 1)
mat.m2.multiplicar(3, 3)
mat.m2.dividir(3, 2)
print(mat.m1.PI)
"""

"""
Punto 5. Modifica 'prueba.py' y ejecútalo:

from matematica import m1, m2


m1.sumar(3,3)
m1.restar(3, 1)
m2.multiplicar(3, 3)
m2.dividir(3, 2)
print(m1.PI)
"""

"""
Punto 7. Modifica 'prueba.py' y ejecútalo
"""

import matematica

matematica.sumar(3, 3)
matematica.restar(3, 1)
matematica.multiplicar(3, 3)
matematica.dividir(3, 2)
print(matematica.PI)