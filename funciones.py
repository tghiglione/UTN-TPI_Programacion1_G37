
import csv

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

    if not paises:
        print("No hay países cargados para mostrar.")
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

    # Encabezado
    print(f"\nListado de países ordenados por {criterio_valido} ({'descendente' if descendente else 'ascendente'}):\n")
    print("Nombre", "Población", "Superficie", "Continente","\n")

    # Mostrar cada país
    for pais in paises_ordenados:
        print(pais["nombre"], pais["poblacion"], pais["superficie"], pais["continente"])

""" Realiza la busqueda por el nombre del pais """

def buscar_pais(paises, nombre):
        if not paises:
            print("No hay países cargados para mostrar.")
            return
        pais_encontrado = ""
        i=0
        while i < len(paises) and pais_encontrado == "":    # Se uiliza ciclo while ya que sabemos que los paises no se pueden repetir y asi se evitan ciclos innecesarios
            if paises[i]['nombre'].lower() == nombre.lower():
                pais_encontrado = paises[i]
            i += 1
        
        if pais_encontrado != "":
            print("Pais encontrado: \n")
            print(pais_encontrado["nombre"], pais_encontrado["poblacion"], pais_encontrado["superficie"], pais_encontrado["continente"])
        else:
            print("No se encuentra ese pais.")

"""Devuelve una lista de paises pertenecientes al continente indicado."""

def filtrar_por_continente(paises, continente):
    if not paises:
        print("No hay países cargados para mostrar.")
        return
    
    paises_encontrados = []

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            paises_encontrados.append(pais)
    
    if len(paises_encontrados) != 0:
        print(f"Lista de paises de {continente}\n")
        for pais_filtrado in paises_encontrados:
            print(pais_filtrado["nombre"], pais_filtrado["poblacion"], pais_filtrado["superficie"], pais_filtrado["continente"])
    else:
        print(f"El continente es invalido o no hay ningun pais para {continente}")

def filtrar_por_rango(paises, campo, minimo, maximo):
    """Devuelve paises con poblacion o superficie dentro del rango."""
    pass

def obtener_mayor_menor(paises, campo):
    """Devuelve los paises con el valor maximo y minimo de un campo."""

def promedio_poblacion_por_continente(paises):
    """Calcula el promedio de poblacion agrupado por continente."""

def cantidad_paises_por_continente(paises):
    """Cuenta cuántos paises hay en cada continente."""

def top_3_poblacion(paises):
    """Muestra los tres paises con mayor poblacion."""

def menu_principal(paises):
    """Menu de opciones"""
    pass