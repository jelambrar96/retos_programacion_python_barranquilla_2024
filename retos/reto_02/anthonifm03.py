
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

if __name__ == '__main__':
    """
    escribe lo que quieras que tu codigo haga cuando se llame directamente
    """
k = conteo_421(4)
print(k)
assert k == 2

