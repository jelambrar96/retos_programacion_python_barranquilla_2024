import unittest
import sys
import importlib.util

class TestReto03(unittest.TestCase):

    def test_fizzbuzz_exists_and_correct_output(self):
        # Tomar el nombre del archivo desde los argumentos de la línea de comando
        filename = sys.argv.pop()  # Remueve el último argumento que es el nombre del archivo
        spec = importlib.util.spec_from_file_location("module.name", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Verificar que la función existe
        self.assertTrue(hasattr(module, 'fizzbuzz'), "La función 'fizzbuzz' no existe en el archivo.")

        # Verificar que la función devuelve el resultado esperado para la entrada dada
        self.assertEqual(module.fizzbuzz(), None, "La función 'fizzbuzz' no devuelve el resultado esperado para la entrada.")
        self.assertEqual(module.fizzbuzz(end=51), None, "La función 'fizzbuzz' no devuelve el resultado esperado para la entrada. end=51")
        self.assertEqual(module.fizzbuzz(start=10, end=51), None, "La función 'fizzbuzz' no devuelve el resultado esperado para la entrada. start=10, end=51")
        self.assertEqual(module.fizzbuzz(start=40, end=1), None, "La función 'fizzbuzz' no devuelve el resultado esperado para la entrada.")

if __name__ == '__main__':
    unittest.main()
