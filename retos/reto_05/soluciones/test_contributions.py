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

    assert hasattr(module, 'celcius_to_fahrenheit'), "ERROR: el modulo 'celcius_to_fahrenheit' no existe"
    assert hasattr(module, 'celcius_to_kelvin'), "ERROR: el modulo 'celcius_to_kelvin' no existe"
    assert hasattr(module, 'kelvin_to_fahrenheit'), "ERROR: el modulo 'kelvin_to_fahrenheit' no existe"
    assert hasattr(module, 'kelvin_to_celcius'), "ERROR: el modulo 'kelvin_to_celcius' no existe"
    assert hasattr(module, 'fahrenheit_to_celcius'), "ERROR: el modulo 'fahrenheit_to_celcius' no existe"
    assert hasattr(module, 'fahrenheit_to_kelvin'), "ERROR: el modulo 'fahrenheit_to_kelvin' no existe" 

    assert module.celcius_to_fahrenheit(module.fahrenheit_to_celcius(18)) == 18



if __name__ == '__main__':
    test_verificar_ejecutar_function()
