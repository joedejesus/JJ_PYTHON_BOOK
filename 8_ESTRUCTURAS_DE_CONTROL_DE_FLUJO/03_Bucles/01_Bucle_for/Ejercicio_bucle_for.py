# Enunciado:
"""Escribe un programa que use un bucle "for" para iterar sobre una secuencia inmutable  de  números
y, con la ayuda de una operación aritmética básica asociada a una variable "x" definida  dentro  del
bucle, sume 1 a cada número e imprima el resultado de cada suma "x" y  el  número  original  "i"  en
formato  "f-string".  Además,  haz  que  el  programa  imprima  "Fin  del  bucle"  al  finalizar  la
iteración."""

# Ejercicio_bucle_for.py

# Explicación:
"""Definimos una variable llamada "rango_numeros" y le asignamos un rango de números del 1 al 9  (1,
10) utilizando el constructor "range()", que genera una secuencia inmutable de números enteros.

Luego, utilizamos un bucle "for" para iterar sobre cada elemento del rango. Para ello, escribimos la
palabra clave "for", seguida de la variable "i", que representa cada elemento de la secuencia y  que
definimos en este momento, seguida del operador "in"  para  indicar  sobre  qué  secuencia  queremos
realizar la iteración y el nombre de la secuencia  sobre  la  que  queremos  iterar,  en  este  caso
"rango_numeros". A continuación, escribimos dos puntos (:) para indicar el final de la  expresión  y
el inicio del bloque de código asociado al bucle "for".

Dentro del bucle "for", definimos una variable llamada "x" y le asignamos el resultado de sumar 1  a
la variable "i" en cada iteración del bucle. Para ello, utilizamos la expresión (i + 1), que calcula
el valor de "i" más 1 y lo asigna a "x". Colocamos esta operación justo debajo del bucle "for",  con
una indentación de cuatro espacios desde el margen izquierdo. De esta forma, en cada  iteración  del
bucle, "x" contendrá el valor de "i" incrementado en 1.

A continuación, dentro del bucle "for", utilizamos la función "print()", que colocamos justo  debajo
de la operación aritmética, con una indentación de cuatro espacios desde el margen izquierdo. Dentro
de la función "print()", colocamos la variable "i" para imprimir  su  valor  en  cada  iteración  al
ejecutar el  código,  acompañada  de  una  cadena  formateada  "f-string"  que  incluye  un  mensaje
descriptivo que indica el resultado de sumar 1 a "i" y el valor de "x".

El bucle "for" comienza a iterar sobre el rango en el orden en que los elementos son  generados  por
el objeto "range", que produce números en un orden definido por sus argumentos (start, stop,  step).
En cada iteración, la variable "i" toma el valor del elemento actual del rango, le suma 1  y  guarda
el resultado en la variable "x", y el bloque de código asociado al bucle, en este caso,  la  función
"print()", se ejecuta imprimiendo el valor de (i + 1), que es "x".

Este proceso se repite hasta que se han recorrido todos los elementos del rango. El resultado es  la
impresión en consola de los números del 1 al 9, incrementados en 1, cada uno en una nueva línea.

Finalmente, hacemos que el programa imprima  el  mensaje  "Fin  del  bucle"  utilizando  la  función
"print()", que colocamos fuera del bloque de código del bucle "for" y que se ejecuta una vez que  el
bucle ha terminado de iterar sobre todos los elementos de la secuencia."""

# Código:
rango_numeros = range(1, 10)

for i in rango_numeros:
    x = (i + 1)
    print(f"El resultado de sumar 1 a {i} es {x}")

print("Fin del bucle")

# Nota Importante:
"""Es importante recordar que la variable "i" se define dentro del  bucle  y  que  su  alcance  está
limitado al bloque del bucle. En este caso, estamos trabajando con un rango de números definido  con
el constructor "range()", que genera una secuencia inmutable de números.

El bucle "for" no modifica los elementos de la secuencia sobre la que itera,  sino  que  simplemente
recorre cada uno de ellos, ya que, de otra forma, se produciría un  error  de  tipo  "TypeError"  al
intentar modificar una secuencia inmutable como el rango generado por "range()".

Si se necesita modificar una secuencia mutable, como una lista, mientras se  itera  sobre  ella,  es
recomendable  iterar  sobre  una  copia  de  la  secuencia  para  evitar   errores   inesperados   o
comportamientos no deseados. Esto se  puede  lograr  utilizando  técnicas  como  el  "slicing"  (por
ejemplo, lista[:]) o el constructor "list()" para crear una copia explícita.

Por último, es importante destacar que el bucle "for" en Python es  una  herramienta  poderosa  para
iterar sobre cualquier objeto iterable, como listas, tuplas, cadenas, diccionarios, conjuntos y más.
Además, permite realizar operaciones sobre cada uno de sus elementos de manera eficiente y  legible,
aprovechando las características del tipo de datos de la secuencia iterada."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
