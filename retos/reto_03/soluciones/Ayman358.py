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
        print(i)



if __name__ == "__main__":
    print("prueba 1")
    fizzbuzz(1, 20)
    print("prueba 2")
    fizzbuzz(20, 1)
