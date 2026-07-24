# Enunciado:
"""Escribe un programa que, dada una lista de números, calcule la  suma  de  los  cuadrados  de  los
números pares y la suma de los cubos de los números impares. Para ello, crea dos funciones: una  que
sume los cuadrados de los números pares y otra que sume los cubos de los números impares.

Por último, implementa una tercera función que reciba la lista y  devuelva  la  suma  total  de  los
resultados obtenidos por las dos funciones anteriores. Además, muestra en la consola los  resultados
de cada función y la suma total llamando a la función correspondiente con la  ayuda  de  la  función
"print()"."""

# Examen_a_funciones.py

# Lista de números.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Suma de los cuadrados de los números pares.
def suma_cuadrados_numeros_pares(lista):
    suma = 0
    for i in lista:
        if (i % 2 == 0):
            suma += (i ** 2)
    return suma

# Suma de los cubos de los números impares.
def suma_cubos_numeros_impares(lista):
    suma = 0
    for i in lista:
        if (i % 2 != 0):
            suma += (i ** 3)
    return suma

# Suma total de los resultados de ambas funciones.
def suma_funciones(lista):
    a = suma_cuadrados_numeros_pares(lista)
    b = suma_cubos_numeros_impares(lista)
    return a + b

# Resultados.
print(suma_cuadrados_numeros_pares(lista))
print(suma_cubos_numeros_impares(lista))
print(suma_funciones(lista))

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────