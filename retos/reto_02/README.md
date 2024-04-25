# Reto 02

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_02, por ejemplo: `jelambrar96_reto_02`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_02
    git push origin NombreUsusarioGithub_reto_02
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 

## Reto

El reto consiste en contruir una función python llamada `conteo_421` esta función tiene como entradas un número entero y como salida otro número entero. La función debe ser capaz de contar el número de veces que un número repite el siguiente loop: 
- Mientras el número sea mayor a 1
    - Si el numero es par le aplicamos division entera entre dos 
    - Si el número es impar lo multiplicamos por tres y le sumamos 1

Por ejemplo: 
Vamos a tomar el caso del número 4.
- El número 4 entra al loop porque es mayor que 1. El conteo es 1, como es par, el nuevo valor que toma es 2.
- El número 2 entra al loop porque es mayor que 1. El conteo es 2, como es par, el nuevo valor que toma es 1. 
- Como el número no es mayor a 1. Retornamos el valor del contador, es decir, 2.

## Tip:

Revisa el archivo template. El arhivo template tiene una sección al final donde puedes escribir código que quieres que se ejecute solo cuando se llame directamente el archivo. Aprovecha ese espacio para hacer pruebas allí.

