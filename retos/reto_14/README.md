# Reto 14

## Pasos para realizar el reto

Realiza los siguientes pasos para realizar el reto: 
- Construye una rama (branch) siguiendo el formato NombreUsusarioGithub_reto_14, por ejemplo: `jelambrar96_reto_14`
- Dentro de la carpeta soluciones escribe un archvivo con tu nombre de usuario de github y con extensión python. Por ejemplo `jelambrar96.py`
- El archivo que hayas creado deber ser capaz de resolver el reto. 
- Crea un commit con tus cambios:
    ```bash
    git add ruta/archivo/creado
    git commit -m NombreUsusarioGithub_reto_14
    git push origin NombreUsusarioGithub_reto_14
    ```
- Realiza un [**pull request**](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) al repositorio principal de retos barranquilla. 


# Reto 

1. Construye una función llamada `cifras_binarias` que tome un número entero no negativo y obtenga la lista de cifras del número en base dos (sistema binario) de forma que el primer valor de la lista corresponda al "bit" menos significativo. 
2. Construye una función llamada `dec_binario` que tome un número enterio no negativo y retorne una cadena equivalente a su representación en binario. 
3. Construye una función llamada `binario_dec` que tome una cadena y retorne el equivalente número en sistema decimal.
3. Construye una función llamada `es_numero_odiosio` que tome número entero y retorne un booleano que determine si es un número es odioso o no. Un número es odioso si la suma de sus cifras en sistema binario es un número impar. 
4. Construye una función llamada `es_numero_malvado` que tome número entero y retorne un booleano que determine si es un número es malvado o no. Un número es odioso si la suma de sus cifras en sistema binario es un número par. 
