# Comparacion de Soluciones Analiticas y Numericas

## Descripcion del Problema
En este proyecto se analiza una Ecuacion Diferencial Ordinaria (EDO) de primer orden separable:
dy/dt = t * y
Con la condicion inicial y(0) = 1, en el intervalo de tiempo t en [0, 1].

El objetivo es comparar la solucion obtenida mediante metodos analiticos (exactos) frente a la aproximacion numerica usando el Metodo de Euler.

## 1. Solucion Analitica (Separacion de Variables)
Para resolverla analiticamente, separamos las variables y y t:
dy / y = t dt

Integrando ambos lados:
ln|y| = (t^2)/2 + C

Despejando y y aplicando la condicion inicial y(0) = 1, obtenemos la solucion exacta:
y(t) = e^((t^2)/2)

## 2. Solucion Numerica (Metodo de Euler)
El Metodo de Euler aproxima la solucion dando pasos discretos de tamaño h. La formula iterativa es:
y_(n+1) = y_n + h * f(t_n, y_n)

Para este problema, usamos un tamaño de paso h = 0.2.

## Resultados
Al ejecutar el script main.py, se genera una tabla en consola y una grafica comparativa.
* La solucion exacta (linea roja punteada) representa el comportamiento real de la funcion.
* La aproximacion de Euler (linea azul con puntos) sigue la tendencia con un margen de error por paso.

## Como ejecutar
1. Tener Python instalado.
2. Instalar dependencias: pip install numpy matplotlib
3. Ejecutar el script: python main.py
