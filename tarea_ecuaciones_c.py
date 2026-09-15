import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Datos
T0 = 34.52
k = -0.00683

# Temperatura ambiente
def Ta(t):
    return 28.1 * np.cos(1.166 * (t/12 - 1)**2)

# Ecuación diferencial
def modelo(T, t):
    return k * (T - Ta(t))

# Tiempo
t = np.linspace(0, 24, 500)

# Solución numérica
temperatura = odeint(modelo, T0, t).flatten()

# Temperatura ambiente
ambiente = Ta(t)

# Gráfica
plt.figure(figsize=(10, 6))

plt.plot(t, temperatura, label="Temperatura del cadáver")
plt.plot(t, ambiente, "--", label="Temperatura ambiente")

plt.xlabel("Tiempo desde las 4:00 a. m. (horas)")
plt.ylabel("Temperatura (°C)")
plt.title("Enfriamiento del cadáver - Literal c")

plt.legend()
plt.grid()

# =========================
# TABLA DE VALORES
# =========================

horas = np.array([0, 4, 6, 8, 12, 16, 18, 20, 24])

temperatura_valores = odeint(modelo, T0, horas).flatten()
ambiente_valores = Ta(horas)

print()
print("TABLA DE VALORES")
print("---------------------------------------------")
print("Tiempo | Cadáver (°C) | Ambiente (°C)")
print("---------------------------------------------")

for i in range(len(horas)):
    print(f"{horas[i]:6.0f} | {temperatura_valores[i]:13.2f} | {ambiente_valores[i]:13.2f}")

print("---------------------------------------------")

# =========================
# MAYOR CERCANÍA A LA TEMPERATURA AMBIENTE
# =========================

diferencia = np.abs(temperatura - ambiente)

indice = np.argmin(diferencia)

tiempo_cercano = t[indice]
T_cercano = temperatura[indice]
Ta_cercano = ambiente[indice]
diferencia_minima = diferencia[indice]

print()
print("MAYOR CERCANÍA A LA TEMPERATURA AMBIENTE")
print("---------------------------------------------")
print("Tiempo =", round(tiempo_cercano, 2), "horas")
print("Temperatura del cadáver =", round(T_cercano, 2), "°C")
print("Temperatura ambiente =", round(Ta_cercano, 2), "°C")
print("Diferencia mínima =", round(diferencia_minima, 2), "°C")

plt.show()
