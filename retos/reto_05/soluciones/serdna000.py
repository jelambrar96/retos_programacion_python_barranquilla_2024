def celcius_to_fahrenheit(gCelcius):
    gFahrenheit = (gCelcius * 9/5) + 32
    return print(gFahrenheit)

def celcius_to_kelvin(gCelcius):
    gKelvin = gCelcius + 273.15
    assert gKelvin < 0, "La funcion no acepta numero negativos menores a 273.15"
    return print(gKelvin)

def kelvin_to_fahrenheit(gKelvin):
    gFahrenheit = (gKelvin - 273.15) * 9/5 + 32
    return print(gFahrenheit)

def kelvin_to_celcius(gKelvin):
    gCelcius = gKelvin - 273.15
    return print(gCelcius)

def fahrenheit_to_celcius(gFahrenheit):
    gCelcius = (gFahrenheit - 32) * 5/9
    return print(gCelcius)

def fahrenheit_to_kelvin(gFahrenheit):
    gKelvin = (gFahrenheit - 32) * 5/9 + 273,15
    assert gKelvin < 0, "La funcion no acepta numero negativos menores a 273.15"
    return print(gKelvin)

if __name__ == '__main__':
    celcius_to_fahrenheit(24)