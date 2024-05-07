"""
## Reto

1. Construye una función llamada `celcius_to_fahrenheit` 
    que dado un numero flotante que represente la temperatura en grados celcius la convierta a grados fahrenheit
2. Construye una función llamada `celcius_to_kelvin` 
    que dado un numero flotante que represente la temperatura en grados celcius la convierta a grados kelvin
3. Construye una función llamada `kelvin_to_fahrenheit` 
    que dado un numero flotante que represente la temperatura en grados kelvin la convierta a grados fahrenheit
1. Construye una función llamada `kelvin_to_celcius` 
    que dado un numero flotante que represente la temperatura en grados kelvin la convierta a grados celcius
1. Construye una función llamada `fahrenheit_to_celcius` 
    que dado un numero flotante que represente la temperatura en grados fahrenheit la convierta a grados celcius
1. Construye una función llamada `fahrenheit_to_kelvin` 
    que dado un numero flotante que represente la temperatura en grados fahrenheit la convierta a grados kelvin
"""

def celcius_to_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f


def celcius_to_kelvin(c):
    k = c + 273
    return k


def kelvin_to_fahrenheit(k):
    c = kelvin_to_celcius(k)
    f = celcius_to_fahrenheit(c)
    return f
    k=celcius_to_fahrenheit

def kelvin_to_celcius(k):
    c = k - 273
    return c

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celcius(f)
    k = kelvin_to_celcius(c)
    return k


def fahrenheit_to_celcius(f):
    f=(9*C/5)+32
    return c


if __name__ == '__main__':
    print("30c to f:", celcius_to_fahrenheit(30))
    # fahrenheit_to_celcius()
    print ("40c to f:", celcius_to_fahrenheit(40))
    def celcius_to_kelvin
    print celcius_to_kelvin 
    "c=(K)+273"


