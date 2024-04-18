import unittest
import sys
import importlib.util

class TestConteo421(unittest.TestCase):

    def test_conteo_421_exists_and_correct_output(self):
        # Tomar el nombre del archivo desde los argumentos de la línea de comando
        filename = sys.argv.pop()  # Remueve el último argumento que es el nombre del archivo
        spec = importlib.util.spec_from_file_location("module.name", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Verificar que la función existe
        self.assertTrue(hasattr(module, 'conteo_421'), "La función 'conteo_421' no existe en el archivo.")

        # Verificar que la función devuelve el resultado esperado para la entrada dada
        result = module.conteo_421(1)
        self.assertEqual(result, 0, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 1.")
        self.assertEqual(111, 27, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 27.")
        self.assertEqual(9, 84, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 84.")
        self.assertEqual(15, 22, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 22.")
        self.assertEqual(35, 79, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 79.")
        self.assertEqual(26, 33, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 33.")
        self.assertEqual(34, 39, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 39.")
        self.assertEqual(20, 18, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 18.")
        self.assertEqual(109, 41, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 41.")
        self.assertEqual(16, 46, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 46.")
        self.assertEqual(5, 5, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 5.")

if __name__ == '__main__':
    unittest.main()
