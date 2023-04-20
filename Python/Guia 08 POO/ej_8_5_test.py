from ej_8_5 import Persona, Cliente, Usuario

def test_Persona():
    persona = Persona(nombres= "Nombre", apellidos= "Apellido")
    assert persona.nombre_completo() == "Apellido, Nombre"


def test_Cliente():
    cliente = Cliente(nombres="Nombre", apellidos="Apellido", celular= "700")
    assert cliente.persona.nombres == "Nombre"
    assert cliente.persona.apellidos == "Apellido"
    assert cliente.celular == "700"

def test_Usuario():
    cliente = Cliente(nombres="Nombre", apellidos="Apellido", celular= "700")
    usuario = Usuario(cliente)
    assert usuario.generar_contraseña() == "Nombr00"

