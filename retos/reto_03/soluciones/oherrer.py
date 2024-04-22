def fizzbuzz (start=1 , end=101 ):
    paso = 1
    if start > end:
        paso =-1


    for i in range (start, end, paso):
        
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")  
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")  
        else:
            print(i)


if __name__ =="__main__":
    fizzbuzz(15,2)        


