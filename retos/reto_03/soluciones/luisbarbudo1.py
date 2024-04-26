"""
escribe informacion de tu codigo aqui. 
"""

def fizzbuzz(end=101, start=1):
    """
    documenta tu funcion aqui
    """
    for n in range(start,end,1):
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 3 == 0:
            print("fizz") 
        elif n % 5 == 0:
            print("buzz")
        else :
            print(n)    

    for n in range(start,end,-1):
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 3 == 0:
            print("fizz") 
        elif n % 5 == 0:
            print("buzz")
        else :
            print(n)          
              




    pass
    # para imprimir un numero print(3)
    # para ver si un numero es divisible por otro 4 % 2 == 0: esta operacion arroja true
    # para recorer una secuencia usa el for: for i in range(incio, final, paso): 
    # paso =  start < end ? 1 : -1, 



if __name__ == '__main__':
    """
    escribe lo que quieras que tu codigo haga cuando se llame directamente
    """
    fizzbuzz(start=15, end=2)
    