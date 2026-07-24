# Enunciado:
"""Define dos variables, "a" y "b". Asigna un valor  entero  a  la  variable  "a"  y  una  operación
aritmética a la variable "b". Esta última debe dar como resultado  el  mismo  valor  asignado  a  la
primera. Compara ambas variables con los operadores de igualdad (==) y desigualdad (!=). Finalmente,
usa la función "print()" para mostrar el resultado de las comparaciones en la consola  y  acompáñalo
con un mensaje descriptivo."""

# Ejercicio_operadores_comparativos.py

# Explicación:
"""Definimos dos variables. La primera, llamada "a", a la cual le asignamos el valor entero 190.  La
segunda, llamada "b", a la cual le asignamos una operación aritmética que, al evaluarse, da el mismo
valor. En este caso, ((30 * 3) + (20 * 5)) da como resultado 190.

Luego, comparamos ambas variables, primero con el  operador  de  igualdad  (==)  y  después  con  el
operador de desigualdad (!=), encerrando las  expresiones  entre  paréntesis  para  que  se  evalúen
correctamente. En ambos casos, asignamos el resultado a una  variable  con  un  nombre  descriptivo:
"igualdad" y "desigualdad", respectivamente.

Finalmente, mostramos los resultados de las  comparaciones  en  la  consola  utilizando  la  función
"print()", acompañados de un mensaje que describe el resultado de  la  comparación.  En  este  caso,
aunque el contenido de las variables parece diferente a simple vista, en esencia es  igual,  ya  que
ambas contienen el valor 190."""

# Código:
a = 190
b = ((30 * 3) + (20 * 5))

igualdad = (a == b)
print("El primer número es igual al segundo:", igualdad)

desigualdad = (a != b)
print("El primer número es diferente al segundo:", desigualdad)

# Nota Importante:
"""En programación, lo que parece diferente  a  primera  vista  puede  ser  idéntico  en  esencia  y
viceversa. Por ello, los operadores comparativos son herramientas fundamentales que permiten evaluar
rápidamente si dos elementos son iguales  o  diferentes,  lo  cual  resulta  especialmente  útil  al
trabajar con estructuras complejas o grandes volúmenes de datos."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
