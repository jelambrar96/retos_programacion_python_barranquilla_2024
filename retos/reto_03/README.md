# Reto 03: FizzBuzz

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_02, por ejemplo: `jelambrar96_reto_03`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_03
    git push origin NombreUsusarioGithub_reto_03
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 

## Reto

Escribe una función en python llamada `fizzbuzz`, que acepte dos parámetros enteros **start** y **end**. Los valores predeterminados para **start** y **end** son 1 y 101, respectivamente. El programa debe mostrar por consola en cada línea los números desde **start** hasta **end** (sin incluirlo). Y además debe hacer lo siguiente:  
- Para los múltiplos de 3 reemplazar el número por la palabra "fizz".
- Para los múltiplos de 5 reemplazar el número por la palabra "buzz".
- Para los múltiplos de 3 y de 5 a la vez reemplar el número por la palabra "fizzbuzz".
Si **end** es menor a **start** los números deben ir de forma descendente.  


## Ejemplos: 

### Ejemplo 1

Para `end = 5`
```plain 
1
2
fizz
4
```

### Ejemplo 2

Para `start = 15` y `end = 2`
```
fizzbuzz
14
13
fizz
11
buzz
fizz
8
7
6
buzz
4
fizz
```

## Tip:

Ten prensente el orden en que estás realizando las condiciones. Esto puede afectar la salida de tu codigo.
