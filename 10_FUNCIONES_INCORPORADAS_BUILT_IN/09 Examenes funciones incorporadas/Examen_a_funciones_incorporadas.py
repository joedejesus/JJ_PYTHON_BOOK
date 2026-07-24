# Enunciado:
"""Escribe un programa que, dada una lista de palabras, imprima únicamente aquellas que  tengan  más
de ocho caracteres. Para ello, utiliza una función externa que contenga  una  lista  interna  y  una
función interna que filtre las palabras mediante  "yield",  devolviendo  solo  las  que  cumplan  la
condición. Por último, muestra el resultado de la lista filtrada en la consola, este resultado  debe
ser una lista y no otra estructura de datos."""

# Examen_a_funciones_incorporadas.py

# Función externa que contiene una lista interna.
def externa(lista):
    lista = ["python", "programacion", "computadora", "escritorio"]

    # Función interna que filtra las palabras largas.
    def lista_palabras():
        for i in lista:
            if (len(i) > 8):
                yield i
    return lista_palabras

# Llamada a la función externa.
resultado = externa(None)

# Mostrar el resultado.
print(list(resultado()))

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────