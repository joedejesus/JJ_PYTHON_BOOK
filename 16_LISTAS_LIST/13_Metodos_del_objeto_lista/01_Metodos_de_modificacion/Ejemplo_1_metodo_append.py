# Enunciado:
"""El método ".append()" en Python se utiliza para agregar un elemento al final de una  lista.  Este
método modifica la lista original directamente, añadiendo el nuevo elemento como  el  último  de  la
secuencia. Es una herramienta útil para trabajar con listas  dinámicas,  ya  que  permite  construir
listas de manera incremental.

El método ".append()" puede aplicarse a cualquier objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método modifica la lista original directamente, lo que significa que  no  es  necesario
asignar el resultado de su aplicación a una nueva variable, ya que no devuelve un nuevo objeto, sino
que altera el objeto existente. Este comportamiento es consistente con la naturaleza mutable de  las
listas en Python.

El método ".append()" recibe un único argumento, que es el elemento que se desea agregar a la lista.
Este argumento  puede  ser  de  cualquier  tipo  de  dato,  incluidos  números,  cadenas,  listas  y
diccionarios, entre otros, ya sea de forma literal o almacenado en una variable. Si se desea agregar
múltiples elementos, es necesario utilizar el método varias  veces  o  emplear  otros  métodos  como
".extend()" o la concatenación de listas. Además, si el  elemento  contiene  más  de  un  valor,  se
insertará como un solo elemento al final de la lista, manteniendo su estructura original  dentro  de
ella.

Por último, el método ".append()" es una herramienta sencilla pero poderosa para  agregar  elementos
al final de las listas en Python, lo que permite una manipulación eficiente y flexible de los  datos
en este tipo de estructura."""

# Ejemplo_1_metodo_append.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de números enteros. Esta lista se
utilizará para demostrar el funcionamiento del método ".append()".

A continuación, aplicamos el método ".append()" a la variable  "lista".  Para  ello,  escribimos  el
nombre de la variable "lista", seguido del nombre del método ".append()", y dentro de los paréntesis
pasamos como argumento el elemento que deseamos agregar, en este caso, la cadena de texto  "Elemento
Agregado".

Por último, utilizamos la función "print()" para mostrar el contenido de la  lista  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método a la lista.

De esta forma, hemos agregado un elemento al final de la lista y modificado  directamente  la  lista
original mediante el método ".append()"."""

# Código:
lista = [1, 2, 3]

lista.append("Elemento Agregado")
print(f"Este es el resultado de aplicar el método a la lista: {lista}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".append()" modifica la lista original directamente,
ya que las listas en Python son mutables. Esto significa que cualquier cambio realizado en la  lista
afecta al objeto original, lo que puede ser útil  en  muchos  casos,  pero  también  puede  provocar
errores si no se maneja con cuidado.

Si se desea agregar múltiples elementos a una lista, se puede utilizar el método ".append()"  varias
veces en un bucle o emplear otros métodos como ".extend()" para agregar varios elementos de una sola
vez. Además, es importante recordar que el método ".append()" siempre agrega el  nuevo  elemento  al
final de la lista, manteniendo el orden de los elementos existentes.

Por último, el método ".append()" es una herramienta esencial para trabajar con  listas  en  Python,
pero su uso debe ir acompañado de una comprensión clara de sus características  y  limitaciones.  De
esta forma, se podrán aprovechar al máximo sus capacidades y evitar posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
