# Enunciado:
"""Calcula el resultado de la siguiente operación (2 ** 3 * 5 + 7 // 3). Usa paréntesis para  forzar
el orden de precedencia y de evaluación según la jerarquía  de  operadores  en  Python.  Finalmente,
muestra el resultado en la consola utilizando la función "print()". El resultado debe ser 42."""

# Ejercicio_operadores_aritmeticos.py

# Explicación:
"""Definimos una variable llamada "operacion" que almacena el resultado de la operación  aritmética.
Realizamos la operación encerrando entre paréntesis cada parte para forzar el orden de precedencia y
de evaluación según la jerarquía de operadores. Finalmente,  imprimimos  el  valor  de  la  variable
usando la función "print()" para mostrar el resultado de la operación en la consola,  acompañado  de
un mensaje descriptivo."""

# Código:
operacion = (((2 ** 3) * 5) + (7 // 3))
print("El resultado de la operación es =", operacion)

# Nota Importante:
"""Usamos paréntesis en las operaciones para forzar el orden de precedencia y de evaluación según la
jerarquía de operadores en Python. La operación se evalúa siguiendo las reglas  de  precedencia.  En
este caso, primero se realiza la operación de potencia (2 ** 3), luego la de multiplicación (8 *  5)
y la división entera (7 // 3), y, finalmente, la suma (40 + 2). De esta manera, el  resultado  final
es 42.

Cabe destacar que, aunque no se usaran paréntesis, el  resultado  sería  el  mismo,  ya  que  Python
respeta la jerarquía de operadores. Sin embargo, el uso de paréntesis demuestra cómo  se  maneja  la
precedencia y evaluación de operaciones aritméticas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────