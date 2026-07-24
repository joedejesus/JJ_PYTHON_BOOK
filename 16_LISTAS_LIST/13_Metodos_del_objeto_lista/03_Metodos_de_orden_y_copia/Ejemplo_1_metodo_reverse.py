# Enunciado:
"""El método ".reverse()" en Python se utiliza para invertir el orden de los elementos de una lista.
Este método modifica la lista original directamente, reorganizando los elementos en el orden inverso
al que se encontraban originalmente.

El método ".reverse()" puede aplicarse a cualquier objeto de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método modifica la lista original directamente, lo que significa que  no  es  necesario
asignar el resultado de su aplicación a una nueva variable, ya que no devuelve un nuevo objeto, sino
que altera el objeto existente. Este comportamiento es consistente con la naturaleza mutable de  las
listas en Python.

El método ".reverse()" no toma argumentos adicionales, ya que su propósito es  simplemente  invertir
el orden de los elementos de la lista. Esto lo convierte en una  herramienta  sencilla  y  eficiente
para reorganizar listas sin necesidad de crear una nueva lista ni realizar  operaciones  adicionales
para lograr el mismo resultado.

Además, los elementos de la lista se reordenan de tal manera que el primer elemento se convierte  en
el último, el segundo elemento se convierte en el penúltimo y así sucesivamente, hasta que todos los
elementos hayan sido invertidos.

Por último, el método ".reverse()" es una herramienta sencilla pero útil para invertir el  orden  de
los elementos en listas en Python, lo que permite una manipulación eficiente de datos en estructuras
de lista."""

# Ejemplo_1_metodo_reverse.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una  lista  de  números  enteros  en  orden
descendente del 9 al 0. Esta  lista  se  utilizará  para  demostrar  el  funcionamiento  del  método
".reverse()".

A continuación, aplicamos el método ".reverse()" a la variable "lista".  Para  ello,  escribimos  el
nombre de la variable "lista", seguido del nombre del método ".reverse()" con los paréntesis vacíos,
ya que este método no requiere ningún argumento para funcionar.

Por último, utilizamos la función "print()" para mostrar el contenido de la  lista  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método a la lista.

De esta forma, hemos invertido completamente el orden de los elementos de la lista y  modificado  la
lista original directamente mediante el método ".reverse()"."""

# Código:
lista = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

lista.reverse()
print(f"Este es el resultado de aplicar el método a la lista: {lista}")

# Nota Importante:
"""Es  fundamental  tener  en  cuenta  que  el  método  ".reverse()"  modifica  la  lista   original
directamente, ya que las listas  en  Python  son  mutables.  Esto  significa  que  cualquier  cambio
realizado en la lista afecta al objeto original, lo que puede ser útil en muchos casos, pero también
puede dar lugar a errores si no se maneja con cuidado.

Es importante recordar que este método invierte el orden de los elementos de la lista. Si  se  desea
conservar el orden original de la lista antes de invertirla, se debe realizar una copia de la  lista
antes de aplicar el método ".reverse()". Esto se puede lograr utilizando  el  método  ".copy()",  el
cual crea una nueva lista con los mismos elementos, permitiendo así mantener  una  referencia  a  la
lista original antes de invertirla.

Además, el método ".reverse()" es útil en situaciones en las que se necesita reorganizar  una  lista
para un contexto diferente o para realizar operaciones que requieren  un  orden  específico  de  los
elementos.

Por último, el método ".reverse()" es una herramienta esencial para trabajar con listas  en  Python,
pero su uso debe ir acompañado de una comprensión clara de sus características  y  limitaciones.  De
esta forma, se podrán aprovechar al máximo sus capacidades y evitar posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
