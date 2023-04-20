from validacion import validar


def test_validar_entero_natural():
   assert validar.entero_natural("1") == 1
   assert validar.entero_natural("0") == False
   assert validar.entero_natural(100_000) == 100000
   assert validar.entero_natural("1.2") == False


def test_validar_real_positivo():
    assert validar.real_positivo("1.0") == 1.0
    assert validar.real_positivo("+1.0") == 1.0
    assert validar.real_positivo("0") == 0
    assert validar.real_positivo("-1.1") == False
    assert validar.real_positivo("") == False


def test_validar_cadena_no_vacia():
    assert validar.cadena_no_vacia("cadena") == "cadena"
    assert validar.cadena_no_vacia("cadena   ") == "cadena"
    assert validar.cadena_no_vacia("3") == "3"
    assert validar.cadena_no_vacia("") == False
