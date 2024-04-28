def celcius_to_fahrenheit(temp):
    f= (temp*1.8)+32
    return f
   

def celcius_to_kelvin(temp):
    k=temp+273.15
    return k


def kelvin_to_fahrenheit(temp):
    f1=(temp-273.15)*1.8+32
    return f1


def kelvin_to_celcius(temp):
    c=temp-273.15
    return c


def fahrenheit_to_celcius(temp):
    c2=(32*temp -32) * (5/9)
    return c2


def fahrenheit_to_kelvin(temp):
    y=(temp-32) * (5/9) +273.15
    return y


if __name__ == '__main__':

g= float(input("Digite la tempratura en celcius para convertir a fahrenheit: " ))
print("La tempreratura",g,"°", "es equivalente a", celcius_to_fahrenheit(g), "°F" )

k= float(input("Digite la tempratura en celcius para convertir a kelvin: " ))
print("La tempreratura",k,"°", "es equivalente a", celcius_to_kelvin(k), "K" )

k2=float(input("Digite la temperatura en kelvin para convertir a fahrenheit: " ))
print("La tempreratura",k2,"K", "es equivalente a", kelvin_to_fahrenheit(k2), "°F" )

j=float(input("Digite la temperatura en kelvin para convertir a celcius: " ))
print("La tempreratura",j,"K", "es equivalente a", kelvin_to_celcius(j), "°C" )

h=float(input("Digite la temperatura en fahrenheit para convertir a celcius: " ))
print("La tempreratura",h,"°F", "es equivalente a", fahrenheit_to_celcius(h), "°C" )

r=float(input("Digite la temperatura en fahrenheit para convertir a kelvin: " ))
print("La tempreratura",r,"°F", "es equivalente a", fahrenheit_to_kelvin(r), "K" )
pass