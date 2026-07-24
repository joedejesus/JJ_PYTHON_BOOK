# Enunciado:
"""Escribe un programa que solicite al usuario un número entero, un número decimal,  una  cadena  de
texto y un valor booleano escrito como "True" o "False". Cada entrada debe convertirse a su tipo  de
dato correspondiente: (int), (float), (str) y (bool).

Después de convertir los valores, crea un diccionario llamado "info" que almacene  cada  dato  junto
con su tipo real en Python utilizando la función "type()". El diccionario debe  incluir  las  claves
"entero", "decimal", "texto" y "booleano", cada una asociada a una tupla con el valor ingresado y su
tipo.

Por último, muestra el diccionario completo de forma legible y verifica si el  número  entero  y  el
número decimal pueden sumarse sin producir errores, mostrando el resultado de la suma."""

# Examen_tipos_de_datos_basicos.py

# Solicitud de datos al usuario.
entero = int(input("Introduce un número entero: "))
decimal = float(input("Introduce un número decimal: "))
texto = str(input("Introduce una cadena de texto: "))
booleano = input("Introduce un valor booleano (True/False): ")

# Conversión del valor booleano.
if (booleano.lower() == "true"):
    booleano = True
else:
    booleano = False

# Construcción del diccionario.
info = {
    "entero":   (entero, type(entero)),
    "decimal":  (decimal, type(decimal)),
    "texto":    (texto, type(texto)),
    "booleano": (booleano, type(booleano))
}

# Muestra del diccionario.
print("\n--- Información recopilada ---")
for clave, valor in info.items():
    print(f"{clave}: valor={valor[0]}, tipo={valor[1]}")

# Suma entre entero y decimal.
resultado_suma = (entero + decimal)
print(f"\nResultado de sumar el entero y el decimal: {resultado_suma}")

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────