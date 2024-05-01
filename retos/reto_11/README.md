# Reto 11

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_11, por ejemplo: `jelambrar96_reto_11`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_11
    git push origin NombreUsusarioGithub_reto_11
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 

## Reto

1. Construye una función llamada `es_triangulo` que tome como parámetro tres numeros `a`, `b` y `c`, la función debe detemrinar si son números válidos para un triángulo. Es decir, los tres números deben ser no-negativos, no pueden ser igual a cero al mismo tiempo y el número mayor no puede ser mayor a la suma de los dos menores. 
2. Construye una función llamda `es_equilatero`  que tome como parámetro tres numeros `a`, `b` y `c`, y determine si con los tres lados ingresados se obtiene un triángulo equilátero. 
3. Construye una función llamda `es_isoceles`  que tome como parámetro tres numeros `a`, `b` y `c`, y determine si con los tres lados ingresados se obtiene un triángulo isóceles. 
4. Construye una función llamda `es_escaleno`  que tome como parámetro tres numeros `a`, `b` y `c`, y determine si con los tres lados ingresados se obtiene un triángulo escaleno. 
5. Construye una función llamda `es_rectangulo`  que tome como parámetro tres numeros `a`, `b` y `c`, y determine si con los tres lados ingresados se obtiene un triángulo rectángulo. Tip: recuerda el teorema de Pitágoras.