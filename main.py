from funciones import (
    carga_datos_csv,
    listar_paises,
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_rango,
    obtener_mayor_menor,
    promedio_poblacion_por_continente,
    cantidad_paises_por_continente,
    top_3_poblacion,
)


def main():
    ruta = "paises.csv"
    paises = carga_datos_csv(ruta)
    opcion = ""
    while opcion != "6":
        print(
            "1. Buscar país por nombre\n"
            "2. Filtrar por continente\n"
            "3. Filtrar por rango (población o superficie)\n"
            "4. Ordenar países\n"
            "5. Mostrar estadísticas\n"
            "6. Salir\n"
        )
        opcion = input("Seleccione una opción\n> ")

        match opcion:
            case "1":
                buscar_pais(paises)
            case "2":
                filtrar_por_continente(paises)
            case "3":
                filtrar_por_rango(paises)
            case "4":
                listar_paises(paises)
            case "5":
                pass
            case "6":
                print("Saliendo del programa...")
            case _:
                print("Opción no válida.")
        input("\n\nPresione enter para volver al MENU...")
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        )

    """
    print(paises)
    print("_" * 65)
    listar_paises(paises,2,False)
    print("_" * 65)
    buscar_pais(paises,"Japon")
    print("_" * 65)
    filtrar_por_continente(paises,"Europa")
    print("_" * 65)
    filtrar_por_rango(paises, "poblacion", 0, 99999999)
    print("_" * 65)
    obtener_mayor_menor(paises, "superficie")
    print("_" * 65)
    promedio_poblacion_por_continente(paises)
    print("_" * 65)
    cantidad_paises_por_continente(paises)
    print("_" * 65)
    top_3_poblacion(paises)
    """


if __name__ == "__main__":
    main()
