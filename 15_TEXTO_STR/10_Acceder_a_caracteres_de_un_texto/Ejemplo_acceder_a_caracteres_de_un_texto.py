# Enunciado:
"""Para acceder a los caracteres de un texto en Python, se utiliza el índice de la cadena. El índice
es un número entero que identifica la posición de un carácter en una cadena de texto. Los índices en
Python, para cualquier secuencia ordenada, comienzan en 0. Esto significa que el primer carácter  de
una cadena de texto tiene el índice 0, el segundo carácter tiene el índice 1, y  así  sucesivamente.
Este sistema de indexación es fundamental para trabajar con secuencias en  Python,  ya  que  permite
acceder de manera directa a cualquier elemento de la secuencia mediante su posición.

Los textos en Python son secuencias  ordenadas  de  caracteres  y  cada  carácter  tiene  un  índice
asociado. Aunque los textos en Python son inmutables, también son iterables, lo  que  significa  que
podemos recorrer o acceder a cada carácter individualmente utilizando su índice, aunque no se puedan
modificar directamente.

Esto es útil para manipular o inspeccionar partes específicas de un texto,  ya  que  cada  carácter,
incluidos los espacios en blanco, tiene una posición definida dentro de la cadena. Además, el uso de
índices negativos permite acceder a los caracteres desde el final de la cadena, donde el índice "-1"
corresponde al último carácter, el índice "-2" al penúltimo, y así sucesivamente. Esta  flexibilidad
hace que el manejo de cadenas en Python sea muy potente y versátil."""

# Ejemplo_acceder_a_caracteres_de_un_texto.py

# Explicación:
"""Definimos una variable llamada "texto" y  le  asignamos  la  cadena  de  texto  "Programación  en
Python", la cual se utilizará para acceder al carácter que se encuentra en la séptima  posición  del
texto.

A continuación, definimos una variable llamada "caracter" y le asignamos el resultado de aplicar  el
operador de indexación "[]" a la variable "texto" con el índice 6. Para ello, utilizamos el operador
de indexación con el número seis en su interior, "[6]", precedido por la variable "texto", donde  el
número dentro de los corchetes representa el índice del carácter al que queremos  acceder.  De  esta
forma, obtenemos el carácter que se encuentra en la séptima  posición  del  texto  "Programación  en
Python", que es "a".

Finalmente, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", indicando que se trata del séptimo carácter del texto.

Además, accedemos a otros dos caracteres del texto de forma directa utilizando la función  "print()"
en formato "f-string" y el operador de indexación "[]" con los índices correspondientes. Para  ello,
utilizamos el operador de indexación con el número cuatro en su interior, "[4]",  precedido  por  la
variable "texto" para acceder al quinto carácter del texto, que es "r", y el operador de  indexación
con el número nueve en su interior, "[9]", precedido por la variable "texto" para acceder al  décimo
carácter del texto, que es "i".

En ambos casos, las operaciones se realizan dentro de las llaves {} de las expresiones de la  cadena
"f-string" para mostrar el resultado, acompañado de un mensaje descriptivo que indica que  se  trata
del quinto y del décimo carácter del texto, respectivamente."""

# Código:
texto = "Programación en Python"
caracter = texto[6]
print(f"Este es el séptimo carácter del texto: {caracter}")

print(f"Este es el quinto carácter del texto: {texto[4]}")
print(f"Este es el décimo carácter del texto: {texto[9]}")

# Nota Importante:
"""Es fundamental tener en cuenta que los espacios en blanco también tienen un índice,  por  lo  que
deben considerarse al calcular la posición  de  un  carácter.  Esto  significa  que  cada  carácter,
incluidos los espacios, los signos de puntuación y los caracteres especiales,  ocupan  una  posición
única dentro de la cadena. Además, es importante recordar que los índices en Python comienzan en  0,
lo que significa que el primer carácter de una cadena está en  la  posición  0,  el  segundo  en  la
posición 1, y así sucesivamente.

Python también permite el uso de índices negativos para acceder a los caracteres desde el  final  de
la cadena. Por ejemplo, el índice "-1" corresponde al último carácter, el índice "-2" al  penúltimo,
y así sucesivamente. Esto es especialmente útil cuando se necesita  acceder  a  elementos  desde  el
final sin conocer la longitud exacta de la cadena.

Por último, intentar acceder a un índice fuera del rango de la cadena  generará  un  error  de  tipo
"IndexError", por lo que es importante asegurarse de que el índice esté dentro de los límites de  la
cadena. Para evitar este error, se puede utilizar la función "len()" para determinar la longitud  de
la  cadena  y  garantizar  que  los  índices  utilizados  estén  dentro  del  rango  válido.   Estas
características hacen que el manejo de índices en Python sea una herramienta poderosa para  trabajar
con cadenas de texto de manera eficiente y segura."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
