def conteo_421(a):
    contador = 0
    while a > 1:
        if a % 2 == 0:
            a //= 2
            contador += 1
        else:
            a *= 3
            a += 1
            contador += 1
    return contador

print(conteo_421(27))