def fizzbuzz(start=1, end=101):
    if start<end:
        secuencia= range(start,end)
        for item in secuencia:
            if item%3==0 and item%5==0:
                print("Fizzbuzz")
            elif item%3==0:
                print("Fizz")
            elif item%5==0:
                print("Buzz")
            else:
                print(item)

    else:
        secuencia= range(start,end, -1)
        for item in secuencia:
            if item%3==0 and item%5==0:
                print("Fizzbuzz")
            elif item%3==0:
                print("Fizz")
            elif item%5==0:
                print("Buzz")
            else:
                print(item)
    pass

if __name__ == '__main__':
   start=int(input("Escribe el número inicial: ")) 
   end=int(input("Escribe el número a finalizar: "))
   print(fizzbuzz(start, end))