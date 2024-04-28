
def incremento(n: int) -> int:
    """Incrementa el valor dado en 1."""
    return n + 1


def decremento(n: int) -> int:
    """Decrementa el valor dado en 1."""
    return n - 1

# -----------------------------------------------------------------------------
# SOLUCIONES EMPLEANDO CICLOS
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# SOLUCIONES EMPLEANDO RECURSIVIDAD
# -----------------------------------------------------------------------------

def absoluto_recursivo(n: int) -> int:
    """
    Compute the absolute value of an integer recursively.
    
    Args:
    n (int): The integer whose absolute value is to be found.
    
    Returns:
    int: The absolute value of the integer.
    """
    def aux(n: int, m: int):
        """
        Helper recursive function to calculate the absolute value.
        """
        if n > 0:
            return aux(decremento(n), incremento(m))
        elif n < 0:
            return aux(incremento(n), incremento(m))
        else:
            return m
    return aux(n, 0)


def cambio_signo_recursivo(n: int) -> int:
    """
    Change the sign of an integer recursively.
    
    Args:
    n (int): The integer whose sign is to be changed.
    
    Returns:
    int: The integer with its sign changed.
    """
    def aux(n: int, m: int):
        """
        Helper recursive function to change the sign of the integer.
        """
        if n > 0:
            return aux(decremento(n), incremento(m))
        elif n < 0:
            return aux(incremento(n), decremento(m))
        else:
            return m
    return aux(n, 0)


def suma_recursiva(n: int, m: int) -> int:
    """
    Sum two integers recursively.
    
    Args:
    n (int): First integer.
    m (int): Second integer to be added to the first.
    
    Returns:
    int: The sum of the two integers.
    """
    if m > 0:
        return suma_recursiva(incremento(n), decremento(m))
    elif m < 0:
        return suma_recursiva(decremento(n), incremento(m))
    else:
        return n


def resta_recursiva(n: int, m: int) -> int:
    """
    Subtract one integer from another recursively.
    
    Args:
    n (int): Integer from which to subtract.
    m (int): Integer to be subtracted.
    
    Returns:
    int: The result of the subtraction.
    """
    if m > 0:
        return resta_recursiva(decremento(n), decremento(m))
    elif m < 0:
        return resta_recursiva(incremento(n), incremento(m))
    else:
        return n


def multiplicacion_recursiva(n: int, m: int):
    """
    Multiply two integers recursively.
    
    Args:
    n (int): First integer.
    m (int): Second integer to be multiplied with the first.
    
    Returns:
    int: The product of the two integers.
    """
    def aux(producto, nx, mx):
        """
        Helper recursive function to calculate the product.
        """
        if mx == 0:
            return producto
        return aux(suma_recursiva(producto, nx), nx, decremento(mx))
    bandera = False
    if m < 0:
        bandera = True
        n = absoluto_recursivo(n)
        m = absoluto_recursivo(m)
    producto = aux(0, n, m)
    if bandera:
        producto = cambio_signo_recursivo(producto)
    return producto


def division_entera_recursiva(n: int, m: int):
    """
    Perform integer division of two numbers recursively.
    
    Args:
    n (int): Numerator.
    m (int): Denominator (must not be zero).
    
    Returns:
    tuple: A tuple containing the quotient and the remainder.
    """
    assert m != 0, "ERROR m == 0"
    def aux(resto, contador, mx):
        """
        Helper recursive function to calculate quotient and remainder.
        """
        if resto < mx:
            return contador, resto
        return aux(resta_recursiva(resto, mx), incremento(contador), mx)
    bandera_n = n < 0
    bandera_m = m < 0
    absoluto_m = absoluto_recursivo(m)
    absoluto_n = absoluto_recursivo(n)
    cociente, residuo = aux(absoluto_n, 0, absoluto_m)
    cociente = cambio_signo_recursivo(cociente) if bandera_m ^ bandera_n else cociente
    residuo = cambio_signo_recursivo(residuo) if bandera_n else residuo
    return cociente, residuo


def potencia_recursiva(n: int, m: int) -> int:
    """
    Calculate the power of a number recursively.
    
    Args:
    n (int): The base.
    m (int): The exponent (must be non-negative).
    
    Returns:
    int: The result of raising the base to the power of the exponent.
    """
    assert m >= 0, "ERROR, m <= 0"
    def aux(pot: int, nx: int, mx: int):
        """
        Helper recursive function to calculate the power.
        """
        if mx == 0:
            return pot
        return aux(multiplicacion_recursiva(pot, nx), nx, decremento(mx))
    return aux(1, n, m)


# -----------------------------------------------------------------------------
# TESTING
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    assert incremento(0) == 1, "La función 'incremento' no devuelve el resultado esperado para n = 0"
    assert incremento(4) == 5, "La función 'incremento' no devuelve el resultado esperado para n = 4"
    assert incremento(-4) == -3, "La función 'incremento' no devuelve el resultado esperado para n = -3"

    assert decremento(0) == -1, "La función 'decremento' no devuelve el resultado esperado para n = 0"
    assert decremento(4) == 3, "La función 'decremento' no devuelve el resultado esperado para n = 4"
    assert decremento(-4) == -5, "La función 'decremento' no devuelve el resultado esperado para n = -4"

    assert suma(0, 0) == (0 + 0), "La función 'suma' no devuelve el resultado esperado para n = 0, m = 0"
    assert suma(4, 3) == (4 + 3), "La función 'suma' no devuelve el resultado esperado para n = 4, m = 3"
    assert suma(-4, 6) == (-4 + 6), "La función 'suma' no devuelve el resultado esperado para n = -4, m = 6"

    assert resta(0, 0) == (0 - 0), "La función 'resta' no devuelve el resultado esperado para n = 0, m = 0"
    assert resta(4, 3) == (4 - 3), "La función 'resta' no devuelve el resultado esperado para n = 4, m = 3"
    assert resta(-4, 6) == (-4 - 6), "La función 'resta' no devuelve el resultado esperado para n = -4, m = 6"

    assert multiplicacion(0, 0) == (0 * 0), "La función 'multiplicacion' no devuelve el resultado esperado para n = 0, m = 0"
    assert multiplicacion(4, 3) == (4 * 3), "La función 'multiplicacion' no devuelve el resultado esperado para n = 4, m = 3"
    assert multiplicacion(4, 6) == (4 * 6), "La función 'multiplicacion' no devuelve el resultado esperado para n = -4, m = 6"    
        
    assert potencia(5, 2) == (5 ** 2), "La función 'potencia' no devuelve el resultado esperado para n = 5, m = 2"
    assert potencia(4, 3) == (4 ** 3), "La función 'potencia' no devuelve el resultado esperado para n = 4, m = 3"
    assert potencia(3, 3) == (3 ** 3), "La función 'potencia' no devuelve el resultado esperado para n = 3, m = 3"    
    assert potencia(3, 0) == (3 ** 0), "La función 'potencia' no devuelve el resultado esperado para n = 3, m = 3"    

    assert division_entera(5, 2)[0] == (5 // 2), "La función 'division' no devuelve el resultado esperado para n = 5, m = 2"
    assert division_entera(4, 3)[0] == (4 // 3), "La función 'division' no devuelve el resultado esperado para n = 4, m = 3"
    assert division_entera(3, 3)[0] == (3 // 3), "La función 'division' no devuelve el resultado esperado para n = 3, m = 3"    
    assert division_entera(5, 2)[1] == (5 % 2), "La función 'division' no devuelve el resultado esperado para n = 5, m = 2"
    assert division_entera(4, 3)[1] == (4 % 3), "La función 'division' no devuelve el resultado esperado para n = 4, m = 3"
    assert division_entera(3, 3)[1] == (3 % 3), "La función 'division' no devuelve el resultado esperado para n = 3, m = 3"    

    # prueba funciones recursivas

    assert suma_recursiva(0, 0) == (0 + 0), "La función 'suma_recursiva' no devuelve el resultado esperado para n = 0, m = 0"
    assert suma_recursiva(4, 3) == (4 + 3), "La función 'suma_recursiva' no devuelve el resultado esperado para n = 4, m = 3"
    assert suma_recursiva(-4, 6) == (-4 + 6), "La función 'suma_recursiva' no devuelve el resultado esperado para n = -4, m = 6"

    assert resta_recursiva(0, 0) == (0 - 0), "La función 'resta_recursiva' no devuelve el resultado esperado para n = 0, m = 0"
    assert resta_recursiva(4, 3) == (4 - 3), "La función 'resta_recursiva' no devuelve el resultado esperado para n = 4, m = 3"
    assert resta_recursiva(-4, 6) == (-4 - 6), "La función 'resta_recursiva' no devuelve el resultado esperado para n = -4, m = 6"

    assert multiplicacion_recursiva(0, 0) == (0 * 0), "La función 'multiplicacion_recursiva' no devuelve el resultado esperado para n = 0, m = 0"
    assert multiplicacion_recursiva(4, 3) == (4 * 3), "La función 'multiplicacion_recursiva' no devuelve el resultado esperado para n = 4, m = 3"
    assert multiplicacion_recursiva(4, 6) == (4 * 6), "La función 'multiplicacion_recursiva' no devuelve el resultado esperado para n = -4, m = 6"    
        
    assert potencia_recursiva(2, 2) == (2 ** 2), "La función 'potencia_recursiva' no devuelve el resultado esperado para n = 5, m = 2"
    assert potencia_recursiva(2, 3) == (2 ** 3), "La función 'potencia_recursiva' no devuelve el resultado esperado para n = 4, m = 3"
    assert potencia_recursiva(3, 0) == (3 ** 0), "La función 'potencia_recursiva' no devuelve el resultado esperado para n = 3, m = 3"    

    assert division_entera_recursiva(5, 2)[0] == (5 // 2), "La función 'division' no devuelve el resultado esperado para n = 5, m = 2"
    assert division_entera_recursiva(4, 3)[0] == (4 // 3), "La función 'division' no devuelve el resultado esperado para n = 4, m = 3"
    assert division_entera_recursiva(3, 3)[0] == (3 // 3), "La función 'division' no devuelve el resultado esperado para n = 3, m = 3"    

    assert division_entera_recursiva(5, 2)[1] == (5 % 2), "La función 'division' no devuelve el resultado esperado para n = 5, m = 2"
    assert division_entera_recursiva(4, 3)[1] == (4 % 3), "La función 'division' no devuelve el resultado esperado para n = 4, m = 3"
    assert division_entera_recursiva(3, 3)[1] == (3 % 3), "La función 'division' no devuelve el resultado esperado para n = 3, m = 3"   
