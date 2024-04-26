def conteo_421(num):

    contador=0

    while num>1:

        if num%2==0:
            num//=2
            print("El nuevo valor es: ", num)
            contador+=1
            print("Contador: ", contador)
        
        else:
            num*=3
            num+=1
            print("El nuevo valor es: ", num)
            contador+=1
            print("Contador:", contador)

    return contador

if __name__=="__main__":

    num=int(input("Escribe un número entero: "))
    print("El número es: ", num, "El contador final es: ", conteo_421(num))