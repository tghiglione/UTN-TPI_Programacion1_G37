import csv


""" Función auxiliar para validar que la lista de paises no esté vacía"""


def validar_lista_paises(paises, mensaje="No hay países cargados para mostrar."):
    if not paises:
        print(mensaje)
        return False
    return True


""" Función auxiliar para muestreo de listados"""


def mostrar_paises(lista_a_mostrar, mensaje="Listado de países:"):
    print(f"\n{mensaje}")
    print("-" * 69)

    # Encabezado con anchura fija
    print(
        "| {:<15}| {:<15}| {:<15}| {:<15}|".format(
            "Nombre", "Población", "Superficie", "Continente"
        )
    )
    print("-" * 69)

    # Mostrar cada país con las columnas alineadas
    for pais in lista_a_mostrar:
        print(
            "| {nombre:<15}| {poblacion:<15}| {superficie:<15}| {continente:<15}|".format(
                **pais
            )
        )
    print("-" * 69)


""" Lee un archivo CSV con información de países y devuelve una lista de diccionarios.
    Cada país tiene las claves: nombre, poblacion, superficie, continente y sus valores
    correspondientes segun el csv"""


def carga_datos_csv(ruta):

    paises = []  # lista donde se guardan todos los países

    try:
        with open(ruta, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    # Validar campos obligatorios
                    if (
                        not fila["nombre"]
                        or not fila["poblacion"]
                        or not fila["superficie"]
                        or not fila["continente"]
                    ):
                        print(f"Registro incompleto: {fila}")
                        continue

                    # Crear diccionario del país
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip(),
                    }

                    paises.append(pais)

                except ValueError:
                    print(f"Error en el manejo de archivo: {fila}")
                    continue

        print(f"Se cargaron {len(paises)} países correctamente.\n")
        return paises

    except FileNotFoundError:
        print("Error: El archivo no fue encontrado. Verifique la ruta y/o el nombre.")
        return []

    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return []


""" OPCION 1 - Realiza la busqueda por el nombre del pais """


def buscar_pais(paises):

    if not validar_lista_paises(paises):
        return
    nombre = input("Ingrese el nombre del país a buscar\n> ")
    pais_encontrado = []
    i = 0
    while (
        i < len(paises) and pais_encontrado == []
    ):  # Se uiliza ciclo while ya que sabemos que los paises no se pueden repetir y asi se evitan ciclos innecesarios
        if paises[i]["nombre"].lower() == nombre.lower():
            pais_encontrado.append(paises[i])
        i += 1

    if pais_encontrado != []:
        mostrar_paises(pais_encontrado, "Pais encontrado: \n")
    else:
        print("No se encuentra ese pais.")


""" OPCION 2 - Devuelve una lista de paises pertenecientes al continente indicado."""


def filtrar_por_continente(paises):
    if not validar_lista_paises(paises):
        return

    continentes = {
        "1": "America",
        "2": "Europa",
        "3": "Asia",
        "4": "Africa",
        "5": "Oceania",
        "6": "Antartida",
    }

    continente = ""
    while continente not in continentes:
        continente = input(
            "Seleccione un continente:\n"
            "1- América\n2- Europa\n3- Asia\n4- África\n5- Oceanía\n6- Antártida\n> "
        )

    continente = continentes[continente]

    paises_encontrados = []

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            paises_encontrados.append(pais)

    if len(paises_encontrados) != 0:
        mostrar_paises(paises_encontrados, f"Lista de paises de {continente}\n")
    else:
        print(f"El continente es invalido o no hay ningun pais para {continente}")


""" OPCIÓN 3 - Devuelve paises con poblacion o superficie dentro del rango."""


def filtrar_por_rango(paises):
    if not validar_lista_paises(paises):
        return

    print(
        "Elija el criterio a utilizar para filtrar\n"
        "1. Población.\n"
        "2. Superficie.\n"
    )
    campo_carga = input("Seleccione una opción\n> ")
    if campo_carga == "1":
        campo = "poblacion"
    elif campo_carga == "2":
        campo = "superficie"
    else:
        print("Ingreso inválido")
        return

    try:
        minimo_carga = input(f"Ingrese el límite inferior del rango de {campo}\n> ")
        maximo_carga = input(f"Ingrese el límite superior del rango de {campo}\n> ")
        minimo = int(minimo_carga)
        maximo = int(maximo_carga)
    except:
        print(
            "\nIngrese valores validos."
            f"\nIngresó un mínimo = {minimo_carga}"
            f"\nIngresó un máximo = {maximo_carga}"
            "\nUn ejemplo de ingreso correcto sería: \n- Mínimo = 505990 \n- Máximo = 45376763"
        )
        return

    if minimo < 0 or maximo < 0 or minimo >= maximo:
        print("Valores mínimos y máximos inválidos.")
        return

    paises_filtrados = []
    for pais in paises:
        if minimo < pais[campo] < maximo:
            paises_filtrados.append(pais)

    if len(paises_filtrados) != 0:
        mostrar_paises(
            paises_filtrados,
            f"Lista de paises que tienen una {campo} entre {minimo} y {maximo}",
        )
    else:
        print(
            f"No hay paises que tengan una {campo} entre {minimo} y {maximo} en nuestros registros."
        )

    return paises_filtrados


""" OPCION 4 - Devuelve los paises ordenados segun un criterio indicado """


def listar_paises(paises):

    if not validar_lista_paises(paises):
        return

    criterio = input(
        "Seleccione un criterio para ordenar la lista:"
        "\n1- Nombre"
        "\n2- Población"
        "\n3- Superficie"
        "\n4- Continente"
        "\n>"
    )
    # Validamos que el criterio sea correcto
    match criterio:
        case "1":
            criterio_valido = "nombre"
        case "2":
            criterio_valido = "poblacion"
        case "3":
            criterio_valido = "superficie"
        case "4":
            criterio_valido = "continente"
        case _:
            print("Criterio inválido.")
            return

    orden = input(
        "\nElija en que orden quiere ordenar la lista:"
        "\n1- Ascendente  (menor a mayor o A a la Z)"
        "\n2- Descendente (mayor a menor o Z a la A)"
        "\n>"
    )
    match orden:
        case "1":
            descendente = False
        case "2":
            descendente = True
        case _:
            print("Ingreso inválido.")
            return

    # Se ordena la lista usando sorted() y una función lambda
    paises_ordenados = sorted(
        paises, key=lambda item: item[criterio_valido], reverse=descendente
    )

    # Mostrar cada país
    mostrar_paises(
        paises_ordenados,
        f"\nListado de países ordenados por {criterio_valido} ({'descendente' if descendente else 'ascendente'}):\n",
    )


""" OPCION 5 - Simplemente para no tener que desarrollar el menu de la opcion 5 en el principal """


def estadisticas(paises):
    if not validar_lista_paises(paises):
        return

    print(
        "\n1. Obtener el pais con mayor y menor superficie o poblacion\n"
        "2. Promedio de población por continente\n"
        "3. Promedio de m2 de superficie por continente\n"
        "4. Cantidad de paises por continente\n"
        "5. Top 3 paises con mayor población\n"
    )
    opcion = input("Seleccione una opción\n> ")

    match opcion:
        case "1":
            campo = ""
            while campo != "1" and campo != "2":
                criterio = int(
                    input(
                        "\nSeleccione el criterio bajo el cual desea obtener el menor y mayor"
                        "\n1- Superficie"
                        "\n2- Población"
                        "\n>"
                    )
                )
                if criterio == "1":
                    campo = "superficie"
                elif criterio == "2":
                    campo = "poblacion"
                else:
                    print("\nSe ingreso un valor erroneo, volviendo al menú.")
            obtener_mayor_menor(paises, campo)
        case "2":
            promedio_poblacion_por_continente(paises)
        case "3":
            promedio_superficie_por_continente(paises)
        case "4":
            cantidad_paises_por_continente(paises)
        case "5":
            top_3_poblacion(paises)
        case "_":
            print("Ingreso una opción invalida. Volviendo al menú")
            return


""" OPCION 5.1 - Devuelve los paises con el valor maximo y minimo de un campo."""


def obtener_mayor_menor(paises, campo):
    paises_min_max = []
    pais_max, pais_min = paises[0], paises[0]

    validar_lista_paises(paises)
    for pais in paises:
        if pais[campo] > pais_max[campo]:
            pais_max = pais
        if pais[campo] < pais_min[campo]:
            pais_min = pais

    paises_min_max.append(pais_max)
    paises_min_max.append(pais_min)

    mostrar_paises(paises_min_max, f"Paises con mayor y menor {campo}")


""" OPCION 5.2 - Calcula el promedio de poblacion agrupado por continente."""


def promedio_poblacion_por_continente(paises):

    suma_poblacion_por_continente = {}
    conteo_pais_por_continente = {}

    for pais in paises:
        continente = pais["continente"]
        poblacion = pais["poblacion"]

        if continente not in suma_poblacion_por_continente:
            suma_poblacion_por_continente[continente] = poblacion
            conteo_pais_por_continente[continente] = 1
        else:
            suma_poblacion_por_continente[continente] += int(poblacion)
            conteo_pais_por_continente[continente] += 1

    for continente in suma_poblacion_por_continente:
        promedio = suma_poblacion_por_continente[
            continente
        ] / conteo_pais_por_continente.get(continente)
        print(f"Promedio {continente}: {promedio}")


""" OPCION 5.3 - Promedio de superficies por continente."""


def promedio_superficie_por_continente(paises):
    # Como solo son 6 continentes los puedo inicialziar acá
    CONTINENTES_BASE = {
        "America": 0,
        "Europa": 0,
        "Asia": 0,
        "Africa": 0,
        "Oceania": 0,
        "Antartida": 0,
    }

    # Inicialización de diccionarios usando el diccionario de continentes
    suma_superficie_por_continente = CONTINENTES_BASE.copy()
    conteo_pais_por_continente = CONTINENTES_BASE.copy()

    # Primera pasada: Acumular datos
    for pais in paises:
        continente = pais["continente"]
        superficie = pais["superficie"]

        suma_superficie_por_continente[continente] += superficie
        conteo_pais_por_continente[continente] += 1

    print("\n--- PROMEDIO DE SUPERFICIE POR CONTINENTE ---\n")

    # Segunda pasada: Calcular y mostrar promedios
    for continente in suma_superficie_por_continente:
        suma = suma_superficie_por_continente[continente]
        conteo = conteo_pais_por_continente[continente]

        if conteo > 0:
            promedio = suma / conteo
            # Uso de separador de miles con :,.2f
            print(f"Promedio de superficie para {continente}: {promedio} km²")
        else:
            # Maneja el caso donde el continente fue inicializado pero no tiene países cargados
            print(
                f"Promedio de superficie para {continente}: 0.00 km² (Sin países cargados o cargados con superficie igual a 0)"
            )


""" OPCION 5.4 - Cuenta cuántos paises hay en cada continente."""


def cantidad_paises_por_continente(paises):

    conteo_pais_por_continente = {}

    for pais in paises:
        continente = pais["continente"]

        if continente not in conteo_pais_por_continente:
            conteo_pais_por_continente[continente] = 1
        else:
            conteo_pais_por_continente[continente] += 1

    for continente in conteo_pais_por_continente:
        print(
            f"Cantidad de paises en {continente}: {conteo_pais_por_continente[continente]}"
        )


""" OPCION 5.5 - Muestra los tres paises con mayor poblacion."""


def top_3_poblacion(paises):

    paises_ordenados = sorted(paises, key=lambda item: item["poblacion"], reverse=True)
    top_3 = paises_ordenados[:3]
    mostrar_paises(top_3, "\nTop 3 paises mas poblados:\n")
