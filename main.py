import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# PROBLEMA: Ecuación Diferencial Separable
# Ecuación: dy/dt = t * y
# Condición Inicial: y(0) = 1
# Intervalo: t en [0, 1], Paso h = 0.2
# =====================================================================

# 1. Definir la función de la EDO
def f(t, y):
    return t * y

# 2. Solución Analítica (usando Separación de Variables)
# dy/y = t dt  =>  ln|y| = t^2/2 + C  =>  y(t) = e^(t^2/2)
def solucion_exacta(t):
    return np.exp(t**2 / 2)

# 3. Parámetros del Método de Euler
t0, y0 = 0.0, 1.0
t_fin = 1.0
h = 0.2

# 4. Implementación del Método de Euler
t_vals = np.arange(t0, t_fin + h/2, h) # Genera [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y_euler = np.zeros(len(t_vals))
y_euler[0] = y0

for i in range(len(t_vals) - 1):
    y_euler[i+1] = y_euler[i] + h * f(t_vals[i], y_euler[i])

# 5. Calcular la solución exacta en los mismos puntos
y_exacta = solucion_exacta(t_vals)

# 6. Imprimir tabla de comparación en consola
print(f"{'t':<5} | {'Euler (Num)':<12} | {'Exacta (Ana)':<12} | {'Error':<10}")
print("-" * 45)
for t, ye, yex in zip(t_vals, y_euler, y_exacta):
    error = abs(yex - ye)
    print(f"{t:<5.1f} | {ye:<12.5f} | {yex:<12.5f} | {error:<10.5f}")

# 7. Graficar resultados
plt.figure(figsize=(9, 6), dpi=300)
plt.plot(t_vals, y_euler, 'bo-', label='Método de Euler (h=0.2)', markersize=8)
plt.plot(t_vals, y_exacta, 'r--', label='Solución Exacta (Analítica)', linewidth=2)
plt.title('Comparación: Ecuación Separable dy/dt = t*y', fontsize=14)
plt.xlabel('Tiempo t', fontsize=12)
plt.ylabel('y(t)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Guardar y mostrar la gráfica
plt.savefig('comparacion_euler_analitica.png', dpi=300)
print("\nGráfica guardada como 'comparacion_euler_analitica.png'")
plt.show()
