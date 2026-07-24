# Enunciado:
"""Escribe un programa que solicite dos números al usuario y realice una división  entre  ellos.  El
programa debe manejar excepciones para controlar valores no válidos, divisiones por cero  y  errores
inesperados.

El resultado de la división debe validarse mediante una lista predefinida de valores permitidos.  Si
el resultado no pertenece a esa lista, se debe generar una excepción específica.

Por último, el programa debe mostrar un mensaje adecuado para cada tipo de error y finalizar siempre
con un mensaje que indique que la ejecución ha finalizado."""

# Examen_excepciones.py

# Lista de valores válidos.
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Validación del resultado.
def opcion_valida(opcion):
    if (opcion not in lista):
        raise ValueError("Opción inválida")
    elif (opcion == 0):
        raise ZeroDivisionError("No se permite la opción 0")
    elif (opcion == 4):
        raise Exception("Opción inválida")
    return opcion

# Solicitud de datos.
a = float(input("Ingrese el numerador: "))
b = float(input("Ingrese el denominador: "))

# Manejo de excepciones.
try:
    resultado = opcion_valida(a / b)
    print(f"El resultado de la división es: {resultado}")
except ValueError as ve:
    print(f"Por favor, ingrese números válidos. Detalle: {ve}")
except ZeroDivisionError as zde:
    print(f"Error: No se puede dividir por cero. Detalle: {zde}")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    print("Fin del programa.")

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────