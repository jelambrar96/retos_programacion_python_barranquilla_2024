def celcius_to_fahrenheit (GC):

    GF = (GC * 9/5) + 32

    return GF



def celcius_to_kelvin (GC):

    GK = GC + 273.15

    return GK



def  kelvin_to_fahrenheit (GK):

    GF = 1.8 * (GK - 273) + 32

    return GF


def kelvin_to_celcius (GK):

    GC = GK - 273.15

    return GC

def fahrenheit_to_celcius (GF):

    GC = (GF - 32) * 0.5556

    return GC

def fahrenheit_to_kelvin (GF):

    GK = 5/9*(GF - 32) + 273.15

    return GK


if __name__ == '__main__':
    print(celcius_to_fahrenheit(20))
    print(celcius_to_kelvin (20))
    print(kelvin_to_fahrenheit (20))
    print(kelvin_to_celcius (20))
    print(fahrenheit_to_celcius(20))
    print(fahrenheit_to_kelvin(20))

