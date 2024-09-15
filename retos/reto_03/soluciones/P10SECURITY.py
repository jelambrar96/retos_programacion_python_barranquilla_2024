"""
CODIGO QUE IMPRIE FIZZBUZZ SI ENCUENTRA UN NUMERO DIVISIBLE POR  Y 5 
FIZZ SI ENCUENTRA UN NUERO DIVISIBLE POR  3  
BUZZ SI ENCUENTRA UN NUMERO DIVISIBLE POR 5.
"""

def fizzbuzz(fin=101, inicio=1):
    """
    documenta tu funcion aqui
    """
    paso = 1
    if inicio>fin: 
        paso =-1

    range = range(inicio, fin, paso)
    for item in range:
        if  item%3==0  and item%5==0:
            print ("fizzbuzz")
        elif item%3==0 :
            print ("fizz")
        elif item%5==0 :
            print ("buzz")
        else:
            print ("item")