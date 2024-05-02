'''
1. Construye una función llamada `incremento` que dado un entero, lo incrementa en 1. 
2. Construye una función llamada `decremento` que dado un entero, lo reduzca en 1.
3. Construye una función llamada `suma` que tenga los parámetros `n` y `m`, la salida de esta función debe ser el resultado de llamar 
a la función `incremento` un número `m` de veces. 
4. Construye una función llamada `resta` que tenga los parámetros `n` y `m`, la salida de esta función debe ser el resultado de llamar 
a la función `decremento` un número `m` de veces. 
5. Construye una función llamada `multiplicacion` que tenga dos parámetros `n` y `m`, la salida de esta función debe ser el resultado de 
llamar a la función `suma` un número `m` de veces.
6. Construye una función llamada `division_entera` que tenga dos parámetros `n` y `m`, la salida de esta función son dos parámetros: 
    1.  El primero es numero de veces que le tenemos que restar `m` a `n` mientras que `n` sea mayor a cero. Tienes que llamar a la función 
    `resta`
    2.  El segundo es el residuo de esa operación. 
7. Construye una función `potencia` que tenga dos parámetros `n` y `m`, la salida de esta función debe ser el resultado de llamar a la 
función `multiplicacion` un número `m` de veces.
'''

def incremento(num):
    return num + 1

def decremento(num):
    return num - 1


def suma(n, m):
    for i in range(m):
        n = incremento(n)
    return n

def resta(n, m):
    for i in range(m):
        n = decremento(n)
    return n

def multiplicacion(n, m):
    resultado = 0
    for i in range(m):
        resultado = suma(resultado, n)
    return resultado

def division_entera(n, m):
    veces_restar = 0
    while n >= m:
        n = resta(n, m)
        veces_restar += 1
    return veces_restar, n

def potencia(n, m):
    resultado = 1
    for i in range(m):
        resultado = multiplicacion(resultado, n)
    return resultado

if __name__ == '__main__':
    """
    escribe lo que quieras que tu codigo haga cuando se llame directamente
    """    
    print("el numero es:", 3," su incremento es ", incremento(2))
    print("el numero es:", 3," su decremento es ", decremento(3))
    print("el numero es:", 3," y el numero ", 4,"  la suma es ", suma(3,4))
    print("el numero es:", 3," y el numero ", 4,"  la resta es ", resta(3,4))
    print("el numero es:", 3," y el numero ", 4,"  la multiplicacion es ", multiplicacion(3,4))
    print("el numero es:", 3," y el numero ", 4,"  es ", division_entera(3,4))
    print("el numero es:", 3," y el numero ", 4,"  la potencia es ", potencia(3,4))
