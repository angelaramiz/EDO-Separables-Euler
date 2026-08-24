# Comparación de Soluciones Analíticas y Numéricas

## 🎯 Descripción del Problema
En este proyecto se analiza una **Ecuación Diferencial Ordinaria (EDO) de primer orden separable**:
$$ \frac{dy}{dt} = t \cdot y $$
Con la condición inicial $y(0) = 1$, en el intervalo de tiempo $t \in [0, 1]$.

El objetivo es comparar la solución obtenida mediante métodos analíticos (exactos) frente a la aproximación numérica usando el Método de Euler.

## 🧮 1. Solución Analítica (Separación de Variables)
Para resolverla analíticamente, separamos las variables $y$ y $t$:
$$ \frac{dy}{y} = t \, dt $$
Integrando ambos lados:
$$ \int \frac{1}{y} dy = \int t \, dt \implies \ln|y| = \frac{t^2}{2} + C $$
Despejando $y$ y aplicando la condición inicial $y(0) = 1$, obtenemos la solución exacta:
$$ y(t) = e^{t^2 / 2} $$

## 💻 2. Solución Numérica (Método de Euler)
El Método de Euler aproxima la solución dando pasos discretos de tamaño $h$. La fórmula iterativa es:
$$ y_{n+1} = y_n + h \cdot f(t_n, y_n) $$
Para este problema, usamos un tamaño de paso **$h = 0.2$**.

## 📊 Resultados
Al ejecutar el script `main.py`, se genera una tabla en consola y una gráfica comparativa. 
* La **solución exacta** (línea roja punteada) representa el comportamiento real de la función.
* La **aproximación de Euler** (línea azul con puntos) sigue la tendencia, pero acumula un pequeño error en cada paso debido a la linealización de la curva.

## 🚀 Cómo ejecutar
1. Asegúrate de tener Python instalado.
2. Instala las dependencias necesarias: `pip install numpy matplotlib`
3. Ejecuta el script: `python main.py`
