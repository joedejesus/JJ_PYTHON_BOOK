# Enunciado:
"""Para acceder a los elementos de una lista en Python, se utiliza el índice de la lista. El  índice
es un número entero que identifica la posición de un elemento dentro de una lista.  En  Python,  los
índices de cualquier secuencia ordenada comienzan en 0. Esto significa que el primer elemento de una
lista tiene el índice 0, el segundo elemento tiene el índice 1, y así sucesivamente. Este sistema de
indexación es fundamental para trabajar con secuencias en Python, ya que permite acceder  de  manera
directa a cualquier elemento de la secuencia utilizando su posición.

Las listas en Python son secuencias  ordenadas  de  elementos,  y  cada  elemento  tiene  un  índice
asociado. Las listas son mutables, lo que significa que podemos modificar sus elementos directamente
utilizando su índice. Además, las listas son iterables, lo que permite recorrer  y  acceder  a  cada
elemento individualmente utilizando su índice u otros métodos de iteración.

Esto es útil para manipular o inspeccionar partes específicas de una lista, ya  que  cada  elemento,
incluidos los valores repetidos, tiene una posición definida dentro de la lista.

Por último, el uso de índices negativos permite acceder a los elementos desde el final de la  lista,
donde el  índice  "-1"  corresponde  al  último  elemento,  el  índice  "-2"  al  penúltimo,  y  así
sucesivamente. Esta flexibilidad hace que el manejo de listas en Python sea muy útil y versátil."""

# Ejemplo_acceder_a_elementos_de_una_lista.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de elementos [10, 20, 30, 40, 50,
60], la cual se utilizará para acceder a sus elementos mediante índices.

A continuación, definimos una variable llamada "elemento" y le asignamos el resultado de aplicar  el
operador de indexación "[]" a la variable "lista" con el índice 2. Para ello, utilizamos el operador
de indexación con el número dos en su interior, "[2]", precedido por la variable "lista",  donde  el
número dentro de los corchetes representa el índice del elemento al que queremos  acceder.  De  esta
forma, obtenemos el elemento que se encuentra en la tercera posición de la lista, que es "30".

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string", que indica que se trata del tercer elemento de la lista.

Por último, accedemos a otros dos elementos de la lista  de  forma  directa  utilizando  la  función
"print()" en formato "f-string" y el operador de indexación "[]" con los  índices  correspondientes.
Para ello, utilizamos el operador de  indexación  con  el  número  cuatro  en  su  interior,  "[4]",
precedido por la variable "lista" para acceder al quinto elemento de la lista, que  es  "50",  y  el
operador de indexación con el número menos tres en su interior, "[-3]", precedido  por  la  variable
"lista" para acceder al tercer elemento desde el final de la lista, que es "40".

En ambos casos, las operaciones se realizan dentro de las llaves {} de las expresiones de la  cadena
"f-string" para mostrar  el  resultado  sin  necesidad  de  asignarlo  a  una  variable  intermedia,
acompañado de un mensaje descriptivo que indica que se trata del quinto y del tercer elemento  desde
el final de la lista, respectivamente."""

# Código:
lista = [10, 20, 30, 40, 50, 60]

elemento = lista[2]
print(f"Este es el tercer elemento de la lista: {elemento}")

print(f"Este es el quinto elemento de la lista: {lista[4]}")
print(f"Este es el tercer elemento desde el final de la lista: {lista[-3]}")

# Nota Importante:
"""Es fundamental tener en cuenta que los índices en Python comienzan desde 0, lo que significa  que
el primer elemento de una lista está en  la  posición  0,  el  segundo  en  la  posición  1,  y  así
sucesivamente.

Python también permite el uso de índices negativos para acceder a los elementos desde el final de la
lista. Por ejemplo, el índice "-1" corresponde al último elemento, el índice "-2"  al  penúltimo,  y
así sucesivamente. Esto es especialmente útil cuando se necesita acceder a elementos desde el  final
sin conocer la longitud exacta de la lista.

Aunque las listas en Python son objetos mutables, en este ejemplo  solo  estamos  accediendo  a  los
elementos sin modificarlos, lo que proporciona una forma segura de trabajar con listas  sin  alterar
su contenido. Sin embargo,  es  importante  tener  cuidado  al  modificar  elementos  de  una  lista
utilizando índices, ya que esto puede afectar el comportamiento de otras  partes  del  programa  que
dependan de esos elementos.

Por último, intentar acceder a un índice fuera del rango de la  lista  generará  un  error  de  tipo
"IndexError", por lo que es importante asegurarse de que el índice esté dentro de sus límites.  Para
evitar este error, se puede utilizar la función "len()" para determinar la longitud de  la  lista  y
garantizar que los índices utilizados estén dentro del rango válido. Estas características hacen que
el manejo de índices en Python sea una herramienta útil para trabajar con listas de manera eficiente
y segura."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
