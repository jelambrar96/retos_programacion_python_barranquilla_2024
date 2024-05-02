def incremento(entero):
    entero += 1
    return entero

def decremento(entero):
    entero -= 1
    return entero

def suma(n, m):
    sum = n
    for i in range(m):
        sum = incremento(sum)
    return sum

def resta (n, m):
    res = n
    for i in range(m):
        res = decremento(res)
    return res

def multiplicacion(n, m):
    mul = 0
    for i in range(m):
        mul = suma(mul, n)
    return mul

def division_entera(n, m):
    contador = 0
    while n >= m:
        n = resta(n, m)
        contador += 1
    return contador, n

def potencia(n, m):
    pot = 1
    for i in range(m):
        pot = multiplicacion(pot, n)
    return pot

