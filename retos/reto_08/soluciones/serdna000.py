from math import sqrt
from math import log2
def es_primo(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    raiz = round(sqrt(n))
    contador = 0
    if n == 2:
        raiz = n
    elif n == 3:
        raiz = n
    else:
        for i in range(2, raiz):
            if n % i == 0:
                contador += 1
    
    return contador == 0

def criba_heratosteles(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    listaPrimos = []
    for i in range(2, n):
        if es_primo(i):
            listaPrimos.append(i)
    
    return listaPrimos
    
def es_primo_mersenne(n):
    if n < 0 :
        raise Exception('El numero es menor que 0')
    
    mersenne = 0
    if not(es_primo(n)):
        return False
    else:
        mersenne = log2(n + 1)


print(es_primo(8.5))
print(criba_heratosteles(17))