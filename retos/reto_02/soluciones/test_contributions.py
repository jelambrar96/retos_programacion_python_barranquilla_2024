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
    
    assert hasattr(module, 'conteo_421'), f"ERROR: el modulo conteo_421 no existe en el archivo"    
    assert module.conteo_421(1) == 0, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 1."
    assert module.conteo_421(62) == 107, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 62."
    assert module.conteo_421(56) == 19, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 56."
    assert module.conteo_421(27) == 111, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 27."
    assert module.conteo_421(77) == 22, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 77."
    assert module.conteo_421(55) == 112, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 55."
    assert module.conteo_421(28) == 18, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 28."
    assert module.conteo_421(88) == 17, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 88."
    assert module.conteo_421(21) == 7, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 21."
    assert module.conteo_421(47) == 104, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 47."
    assert module.conteo_421(9) == 19, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 9."
    assert module.conteo_421(48) == 11, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 48."
    assert module.conteo_421(54) == 112, "La función 'conteo_421' no devuelve el resultado esperado para la entrada 54."
    


if __name__ == '__main__':
    test_verificar_ejecutar_function()
