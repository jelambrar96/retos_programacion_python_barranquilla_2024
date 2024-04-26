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
    
    assert hasattr(module, 'incremento'), f"ERROR: el modulo incremento no existe en el archivo"
    assert module.incremento(0) == 1, "La función 'incremento' no devuelve el resultado esperado para n = 0"
    assert module.incremento(4) == 5, "La función 'incremento' no devuelve el resultado esperado para n = 4"
    assert module.incremento(-4) == -3, "La función 'incremento' no devuelve el resultado esperado para n = -3"

    assert hasattr(module, 'decremento'), f"ERROR: el modulo decremento no existe en el archivo"    
    assert module.decremento(0) == -1, "La función 'decremento' no devuelve el resultado esperado para n = 0"
    assert module.decremento(4) == 3, "La función 'decremento' no devuelve el resultado esperado para n = 4"
    assert module.decremento(-4) == -5, "La función 'decremento' no devuelve el resultado esperado para n = -4"

    assert hasattr(module, 'suma'), f"ERROR: el modulo suma no existe en el archivo"  
    assert module.suma(0, 0) == (0 + 0), "La función 'suma' no devuelve el resultado esperado para n = 0, m = 0"
    assert module.suma(4, 3) == (4 + 3), "La función 'suma' no devuelve el resultado esperado para n = 4, m = 3"
    assert module.suma(-4, 6) == (-4 + 6), "La función 'suma' no devuelve el resultado esperado para n = -4, m = 6"

    assert hasattr(module, 'resta'), f"ERROR: el modulo resta no existe en el archivo"
    assert module.resta(0, 0) == (0 - 0), "La función 'suma' no devuelve el resultado esperado para n = 0, m = 0"
    assert module.resta(4, 3) == (4 - 3), "La función 'suma' no devuelve el resultado esperado para n = 4, m = 3"
    assert module.resta(-4, 6) == (-4 - 6), "La función 'suma' no devuelve el resultado esperado para n = -4, m = 6"

    assert hasattr(module, 'multiplicacion'), f"ERROR: el modulo multiplicacion no existe en el archivo"    
    assert module.multiplicacion(0, 0) == (0 * 0), "La función 'multiplicacion' no devuelve el resultado esperado para n = 0, m = 0"
    assert module.multiplicacion(4, 3) == (4 * 3), "La función 'multiplicacion' no devuelve el resultado esperado para n = 4, m = 3"
    assert module.multiplicacion(4, 6) == (4 * 6), "La función 'multiplicacion' no devuelve el resultado esperado para n = -4, m = 6"    
        
    assert hasattr(module, 'potencia'), f"ERROR: el modulo potencia no existe en el archivo"    
    assert module.potencia(5, 2) == (5 ** 2), "La función 'potencia' no devuelve el resultado esperado para n = 5, m = 2"
    assert module.potencia(4, 3) == (4 ** 3), "La función 'potencia' no devuelve el resultado esperado para n = 4, m = 3"
    assert module.potencia(3, 3) == (3 ** 3), "La función 'potencia' no devuelve el resultado esperado para n = 3, m = 3"    

    assert hasattr(module, 'division_entera'), f"ERROR: el modulo division_entera no existe en el archivo"    


if __name__ == '__main__':
    test_verificar_ejecutar_function()
