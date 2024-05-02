# Reto 09

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_09, por ejemplo: `jelambrar96_reto_09`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_09
    git push origin NombreUsusarioGithub_reto_09
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 

## Reto

1. Construye una función llamada `es_fibonacci` que tome como entrada un número n y devuelva un booleano que indique si pertenece o no a la serie fibonnaci. 
2. Construye una función llamada `termino_fibonacci` que tome como entrada un número n y devuelva el `n-simo` término de la serie fibonnaci. Serie Fibonnaci: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...` Para este caso, tomemos que el 0 es el término 0. 
3. Construye una función llamada `rango_fibonaci` que tome como entrada dos número enteros `n` y `m` y devuelva una lista con los números que pertenecen a la serie fibonnaci que son mayores o iguales que `n` y menores que `m`.

