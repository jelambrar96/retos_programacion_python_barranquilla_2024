"""
escribe informacion de tu codigo aqui. 
"""
def conteo_421(numero):
    contador=0
    while numero>1:
        if numero%2==0:
            numero//=2
            print("el nuevo valor es:",numero)
            contador+=1
            print("contador",contador)
        else:
            numero*=3
            numero+=1
            print("el nuevo valor es:",numero)
            contador+=1
            print("contador", contador)
    return contador
    
    


if __name__ == '__main__':
    """
    escribe lo que quieras que tu codigo haga cuando se llame directamente
    """
    numero=int(input("digite un numero entero:"))
    print("el numero es:", numero,"y el numero de veces que se repite el proceso es", conteo_421(numero))