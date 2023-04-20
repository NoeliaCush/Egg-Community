import paquete.main as main

def test_es_entero():
    assert main.es_entero(10) == True
    assert main.es_entero("10") == True
    assert main.es_entero("+10") == True
    assert main.es_entero("-10") == True
    assert main.es_entero(10.10) == False
    assert main.es_entero("10.10") == False
    assert main.es_entero("texto") == False
    assert main.es_entero("") == False
    assert main.es_entero("+") == False
    assert main.es_entero(["12, 123"]) == False