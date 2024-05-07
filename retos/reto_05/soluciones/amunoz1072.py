'''
1. Construye una función llamada `celcius_to_fahrenheit` que dado un numero flotante que represente la temperatura 
en grados celcius la convierta a grados fahrenheit
2. Construye una función llamada `celcius_to_kelvin` que dado un numero flotante que represente la temperatura 
en grados celcius la convierta a grados kelvin
3. Construye una función llamada `kelvin_to_fahrenheit` que dado un numero flotante que represente la temperatura 
en grados kelvin la convierta a grados fahrenheit
4. Construye una función llamada `kelvin_to_celcius` que dado un numero flotante que represente la temperatura 
en grados kelvin la convierta a grados celcius
5. Construye una función llamada `fahrenheit_to_celcius` que dado un numero flotante que represente la temperatura en
 grados fahrenheit la convierta a grados celcius
6. Construye una función llamada `fahrenheit_to_kelvin` que dado un numero flotante que represente la temperatura en
 grados fahrenheit la convierta a grados kelvin
'''
def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def celcius_to_kelvin(celcius):
    return celcius + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

if __name__ == '__main__':
    celcius=float(input('Ingrese el valor en grados celcius '))
    print('Los ',celcius, 'Grados Celcius a ',celcius_to_fahrenheit(celcius),' fahrenheit')
    print('Los ',celcius, 'Grados Celcius a ',celcius_to_kelvin(celcius),' kelvin')

    kelvin=float(input('Ingrese el valor en grados kelvin '))
    print('Los ',kelvin, 'Grados Kelvin a ',kelvin_to_fahrenheit(kelvin),' fahrenheit')
    print('Los ',kelvin, 'Grados Kelvin a ',kelvin_to_celcius(kelvin),' celcius')

    fahrenheit=float(input('Ingrese el valor en grados fahrenheit '))
    print('Los ',fahrenheit, 'Grados fahrenheit a ',fahrenheit_to_celcius(fahrenheit),' celciust')
    print('Los ',fahrenheit, 'Grados fahrenheit a ',fahrenheit_to_kelvin(fahrenheit),' celciust')