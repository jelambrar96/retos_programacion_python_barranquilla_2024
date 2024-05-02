# Reto 07

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_07, por ejemplo: `jelambrar96_reto_07`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_07
    git push origin NombreUsusarioGithub_reto_07
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 

## Reto

1. Construye una función llamada `solucion_cuadratica` que tome tres parámetros, `a`, `b` y `c`. La función debe devolver las soluciones de la expresión cuadrática en una tupla. 

```
a * x ** 2 + b * x + c = 0
```

Aplica manejo de excepciones para los casos en que las soluciones no pueden ser encontradas.
 