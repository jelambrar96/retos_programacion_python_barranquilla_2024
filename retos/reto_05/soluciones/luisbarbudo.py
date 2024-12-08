## Reto
"""
1. Construye una función llamada `celcius_to_fahrenheit` que dado un numero flotante que represente la temperatura en grados celcius la convierta a grados fahrenheit
2. Construye una función llamada `celcius_to_kelvin` que dado un numero flotante que represente la temperatura en grados celcius la convierta a grados kelvin
3. Construye una función llamada `kelvin_to_fahrenheit` que dado un numero flotante que represente la temperatura en grados kelvin la convierta a grados fahrenheit
1. Construye una función llamada `kelvin_to_celcius` que dado un numero flotante que represente la temperatura en grados kelvin la convierta a grados celcius
1. Construye una función llamada `fahrenheit_to_celcius` que dado un numero flotante que represente la temperatura en grados fahrenheit la convierta a grados celcius
1. Construye una función llamada `fahrenheit_to_kelvin` que dado un numero flotante que represente la temperatura en grados fahrenheit la convierta a grados kelvin
"""
def celcius_to_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f

if __name__ == "__main__":
    print("30c to f:", celcius_to_fahrenheit(30))

def fahrenheit_to_celcius(f):
    c = (f - 32) * 5 / 9
    return c

if __name__ == "__main__":
    print(fahrenheit_to_celcius(30))


def celcius_to_kelvin(c):
    k = c + 273.15
    return k

 if __name__ == "__main__":
    print(celcius_to_kelvin(1))   

