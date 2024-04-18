# Bienvenido al Repositorio de Retos de Programación en Python

¡Hola y bienvenido al repositorio de retos de programación en Python! Aquí encontrarás una serie de desafíos diseñados para poner a prueba tus habilidades de programación en Python. Ya seas un principiante o un experto en Python, ¡te invitamos a participar y mejorar tus habilidades!

## ¿Cómo Ejecutar los Retos?

Cada reto de programación viene con su propia carpeta dentro del repositorio. Dentro de cada carpeta encontrarás el enunciado del reto y, en algunos casos, archivos de prueba para comprobar la validez de tu solución.

Para ejecutar un reto:

1. Navega a la carpeta del reto que deseas resolver.
2. Sigue las instrucciones proporcionadas en el archivo README dentro de esa carpeta.
3. ¡Desarrolla tu solución y comprueba si pasa las pruebas!

¡Esperamos que disfrutes resolviendo los retos y contribuyendo a esta comunidad de programadores en Python!

## ¿Cómo Contribuir?

¡Nos encantaría recibir contribuciones de la comunidad para hacer este repositorio aún mejor! Aquí están los pasos para contribuir:

1. **Fork del Repositorio**: Haz un fork de este repositorio a tu cuenta de GitHub.

2. **Clona tu Repositorio Forked**: Clona el repositorio desde tu cuenta de GitHub a tu máquina local.

   ```bash
   git clone https://github.com/jelambrar96/retos_programacion_python_barranquilla_2024.git
   ```

3. **Agrega el remote del repo original como upstream**: Con esto puedes fácilmente actualizar tu repositorio.

    ```bash
    git remote add upstream https://github.com/jelambrar96/retos_programacion_python_barranquilla_2024.git
    ```

4. **Crea una Rama (Branch)**: Crea una nueva rama para trabajar en tu contribución.

   ```bash
   git checkout -b usuariogithub_reto_XX
   ```

    Donde **usuariogithub** corresponde al usuario github que has creado y **XX** al número del reto que estás haciendo.


5. **Realiza tus Cambios**: Realiza los cambios necesarios en el código para resolver el reto o agregar nuevas funcionalidades. Usualmente tendrás que crear un archivo con tu nombre de ususario en github y extensión `.py` o un directorio con tu nombre de usuario donde desarrollarás la solución. En algunos ejercicios vas a tener un archivo o carpeta llamado `template` que te podrá ser de gran ayuda. 

6. **Agrega y Commitea tus Cambios**:
   ```bash
   git add .
   git commit -m "Descripción de tus cambios"
   ```

7. **Push a tu Repositorio en GitHub**:
   ```bash
   git push origin usuariogithub_reto_XX
   ```

8. **Envía un Pull Request (PR)**: Ve a tu repositorio en GitHub y haz clic en el botón "Compare & Pull Request" para enviar tu PR a este repositorio principal. Recomendamos que el título del Pull Request sea el mismo que el de la rama que has creado.  

9.  **Espera la Revisión**: Nuestro equipo revisará tu PR y te proporcionará retroalimentación si es necesario. Una vez que sea aprobado, ¡tu contribución se fusionará con el repositorio principal!


### ¿Cómo actualizar mi rama master?

Entra en tu rama master:
   ```bash
   git checkout master
   ```

Actualiza si hubo algún cambio
   ```bash
   git fetch upstream
   ```

Trae los cambios de la rama master en upstream a tu local.
   ```bash
   git pull upstream master
   ```
