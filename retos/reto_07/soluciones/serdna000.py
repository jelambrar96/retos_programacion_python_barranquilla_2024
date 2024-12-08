from math import sqrt
def solucion_cuadratica(a = 1, b = 1, c = 1):
    try:
        resultado1 = ((-b) + sqrt(b**2 - 4*a*c)) / 2*a
        resultado2 = ((-b) - sqrt(b**2 - 4*a*c)) / 2*a
        return (resultado1, resultado2)
    except:
        print('Error el codigo no se pudo ejecutar correctamente')
    
solucion_cuadratica(1,-5,6)