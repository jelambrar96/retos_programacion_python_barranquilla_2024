# Reto 12

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_12, por ejemplo: `jelambrar96_reto_12`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_12
    git push origin NombreUsusarioGithub_reto_12
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 


# Reto 

1. Construye una función llamada `es_biciesto` que tome un numero entero que representará un año y retorne un booleano que indica si año es biciesto o no. La regla establece que un año es bisiesto si es divisible por 4, excepto en los casos en los que es divisible por 100, a menos que también sea divisible por 400.
 