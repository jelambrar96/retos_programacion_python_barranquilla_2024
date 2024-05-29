def es_fibonacci(n):
    lista_fibonacci = [0, 1]
    for i in range(n):
        if lista_fibonacci[i] + lista_fibonacci[i+1] <= n:
            lista_fibonacci.append(lista_fibonacci[i] + lista_fibonacci[i+1])
        else:
            break
    
    return n in lista_fibonacci

def termino_fibonacci(n):
    lista_fibonacci = [0, 1]
    for i in range(n):
        if len(lista_fibonacci) < n:
            lista_fibonacci.append(lista_fibonacci[i] + lista_fibonacci[i+1])
        else:
            break

    return lista_fibonacci[-1]

def rango_fibonaci(n,m):
    lista_fibonacci = [0, 1]
    for i in range(m):
        if lista_fibonacci[i] + lista_fibonacci[i+1] < m:
            lista_fibonacci.append(lista_fibonacci[i] + lista_fibonacci[i+1])
        else:
            break
    
    return [num for num in lista_fibonacci if num >= n]

print(es_fibonacci(22))
print(termino_fibonacci(15))
print(rango_fibonaci(8,150))
