# Reto 10

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_10, por ejemplo: `jelambrar96_reto_10`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_10
    git push origin NombreUsusarioGithub_reto_10
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 

## Reto

1. Construye una función llamada cifras, que tome un número entero no negativo y devuelva una lista de las cifras que éste contiene. 
2. Construye una función llamada `es_armstrong` que tome un numero entero no negativo, y devuelva un booleano que indique si es un número armstrong o no. Un número de `n` dígitos es un número de Armstrong si es igual a la suma de las `n-ésimas` potencias de sus dígitos. Por ejemplo, 371, 8208 y 4210818 son números de Armstrong ya que
    ```
        371 = 3**3 + 7**3 + 1**3 y  
        8208 = 8**4 + 2**4 + 0**4 + 8**4 
    4210818 = 4**7 + 2**7 + 1**7 + 0**7 + 8**7 + 1**7 + 8**7
    ```
3. Construye una función llamada `es_feliz` que tome un numero entero no negativo, y devuelva un booleano que indique si es un número feliz o no. Si un número entero positivo es reemplazado por la suma de los cuadrados de sus dígitos y repitiendo sucesivamente el proceso nos da 1, es un número feliz. Si, por el contrario, entra en un bucle que no incluye el 1 estamos ante un número infeliz. 7 es un número feliz, ya que:
    ```
    7**2 = 49
    4**2 + 9**2 = 97
    9**2 + 7**2 = 130
    1**2 + 3**2 + 0**2 = 10
    1**2 + 0**2 = 1.
    ```
4. Construye una función llamada `es_primo_feliz` que tome un número entero no negativo y devuelva `True` cuando el número sea primo y feliz al mismo tiempo. De lo contrario, devuelve `False`.