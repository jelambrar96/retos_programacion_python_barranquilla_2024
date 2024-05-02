def fizzbuzz(end=101, start=1):
            
    if start<end:
        secuencia= range(start, end)
        for item in secuencia:
            if item%3==0 and item%5==0:
                print("fizzbuzz")
            elif item%5==0:
                print("buzz")
            elif item%3==0:
                print(("fizz"))
            else:
                print(item)
    else:
        secuencia= range(start, end, -1)
        for item in secuencia:
            if item%3==0 and item%5==0:
                print("fizzbuzz")
            elif item%5==0:
                print("buzz")
            elif item%3==0:
                print("fizz")
            else:
                print(item)

       
    pass


if __name__ == '__main__':
    
    start=int(input("digite el numero a empezar:"))
    end=int(input("digite el numero a finalizar:"))
    print(fizzbuzz(start, end))
    pass

    