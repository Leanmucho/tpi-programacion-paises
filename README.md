# Gestión de Datos de Países en Python

Trabajo Práctico Integrador de Programación 1.

## Integrantes

- Acuña Leandro
- Alan Benítez

## Descripción

Aplicación de consola desarrollada en Python 3 para gestionar información de países desde un archivo CSV. El programa permite cargar datos, agregar nuevos países, actualizar población y superficie, buscar, filtrar, ordenar y calcular estadísticas básicas.

Cada país se guarda como un diccionario con estos campos:

- `nombre`
- `poblacion`
- `superficie`
- `continente`

Todos los países se almacenan en una lista y se leen/escriben desde `paises.csv`.

## Archivos principales

- `main.py`: código fuente del programa.
- `paises.csv`: dataset base con 20 países.
- `informe_tpi.md`: versión editable del informe académico.
- `informe_tpi.pdf`: informe académico en formato PDF.
- `assets/`: diagrama de flujo y capturas de ejecución utilizadas en el informe.

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

## Opciones del menú

1. Listar países
2. Agregar país
3. Actualizar población y superficie
4. Buscar país por nombre
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
0. Salir

## Ejemplos de uso

Buscar por nombre:

```text
Nombre o parte del nombre: ar
Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
```

Filtrar por continente:

```text
Continente: Europa
Alemania ...
Francia ...
España ...
Italia ...
Reino Unido ...
```

Mostrar estadísticas:

```text
País con mayor población
País con menor población
Promedio de población
Promedio de superficie
Cantidad de países por continente
```

## Persistencia de datos

Las altas y actualizaciones se guardan automáticamente en `paises.csv`, por lo que los cambios se conservan después de cerrar el programa.

## Documentación PDF

El archivo `informe_tpi.pdf` está incluido en la raíz del proyecto.
