# Reto 15: Triángulo de Pascal

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_14, por ejemplo: `jelambrar96_reto_15`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_15
    git push origin NombreUsusarioGithub_reto_15
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 


# Reto 

Objetivo: Crear una función en Python llamada `triangulopascal` que tome un parámetro entero `n` y imprima el triángulo de Pascal correspondiente.

Estructura de la función:

 La función `triangulopascal` recibirá un parámetro `n`, que representará el número de filas del triángulo de Pascal.
 La función imprimirá el triángulo de Pascal utilizando una estructura de datos adecuada (por ejemplo, una lista de listas).
 Cada fila del triángulo se representará como una lista de números enteros, donde cada número es el binomio de Newton correspondiente.

Algoritmo:

1. Inicializa una lista `pascaltriangle` con `n` filas, todas vacías.
2. Itera sobre cada fila `i` del triángulo (desde 0 hasta `n-1`):
	 Para la primera fila (`i == 0`), agrega la lista `[1]` a `pascaltriangle`.
	 Para las filas restantes (`i > 0`):
		+ Calcula los elementos de la fila actual utilizando la fórmula de binomio de Newton: `pascaltriangle[i][j] = pascaltriangle[i-1][j-1] + pascaltriangle[i-1][j]` (donde `j` es el índice dentro de la fila).
		+ Agrega la lista de elementos calculados a `pascaltriangle`.
3. Imprime el triángulo de Pascal utilizando una estructura de impresión adecuada (por ejemplo, utilizando un bucle `for` y `print`).

Ejemplo:

Si se llama a la función `triangulopascal` con `n = 5`, debería imprimir el siguiente triángulo de Pascal:
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```
Pistas y recursos adicionales:

 Utiliza listas y bucles para implementar la función.
 Puedes utilizar la fórmula de binomio de Newton para calcular los elementos del triángulo.
 Considera utilizar una función auxiliar para calcular los elementos de cada fila, si lo deseas.

Evaluación:

 La función `triangulopascal` debe recibir un parámetro entero `n` y imprimir el triángulo de Pascal correspondiente.
 La función debe ser capaz de manejar valores de `n` entre 1 y 100, por ejemplo.
 La salida debe ser legible y fácil de entender.

Bonus:

* Agrega una opción para imprimir el triángulo de Pascal en formato de texto o CSV.
* Implementa una función para calcular la suma de los elementos de cada fila o la suma total del triángulo.

¡Buena suerte con el reto!
