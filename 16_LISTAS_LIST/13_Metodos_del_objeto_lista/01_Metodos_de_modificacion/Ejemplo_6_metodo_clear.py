# Enunciado:
"""El método ".clear()" en Python se utiliza  para  eliminar  todos  los  elementos  de  una  lista,
dejándola vacía. Este método modifica la lista original directamente, eliminando todos los elementos
que contiene, pero manteniéndola como un objeto válido y mutable.

El método ".clear()" puede aplicarse a cualquier  objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método modifica la lista original directamente, lo que significa que  no  es  necesario
asignar el resultado de su aplicación a una nueva variable, ya que no devuelve un nuevo objeto, sino
que altera el objeto existente. Este comportamiento es consistente con la naturaleza mutable de  las
listas en Python.

El método ".clear()" no toma argumentos adicionales, ya que su propósito es  simplemente  vaciar  la
lista. Esto lo convierte en una herramienta sencilla y eficiente para reiniciar  listas,  aunque  no
necesariamente libera memoria, ya que los elementos eliminados pueden seguir  estando  referenciados
en otros lugares del programa.

Por último, el método ".clear()" es una herramienta sencilla,  pero  útil,  para  vaciar  listas  en
Python, permitiendo una manipulación eficiente de datos en estructuras de lista."""

# Ejemplo_6_metodo_clear.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista con  distintos  tipos  de  datos,
incluyendo valores booleanos, números enteros, cadenas de texto y  una  expresión  matemática.  Esta
lista se utilizará para demostrar el funcionamiento del método ".clear()".

A continuación, aplicamos el método ".clear()" a la  variable  "lista".  Para  ello,  escribimos  el
nombre de la variable "lista" seguido del nombre del método ".clear()" con los paréntesis vacíos, ya
que este método no requiere ningún argumento para funcionar.

Por último, utilizamos la función "print()" para mostrar el contenido de la  lista  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método a la lista.

De esta forma, hemos vaciado completamente la lista y modificado la lista original directamente  con
el método ".clear()"."""

# Código:
lista = [1, True, 3, "Hola", 5, False, "Adiós", (7 + 5)]

lista.clear()
print(f"Este es el resultado de aplicar el método a la lista: {lista}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".clear()" modifica la lista original  directamente,
ya que las listas en Python son mutables. Esto significa que cualquier cambio realizado en la  lista
afecta al objeto original, lo que puede ser útil en  muchos  casos,  pero  también  puede  llevar  a
errores si no se maneja con cuidado.

Es importante recordar que este método elimina todos los elementos de la lista, dejándola vacía.  Si
se desea conservar los elementos de la lista antes de vaciarla, se debe realizar  una  copia  de  la
lista antes de aplicar el método ".clear()". Esto se puede lograr utilizando el método ".copy()", el
cual crea una nueva lista con los mismos elementos, permitiendo así mantener  una  referencia  a  la
lista original antes de vaciarla.

Además, el método ".clear()" es útil en situaciones en las que se necesita reiniciar una lista  para
reutilizarla en un contexto diferente. Sin embargo, no libera memoria automáticamente,  ya  que  los
elementos eliminados pueden seguir siendo referenciados en otras partes del programa.

Por último, el método ".clear()" es una herramienta esencial para trabajar  con  listas  en  Python,
pero su uso debe ser acompañado de una comprensión clara de sus características y  limitaciones.  De
esta forma, se podrá aprovechar al máximo sus capacidades y evitar  posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────