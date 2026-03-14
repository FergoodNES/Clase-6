# Problema 5: Sistema de Riego Automatizado para Agricultura

def leer_sensores_humedad():
    # Función para leer datos de sensores de humedad del suelo
    humedad = float(input("Ingrese porcentaje de humedad del suelo (0-100): "))
    return humedad

def consultar_previsiones():
    # Función para consultar las previsiones meteorológicas
    clima = int(input("Ingrese pronóstico (0: Despejado, 1: Lluvia): "))
    return clima

def calcular_optima_riego(humedad, lluvia):
    # Procedimiento para calcular la cantidad óptima de riego
    if humedad < 30 and lluvia == 0:
        print("[DIAGNÓSTICO] Necesidad de riego: ALTA. Suelo seco y sin lluvia a la vista.")
        return True
    else:
        print("[DIAGNÓSTICO] Necesidad de riego: NULA. Condiciones óptimas o lluvia prevista.")
        return False

def controlar_valvulas(sector, estado):
    # Función para controlar las válvulas de riego en diferentes secciones
    if estado:
        print(f"[COMANDO] Abriendo válvulas del Sector {sector}...")
    else:
        print(f"[COMANDO] Cerrando válvulas del Sector {sector}...")
    return True

def main():
    print("\n--- CONTROL DE RIEGO AUTOMÁTICO ---")
    
    humedad_actual = leer_sensores_humedad()
    lluvia_prevista = consultar_previsiones()
    
    necesita_riego = calcular_optima_riego(humedad_actual, lluvia_prevista)
    
    if necesita_riego:
        exito = controlar_valvulas(1, True)
        if exito:
            print("Operación de riego iniciada con éxito.")
    else:
        controlar_valvulas(1, False)

if __name__ == "__main__":
    main()