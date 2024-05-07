def celsius_to_fahrenheit(gc):
    c_f=(gc*9/5)+32

    return c_f

def celsius_to_kelvin(gc):
    c_k= gc + 273.15

    return c_k

def kelvin_to_fahrenheit(gk):
    k_f=celsius_to_fahrenheit(gk-273.15)
        
    return k_f

def kelvin_to_celsius(gk):
    k_f=kelvin_to_fahrenheit(gk)
    k_c=fahrenheit_to_celcius(k_f)
    
    return k_c

def fahrenheit_to_celcius(gf):
    f_c=(gf - 32) * 5/9

    return f_c

def fahrenheit_to_kelvin(gf):
    f_c=fahrenheit_to_celcius(gf)
    f_k=celsius_to_kelvin(f_c)

    return f_k



if __name__=="__main__":
    print("celsius_to_fahrenheit: ",celsius_to_fahrenheit(0))
    print("celsius_to_kelvin: ",celsius_to_kelvin(0))
    print("kelvin_to_fahrenheit: ",kelvin_to_fahrenheit(0))
    print("kelvin_to_celsius: ",kelvin_to_celsius(0))
    print("fahrenheit_to_celsius: ",fahrenheit_to_celcius(0))
    print("fahrenheit_to_kelvin: ",fahrenheit_to_kelvin(0))