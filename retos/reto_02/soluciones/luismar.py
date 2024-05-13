def conteo_421(num):
  cont = 0
  while num > 1:
    if num % 2 == 0:
      num //= 2
      cont += 1
    else:
      num *= 3
      num += 1
      cont += 1
  return cont


if __name__=="__main__":
    num=int(input("Ingrese su numero"))
    print(conteo_421(num))