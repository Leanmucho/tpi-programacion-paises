import csv
import unicodedata
from pathlib import Path


CSV_PATH = Path("paises.csv")
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises(ruta_csv=CSV_PATH):
    paises = []

    try:
        with ruta_csv.open("r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames != CAMPOS:
                print("Error: el CSV no tiene el formato esperado.")
                return []

            for numero_fila, fila in enumerate(lector, start=2):
                try:
                    paises.append(
                        {
                            "nombre": validar_texto_csv(fila["nombre"]),
                            "poblacion": int(fila["poblacion"]),
                            "superficie": int(fila["superficie"]),
                            "continente": validar_texto_csv(fila["continente"]),
                        }
                    )
                except (TypeError, ValueError):
                    print(f"Error de formato en la fila {numero_fila}. Se omite.")
    except FileNotFoundError:
        print("No se encontro paises.csv. Se iniciara con una lista vacia.")

    return paises


def guardar_paises(paises, ruta_csv=CSV_PATH):
    with ruta_csv.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(paises)


def validar_texto_csv(valor):
    texto = str(valor).strip()
    if not texto:
        raise ValueError("Campo vacio")
    return texto


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("El campo no puede estar vacio.")


def pedir_entero(mensaje, minimo=0):
    while True:
        valor = input(mensaje).strip()

        try:
            numero = int(valor)
            if numero >= minimo:
                return numero
            print(f"Debe ingresar un numero mayor o igual a {minimo}.")
        except ValueError:
            print("Debe ingresar un numero entero valido.")


def pedir_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion in opciones_validas:
            return opcion
        print("Opcion invalida. Intente nuevamente.")


def normalizar(texto):
    texto_limpio = texto.strip().lower()
    texto_sin_tildes = unicodedata.normalize("NFD", texto_limpio)
    return "".join(
        caracter for caracter in texto_sin_tildes
        if unicodedata.category(caracter) != "Mn"
    )


def mostrar_pais(pais):
    print(
        f"{pais['nombre']:<25} | "
        f"Poblacion: {pais['poblacion']:>12} | "
        f"Superficie: {pais['superficie']:>10} km2 | "
        f"Continente: {pais['continente']}"
    )


def mostrar_paises(paises):
    if not paises:
        print("No hay paises para mostrar.")
        return

    for pais in paises:
        mostrar_pais(pais)


def agregar_pais(paises):
    print("\nAgregar pais")
    nombre = pedir_texto("Nombre: ")

    if buscar_exacta(paises, nombre) is not None:
        print("Ya existe un pais con ese nombre.")
        return

    poblacion = pedir_entero("Poblacion: ", minimo=1)
    superficie = pedir_entero("Superficie en km2: ", minimo=1)
    continente = pedir_texto("Continente: ")

    paises.append(
        {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente,
        }
    )
    guardar_paises(paises)
    print("Pais agregado y guardado en el CSV.")


def buscar_exacta(paises, nombre):
    nombre_buscado = normalizar(nombre)
    for indice, pais in enumerate(paises):
        if normalizar(pais["nombre"]) == nombre_buscado:
            return indice
    return None


def actualizar_pais(paises):
    print("\nActualizar pais")
    nombre = pedir_texto("Ingrese el nombre exacto del pais: ")
    indice = buscar_exacta(paises, nombre)

    if indice is None:
        print("No se encontro un pais con ese nombre.")
        return

    mostrar_pais(paises[indice])
    paises[indice]["poblacion"] = pedir_entero("Nueva poblacion: ", minimo=1)
    paises[indice]["superficie"] = pedir_entero("Nueva superficie en km2: ", minimo=1)
    guardar_paises(paises)
    print("Datos actualizados y guardados en el CSV.")


def buscar_por_nombre(paises):
    print("\nBuscar pais")
    busqueda = normalizar(pedir_texto("Nombre o parte del nombre: "))
    resultados = [
        pais for pais in paises if busqueda in normalizar(pais["nombre"])
    ]

    if resultados:
        mostrar_paises(resultados)
    else:
        print("No se encontraron paises con esa busqueda.")


def filtrar_por_continente(paises):
    continente = normalizar(pedir_texto("Continente: "))
    resultados = [
        pais for pais in paises if normalizar(pais["continente"]) == continente
    ]
    mostrar_resultados_filtro(resultados)


def filtrar_por_rango(paises, campo):
    minimo = pedir_entero(f"{campo.capitalize()} minima: ", minimo=0)
    maximo = pedir_entero(f"{campo.capitalize()} maxima: ", minimo=minimo)
    resultados = [pais for pais in paises if minimo <= pais[campo] <= maximo]
    mostrar_resultados_filtro(resultados)


def mostrar_resultados_filtro(resultados):
    if resultados:
        mostrar_paises(resultados)
    else:
        print("No hay paises que cumplan con ese filtro.")


def menu_filtros(paises):
    print("\nFiltros")
    print("1. Por continente")
    print("2. Por rango de poblacion")
    print("3. Por rango de superficie")
    opcion = pedir_opcion("Seleccione una opcion: ", {"1", "2", "3"})

    if opcion == "1":
        filtrar_por_continente(paises)
    elif opcion == "2":
        filtrar_por_rango(paises, "poblacion")
    else:
        filtrar_por_rango(paises, "superficie")


def ordenar_paises(paises):
    print("\nOrdenamientos")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")
    campo_opcion = pedir_opcion("Seleccione el campo: ", {"1", "2", "3"})

    print("1. Ascendente")
    print("2. Descendente")
    orden_opcion = pedir_opcion("Seleccione el orden: ", {"1", "2"})

    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    campo = campos[campo_opcion]
    descendente = orden_opcion == "2"

    paises_ordenados = sorted(
        paises,
        key=lambda pais: normalizar(pais[campo]) if campo == "nombre" else pais[campo],
        reverse=descendente,
    )
    mostrar_paises(paises_ordenados)


def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos para calcular estadisticas.")
        return

    pais_mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])
    promedio_poblacion = sum(pais["poblacion"] for pais in paises) / len(paises)
    promedio_superficie = sum(pais["superficie"] for pais in paises) / len(paises)
    cantidad_por_continente = {}

    for pais in paises:
        continente = pais["continente"]
        cantidad_por_continente[continente] = cantidad_por_continente.get(continente, 0) + 1

    print("\nEstadisticas")
    print("Pais con mayor poblacion:")
    mostrar_pais(pais_mayor_poblacion)
    print("Pais con menor poblacion:")
    mostrar_pais(pais_menor_poblacion)
    print(f"Promedio de poblacion: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km2")
    print("Cantidad de paises por continente:")

    for continente, cantidad in sorted(cantidad_por_continente.items()):
        print(f"- {continente}: {cantidad}")


def mostrar_menu():
    print("\nGestion de Datos de Paises")
    print("1. Listar paises")
    print("2. Agregar pais")
    print("3. Actualizar poblacion y superficie")
    print("4. Buscar pais por nombre")
    print("5. Filtrar paises")
    print("6. Ordenar paises")
    print("7. Mostrar estadisticas")
    print("0. Salir")


def ejecutar_programa():
    paises = cargar_paises()

    while True:
        mostrar_menu()
        opcion = pedir_opcion("Seleccione una opcion: ", {"0", "1", "2", "3", "4", "5", "6", "7"})

        if opcion == "0":
            print("Programa finalizado.")
            break
        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_por_nombre(paises)
        elif opcion == "5":
            menu_filtros(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)


if __name__ == "__main__":
    ejecutar_programa()
