
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
    print("-" * 65)

    # Encabezado con anchura fija
    print(f"|{'Nombre':<15}|{'Población':<15}|{'Superficie':<15}|{'Continente':<15}|")
    print("-" * 65)

    # Mostrar cada país con las columnas alineadas
    for pais in lista_a_mostrar:
        print(f"|{pais['nombre']:<15}|{pais['poblacion']:<15}|{pais['superficie']:<15}|{pais['continente']:<15}|")
    print("-" * 65)



""" Lee un archivo CSV con información de países y devuelve una lista de diccionarios.
    Cada país tiene las claves: nombre, poblacion, superficie, continente y sus valores
    correspondientes segun el csv"""
def carga_datos_csv(ruta):

    paises = []  # lista donde se guardan todos los países

    try:
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    # Validar campos obligatorios
                    if not fila["nombre"] or not fila["poblacion"] or not fila["superficie"] or not fila["continente"]:
                        print(f"Registro incompleto: {fila}")
                        continue

                    # Crear diccionario del país
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
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


""" Devuelve los paises ordenados segun un criterio indicado """
def listar_paises(paises, criterio, descendente=False):

    if not validar_lista_paises(paises):
        return

    # Validamos que el criterio sea correcto
    match criterio:
        case 1:
            criterio_valido = "nombre"
        case 2:
            criterio_valido = "poblacion"
        case 3:
            criterio_valido = "superficie"
        case 4:
            criterio_valido = "continente"
        case _:
            print(f"Criterio inválido.")
            return

    # Se ordena la lista usando sorted() y una función lambda
    paises_ordenados = sorted(paises, key=lambda item: item[criterio_valido], reverse=descendente)

    # Mostrar cada país
    mostrar_paises(paises_ordenados, f"\nListado de países ordenados por {criterio_valido} ({'descendente' if descendente else 'ascendente'}):\n")


""" Realiza la busqueda por el nombre del pais """
def buscar_pais(paises, nombre):
    if not validar_lista_paises(paises):
            return
    pais_encontrado = []
    i=0
    while i < len(paises) and pais_encontrado == []:    # Se uiliza ciclo while ya que sabemos que los paises no se pueden repetir y asi se evitan ciclos innecesarios
        if paises[i]['nombre'].lower() == nombre.lower():
            pais_encontrado.append(paises[i])
        i += 1

    if pais_encontrado != []:
        mostrar_paises(pais_encontrado, "Pais encontrado: \n")
    else:
        print("No se encuentra ese pais.")


"""Devuelve una lista de paises pertenecientes al continente indicado."""
def filtrar_por_continente(paises, continente):
    if not validar_lista_paises(paises):
        return

    paises_encontrados = []

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            paises_encontrados.append(pais)

    if len(paises_encontrados) != 0:
        mostrar_paises(paises_encontrados, f"Lista de paises de {continente}\n")
    else:
        print(f"El continente es invalido o no hay ningun pais para {continente}")


"""Devuelve paises con poblacion o superficie dentro del rango."""
def filtrar_por_rango(paises, campo, minimo, maximo):


    if not validar_lista_paises(paises):
        return

    # Valido los parametros, campos no lo valido porque estaría bueno que se elija desde el menú, para evitar errores de tipeo y ahorrar tiempo al usuario escribiendo y a nosotros validando.
    if (minimo >= maximo) or minimo < 0 or maximo < 0:
        print(f'Valores Mínimos y Máximos invalidos.')
        return

    # Creo lista vacía para completar con los potenciales paises encontrados.
    paises_filtrados = []
    for pais in paises:
        if (minimo < pais[campo] < maximo):
            paises_filtrados.append(pais)

    if len(paises_filtrados) != 0:
        mostrar_paises(paises_filtrados, f"Lista de paises que tienen una {campo} entre {minimo} y {maximo}")

    else:
        print(f"No hay paises que tengan una {campo} entre {minimo} y {maximo} en nuestros registros.")

    # Retorno la lista por si alguna ves es necesario usarla...
    return(paises_filtrados)


"""Devuelve los paises con el valor maximo y minimo de un campo."""
def obtener_mayor_menor(paises, campo):
    # Variables auxiliares
    paises_min_max = []
    pais_max, pais_min = paises[0], paises[0]

    # Valido lista de paises
    validar_lista_paises(paises)
    # Si esta OK la proceso
    for pais in paises:
        # Guardo los max y min
        if pais[campo] > pais_max[campo]:
            pais_max = pais
        if pais[campo] < pais_min[campo]:
            pais_min = pais

    # Para poder mostrarla creo una lista de diccionarios
    paises_min_max.append(pais_max)
    paises_min_max.append(pais_min)

    # Muestro la lista final en forma tabular
    mostrar_paises(paises_min_max, f"Paises con mayor y menor {campo}")

"""Calcula el promedio de poblacion agrupado por continente."""
def promedio_poblacion_por_continente(paises):

    if not validar_lista_paises(paises):
        return

    suma_poblacion_por_continente = {}
    conteo_pais_por_continente = {}

    for pais in paises:
        continente = pais['continente']         #por cada pais tomo el continente y su poblacion
        poblacion = pais['poblacion']

        if continente not in suma_poblacion_por_continente:
            suma_poblacion_por_continente[continente] = poblacion       # armo dos diccionarios con el conteo de paises por continente y tambien sumando la poblacion por continente
            conteo_pais_por_continente[continente] = 1
        else:
            suma_poblacion_por_continente[continente] += int(poblacion)
            conteo_pais_por_continente[continente] += 1

    for continente in suma_poblacion_por_continente:
        promedio = suma_poblacion_por_continente[continente] / conteo_pais_por_continente.get(continente)       #calculo e imprimo el promedio de poblacion de cada continente
        print(f"Promedio {continente}: {promedio}")        


"""Cuenta cuántos paises hay en cada continente."""
def cantidad_paises_por_continente(paises):
    if not validar_lista_paises(paises):
        return

    conteo_pais_por_continente = {}

    for pais in paises:
        continente = pais['continente']

        if continente not in conteo_pais_por_continente:    #armo diccionario con el conteo de paises por continente
            conteo_pais_por_continente[continente] = 1
        else:
            conteo_pais_por_continente[continente] += 1

    for continente in conteo_pais_por_continente:
        print(f"Cantidad de paises en {continente}: {conteo_pais_por_continente[continente]}")  #imprimo el conteo de paises por continente


"""Muestra los tres paises con mayor poblacion."""
def top_3_poblacion(paises):

    if not validar_lista_paises(paises):
        return

    # Se ordena la lista usando sorted() y una función lambda
    paises_ordenados = sorted(paises, key=lambda item: item['poblacion'], reverse=True)

    #solo tomo los 3 primeros
    top_3 = paises_ordenados[:3]

    # Mostrar cada país
    mostrar_paises(top_3, f"\nTop 3 paises mas poblados:\n")


"""Menu de opciones"""
def menu_principal(paises):
    pass
