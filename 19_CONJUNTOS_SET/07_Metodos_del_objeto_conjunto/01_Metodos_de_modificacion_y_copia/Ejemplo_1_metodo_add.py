# Enunciado:
"""El método ".add()" en Python se utiliza para  agregar  un  elemento  a  un  conjunto  (set).  Los
conjuntos no mantienen un orden específico en sus elementos, por lo que,  al  agregar  un  elemento,
este simplemente pasa a formar parte del conjunto, sin una posición determinada ni predecible.

Este método modifica el conjunto original directamente, añadiendo  el  nuevo  elemento  si  no  está
presente, por lo que es una herramienta útil para trabajar con conjuntos dinámicos, ya  que  permite
construir conjuntos de manera incremental y garantiza que no existan elementos duplicados.

El método ".add()" puede aplicarse a cualquier objeto de tipo  set  en  Python,  ya  sean  conjuntos
literales, variables que contienen conjuntos o incluso resultados de otras operaciones  que  generan
conjuntos. Este método modifica el conjunto original, lo que significa que no es  necesario  asignar
el resultado de su aplicación a una nueva variable, ya que no devuelve un  nuevo  objeto,  sino  que
altera el objeto existente. Este comportamiento es consistente con  la  naturaleza  mutable  de  los
conjuntos en Python.

El método ".add()" toma un único argumento, que es el elemento que se  desea  agregar  al  conjunto.
Este argumento debe ser un objeto inmutable, como números, cadenas o tuplas inmutables,  ya  sea  de
forma literal o almacenado en una variable. Si se desean agregar múltiples elementos,  es  necesario
utilizar el método varias veces o emplear otros métodos como ".update()". Además, si el elemento  ya
existe en el conjunto, no se  agregará  de  nuevo,  ya  que  los  conjuntos  no  permiten  elementos
duplicados.

Por último, el método ".add()" es una herramienta sencilla pero poderosa para  agregar  elementos  a
conjuntos y permite una manipulación eficiente y flexible de datos en este tipo de estructuras."""

# Ejemplo_1_metodo_add.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".add()".

A continuación, aplicamos el método ".add()" a la variable  "conjunto".  Para  ello,  escribimos  el
nombre de la variable "conjunto", seguido del nombre del método ".add()", y dentro de los paréntesis
pasamos como argumento el elemento que deseamos agregar, en este caso, el número entero 73.

Por último, utilizamos la función "print()" para mostrar el contenido del conjunto  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método al conjunto.

De esta forma, hemos agregado un elemento al conjunto y modificado el conjunto original directamente
con el método ".add()"."""

# Código:
conjunto = {1, 2, 3}

conjunto.add(73)
print(f"Este es el resultado de aplicar el método al conjunto: {conjunto}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".add()" modifica el conjunto original directamente,
ya que los conjuntos en Python son mutables. Esto significa que cualquier  cambio  realizado  en  el
conjunto afecta al objeto original, lo que puede ser  útil  en  muchos  casos,  pero  también  puede
provocar errores si no se maneja con cuidado.

Si se desean agregar múltiples elementos a un conjunto, se puede utilizar el método ".add()"  varias
veces en un bucle o emplear otros métodos, como ".update()", para agregar varios  elementos  de  una
sola vez. Además, es importante recordar que el método ".add()" solo agrega el elemento si  no  está
presente, ya que los conjuntos no permiten elementos duplicados ni mantienen un orden específico  en
sus elementos.

Además, los elementos dentro de los conjuntos no tienen posiciones ni un orden definido, por lo que,
cuando se agrega un elemento a un conjunto, este no se coloca en una posición específica,  sino  que
simplemente se añade al conjunto. Esto significa que el elemento pasa a formar parte del conjunto, y
su representación al imprimirlo puede variar, pero esto no implica que tenga  una  posición  interna
específica.

Por último, el método ".add()" es una herramienta esencial para trabajar con  conjuntos  en  Python,
pero su uso debe ir acompañado de una comprensión clara de sus características  y  limitaciones.  De
esta forma, se podrán aprovechar al máximo sus capacidades y evitar posibles  inconvenientes  en  su
uso."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────