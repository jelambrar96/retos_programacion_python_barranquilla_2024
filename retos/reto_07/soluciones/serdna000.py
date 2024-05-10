from math import sqrt
class ErrorNumeroNegativo(Exception):
    pass

def solucion_cuadratica(a = 1, b = 1, c = 1):
    try:
        if a == 0:
            return -c/b
        else:
            if b**2 - 4*a*c > 0:
                resultado1 = ((-b) + sqrt(b**2 - 4*a*c)) / 2*a
                resultado2 = ((-b) - sqrt(b**2 - 4*a*c)) / 2*a
                return (resultado1, resultado2)
            elif b**2 - 4*a*c == 0:
                resultado1 = -b / 2*a
                return resultado1
            else:
                raise ErrorNumeroNegativo('El Discriminante es un numero negativo, por lo tanto no hay solucion')
            
    except ErrorNumeroNegativo as e:
        print(f'Error de numero negativo: {e}')
    except:
        print('Error el codigo no se pudo ejecutar correctamente')
    
print(solucion_cuadratica(7,5,1))