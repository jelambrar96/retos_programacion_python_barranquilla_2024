def incremento(n: int) -> int:
    """Incrementa el valor dado en 1."""
    return n + 1


def decremento(n: int) -> int:
    """Decrementa el valor dado en 1."""
    return n - 1


def absoluto(n: int) -> int:
    """Calcula el valor absoluto de un número entero usando incrementos y decrementos."""
    contador = 0
    while n != 0:
        # Ajusta n hacia 0 y cuenta los pasos necesarios.
        n = incremento(n) if n < 0 else decremento(n)
        contador = incremento(contador)
    return contador


def cambio_signo(n: int) -> int:
    """Cambia el signo de un número entero, devolviendo su negativo."""
    contador = 0
    while n != 0:
        # Ajusta n hacia 0, incrementando o decrementando contador basado en el signo de n.
        n = incremento(n) if n < 0 else decremento(n)
        contador = incremento(contador) if n < 0 else decremento(contador)
    return contador


def suma(n: int, m: int) -> int:
    """Suma dos números enteros ajustando el primero por el valor del segundo."""
    while m != 0:
        n = incremento(n) if m > 0 else decremento(n)
        m = decremento(m) if m > 0 else incremento(m)
    return n


def resta(n: int, m: int) -> int:
    """Resta dos números enteros ajustando el primero en dirección opuesta al segundo."""
    while m != 0:
        n = decremento(n) if m > 0 else incremento(n)
        m = decremento(m) if m > 0 else incremento(m)
    return n


def multiplicacion(n: int, m: int) -> int:
    """Multiplica dos números utilizando suma repetitiva."""
    acumulador = 0
    bandera = m < 0
    while m != 0:
        acumulador = suma(acumulador, n)
        m = incremento(m) if bandera else decremento(m)
    return cambio_signo(acumulador) if bandera else acumulador


def division_entera(n: int, m: int) -> tuple:
    """Realiza la división entera entre dos números, devolviendo el cociente y el residuo."""
    assert m != 0, "ERROR m == 0"
    bandera_n = n < 0
    bandera_m = m < 0
    absoluto_m = absoluto(m)
    absoluto_n = absoluto(n)
    contador = 0
    while absoluto_n >= absoluto_m:
        absoluto_n = resta(absoluto_n, absoluto_m)
        contador = incremento(contador)
    cociente = cambio_signo(contador) if bandera_m ^ bandera_n else contador
    residuo = cambio_signo(absoluto_n) if bandera_n else absoluto_n
    return cociente, residuo


def potencia(n: int, m: int) -> int:
    """Calcula la potencia de un número elevado a otro usando multiplicación repetitiva."""
    assert m >= 0, "ERROR, m <= 0"
    potencia = 1
    while m != 0:
        potencia = multiplicacion(potencia, n)
        m = decremento(m)
    return potencia
