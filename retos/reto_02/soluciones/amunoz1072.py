def conteo_421(num):
    con=0
    while num > 1:
        con+=1
        if num%2==0:
            num//=2
            print(num)
        else:
            num*=3
            num+=1
            print(num)
    return con

if __name__ == '__main__':
    """
    escribe lo que quieras que tu codigo haga cuando se llame directamente
    """
    numero=int(input("Ingrese un numero entero:"))
    print("el numero es:", numero,"y el numero de veces que se repite el proceso es", conteo_421(numero))