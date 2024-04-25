def conteo (num):
    contador=0
    while num>1:
        if num%2==0:
            num//=2
            print("El nuevo valor es: ", num)
            contador+=1
            print("contador",contador)
        
        else:
            num*=3
            num+=1
            print("el nuevo valor: ",num)
            contador+=1
            print("contador", contador)
    return contador

if __name__ == '__main__':
    num = int(input("Escribe un número entero: "))
    print(">El número es:", num, ", las veces que se repitio el proceso fue: ",conteo(num))
