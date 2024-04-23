import os
import unittest
import sys
import importlib.util


def test_verificar_ejecutar_function():
    last_argument = sys.argv[-1]
    ruta_archivo = f"{last_argument}.py"
    assert os.path.isfile(ruta_archivo), f"ERROR: el archivo {ruta_archivo} no existe"
    
    spec = importlib.util.spec_from_file_location("module.name", ruta_archivo)
    module = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = module
    spec.loader.exec_module(module)
    
    assert hasattr(module, 'fizzbuzz'), f"ERROR: el modulo conteo_421 no existe en el archivo"    

    assert module.fizzbuzz() == None, "La función 'fizzbuzz' no devuelve el resultado esperado para la entrada."
    assert module.fizzbuzz(end=51) ==  None, "La función 'fizzbuzz' no devuelve el resultado esperado para la entrada. end=51"
    assert module.fizzbuzz(start=10, end=51) == None, "La función 'fizzbuzz' no devuelve el resultado esperado para la entrada. start=10, end=51"
    assert module.fizzbuzz(start=40, end=1) ==  None, "La función 'fizzbuzz' no devuelve el resultado esperado para la entrada."
    


if __name__ == '__main__':
    test_verificar_ejecutar_function()
