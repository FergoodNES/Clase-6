# Problema 1: Control de Temperatura en un Edificio Inteligente

def leer_sensores_temperatura():
    # Función para leer datos de sensores
    temp = float(input("Ingrese la temperatura actual de la zona (°C): "))
    return temp

def calcular_temperatura_optima(hora, ocupacion, clima_externo):
    # Función para calcular la temperatura óptima en cada zona
    if ocupacion > 50 or hora > 12:
        return 21.0
    else:
        return 23.5

def enviar_senales_ajuste(zona, temp_objetivo):
    # Procedimiento para enviar señales de ajuste
    print(f"[ACCIÓN] Ajustando termostato de la Zona {zona} a {temp_objetivo}°C.")

def analizar_consumo_energia(temp_actual, temp_ideal):
    # Función para registrar y analizar el consumo
    diferencial = abs(temp_actual - temp_ideal)
    consumo_kwh = diferencial * 1.5
    return consumo_kwh

def main():
    print("\n--- SISTEMA DE CLIMA INTELIGENTE ---")
    zona = int(input("Ingrese ID de la Zona: "))
    hora = int(input("Ingrese hora actual (0-23): "))
    ocupacion = int(input("Ingrese porcentaje de ocupación (0-100): "))
    clima = float(input("Ingrese temperatura externa actual (°C): "))
    
    temp_actual = leer_sensores_temperatura()
    temp_ideal = calcular_temperatura_optima(hora, ocupacion, clima)
    
    enviar_senales_ajuste(zona, temp_ideal)
    consumo = analizar_consumo_energia(temp_actual, temp_ideal)
    
    print(f"[REPORTE] Consumo estimado para el ajuste: {consumo:.2f} kWh")

if __name__ == "__main__":
    main()