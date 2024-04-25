
def incremento(numero):
    return numero + 1

def decremento(numero):
    return numero - 1

def suma(n, m):
    resultado = n
    for _ in range(m):
        resultado = incremento(resultado)
    return resultado

def resta(n, m):
    resultado = n
    for _ in range(m):
        resultado = decremento(resultado)
    return resultado

def multiplicacion(n, m):
    resultado = 0
    for _ in range(m):
        resultado = suma(resultado, n)
    return resultado

def division_entera(n, m):
    veces_resta = 0
    while n >= m:
        n = resta(n, m)
        veces_resta = incremento(veces_resta)
    return veces_resta, n

def potencia(n, m):
    resultado = 1
    for _ in range(m):
        resultado = multiplicacion(resultado, n)
    return resultado

if __name__ == '__main':
    # Input de usuario
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    # Ejemplos de uso con input de usuario
    print(f"Incremento de {num1} que es :", incremento(num1))  
    print(f"Decremento de {num1} que es :", decremento(num1))  
    print(f"Suma de : {num1} + {num2} es : ", suma(num1, num2))            
    print(f"Resta de : {num1} - {num2} es : ", resta(num1, num2))         
    print(f"Multiplicación: de : {num1} * {num2} : es : ", multiplicacion(num1, num2))  
    print(f"División Entera de : de : {num1} / {num2} es :", division_entera(num1, num2)) 
    print(f"Potencia: de : {num1} ** {num2} : es :", potencia(num1, num2))   
