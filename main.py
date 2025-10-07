from funciones import carga_datos_csv, listar_paises, buscar_pais, filtrar_por_continente, filtrar_por_rango, obtener_mayor_menor

def main():
    ruta = "paises.csv"
    paises = carga_datos_csv(ruta)
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

if __name__ == "__main__":
    main()
