import numpy as np
import matplotlib.pyplot as plt

# EDO: dy/dt = t*y, y(0) = 1, h = 0.2
h = 0.2
t = np.arange(0, 1.1, h)
y_euler = np.zeros(len(t))
y_euler[0] = 1.0

# Método de Euler
for i in range(len(t) - 1):
    y_euler[i + 1] = y_euler[i] + h * (t[i] * y_euler[i])

# Solución exacta: y(t) = exp(t^2 / 2)
y_exacta = np.exp(t**2 / 2)

# Tabla de resultados en consola
print("  t   |   Euler   |  Exacta   |   Error")
print("-" * 42)
for ti, ye, yex in zip(t, y_euler, y_exacta):
    print(f"{ti:4.1f}  |  {ye:7.4f}  |  {yex:7.4f}  |  {abs(yex - ye):7.4f}")

# Gráfica comparativa
plt.figure(figsize=(8, 5))
plt.plot(t, y_euler, 'bo-', label='Euler (h=0.2)')
plt.plot(t, y_exacta, 'r--', label='Solucion Exacta')
plt.title('Metodo de Euler: dy/dt = t*y')
plt.xlabel('Tiempo t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('comparacion_euler_analitica.png', dpi=300)
plt.show()
