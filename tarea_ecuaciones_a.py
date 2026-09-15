import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
Ta = 28.1
C = 6.42
k = -0.00683

# Función de temperatura
def T(t):
    return Ta + C * np.exp(k * t)

# Tiempo en horas desde las 4:00 a. m.
t = np.linspace(0, 240, 500)

# Temperatura del cadáver
temperatura = T(t)

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(t, temperatura, label="Temperatura del cadáver")
plt.axhline(Ta, linestyle="--", label="Temperatura ambiente")

plt.xlabel("Tiempo desde las 4:00 a. m. (horas)")
plt.ylabel("Temperatura (°C)")
plt.title("Enfriamiento del cadáver - Literal a")
plt.legend()
plt.grid()

plt.show()