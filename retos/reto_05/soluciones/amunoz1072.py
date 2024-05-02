
def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def celcius_to_kelvin(celcius):
    return celcius + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

celcius=float(input('Ingrese el valor en grados celcius '))
print('Los ',celcius, 'Grados Celcius a ',celcius_to_fahrenheit(celcius),' fahrenheit')
print('Los ',celcius, 'Grados Celcius a ',celcius_to_kelvin(celcius),' kelvin')

kelvin=float(input('Ingrese el valor en grados kelvin '))
print('Los ',kelvin, 'Grados Kelvin a ',kelvin_to_fahrenheit(kelvin),' fahrenheit')
print('Los ',kelvin, 'Grados Kelvin a ',kelvin_to_celcius(kelvin),' celcius')

