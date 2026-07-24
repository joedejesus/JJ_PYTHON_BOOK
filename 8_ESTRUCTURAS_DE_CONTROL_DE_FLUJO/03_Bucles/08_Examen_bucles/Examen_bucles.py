# Enunciado:
"""Escribe un programa que sume los números pares del 1 al 20 y se detenga cuando la suma  acumulada
supere el límite de 15. El programa debe identificar los números pares, acumular su valor y  detener
el bucle en el momento exacto en que la suma sobrepase el límite.

Por último, una vez superado el  límite,  el  programa  debe  mostrar  el  último  valor  acumulado,
indicando claramente que el límite ha sido superado."""

# Examen_bucles.py

# Inicialización de variables.
numero = 1
suma_pares = 0

# Bucle para sumar números pares.
while (numero <= 20):
    if (numero % 2 == 0):
        suma_pares += numero
        print(f"El número {numero} es par")

        if (suma_pares > 15):
            print(f"Se sobrepasó el límite de 15. Última suma: {suma_pares}")
            break

    numero += 1

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────