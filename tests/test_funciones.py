from servicio.funciones import suma

#python -m pytest
#python -m pytest path

# En visual studio code configuro la carpeta donde están lost test.
# Carpeta que se llame test y las funciones arranquen con test.

def test_funcion_sumar():
    assert suma(2,3) == 5