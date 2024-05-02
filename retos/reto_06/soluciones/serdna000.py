from math import sqrt

def raiz_cuadrada(numero):
    try:
        resultado = sqrt(numero)
        return print(resultado)
    except:
        print("Error, no se pudo ejecutar el codigo")
    
def inverso_multiplicativo (numero):
    try:
        resultado = 1/numero
        return print(resultado)
    except:
        print('Error, no se pudo ejecutar el codigo')
    
inverso_multiplicativo("2")