from funciones import (
    carga_datos_csv,
    listar_paises,
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_rango,
    menu_principal,
    obtener_mayor_menor,
    promedio_poblacion_por_continente,
    cantidad_paises_por_continente,
    top_3_poblacion,
    menu_principal,
)


def main():
    ruta = "paises.csv"
    paises = carga_datos_csv(ruta)
    menu_principal(paises)

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
