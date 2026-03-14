# Problema 2: Gestión de Inventario en un Almacén

def registrar_entrada(stock_actual):
    # Función para registrar la entrada de productos
    cantidad = int(input("Ingrese la cantidad de productos que ingresan: "))
    return stock_actual + cantidad

def registrar_salida(stock_actual):
    # Función para registrar la salida de productos
    cantidad = int(input("Ingrese la cantidad de productos a retirar: "))
    if cantidad > stock_actual:
        print("[ERROR] Stock insuficiente para esta salida.")
        return stock_actual
    return stock_actual - cantidad

def calcular_nivel_optimo(demanda_mensual, dias_entrega):
    # Procedimiento para calcular el nivel óptimo de inventario
    punto_reorden = (demanda_mensual / 30) * dias_entrega
    print(f"[INFO] Punto de reorden sugerido: {punto_reorden:.2f} unidades.")

def generar_alertas(stock_actual, min_seguridad):
    # Función para generar alertas de reabastecimiento
    return stock_actual <= min_seguridad

def main():
    print("\n--- GESTIÓN DE ALMACÉN ---")
    stock = int(input("Ingrese el stock actual en bodega: "))
    minimo = int(input("Ingrese el nivel mínimo de seguridad: "))
    demanda = float(input("Ingrese la demanda mensual proyectada: "))
    
    stock = registrar_entrada(stock)
    stock = registrar_salida(stock)
    
    calcular_nivel_optimo(demanda, 7)
    
    if generar_alertas(stock, minimo):
        print("¡ALERTA CRÍTICA! Es necesario reabastecer inmediatamente.")
    else:
        print(f"Estado del inventario normal. Stock final: {stock}")

if __name__ == "__main__":
    main()