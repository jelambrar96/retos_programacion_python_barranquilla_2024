"""
1. Construye una función llamada `raiz_cuadrada` que tome un numero. Aplica el bloque `try-except` para devolver 
`None` si no es posible obtener la raíz cuadrada.
2. Construye una función llamada `inverso_multiplicativo` que tome un numero y divida 1 entre ese número. 
Aplica el bloque `try-except` para devolver `None` si no es posible obtener el inverso multiplicativo.
"""
import math

def raiz_cuadrada(numero):
    try:
        res = math.sqrt(numero)
        return res
    except (ValueError,TypeError):    
        return None
    

if __name__=="__main__":
    numero=int(input("Ingrese el valor inicial para realizar la operacion: "))


    print('La raiz es ',raiz_cuadrada(numero))