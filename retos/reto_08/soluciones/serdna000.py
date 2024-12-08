from math import sqrt
from math import log2
from math import prod
#Ejercicio1
def es_primo(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    raiz = sqrt(n)
    contador = 0
    if n == 2:
        raiz = n
    elif n == 3:
        raiz = n
    else:
        for i in range(2, int(raiz) + 1):
            if n % i == 0:
                contador += 1

    return contador == 0

#Ejercicio2
def criba_heratosteles(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    listaPrimos = []
    for i in range(2, n-1):
        if es_primo(i):
            listaPrimos.append(i)
    
    return listaPrimos

#Ejercicio3
def es_primo_mersenne(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    mersenne = 0
    if not(es_primo(n)):
        return False
    else:
        mersenne = log2(n + 1)
        mersenne_entero = int(mersenne)
    if mersenne - mersenne_entero == 0:
            return True
    else:
            return False

#Ejercicio4
def descomposicion_factorial(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    lista_primos = criba_heratosteles(n+1)
    lista_factores_primos = []
    n2 = n
    numero = 1

    for primo in lista_primos:
        while n % primo == 0 and numero < n2 :
            n /= primo
            numero *= primo
            lista_factores_primos.append(primo)
        
        if numero == n2:
            return lista_factores_primos

#Ejercicio5
def es_perfecto(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    lista_factores_primos = descomposicion_factorial(n)
    fp_sin_repeticion = set(lista_factores_primos)
    fp_sin_repeticion = list(fp_sin_repeticion)
    lista_divisores = [1]

    for numero in fp_sin_repeticion:
        for i in range(1, lista_factores_primos.count(numero)+1):
            lista_divisores.append(numero**i)
    
    
    for i in range(1, len(lista_divisores) - 2):
        lista_divisores.append(lista_divisores[i]*fp_sin_repeticion[-1])

    respuesta = sum(lista_divisores)

    if respuesta == n:
        return True
    else:
        return False

#Ejercicio6
def son_primos_gemelos(x, y):
    if x < 0 or y < 0:
        raise Exception('El numero es menor que 0')
    
    if es_primo(x) and es_primo(y):
        if abs(x-y) == 2:
            return True
        else:
            return False

#Ejercicio7
def rango_primos_gemelos(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    lista_primos = criba_heratosteles(n)
    lista_primos_gemelos = []
    for i in range(1, len(lista_primos)):
        if son_primos_gemelos(lista_primos[i-1], lista_primos[i]):
            tupla = (lista_primos[i-1], lista_primos[i])
            lista_primos_gemelos.append(tupla)
    
    return lista_primos_gemelos

def son_amigos(n1, n2):
    if n1 < 0 or n2 < 0:
        raise Exception('El numero es menor que 0')
    
    lista = [n1, n2]
    respuesta = []
    for n in lista:
        lista_factores_primos = descomposicion_factorial(n)
        numero2 = prod(lista_factores_primos)
        fp_sin_repeticion = set(lista_factores_primos)
        fp_sin_repeticion = list(fp_sin_repeticion)
        fp_sin_repeticion.sort()
        lista_divisores = [1]

        for numero in fp_sin_repeticion:
            for i in range(1, lista_factores_primos.count(numero)+1):
                lista_divisores.append(numero**i)
        

        lista_divisores.sort()
        lista_divisores_add = lista_divisores

        for i in range(0, len(fp_sin_repeticion)):
            for j in range(0, len(lista_divisores)):
                factor = fp_sin_repeticion[i]*lista_divisores[j]
                if numero2 % factor == 0 and not(numero2 == factor) and factor not in lista_divisores:
                    lista_divisores_add.append(factor)

            lista_divisores = lista_divisores_add
            lista_divisores.sort()

        respuesta.append(sum(lista_divisores))

    if respuesta[0] == n2 and respuesta[1] == n1:
        return True
    else:
        return False

print(es_primo(7))
print(criba_heratosteles(54))
print(es_primo_mersenne(8191))
print(descomposicion_factorial(20))
print(es_perfecto(6))
print(son_primos_gemelos(3,5))
print(rango_primos_gemelos(120))
print(son_amigos(6232,6368))
