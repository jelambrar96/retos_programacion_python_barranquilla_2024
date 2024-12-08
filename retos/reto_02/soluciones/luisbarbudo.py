 
 
def conteo_421(n: int):
    """
    documenta tu funcion aqui 
    """
    c = 0
    while n >1:
        if n%2 ==0:
            n=n//2
        else:
            n = (n*3)+1
        c+=1
    return c


if __name__ == '__main__':
    """
    escribe lo que quieras que tu codigo haga cuando se llame directamente
    """
    n = int(input("inserta un numero:" ))
    print(conteo_421(n))