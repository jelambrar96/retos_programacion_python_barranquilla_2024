# git clone htpps://jelambrar96_reto_04
# Ayman358.py
# git commit Ayman358github_reto_04

def fizzbuzz(start=1, end=101):
    if start < end:
        step = 1
    else:
        step = -1 

    rango = range(start, end, step)
    for i in rango:
        # print(i)
        # if i=(multiplo de 3 reemplazar por el valor "fizz")
        if i% 3==0 and i % 5== 0:
            print ("fizzbuzz")         
        elif i% 3==0 : 
            print  ("fizz")
        elif i % 5 == 0:
            print("buzz")
        # if i=(multiplo de 5 remplazar por el valor "buzz")
        # if i=(multiplo de 3 y 5 remplazar por el valor "fizzbuzz")
        else:
            print(i)




if __name__ == "__main__":
    print("prueba 1")
    fizzbuzz(1, 20)
    print()
    print("prueba 2")
    fizzbuzz(20, 1)
