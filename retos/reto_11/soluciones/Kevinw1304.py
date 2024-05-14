def es_triangulo (a,b,c):

    ##Los números deben ser no negativos ##
    if a<0 or b<0 or c<0:
        return False 
    
    ## Los números no deben ser 0 al mismo tiempo ##
    if a==0 and b==0 and c==0:
        return False

    ## el número mayor no puede ser mayor a la suma de los dos menores ##

    lista_lados = sorted ([a,b,c])
    # print("lista_lados", lista_lados)
    lado_mayor = lista_lados [2]
    lado_menor = lista_lados [0]
    lado_medio = lista_lados [1]
    
    if lado_mayor > (lado_menor + lado_medio):
        return False
    
    return True
    


def es_equilatero (a,b,c):
    if not es_triangulo (a,b,c):
        return False
    
    if a == b and c == a and b == c:
        return True
    else: 
        return False
        

        
def es_isoceles (a,b,c):
    if not es_triangulo (a,b,c):
        return False
    
    # Triangulo isoceles dos de los lados son igaules#
    if a == b or b == c or a == c:
        return True
    else:
        return False


def es_escaleno (a,b,c):
    if not es_triangulo (a,b,c):
        return False
    
    # Triangulo escaleno cuando los tres lados son desiguales #

    if a != b and b != c and c != b:
        return True
    else:
        return False



def es_rectangulo (a,b,c):
    if not es_triangulo (a,b,c):
        return False


    lista_lados = sorted ([a,b,c])
    lado_mayor = lista_lados [2]
    lado_menor = lista_lados [0]
    lado_medio = lista_lados [1]

    if lado_mayor**2 == (lado_menor**2 + lado_medio**2):
        return True
    else:
        return False


if __name__ == '__main__':

    print("es_triangulo(0, 0, 0)", es_triangulo(0, 0, 0))
    print("es_triangulo(3, -2, 1)", es_triangulo(3, -2, 1))
    
    print("es_equilatero(3, 2, 1)", es_equilatero(3, 2, 1))
    print("es_equilatero(3, 3, 3)", es_equilatero(3, 3, 3))
    
    print("es_escaleno(3, 2, 1)", es_escaleno(3, 2, 1))
    print("es_escaleno(3, 2, 2)", es_escaleno(3, 2, 2))
    
    print("es_isoceles(3, 2, 2)", es_isoceles(3, 2, 2))
    print("es_isoceles(3, 1, 2)", es_isoceles(3, 1, 2))

    print("es_rectangulo(3, 4, 5)", es_rectangulo(3, 4, 5))
    print("es_rectangulo(3, 4, 4)", es_rectangulo(3, 4, 4))

