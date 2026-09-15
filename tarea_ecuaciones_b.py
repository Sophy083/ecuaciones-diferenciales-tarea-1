import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# DATOS DEL PROBLEMA

T0 = 34.52
k = -0.00683

# TEMPERATURA AMBIENTE

def Ta(t):
    return (28.1 / 24) * (14.568 - (1 - t/12)**2)


# ECUACIÓN DIFERENCIAL

def modelo(T, t):
    return k * (T - Ta(t))


# TIEMPO

t = np.linspace(0, 24, 500)

# SOLUCIÓN NUMÉRICA

temperatura = odeint(modelo, T0, t).flatten()

ambiente = Ta(t)


# TABLA DE VALORES

horas = np.array([0, 4, 6, 8, 12, 16, 18, 20, 24])

temperatura_valores = odeint(modelo, T0, horas).flatten()

ambiente_valores = Ta(horas)

diferencia_valores = np.abs(
    temperatura_valores - ambiente_valores
)


print("\n")
print("=" * 60)
print("              LITERAL B")
print("=" * 60)

print("\nEcuación diferencial:")
print("dT/dt = -0.00683 [T - Ta(t)]")

print("\nTemperatura ambiente:")
print("Ta(t) = (28.1/24) [14.568 - (1 - t/12)^2]")

print("\nCondición inicial:")
print("T(0) = 34.52 °C")


print("\n")
print("=" * 60)
print("              TABLA DE VALORES")
print("=" * 60)

print(
    f"{'Tiempo (h)':>12}"
    f"{'Cadáver (°C)':>18}"
    f"{'Ambiente (°C)':>18}"
    f"{'Diferencia (°C)':>20}"
)

print("-" * 68)

for i in range(len(horas)):
    print(
        f"{horas[i]:>12.0f}"
        f"{temperatura_valores[i]:>18.2f}"
        f"{ambiente_valores[i]:>18.2f}"
        f"{diferencia_valores[i]:>20.2f}"
    )


# BUSCAR MAYOR CERCANÍA
diferencia = np.abs(temperatura - ambiente)
indice = np.argmin(diferencia)

tiempo_cercano = t[indice]
T_cercano = temperatura[indice]
Ta_cercano = ambiente[indice]
diferencia_minima = diferencia[indice]

print("\n")
print("=" * 60)
print("       MAYOR CERCANÍA A LA TEMPERATURA AMBIENTE")
print("=" * 60)

print(
    "Tiempo =",
    round(tiempo_cercano, 2),
    "horas después de las 4:00 a. m."
)

print(
    "Temperatura del cadáver =",
    round(T_cercano, 2),
    "°C"
)

print(
    "Temperatura ambiente =",
    round(Ta_cercano, 2),
    "°C"
)

print(
    "Diferencia mínima =",
    round(diferencia_minima, 2),
    "°C"
)

# GRÁFICA

plt.figure(figsize=(10, 6))

plt.plot(
    t,
    temperatura,
    label="Temperatura del cadáver"
)

plt.plot(
    t,
    ambiente,
    "--",
    label="Temperatura ambiente"
)

plt.scatter(
    tiempo_cercano,
    T_cercano,
    label="Mayor cercanía"
)

plt.xlabel("Tiempo desde las 4:00 a. m. (horas)")
plt.ylabel("Temperatura (°C)")

plt.title("Enfriamiento del cadáver - Literal b")

plt.legend()
plt.grid()

plt.show()