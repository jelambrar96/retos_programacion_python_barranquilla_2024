 
def raiz_cuadrada(numero):
    try:
        return numero ** 0.5
    except:
        return None
       


def inverso_multiplicativo (numero):
    try:
        return 1/numero
    except:
        return None





if __name__ == '__main__':
    print (raiz_cuadrada(8))
    print (inverso_multiplicativo(0))
pass