# **Explorador de Países: Lectura CSV, Búsquedas y Estadísticas**

### **Trabajo Integrador – Programación I**
_Tecnicatura Universitaria en Programación a Distancia – UTN_

### **Docentes**
- **Coordinador:** Alberto Cortez
- **Profesora:** Cinthia Rigoni
- **Profesor:** Ariel Enferrel
- **Profesores Comisión 10 y 5:** Matías Torres y Martina Zabala

### 👥 **Integrantes**
- **Tomás Ghiglione** (Comisión 5)
- **Gabriel Ezequiel Nieva** (Comisión 10)

## **Descripción del proyecto**

Este proyecto integrador consiste en una aplicación desarrollada en Python que permite gestionar y analizar información sobre países a partir de un archivo CSV.
El sistema implementa funciones de lectura de archivos, filtrado, búsqueda, ordenamiento y estadísticas, aplicando los conceptos fundamentales de listas, diccionarios, estructuras condicionales, bucles y modularización.
El usuario puede consultar países, realizar filtrados por rango de valores, ordenar datos y obtener indicadores como promedios, cantidades y el top 3 de países más poblados, entre otras.

## **Estructura del programa**

El programa se encuentra contenido en una carpeta general. Dentro estan los siguientes archivos:
- funciones.py: Contiene todas las funciones lógicas del programa como lectura de datos en csv, cálculo de estadísticas y búsqueda, filtrado y ordenamiento de países
- main.py: Archivo principal que ejecuta el programa. Presenta un menú interactivo que permite acceder a las distintas funcionalidades implementadas.
- paises.csv: Archivo de datos con la información de los países


## **Instrucciones de ejecución**

1) _Clonar o descargar el proyecto_: Descargá todos los archivos (main.py, funciones.py y paises.csv) en una misma carpeta de tu computadora.
2) _Verificar que Python esté instalado_: Utiliza en terminal el comando python --version
3) _Abrir la terminal en la carpeta del proyecto y ejecuta el programa principal_: Una vez ubicado en la carpeta del proyecto en terminal (por ejemplo C:\Users\TuUsuario\Proyecto_Paises) lanza el comando 'python main.py' para ejecutar el programa
4) _Interacción con el menú_: Una vez iniciado, el programa mostrará un menú interactivo. Ingresá el número correspondiente a la acción que querés realizar y seguí las instrucciones en pantalla.

## **Ejemplos de entradas y salidas**

1) _Menu principal:_
Se despliega un menu principal y se elige del 1 al 5 la accion que se desea realizar. Con la opcion 6 se finaliza la ejecucion del programa
2) _Opcion 1. Buscar país por nombre_:
Al seleccionar esta opcion se le pide al usuario el nombre del pais. Si existe en el archivo, devuelve los datos del mismo.
3) _Opcion 2. Filtrar por continente_:
Se muestra una lista con los continentes (opciones del 1 al 6). Al seleccionar el continente se muestra en forma de lista la informacion de los paises de dicho continente
4) _Opcion 3. Filtrar por rango_:
Se muestran las opciones por poblacion o superficie. Al escoger una, se le pide al usuario el minimo y el maximo del rango a buscar y se mostrara en consola un listado de los paises que cumplan dicho rango.
5) _Opcion 4. Ordenar paises_:
Se desplegara un nuevo menu con opciones del 1 al 4 con distintos criterios de ordenamiento (nombre, poblacion, superficie, continente). Al seleccionar la opcion se muestra el listado completo ordenado segun el criterio
6) _Opcion 5. Estadisticas_:
Se despliega el siguiente menu de opciones para mostrar la estadistica necesaria:
    1. Obtener el pais con mayor y menor superficie o poblacion
    2. Promedio de población por continente
    3. Promedio de km2 de superficie por continente
    4. Cantidad de paises por continente
    5. Top 3 paises con mayor población
7) _Opción 6. Agregar Pais_:
Se realiza una modificacion real tanto de la lista en memoria como del archivo CSV. Basicamente se le solicita al usuario que ingrese los datos de un pais (nombre, poblacion, superficie, continente), se los valida, se verifica que esté todo bien con la lista, y se los guarda tanto en la lista en memoria como en el archivo CSV. También al final muestra la lista de paises actualizados
8) _Opción 7. Modificar Pais_:
Solicita al usuario un nombre de un pais para modificarle superficie y/o poblacion, si no está muestra error y sale, si está en la lista, valida los datos ingresados y modifica el pais, tanto en lista en memoria como en el archivo CSV. Muestra en pantalla como quedó el pais con sus datos modificados

## **Bibliografia**

Lectura de archivos CSV:
https://docs.python.org/es/3.9/library/csv.html

Importacion de modulos:
https://docs.python.org/es/3.13/reference/import.html

Uso de diccionario en python:
https://ellibrodepython.com/diccionarios-en-python

Ordenamiento de diccionario:
https://www.datacamp.com/es/tutorial/sort-a-dictionary-by-value-python

Funciones lambda:
https://www.datacamp.com/es/tutorial/python-lambda-functions
