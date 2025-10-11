from funciones import (
    carga_datos_csv,
    estadisticas,
    listar_paises,
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_rango,
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
                print("\n======      BUSCAR PAIS POR NOMBRE      ======")
                buscar_pais(paises)
            case "2":
                print("\n======      FILTRAR POR CONTINENTE      ======")
                filtrar_por_continente(paises)
            case "3":
                print("\n======      FILTRAR POR RANGO      ======")
                filtrar_por_rango(paises)
            case "4":
                print("\n======      ORDENAR LISTADO      ======")
                listar_paises(paises)
            case "5":
                print("\n======      ESTADISTICAS      ======")
                estadisticas(paises)
            case "6":
                print("Saliendo del programa...")
            case _:
                print("Opción no válida.")

        if opcion != "6":
            input("\n\nPresione enter para volver al MENU...")
            print(
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            )


if __name__ == "__main__":
    main()
