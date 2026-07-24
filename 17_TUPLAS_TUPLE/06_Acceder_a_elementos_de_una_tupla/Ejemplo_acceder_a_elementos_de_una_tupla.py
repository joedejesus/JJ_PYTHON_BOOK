# Enunciado:
"""Para acceder a los elementos de una tupla en Python, se utiliza el índice de la tupla. El  índice
es un número entero que identifica la posición de un elemento en una tupla. Los índices  en  Python,
para cualquier secuencia ordenada, comienzan desde 0. Esto significa que el primer elemento  de  una
tupla tiene el índice 0, el segundo elemento tiene el índice 1 y así sucesivamente. Este sistema  de
indexación es fundamental para trabajar con secuencias en Python, ya que permite acceder  de  manera
directa a cualquier elemento de la secuencia utilizando su posición.

Las tuplas en Python son secuencias ordenadas de elementos y cada elemento tiene un índice asociado.
Las tuplas son inmutables, lo que significa que no podemos modificar sus elementos directamente  una
vez que han sido creadas. Además, las tuplas son iterables, lo que permite recorrer o acceder a cada
elemento individualmente utilizando su índice u otros métodos de iteración.

Esto es útil para inspeccionar partes específicas de una tupla, ya que cada elemento, incluidos  los
valores repetidos, tiene una posición definida dentro  de  la  tupla.  Además,  el  uso  de  índices
negativos permite acceder a los elementos  desde  el  final  de  la  tupla,  donde  el  índice  "-1"
corresponde al último elemento, el índice "-2" al penúltimo y así sucesivamente.  Esta  flexibilidad
hace que el manejo de tuplas en Python sea muy poderoso y versátil."""

# Ejemplo_acceder_a_elementos_de_una_tupla.py

# Explicación:
"""Definimos una variable llamada "tupla" y le asignamos una tupla de elementos (10, 20, 30, 40, 50,
60), la cual será utilizada para acceder a sus elementos mediante índices.

A continuación, definimos una variable llamada "elemento" y le asignamos el resultado de aplicar  el
operador de indexación "[]" a la variable "tupla" con el rango de índices 2:5. Para ello, utilizamos
la expresión "tupla[2:5]", donde los números dentro de los corchetes representan el rango de índices
de los elementos a los que queremos acceder.

De esta forma, obtenemos los elementos que se encuentran en la tercera, cuarta y quinta posición  de
la tupla, que son "30", "40" y "50", correspondientes a los  índices  2,  3  y  4,  respectivamente,
excluyendo el elemento ubicado en el índice 5.

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje  descriptivo  en  formato  "f-string",  indicando  que  se  trata  del  rango  de  elementos
correspondientes a los índices 2, 3 y 4 de la tupla.

Por último, accedemos a otros dos elementos de la tupla  de  forma  directa  utilizando  la  función
"print()" en formato "f-string" y el operador de indexación "[]" con los  índices  correspondientes.
Para ello, utilizamos el operador de  indexación  con  el  número  cuatro  en  su  interior,  "[4]",
precedido de la variable "tupla" para acceder al quinto elemento de la tupla,  que  es  "50",  y  el
operador de indexación con el número menos tres en su interior, "[-3]",  precedido  de  la  variable
"tupla" para acceder al tercer elemento contado desde el final de la tupla, que es "40".

En ambos casos, las operaciones se realizan dentro de las llaves {} de las expresiones de la  cadena
"f-string" para mostrar  el  resultado  sin  necesidad  de  asignarlo  a  una  variable  intermedia,
acompañado de un mensaje descriptivo que indica que se  trata  del  quinto  elemento  y  del  tercer
elemento desde el final de la tupla, respectivamente."""

# Código:
tupla = (10, 20, 30, 40, 50, 60)

elemento = tupla[2:5]
print(f"Este es el rango de elementos correspondientes a los índices 2, 3 y 4 de la tupla: {elemento}")

print(f"Este es el quinto elemento de la tupla: {tupla[4]}")
print(f"Este es el tercer elemento desde el final de la tupla: {tupla[-3]}")

# Nota Importante:
"""Es fundamental tener en cuenta que los índices en Python comienzan desde 0, lo que significa  que
el primer elemento de una tupla está  en  la  posición  0,  el  segundo  en  la  posición  1  y  así
sucesivamente.

Python también permite el uso de índices negativos para acceder a los elementos desde el final de la
tupla. Por ejemplo, el índice "-1" corresponde al último elemento, el índice "-2" al penúltimo y así
sucesivamente. Esto es especialmente útil cuando se necesita acceder a elementos desde el final  sin
conocer la longitud exacta de la tupla.

Dado que las tuplas en Python son objetos inmutables, en este ejemplo solo estamos accediendo a  los
elementos sin modificarlos, lo que proporciona una forma segura  de  trabajar  con  las  tuplas  sin
alterar su contenido. Sin embargo, es importante tener presente que su inmutabilidad  significa  que
no pueden ser modificadas directamente una vez creadas.

Por último, intentar acceder a un índice fuera del rango de la  tupla  generará  un  error  de  tipo
"IndexError", por lo que es importante asegurarse de que el índice esté dentro de los límites de  la
tupla. Para evitar este error, se puede utilizar la función "len()" para determinar la  longitud  de
la  tupla  y  garantizar  que  los  índices  utilizados  estén  dentro  del  rango   válido.   Estas
características hacen que el manejo de índices en Python sea una herramienta poderosa para  trabajar
con tuplas de manera eficiente y segura."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────