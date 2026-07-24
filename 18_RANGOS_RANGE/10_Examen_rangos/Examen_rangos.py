# Enunciado:
"""Escribe un programa que solicite al usuario un número inicial, un número final  y  un  paso.  Con
estos valores, genera un objeto de tipo rango y conviértelo en una lista. A  continuación,  crea  un
segundo rango que recorra los mismos valores en orden inverso y muéstralo en  la  consola  como  una
lista.

Por último, calcula la suma, la cantidad de elementos, el valor máximo y el valor mínimo  del  rango
original utilizando funciones incorporadas para operaciones matemáticas y muestra los resultados  en
la consola."""

# Examen_rangos.py

# Solicitud de datos.
inicio = int(input("Número inicial: "))
fin = int(input("Número final: "))
paso = int(input("Paso: "))

# Rango original.
rango_original = range(inicio, fin, paso)
lista_original = list(rango_original)

print("\n--- Rango original ---")
print("Lista generada:", lista_original)

# Rango inverso.
if (lista_original and paso != 0):
    ultimo = lista_original[-1]
    rango_inverso = range(ultimo, inicio - paso, -paso)
    lista_inversa = list(rango_inverso)
else:
    lista_inversa = []

print("\n--- Rango inverso ---")
print("Lista invertida:", lista_inversa)

# Cálculos.
if (lista_original and paso != 0):
    suma_total = sum(lista_original)
    cantidad = len(lista_original)
    maximo = max(lista_original)
    minimo = min(lista_original)

    print("\n--- Análisis del rango ---")
    print("Suma total:", suma_total)
    print("Cantidad de elementos:", cantidad)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
else:
    print("\nEl rango original está vacío o el paso es cero. No se pueden realizar cálculos.")

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────