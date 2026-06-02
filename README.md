# Gestion de Datos de Paises en Python

Trabajo Practico Integrador de Programacion 1.

## Integrantes

- Acuña Leandro
- Alan Benitez

## Descripcion

Aplicacion de consola desarrollada en Python 3 para gestionar informacion de paises desde un archivo CSV. El programa permite cargar datos, agregar nuevos paises, actualizar poblacion y superficie, buscar, filtrar, ordenar y calcular estadisticas basicas.

Cada pais se guarda como un diccionario con estos campos:

- `nombre`
- `poblacion`
- `superficie`
- `continente`

Todos los paises se almacenan en una lista y se leen/escriben desde `paises.csv`.

## Archivos principales

- `main.py`: codigo fuente del programa.
- `paises.csv`: dataset base con 20 paises.
- `informe_tpi.md`: version editable del informe academico.
- `informe_tpi.pdf`: informe academico en formato PDF.
- `Consigna_TPI_Prog-1.docx.pdf`: consigna original del trabajo.

## Como ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

## Opciones del menu

1. Listar paises
2. Agregar pais
3. Actualizar poblacion y superficie
4. Buscar pais por nombre
5. Filtrar paises
6. Ordenar paises
7. Mostrar estadisticas
0. Salir

## Ejemplos de uso

Buscar por nombre:

```text
Nombre o parte del nombre: ar
Argentina | Poblacion: 45376763 | Superficie: 2780400 km2 | Continente: América
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

Mostrar estadisticas:

```text
Pais con mayor poblacion
Pais con menor poblacion
Promedio de poblacion
Promedio de superficie
Cantidad de paises por continente
```

## Persistencia de datos

Las altas y actualizaciones se guardan automaticamente en `paises.csv`, por lo que los cambios se conservan despues de cerrar el programa.

## Video demostrativo

Pendiente: agregar link publico del video de 10 a 15 minutos.

## Documentacion PDF

El archivo `informe_tpi.pdf` esta incluido en la raiz del proyecto.
