# Problema 4: Optimización de la Producción en una Fábrica

def monitorear_estado_maquinas():
    # Función para monitorear el estado de las máquinas
    horas_uso = int(input("Ingrese las horas de uso continuo de la máquina: "))
    estado = input("Ingrese el estado visible (Ej. 'Ok', 'Falla'): ")
    return horas_uso, estado

def planificar_mantenimiento(horas_uso):
    # Procedimiento para planificar el mantenimiento preventivo
    if horas_uso >= 1000:
        print("[ALERTA] Mantenimiento preventivo REQUERIDO para el próximo turno.")
    else:
        print("[INFO] Mantenimiento no requerido aún.")

def analizar_rendimiento_produccion(real, esperado):
    # Función para analizar el rendimiento de la producción
    if esperado <= 0:
        return 0.0
    eficiencia = (real / esperado) * 100
    return eficiencia

def ajustar_programacion_produccion(demanda, eficiencia):
    # Procedimiento para ajustar la programación de la producción
    if demanda > 5000 and eficiencia < 90:
        print("[ACCIÓN] Aumentando turnos: La eficiencia es baja y la demanda es alta.")
    else:
        print("[ACCIÓN] Manteniendo el ritmo de producción estándar.")

def main():
    print("\n--- CONTROL DE PRODUCCIÓN ---")
    horas, estado = monitorear_estado_maquinas()
    print(f"Estado reportado por el sensor: {estado}")
    
    planificar_mantenimiento(horas)
    
    prod_esperada = int(input("Ingrese la producción esperada de hoy (unidades): "))
    prod_real = int(input("Ingrese la producción real alcanzada (unidades): "))
    
    efic = analizar_rendimiento_produccion(prod_real, prod_esperada)
    print(f"Eficiencia de la línea: {efic:.2f}%")
    
    demanda_mercado = int(input("Ingrese la demanda del mercado para esta semana: "))
    ajustar_programacion_produccion(demanda_mercado, efic)

if __name__ == "__main__":
    main()