"""
Punto 3. Crea un archivo '__init__.py' dentro de la carpeta 'matematica' y
agrega el siguiente código:

from . import matematica_1 as m1
from . import matematica_2 as m2
"""

"""
Punto 6. Modifica el archivo '__init__.py' con el siguiente código
"""

from .matematica_1 import sumar, restar, PI
from .matematica_2 import multiplicar, dividir

