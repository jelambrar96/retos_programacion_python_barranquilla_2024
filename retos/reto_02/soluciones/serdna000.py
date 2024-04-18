def conteo_421(a):
    print(a)
    while a > 1:
        if a % 2 == 0:
            a //= 2
            print(a)
        else:
            a *= 3
            a += 1
            print(a)

conteo_421(27)