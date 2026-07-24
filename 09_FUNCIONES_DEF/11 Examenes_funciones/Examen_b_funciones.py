# Enunciado:
"""Escribe un programa que demuestre cómo pasar funciones como parámetros a  otras  funciones.  Para
ello, define dos funciones que calculen, respectivamente, el cuadrado y el cubo de un número, y  una
tercera función que reciba ambas funciones junto con un valor numérico y devuelva  la  suma  de  sus
resultados."""

# Examen_b_funciones.py

# Función que calcula el cuadrado.
def cuadrado(x):
    return x ** 2

# Función que calcula el cubo.
def cubo(x):
     return x ** 3

# Función que aplica dos funciones a un valor.
def aplica_funciones(f1, f2, valor):
    return f1(valor) + f2(valor)

# Resultado final.
resultado = aplica_funciones(cuadrado, cubo, 2)
print(resultado)

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────