"""
función en python llamada fizzbuzz, que acepte dos parámetros enteros start y end. 
Los valores predeterminados para start y end son 1 y 101, respectivamente.
"""

def fizzbuzz(start=1,end=101):
   
   if start>end:
        inc=-1
   else:
        inc=1

   for i in range(start,end,inc):
       div30=i%3
       div50=i%5
    
       if div30==0 and div50==0:
           print("fizzbuzz")
       elif div30==0:
           print("fizz")
       elif div50==0:
            print("buzz")
       else:
            print(i)


if __name__=="__main__":
    start=int(input("Ingrese el valor inicial para realizar la operacion: "))
    end=int(input("Ingrese el valor final para realizar la operacion: "))

    fizzbuzz(start,end)