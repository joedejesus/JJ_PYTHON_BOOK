# Enunciado:
"""El método ".pop()" en Python se utiliza para eliminar y devolver un elemento de una lista en  una
posición específica. Este método modifica la lista original  directamente,  eliminando  el  elemento
especificado y devolviéndolo como resultado. Si no se proporciona un índice como argumento,  elimina
y devuelve el último elemento de la lista.

El método ".pop()" puede aplicarse  a  cualquier  objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método modifica la lista original directamente, lo que significa que  no  es  necesario
asignar el resultado de su aplicación a una nueva variable, ya que altera el objeto  existente.  Sin
embargo, este comportamiento mutable implica que, si se desea  almacenar  el  elemento  eliminado  y
devuelto, se puede asignar el resultado del método a una nueva variable para su uso posterior.  Este
comportamiento es consistente con la naturaleza mutable de las listas en Python.

El método ".pop()" toma un único argumento opcional, que es el índice  del  elemento  que  se  desea
eliminar y devolver de la lista. Si no se proporciona un índice, se elimina  y  devuelve  el  último
elemento de la lista. Si el índice está fuera del rango de la lista, se  genera  un  error  de  tipo
"IndexError". Por lo tanto, es recomendable verificar el rango del índice antes de intentar eliminar
un elemento o manejar la excepción en caso de que ocurra.

Este argumento puede pasarse al método en forma de un valor  literal,  como  un  número  entero  que
representa el índice del elemento a eliminar, o como una variable que contiene el índice a eliminar,
pero el índice siempre debe ser un número entero válido dentro del rango de la lista.

Por último, el método ".pop()" es una herramienta sencilla, pero poderosa, para eliminar  y  obtener
elementos de listas en Python, permitiendo  una  manipulación  eficiente  y  flexible  de  datos  en
estructuras de lista."""

# Ejemplo_5_metodo_pop.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de números enteros. Esta lista se
utilizará para demostrar el funcionamiento del método ".pop()".

A continuación, definimos una variable llamada "elemento_eliminado" y le asignamos el  resultado  de
aplicar el método ".pop()" a la variable "lista". Para ello, escribimos el  nombre  de  la  variable
"lista" seguido del nombre del método ".pop()", y dentro de los paréntesis, pasamos  como  argumento
el índice del elemento que deseamos eliminar; en este caso, el índice 1, que corresponde al número 2
en la lista.

Por último, utilizamos la función "print()" para mostrar el contenido de  la  lista  en  la  consola
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método a la  lista.  Además,  también  mostramos  el  elemento  eliminado  y  devuelto
utilizando de nuevo la función "print()" acompañada de un mensaje descriptivo en formato  "f-string"
para indicar que se trata del elemento eliminado y devuelto de la lista.

De esta forma, hemos eliminado y almacenado en una variable un  elemento  específico  de  la  lista,
modificando la lista original directamente con el método ".pop()"."""

# Código:
lista = [1, 2, 3, 4, 5]

elemento_eliminado = lista.pop(1)
print(f"Este es el resultado de aplicar el método a la lista: {lista}")
print(f"Este es el elemento eliminado de la lista: {elemento_eliminado}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".pop()" modifica la lista original directamente, ya
que las listas en Python son mutables. Esto significa que cualquier cambio  realizado  en  la  lista
afecta al objeto original, lo que puede ser útil en  muchos  casos,  pero  también  puede  llevar  a
errores si no se maneja con cuidado.

Es importante recordar que este método elimina y devuelve el elemento en la  posición  especificada.
Si no se proporciona un índice, se elimina y devuelve el último elemento de la lista.  Si  se  desea
eliminar un elemento sin devolverlo, se puede utilizar el método ".remove()".

Además, si se desea eliminar varios elementos de una  lista,  se  puede  utilizar  un  bucle  o  una
comprensión de lista para iterar sobre los índices  y  aplicar  el  método  ".pop()"  o  ".remove()"
repetidamente, dependiendo de la necesidad. Sin embargo, es importante tener en cuenta que modificar
una lista mientras se itera sobre ella  puede  llevar  a  resultados  inesperados,  por  lo  que  se
recomienda trabajar con una copia de la lista en estos casos.

Por otro lado, en cuanto a los objetos mutables como las listas,  es  crucial  entender  que  no  es
necesario asignar el resultado de la aplicación de un método que  modifica  la  lista  a  una  nueva
variable, ya que el método modifica la lista  original  directamente.  Sin  embargo,  si  el  método
aplicado devuelve un valor y si este se desea almacenar, entonces es necesario asignar el  resultado
a una nueva variable, la cual contendrá el valor devuelto por el método.

En el caso de intentar asignar a una variable el resultado de aplicar un método que no  devuelve  un
valor a un objeto mutable, el resultado será "None", lo que indica que el método no devuelve  ningún
valor. Es importante comprender qué métodos devuelven valores y cuáles no, para evitar errores en la
manipulación de listas y otros objetos mutables en Python.

Por último, el método ".pop()" es una herramienta esencial para trabajar con listas en Python,  pero
su uso debe ser acompañado de una comprensión clara de sus características y limitaciones.  De  esta
forma, se podrá aprovechar al  máximo  sus  capacidades  y  evitar  posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
