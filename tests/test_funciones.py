from servicio.funciones import suma

#python -m pytest
#python -m pytest path

# En visual studio code configuro la carpeta donde están lost test.
# Carpeta que se llame test y las funciones arranquen con test.

from unittest.mock import Mock

# Supongo que es aleatorio
class Suerte:

    def __init__(self) -> None:
        pass
    def tirar_dado():
        return 5


def test_funcion_sumar():
    # Mockeo una clase
    mock = Mock(spec=Suerte)
    mock.tirar_dado.return_value = 7
    assert suma(2,mock.tirar_dado()) == 9


# MOCKEO DE FUNCION

# from unittest.mock import patch

# # Mockeamos la función usando el decorador patch
# @patch('__main__.funcion_original')
# def test_funcion_mockeada(mock_funcion_original):
#     # Configuramos el comportamiento simulado
#     mock_funcion_original.return_value = "Función mockeada"

#     # Ahora puedes utilizar mock_funcion_original en lugar de funcion_original en tus pruebas
#     resultado = funcion_original()
#     print(resultado)  # Imprimirá "Función mockeada"

# # Ejecutamos la prueba
# test_funcion_mockeada()