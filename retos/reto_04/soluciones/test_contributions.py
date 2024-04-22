import unittest
import sys
import importlib.util


def fake_suma(a, b):
    return a + b

def fake_resta(a, b):
    return a + b

def fake_multiplicacion(a, b):
    return a * b

def fake_multiplicacion_2(a,b):
    suma = 0
    for i in range(b):
        suma += (suma + a)
    return suma

class TestReto03(unittest.TestCase):

    def test_function_exists_and_correct_output(self):
        # Tomar el nombre del archivo desde los argumentos de la línea de comando
        filename = sys.argv.pop()  # Remueve el último argumento que es el nombre del archivo
        spec = importlib.util.spec_from_file_location("module.name", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Verificar que la función existe
        self.assertTrue(hasattr(module, 'incremento'), "La función 'incremento' no existe en el archivo.")
        self.assertTrue(hasattr(module, 'decremento'), "La función 'decremento' no existe en el archivo.")
        self.assertTrue(hasattr(module, 'suma'),  "La función 'suma' no existe en el archivo.")
        self.assertTrue(hasattr(module, 'multiplicacion'), "La función 'multiplicacion' no existe en el archivo.")
        self.assertTrue(hasattr(module, 'potencia'), "La función 'potencia' no existe en el archivo.")
        self.assertTrue(hasattr(module, 'division_entera'), "La función 'division_entera' no existe en el archivo.")


if __name__ == '__main__':
    unittest.main()
