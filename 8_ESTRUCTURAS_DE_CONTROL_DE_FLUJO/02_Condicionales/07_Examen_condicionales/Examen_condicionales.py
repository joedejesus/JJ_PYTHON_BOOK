# Enunciado:
"""Escribe un programa que solicite al  usuario  su  edad  y  determine  su  clasificación  mediante
condicionales. El programa debe identificar si la persona es  niño,  adolescente,  adulto  o  adulto
mayor según el rango de edad correspondiente.

Por último, después de clasificar la edad mediante los condicionales "if...elif...else", utiliza  la
expresión "match" para proporcionar una  descripción  más  específica:  niño  pequeño,  adolescente,
adulto de 18 años o una descripción general en cualquier otro caso. En todos los casos, el  programa
debe mostrar la clasificación de edad y la descripción específica correspondiente."""

# Examen_condicionales.py

# Solicitud de la edad.
edad = int(input("Ingresa tu edad: "))

# Clasificación principal.
if (0 <= edad < 12):
    clasificacion = "Niño"
elif (12 <= edad < 18):
    clasificacion = "Adolescente"
elif (18 <= edad < 65):
    clasificacion = "Adulto"
else:
    clasificacion = "Adulto Mayor"

# Muestra la clasificación.
print(f"Clasificación de edad: {clasificacion}")

# Clasificación específica con "match".
match edad:
    case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11:
        print("¡Eres un niño pequeño!")
    case 12 | 13 | 14 | 15 | 16 | 17:
        print("¡Estás en la etapa de la adolescencia!")
    case 18:
        print("¡Eres un adulto en plena edad laboral!")
    case _:
        print("¡Eres un adulto mayor y mereces respeto!")

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────