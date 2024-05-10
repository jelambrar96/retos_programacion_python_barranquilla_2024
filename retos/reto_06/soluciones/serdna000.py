from math import sqrt
def raiz_cuadrada(numero):
    try:
        return sqrt(numero)
    except:
        return None

def inverso_multiplicativo(numero):
    try:
        return 1/numero
    except ZeroDivisionError:
        return None

print(inverso_multiplicativo(0))