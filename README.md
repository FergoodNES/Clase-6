# Proyecto de Modularidad: Funciones y Procedimientos

Este repositorio contiene la solución a cinco problemas reales mediante el uso de programación modular en Python.

## Análisis de Funciones y Rendimiento

### Problema 1: Control de Temperatura
- **Funciones:** `leer_sensores_temperatura`, `calcular_temperatura_optima`, `analizar_consumo_energia`.
- **Procedimiento:** `enviar_senales_ajuste`.
- **Impacto:** La modularidad permite procesar solo los datos necesarios, optimizando el consumo energético al separar la lectura de la lógica de ajuste.

### Problema 2: Gestión de Inventario
- **Funciones:** `registrar_entrada`, `registrar_salida`, `generar_alertas`.
- **Procedimiento:** `calcular_nivel_optimo`.
- **Impacto:** Al encapsular la lógica de stock, se evitan cálculos redundantes y se mejora la velocidad de respuesta ante alertas de reabastecimiento.

### Problema 3: Navegación de Vehículo Autónomo
- **Funciones:** `leer_sensores_proximidad`, `detectar_obstaculos`.
- **Procedimientos:** `calcular_ruta_optima`, `ajustar_velocidad`.
- **Impacto:** Permite que el sistema tome decisiones críticas (como frenar) de forma aislada y rápida, mejorando la seguridad y el tiempo de viaje.

### Problema 4: Optimización de Producción
- **Funciones:** `monitorear_estado_maquinas`, `analizar_rendimiento_produccion`.
- **Procedimientos:** `planificar_mantenimiento`, `ajustar_programacion_produccion`.
- **Impacto:** La modularidad facilita el mantenimiento predictivo, reduciendo el tiempo de inactividad de las máquinas.

### Problema 5: Sistema de Riego Automatizado
- **Funciones:** `leer_sensores_humedad`, `consultar_previsiones`, `controlar_valvulas`.
- **Procedimiento:** `calcular_optima_riego`.
- **Impacto:** Optimiza el uso del agua al cruzar datos de sensores y clima en funciones separadas antes de accionar las válvulas.
