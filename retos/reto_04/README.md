# Reto 04

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_04, por ejemplo: `jelambrar96_reto_04`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_04
    git push origin NombreUsusarioGithub_reto_04
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 

## Reto

1. Construye una función llamada `incremento` que dado un entero, lo incrementa en 1. 
2. Construye una función llamada `decremento` que dado un entero, lo reduzca en 1.
3. Construye una función llamada `suma` que tenga los parámetros `n` y `m`, la salida de esta función debe ser el resultado de llamar a la función `incremento` un número `m` de veces. 
4. Construye una función llamada `resta` que tenga los parámetros `n` y `m`, la salida de esta función debe ser el resultado de llamar a la función `decremento` un número `m` de veces. 
5. Construye una función llamada `multiplicacion` que tenga dos parámetros `n` y `m`, la salida de esta función debe ser el resultado de llamar a la función `suma` un número `m` de veces.
6.  Construye una función llamada `division_entera` que tenga dos parámetros `n` y `m`, la salida de esta función son dos parámetros: 
    1.  El primero es numero de veces que le tenemos que restar `m` a `n` mientras que `n` sea mayor a cero. Tienes que llamar a la función `resta`
    2.  El segundo es el residuo de esa operación. 
7. Construye una función `potencia` que tenga dos parámetros `n` y `m`, la salida de esta función debe ser el resultado de llamar a la función `multiplicacion` un número `m` de veces.
