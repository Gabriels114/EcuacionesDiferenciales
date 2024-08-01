import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

D = np.loadtxt('Clase 1/oax_qro.txt')
f = D[:, 1] #queretaro  

#derivada numerica
h = 1
a = 1
end = len(f)
df = (f[a+h:end] - f[a:end-h]) / h
#graficando
plt.plot(f, label='f')
plt.plot([a, a+h], [f[a], f[a+h]], 'ro-', label='Derivada')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Gráfica de f y su derivada numérica')
plt.legend()
plt.show()

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

# Calcular la derivada numérica
h = 1e-5
dy = (np.sin(x + h) - np.sin(x - h)) / (2 * h)

# Graficar la función y su derivada
plt.plot(x, y, label='seno(x)')
plt.plot(x, dy, label='derivada de seno(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de seno(x) y su derivada numérica')
plt.legend()
plt.show()
