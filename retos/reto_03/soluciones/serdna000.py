"""
escribe informacion de tu codigo aqui. 
"""

def fizzbuzz(end=101, start=1):
    if (start < end):
        for i in range(start, end, 1):
            if ((i % 3) == 0 and (i % 5) == 0):
                print('fizzbuzz')
            elif ((i % 3) == 0):
                print('fizz')
            elif ((i % 5) == 0):
                print('buzz')
            else:
                print(i)

    elif (start > end):
        for i in range(start, end, -1):
            if ((i % 3) == 0 and (i % 5) == 0):
                print('fizzbuzz')
            elif ((i % 3) == 0):
                print('fizz')
            elif ((i % 5) == 0):
                print('buzz')
            else:
                print(i)


if __name__ == '__main__':
    fizzbuzz(end=2, start=15)
