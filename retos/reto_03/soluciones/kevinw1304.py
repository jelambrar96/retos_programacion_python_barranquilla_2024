"""
escribe informacion de tu codigo aqui. 
"""

def fizzbuzz(end=101, start=1):
  
    paso = 3

    if start > end:
   
        paso = -1

    for i in range (start, end, paso):    
        if i%3 and i%5 == 0:
            print ("FizzBuzz")
        elif i%5==0:
            print ("buzz")   
        elif  i%3==0:
            print ("fizz")   
        else:
            print (i)


if __name__ == '__main__':
    """
    escribe lo que quieras que tu codigo haga cuando se llame directamente
    """
    fizzbuzz (start = 1, end = 50)
