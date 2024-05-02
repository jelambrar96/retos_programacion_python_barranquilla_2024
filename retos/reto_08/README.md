# Reto 08

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_08, por ejemplo: `jelambrar96_reto_08`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_08
    git push origin NombreUsusarioGithub_reto_08
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 

## Reto

1. Construye una funcion llamada `es_primo` que tome de entrada un número entero no negativo, y como salida un boolean (`True` o `False`) que indique si el número es primo o no. El número es primo si solo es divisible entre sí mismo y 1, y no tiene otros divisores. Para determinar esto, la función puede iterar desde 2 hasta la raíz cuadrada del número y comprobar si el número es divisible por algún número en este rango. Si es divisible, devuelve `False`; si termina el bucle sin encontrar divisores, devuelve `True`.
2. Construye una función llamada `criba_heratósteles` que tome como entrada un número entero no negativo `n` y devuelva una lista con todos los números primos desde `0` hasta `n - 1`. Utiliza el método de la Criba de Eratóstenes, donde inicialmente se asumen todos los números como primos y se van eliminando los no primos. Se empieza con el primer número primo, 2, y se eliminan todos sus múltiplos. Luego se avanza al siguiente número no eliminado y se repite el proceso hasta que se ha procesado hasta la raíz cuadrada de `n`.
3. Construye una función llamada `es_primo_mersenne` que tome como entrada un número no negativo y arroje como salida un boolean que indique si es un primo de mersenne o no. Los primos de Mersenne son de la forma `2 ** p - 1`, donde `p` es también un número primo. La función debería primero verificar si `p` es primo (usando `es_primo`), y luego, calcular `2**p - 1` y verificar si este resultado es primo.
4. Construye una función llamada `descomposicion_factorial` que tome como entrada un número entero no negativo y como salida una lista con los factores primos de ese número ordenados ascendentemente. Para encontrar los factores primos, puede comenzar desde el número 2 y dividir repetidamente el número de entrada por este factor mientras sea divisible antes de pasar al siguiente posible factor primo. Ejemplo, para el `n = 12`, la salida debería ser igual a `[2, 2, 3]`
5. Construye una función llamada `es_perfecto` que tome como entrada un número entero no negativo y como salida un booleano que indique si el número es perfecto o no. 
6. Construye una función llamada `son_primos_gemelos` que dado dos números primos identifique si son primos gemelos. Los primos gemelos son pares de números primos que tienen una diferencia de dos (por ejemplo, 11 y 13). Esta función debe tomar dos números y primero verificar si ambos son primos y luego si la diferencia entre ellos es exactamente dos para determinar si son primos gemelos.
7. Construye una función llamada `rango_primos_gemelos` que dato un número entero no negativo `n` y devuelva una lista con todas las parejas de números primos gemelos desde `0` hasta `n - 1`. 
8. Construye una función llamada `son_amigos` que dado dos números enteros no negativos `n1` y `n2`, devuelva un booleano que indique si son números amigos o no. Dos números son amigos si cada uno es igual a la suma de los divisores propios del otro. La función debe calcular la suma de los divisores de `n1` y `n2` y verificar si `n1` es igual a la suma de los divisores de `n2` y viceversa.
