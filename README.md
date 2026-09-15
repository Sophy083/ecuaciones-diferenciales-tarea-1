# Tarea 1 - Ecuaciones Diferenciales
  
**Nombre:** Sophia Henao Jimenez

**CC:** 1033178826

## Descripción

En esta tarea se estudia el enfriamiento de un cadáver mediante la **Ley de Enfriamiento de Newton**.

Se analizan tres situaciones diferentes para la temperatura ambiente:

- **Literal a:** temperatura ambiente constante.
- **Literal b:** temperatura ambiente variable según una función dada.
- **Literal c:** temperatura ambiente variable según una función cosenoidal.

## Contenido del repositorio

- `tarea_ecuaciones_a.py` → Solución del literal a.
- `tarea_ecuaciones_b.py` → Solución numérica del literal b.
- `tarea_ecuaciones_c.py` → Solución numérica del literal c.
- `README.md` → Descripción de la tarea y del contenido del repositorio.

## Métodos utilizados

Para el literal a se utiliza la solución analítica de la Ley de Enfriamiento de Newton.

Para los literales b y c se utiliza un método numérico mediante la función `odeint()` de `scipy.integrate`, debido a que la temperatura ambiente depende del tiempo.

## Resultados principales

### Literal a

Se obtiene una estimación del momento de la muerte de aproximadamente **12,2 horas antes de las 4:00 a. m.**, es decir, aproximadamente a las **3:45 p. m. del día anterior**.

El cadáver se aproxima progresivamente a la temperatura ambiente de 28,1 °C.

### Literal b

La temperatura ambiente es variable durante las 24 horas. La mayor cercanía entre la temperatura del cadáver y la temperatura ambiente ocurre aproximadamente a las **18,61 horas** después de las 4:00 a. m.

La diferencia mínima es aproximadamente **15,70 °C**, por lo que el cadáver no alcanza una temperatura cercana a la ambiental dentro del intervalo analizado.

### Literal c

La temperatura ambiente también es variable. La mayor cercanía ocurre aproximadamente a las **14,19 horas** después de las 4:00 a. m.

La diferencia mínima es aproximadamente **5,58 °C**.
