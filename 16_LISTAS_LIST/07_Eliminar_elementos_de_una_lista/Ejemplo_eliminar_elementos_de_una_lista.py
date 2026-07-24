# Enunciado:
"""Para eliminar elementos de una lista en Python, se utilizan métodos como ".remove()", ".pop()"  y
la palabra clave "del". Estos métodos  permiten  eliminar  elementos  específicos  o  en  posiciones
determinadas de la lista mediante índices.

El índice es un número entero que identifica la posición de un elemento en una lista. Los índices en
Python para cualquier secuencia  ordenada  comienzan  desde  0.  Además,  podemos  utilizar  índices
negativos para eliminar elementos desde el final de la lista.

Las listas en Python son secuencias  ordenadas  de  elementos,  y  cada  elemento  tiene  un  índice
asociado. Son mutables, lo que significa que podemos modificar sus elementos directamente utilizando
su índice u otros métodos de modificación, y son iterables, lo que permite recorrer o acceder a cada
elemento individualmente utilizando su índice u otros métodos de iteración.

La palabra clave "del" elimina un elemento en una  posición  específica  o  un  rango  de  elementos
mediante índices. Si el índice especificado está  fuera  del  rango  de  la  lista,  se  genera  una
excepción "IndexError". Esta palabra clave es útil para eliminar múltiples elementos a  la  vez  sin
devolverlos.

Además de la palabra clave "del", los métodos  ".remove()"  y  ".pop()"  también  se  utilizan  para
eliminar elementos de una lista en Python. Sin embargo, ".remove()" elimina el primer  elemento  que
coincide con el valor especificado, mientras que ".pop()" elimina  y  devuelve  el  elemento  en  el
índice especificado.

Es importante tener en cuenta que al eliminar elementos  de  una  lista,  los  cambios  se  realizan
directamente sobre la lista original, ya que las listas son mutables. Esto  puede  afectar  a  otras
partes del programa que dependan de la lista, por lo  que  es  fundamental  asegurarse  de  que  los
cambios sean intencionales y no generen efectos secundarios no deseados.

Por último, es importante conocer las necesidades específicas  de  cada  situación  para  elegir  el
método de  eliminación  adecuado,  ya  que  cada  uno  tiene  sus  propias  características  y  usos
recomendados. Comprender cómo funcionan estos métodos es esencial para manipular  listas  de  manera
efectiva en Python."""

# Ejemplo_eliminar_elementos_de_una_lista.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de elementos [10, 20, 30, 40, 50,
60], la cual utilizaremos para eliminar uno de sus elementos mediante la palabra clave "del".

Utilizamos la función "print()" para mostrar la lista original  en  la  consola,  acompañada  de  un
mensaje descriptivo en formato "f-string" para indicar que  esta  es  la  lista  antes  de  realizar
cualquier eliminación.

A continuación, eliminamos el tercer elemento de la lista situado  en  el  índice  2  utilizando  la
palabra clave "del". Para ello, escribimos la palabra clave "del" seguida del nombre de la  variable
"lista" y después utilizamos el operador de indexación [] con el número  2  en  su  interior  "[2]",
donde el número dentro de los corchetes representa el índice del elemento que queremos eliminar,  en
este caso el número 30 que se encuentra en la posición 2 de la lista. De esta forma, hemos eliminado
el tercer elemento de la lista utilizando su índice.

Esta operación se realiza directamente sobre la lista original, sin asignar el resultado a una nueva
variable, ya que las listas en Python son mutables y la palabra clave "del" no devuelve ningún valor
que se pueda almacenar en una variable.

Por último, utilizamos la función  "print()"  para  mostrar  la  lista  modificada  en  la  consola,
acompañada de un mensaje descriptivo en formato "f-string" para indicar los cambios realizados."""

# Código:
lista = [10, 20, 30, 40, 50, 60]
print(f"Esta es la lista antes de realizar cualquier eliminación: {lista}")

del lista[2]
print(f"Esta es la lista después de eliminar el tercer elemento: {lista}")

# Nota Muy Importante:
"""En este caso, solo utilizamos la palabra clave "del" para eliminar un elemento específico  de  la
lista, pero es posible eliminar elementos utilizando los métodos ".remove()" y ".pop()".  El  método
".remove()" elimina el primer elemento que coincide con el valor especificado, mientras que ".pop()"
elimina y devuelve el elemento en el índice especificado. Estos métodos no se han incluido  en  este
ejemplo ya que se explican con detalle en la sección correspondiente a métodos del objeto lista.

Es importante tener en cuenta que al eliminar elementos  de  una  lista,  los  cambios  se  realizan
directamente sobre la lista original. Esto puede afectar a otras partes del programa que dependan de
la lista, por lo que es fundamental asegurarse de que los cambios sean intencionales  y  no  generen
efectos secundarios no deseados.

En el caso de las listas no es necesario almacenar el resultado  de  la  eliminación  en  una  nueva
variable, ya que la eliminación se  realiza  directamente  sobre  la  lista  original  debido  a  su
naturaleza mutable. Además, la palabra clave "del" no devuelve ningún valor y, por lo tanto,  no  es
necesario asignar su resultado a una variable, ya que su función principal es eliminar elementos  de
la lista sin devolverlos.

Al igual que al acceder a elementos, intentar eliminar  un  índice  fuera  del  rango  de  la  lista
generará un error de tipo "IndexError". Por lo tanto, es  recomendable  verificar  que  los  índices
utilizados estén dentro de los límites de la lista antes de realizar eliminaciones.  Esto  se  puede
lograr utilizando la función "len()" para determinar la longitud de la lista.

Por último, estas características hacen que las listas en Python sean  una  herramienta  poderosa  y
flexible para trabajar con colecciones de datos, ya que permiten tanto el acceso como la eliminación
de sus elementos de manera eficiente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
