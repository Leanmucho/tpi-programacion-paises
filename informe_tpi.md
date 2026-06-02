# Trabajo Practico Integrador

## Caratula

Institucion: Tecnicatura Universitaria en Programacion a Distancia  
Materia: Programacion 1  
Titulo: Gestion de Datos de Paises en Python  
Integrantes: Acuña Leandro - Alan Benitez  
Fecha de entrega: 2 de junio de 2026

## Indice

1. Objetivo
2. Marco teorico
3. Decisiones tecnicas y arquitectura
4. Flujo del programa
5. Dificultades y conclusiones
6. Bibliografia

## Objetivo

Desarrollar una aplicacion de consola en Python que permita gestionar informacion de paises usando listas, diccionarios, funciones, estructuras condicionales y repetitivas, lectura y escritura de archivos CSV, filtros, ordenamientos y estadisticas basicas.

## Marco teorico

### Listas

Una lista es una estructura de datos que permite almacenar varios elementos en un orden determinado. En el proyecto se utiliza una lista para guardar todos los paises cargados desde el archivo CSV.

### Diccionarios

Un diccionario almacena datos mediante pares clave-valor. En el sistema, cada pais es representado con un diccionario que contiene `nombre`, `poblacion`, `superficie` y `continente`.

### Funciones

Las funciones permiten dividir el programa en partes mas pequenas y reutilizables. Cada funcion del sistema tiene una responsabilidad concreta, por ejemplo cargar datos, guardar datos, buscar, filtrar u ordenar.

### Condicionales

Las estructuras condicionales permiten tomar decisiones segun la opcion elegida por el usuario o segun el resultado de una validacion.

### Ordenamientos

El programa utiliza ordenamientos para mostrar los paises por nombre, poblacion o superficie, tanto en forma ascendente como descendente.

### Estadisticas basicas

Se calculan indicadores como mayor y menor poblacion, promedio de poblacion, promedio de superficie y cantidad de paises por continente.

### Archivos CSV

El formato CSV permite guardar datos tabulares en texto plano. El programa lee los paises desde `paises.csv` y guarda ahi las modificaciones realizadas.

## Decisiones tecnicas y arquitectura

El sistema se implementa en un unico archivo `main.py` para facilitar la entrega y correccion. La informacion se administra en memoria como una lista de diccionarios y se sincroniza con el archivo CSV cada vez que se agrega o actualiza un pais.

## Flujo del programa

```text
Inicio
  |
  v
Cargar paises desde CSV
  |
  v
Mostrar menu principal
  |
  v
Usuario elige opcion
  |
  +--> Listar paises
  +--> Agregar pais y guardar CSV
  +--> Actualizar pais y guardar CSV
  +--> Buscar pais
  +--> Filtrar paises
  +--> Ordenar paises
  +--> Mostrar estadisticas
  +--> Salir
```

## Dificultades y conclusiones

Una dificultad esperada es validar correctamente los datos ingresados por el usuario y evitar errores cuando el CSV tenga datos invalidos. Se resolvio separando la lectura, la validacion y el guardado en funciones distintas.

Como conclusion, el proyecto permite practicar estructuras de datos, modularizacion y persistencia de informacion en archivos.

## Bibliografia

- Documentacion oficial de Python: https://docs.python.org/3/
- Modulo CSV de Python: https://docs.python.org/3/library/csv.html
