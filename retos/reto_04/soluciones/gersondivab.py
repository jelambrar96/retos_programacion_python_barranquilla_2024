
def incremento(inc):
    inc += 1 # a partir de un valor "inc" dado, lo incremente en 1 en cada llamada 
    return inc

def decremento(dec):
    dec -= 1 # a partir de un valor "dec" dado, lo disminuye en 1 en cada llamada
    return dec

def suma(n,m):
    for i in range(m):
        n = incremento(n) # a partir de un valor "n" dado, lo incrementa un numero "m" de veces en 1
    
    return n

def resta(n,m):
    for i in range(m):
        n = decremento(n) # a partir de un valor "n" dado, lo disminuye un numero "m" de veces en 1
    
    return n

def multiplicacion(n,m): # a partir de un valor "n" dado, lo incrementa en su mismo valor "m" veces
    total=0 #variable que va guardando el total del incremento del valor "n" inicial   
    for i in range(m):
        
        total=suma(total,n)

    n=total
    
    return n

multiplicacion(6,5)

def division_entera(n,m):
    dividendo=n #variable que se utiliza para ir disminuyendo el valor de "m"
    numero_veces=0 #contador que enumera el numero de veces que ocurre la resta
    while dividendo>0 and dividendo>=m: #se utilizaron dos condiciones
        numero_veces += 1               #porque en la ultima entrada arrojaba negativo en dividendo
        dividendo=resta(dividendo,m)
    residuo=dividendo
   
    return numero_veces, residuo

division_entera(10,3)

def potencia(n,m):
    base=n #variable que se va multiplicando por si misma acumulando el resultado de cada multiplicacion 
     
    for i in range(m-1): #se disminuye en 1 porque en la primera entrada se realiza la primera multiplicacion
        
        base=multiplicacion(base,n)

    n=base
    
    return n

potencia(4,3)

if __name__=="__main__":
    print("----------INCREMENTO----------")
    print("El resultado de incrementar el numero 5 en 1 es: ", incremento(5))
    
    print("----------DECREMENTO----------")
    print("El resultado de disminuir el numero 10 en 1 es: ",decremento(10))
    
    print("----------SUMA----------")
    print("El resultado de 5 + 8 es: ",suma(5,8))

    print("----------RESTA----------")
    print("El resultado de 9 - 2 es: ",resta(9,2))

    print("----------MULTIPLICACION----------")
    print("El resultado de 6 x 7 es: ",multiplicacion(6,7))

    print("----------DIVISION----------")
    division1,division2=division_entera(8,3)
    print("El cociente de dividir 8/3 es: ", division1)
    print("El residuo de dividir 8/3 es: ", division2)

    print("----------POTENCIA----------")
    print("El resultado de 2^3 es: ",potencia(2,3))