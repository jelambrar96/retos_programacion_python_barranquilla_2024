
def fizzbuzz(start=1,end=101):
   
   if start>end:
        paso=-1
   else:
        paso=1

   for i in range(start,end,paso):
       res1=i%3
       res2=i%5
    
       if res1==0 and res2==0:
           print("fizzbuzz")
       elif res1==0:
           print("fizz")
       elif res2==0:
            print("buzz")
       else:
            print(i)


if __name__=="__main__":
    start=int(input("Ingrese el valor inicial para realizar la operacion: "))
    end=int(input("Ingrese el valor final para realizar la operacion: "))

    fizzbuzz(start,end)
        

        
    
    

    

      
   
