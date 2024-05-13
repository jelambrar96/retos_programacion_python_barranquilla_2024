def fizzbuzz(start = 1, end = 101):
  if start<end:
    for i in range(start, end, 1):
      if((i % 3) == 0 and (i % 5) == 0):
        print("FizzBuzz")
      elif((i % 5) == 0):
        print("Buzz")
      elif((i % 3) == 0 ):
        print("Fizz")
      else:
        print(i)
  else:
    for i in range(start, end, -1):
      if((i % 3) == 0 and (i % 5) == 0):
        print("FizzBuzz")
      elif((i % 5) == 0):
        print("Buzz")
      elif((i % 3) == 0 ):
        print("Fizz")
      else:
        print(i)

if __name__=="__main__":
    fizzbuzz(4,20)