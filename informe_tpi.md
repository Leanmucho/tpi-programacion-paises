# Trabajo Práctico Integrador

## Carátula

Institución: Tecnicatura Universitaria en Programación a Distancia  
Carrera: Tecnicatura Universitaria en Programación  
Materia: Programación 1  
Título: Gestión de Datos de Países en Python  
Integrantes: Acuña Leandro - Alan Benítez  

## Índice

1. Carátula ........................................................................ 1  
2. Índice .......................................................................... 1  
3. Objetivo ........................................................................ 2  
4. Marco teórico ................................................................... 2  
5. Decisiones técnicas y arquitectura .............................................. 3  
6. Diagrama de flujo ............................................................... 3  
7. Capturas de ejecución ........................................................... 4-5  
8. Dificultades y conclusiones ..................................................... 6  
9. Bibliografía y enlaces .......................................................... 6

## Objetivo

Desarrollar una aplicación de consola en Python que permita gestionar información de países usando listas, diccionarios, funciones, estructuras condicionales y repetitivas, lectura y escritura de archivos CSV, filtros, ordenamientos y estadísticas básicas.

El sistema trabaja con un dataset base de 20 países. Cada registro contiene nombre, población, superficie y continente. Además, las operaciones de alta y actualización guardan los cambios en el archivo `paises.csv`, por lo que la información se conserva después de finalizar la ejecución.

## Marco teórico

### Listas

Una lista es una estructura de datos que permite almacenar varios elementos en un orden determinado. En Python, las listas son mutables y pueden recorrerse mediante ciclos, lo que permite procesar colecciones completas de datos [1]. En el proyecto se utiliza una lista para guardar todos los países cargados desde el archivo CSV.

### Diccionarios

Un diccionario almacena información mediante pares clave-valor. Esta estructura permite acceder a cada dato por una clave descriptiva, como `nombre`, `poblacion`, `superficie` o `continente` [1]. En el sistema, cada país es representado como un diccionario.

### Funciones

Las funciones permiten dividir el programa en unidades más pequeñas y reutilizables. La documentación oficial de Python presenta las funciones como bloques con nombre que reciben datos, ejecutan instrucciones y pueden devolver resultados [1]. En el proyecto se aplicó una función por responsabilidad: cargar datos, guardar datos, buscar, filtrar, ordenar y calcular estadísticas.

### Condicionales y ciclos

Las estructuras condicionales permiten tomar decisiones según una opción o una validación. Los ciclos permiten repetir operaciones, por ejemplo recorrer todos los países o mantener activo el menú hasta que el usuario decida salir [1].

### Ordenamientos

Python ofrece herramientas para ordenar colecciones, como `sorted`, que permite definir una clave de ordenamiento y elegir orden ascendente o descendente [1]. En el sistema se usa para ordenar países por nombre, población o superficie.

### Estadísticas básicas

Las estadísticas básicas permiten obtener información resumida del dataset. En este trabajo se calculan máximos, mínimos, promedios y conteos por continente usando recorridos, acumuladores y funciones incorporadas de Python [1].

### Archivos CSV

CSV significa "comma-separated values" y es un formato de texto usado para representar datos tabulares. Python incluye el módulo `csv`, que facilita leer y escribir archivos con encabezados y filas [2]. En el proyecto, `paises.csv` funciona como fuente de datos inicial y como almacenamiento persistente.

## Decisiones técnicas y arquitectura

El sistema se implementa en un único archivo `main.py` para mantener una estructura simple, adecuada al alcance de Programación 1. La información se administra en memoria como una lista de diccionarios y se sincroniza con `paises.csv` cuando el usuario agrega o actualiza un país.

Las decisiones principales fueron:

- Usar `csv.DictReader` y `csv.DictWriter` para leer y escribir registros con encabezados.
- Validar campos vacíos y números inválidos antes de modificar los datos.
- Separar la lógica en funciones con responsabilidades específicas.
- Normalizar búsquedas y filtros para aceptar texto con o sin tildes.
- Guardar automáticamente el CSV después de cada alta o actualización.

## Diagrama de flujo

El siguiente diagrama resume el flujo principal del programa:

![Diagrama de flujo](assets/diagrama_flujo.png)

## Capturas de ejecución

### Ejemplo 1: cálculo de estadísticas

![Captura de estadísticas](assets/captura_estadisticas.png)

### Ejemplo 2: búsqueda por nombre y filtro por continente

![Captura de búsqueda y filtro](assets/captura_busqueda_filtro.png)

## Dificultades y conclusiones

Una de las principales dificultades fue controlar correctamente las entradas del usuario para evitar campos vacíos, números inválidos o búsquedas sin resultados. Para resolverlo, se crearon funciones de validación reutilizables.

Otra dificultad fue mantener los datos actualizados en el CSV. Se resolvió guardando el archivo después de cada operación que modifica información, como agregar o actualizar un país.

Como conclusión, el proyecto permitió practicar estructuras de datos, modularización, lectura y escritura de archivos, filtros, ordenamientos y cálculo de estadísticas. También ayudó a comprender la importancia de separar responsabilidades y validar datos antes de procesarlos.

## Bibliografía y enlaces

[1] Python Software Foundation. Documentación oficial de Python: https://docs.python.org/3/  
[2] Python Software Foundation. Módulo csv: https://docs.python.org/3/library/csv.html  
[3] Repositorio del proyecto: https://github.com/Leanmucho/tpi-programacion-paises
