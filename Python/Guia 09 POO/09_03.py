"""class Prueba:

    @staticmethod
    def método_estático_1():
        print("método_estático_1")

    @staticmethod
    def método_estático_2():
        Prueba.método_estático_1()

    @classmethod
    def método_clase(cls):
        cls.método_estático_2()


Prueba.método_clase()"""

class Empleado():

    def __init__(self, nombre_completo, nombre_proyecto):
        self.nombre = nombre_completo
        self.proyecto = nombre_proyecto

    @staticmethod
    def tareas_a_realizar(nombre_proyecto):
        if nombre_proyecto == "Electromagnetismo":
            tareas = ['tarea_1','tarea_2', 'tarea_3']
        else:
            tareas = ['tarea_1']
        return tareas
    
    """
Crea un método de instancia "trabajar", que guardará en la variable
"tareas" la devolución del método estático las tareas correspondientes,
según el nombre del proyecto. Iterar la variable "tareas" e imprimir cada
tarea: "Tarea completada: {tarea}"
    """
    def trabajar(tareas):
        tareas = Empleado.tareas_a_realizar("Electromagnetismo")
        print(f"Treas completa: {tareas}")

"""
Crea un empleado y llámalo a trabajar en el proyecto
"Electromagnetismo"
"""

e1 = Empleado("Noelia", "Electromagnetismo")
e1.tareas_a_realizar("Electromagnetismo")
e1.trabajar()

