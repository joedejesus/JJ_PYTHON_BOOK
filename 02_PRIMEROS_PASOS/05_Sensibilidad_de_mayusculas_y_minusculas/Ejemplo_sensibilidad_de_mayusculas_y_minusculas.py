# Enunciado:
"""Python distingue entre mayúsculas y minúsculas.  Esto  significa  que  considera  diferentes  las
variables, funciones y clases si tienen distintas combinaciones de mayúsculas y minúsculas.  Por  lo
tanto, cuando hagas referencia a una variable, función o clase, debes usar la misma  combinación  de
mayúsculas y minúsculas que usaste al definirla. Es decir,  debes  escribirla  exactamente  como  la
definiste. De lo  contrario,  Python  no  podrá  encontrarla  y  mostrará  un  error  de  nombre  no
definido."""

# Ejemplo_sensibilidad_de_mayusculas_y_minusculas.py

# Explicación:
"""Definimos una variable llamada "numero" y le asignamos el valor 1. Luego, imprimimos el valor  de
la variable. Después, definimos otra variable llamada "Numero" (con N mayúscula) y le  asignamos  el
valor 2. Intentamos imprimir el valor de la variable  "numero"  (con  n  minúscula)  en  el  segundo
bloque. En este caso, se imprimirá el valor de la  variable  "numero",  que  corresponde  al  primer
bloque. Esto ocurre porque "Numero" y "numero" son variables diferentes, con valores distintos, pero
con nombres similares. Por lo tanto, no se producirá un error, pero tampoco se imprimirá el valor de
"Numero", lo cual no es lo esperado."""

# Código:
numero = 1
print(numero)  # Imprime 1 (Correcto).

Numero = 2
# Imprime 1 (No imprime 2 porque "Numero" y "numero" son diferentes).
print(numero)

# Nota Importante:
"""Para evitar este tipo de errores, recomendamos seguir una convención  de  nombres  consistente  y
usar nombres descriptivos para las variables, funciones y clases. Además, recomendamos usar  siempre
minúsculas para los nombres de variables, funciones y claves de diccionarios,  evitando  el  uso  de
acentos, caracteres especiales y espacios. Para las funciones que  encapsulan  entradas  (inputs)  y
contienen un diccionario en su interior, recomendamos usar números como claves. Esto ayuda a  evitar
errores y hace que el código sea más claro al igualar la  llamada  de  la  función  con  la  entrada
correspondiente. Esto se explicará  con  más  detalle  y  se  entenderá  en  códigos  más  complejos
relacionados con el tema de los diccionarios."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────