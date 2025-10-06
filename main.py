from funciones import carga_datos_csv, listar_paises, buscar_pais, filtrar_por_continente

def main():
    ruta = "paises.csv"
    paises = carga_datos_csv(ruta)
    print(paises)
    print("------------------------")
    listar_paises(paises,2,False)
    print("------------------------")
    buscar_pais(paises,"Japon")
    print("------------------------")
    filtrar_por_continente(paises,"Europa")

if __name__ == "__main__":
    main()