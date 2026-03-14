# Problema 3: Sistema de Navegación para un Vehículo Autónomo

def leer_sensores_proximidad():
    # Función para leer datos de sensores de proximidad y cámaras
    distancia = float(input("Ingrese la distancia del obstáculo más cercano (metros): "))
    return distancia

def calcular_ruta_optima(origen, destino):
    # Procedimiento para calcular la ruta óptima
    print(f"[NAVEGACIÓN] Calculando la ruta más rápida desde '{origen}' hasta '{destino}'...")

def detectar_obstaculos(distancia):
    # Función para detectar y evitar obstáculos
    return distancia < 3.5

def ajustar_velocidad(velocidad):
    # Procedimiento para ajustar la velocidad del vehículo
    print(f"[MOTORES] Ajustando velocidad a {velocidad} km/h.")

def main():
    print("\n--- SISTEMA DE NAVEGACIÓN AUTÓNOMA ---")
    origen = input("Ingrese punto de partida: ")
    destino = input("Ingrese punto de destino: ")
    
    calcular_ruta_optima(origen, destino)
    distancia_sensor = leer_sensores_proximidad()
    
    if detectar_obstaculos(distancia_sensor):
        print("¡PELIGRO! Obstáculo detectado en la trayectoria.")
        ajustar_velocidad(0)
    else:
        ajustar_velocidad(60)

if __name__ == "__main__":
    main()