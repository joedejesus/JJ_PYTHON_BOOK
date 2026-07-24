# Enunciado:
"""Escribe un programa que reciba un iterable y devuelva únicamente las palabras que tengan  más  de
ocho caracteres. Para ello, utiliza una función externa que reciba cualquier iterable y una  función
interna que filtre los elementos  mediante  "yield",  permitiendo  trabajar  con  listas,  tuplas  o
cualquier otro objeto iterable. Por último, muestra  los  resultados  en  la  consola  en  forma  de
lista."""

# Examen_b_funciones_incorporadas.py

# Iterables globales de ejemplo.
tupla_nombres = ("Juan jose corona", "Pedro", "Maria", "Joe", "Ana")
lista_arqueologia = ["museo", "arqueologia", "dinosaurio", "geologia"]

# Función externa que recibe un iterable.
def externa(conjunto_literal):
    lista_informatica = ["python", "programacion", "computadora", "escritorio"]

    # Función interna que filtra palabras largas.
    def interna():
        for i in conjunto_literal:
            if (len(i) > 8):
                yield i
    return interna

# Llamada a la función externa con cualquier iterable.
resultado = externa(["mecanografia", "geologia", "arqueologia", "museo", "dinosaurio", "computadora", "programacion"])

# Muestra los resultados.
print(list(resultado()))

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────