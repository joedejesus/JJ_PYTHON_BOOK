# Enunciado:
"""El método ".pop()" en Python se utiliza para eliminar y devolver el valor asociado  a  una  clave
específica dentro de un diccionario. Este método  modifica  el  diccionario  original  directamente,
eliminando la clave indicada junto con su valor y devolviendo dicho valor como resultado. Si  no  se
proporciona un valor por defecto y la clave no existe, se genera un error de tipo "KeyError".

El método ".pop()"  puede  aplicarse  a  cualquier  objeto  de  tipo  diccionario  en  Python,  como
diccionarios  literales,  variables  que  contienen  diccionarios  o  incluso  resultados  de  otras
operaciones que generan diccionarios.

Este método modifica el diccionario original directamente, lo que  significa  que  no  es  necesario
asignar el resultado de la aplicación del método a una nueva  variable,  ya  que  altera  el  objeto
existente. Sin embargo, este comportamiento mutable implica que, si  se  desea  almacenar  el  valor
eliminado y devuelto, se puede asignar el resultado de la aplicación del método a una nueva variable
para su uso posterior.  Este  comportamiento  es  consistente  con  la  naturaleza  mutable  de  los
diccionarios en Python.

El método ".pop()" toma un argumento obligatorio, que es la  clave  que  se  desea  eliminar,  y  un
argumento opcional, que es el valor por defecto que se devolverá si la clave no  existe.  Si  no  se
proporciona este valor por defecto y la clave no está presente en el  diccionario,  se  generará  un
error de tipo "KeyError".

Además, la clave puede pasarse al método en forma de valor literal, como una cadena o un  número,  o
como una variable que contenga  la  clave  que  se  desea  eliminar,  pero  siempre  debe  coincidir
exactamente con una clave válida presente en el diccionario.

Por último, el método ".pop()" es una herramienta sencilla pero poderosa  para  eliminar  y  obtener
valores de diccionarios en Python, permitiendo una manipulación eficiente y flexible de los datos en
estructuras de tipo diccionario."""

# Ejemplo_1_metodo_pop.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con  varias  claves  y
valores. Este diccionario se utilizará para demostrar el funcionamiento del método ".pop()".

A continuación, definimos una variable llamada "valor_eliminado" y  le  asignamos  el  resultado  de
aplicar el método ".pop()" a la variable "diccionario".  Para  ello,  escribimos  el  nombre  de  la
variable "diccionario", seguido del nombre del método ".pop()" y, dentro de los paréntesis,  pasamos
como argumento la clave que deseamos eliminar; en este caso, la clave "b".

Por último, utilizamos la función "print()" para mostrar el contenido del diccionario en la consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método al diccionario.  Además,  también  mostramos  el  valor  eliminado  y  devuelto
utilizando de nuevo la función "print()", acompañada de un mensaje descriptivo en formato "f-string"
para indicar que se trata del valor eliminado del diccionario.

De esta forma, hemos eliminado y almacenado en una variable un  valor  específico  del  diccionario,
modificando directamente el diccionario original con el método ".pop()"."""

# Código:
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

valor_eliminado = diccionario.pop("b")
print(f"Este es el resultado de aplicar el método al diccionario: {diccionario}")
print(f"Este es el valor eliminado del diccionario: {valor_eliminado}")

# Nota Importante:
"""Es fundamental  tener  en  cuenta  que  el  método  ".pop()"  modifica  el  diccionario  original
directamente, ya que los diccionarios en Python son mutables. Esto significa  que  cualquier  cambio
realizado en el diccionario afecta al objeto original, lo que puede ser útil en muchos  casos,  pero
también puede provocar errores si no se maneja con cuidado.

Es importante recordar que este método elimina y devuelve el valor asociado a la clave especificada.
Si no se proporciona un valor por defecto y la clave  no  existe,  se  generará  un  error  de  tipo
"KeyError". Si se desea evitar este error, se puede proporcionar un valor alternativo  como  segundo
argumento del método.

Además, si se desea eliminar varias claves de un diccionario, se puede utilizar un bucle para iterar
sobre las claves y aplicar el método ".pop()" repetidamente, según sea necesario.  Sin  embargo,  es
importante tener en cuenta que modificar un diccionario mientras se itera sobre  él  puede  producir
resultados inesperados, por lo que se recomienda trabajar con una copia  del  diccionario  en  estos
casos.

Por otro lado, en cuanto a los objetos mutables, como los diccionarios, es crucial entender  que  no
es necesario asignar el resultado de la aplicación de un método que modifica el  diccionario  a  una
nueva variable, ya que el método modifica el diccionario original directamente. Sin embargo,  si  el
método aplicado devuelve un valor y se desea almacenarlo, entonces es necesario asignar el resultado
a una nueva variable, la cual contendrá el valor devuelto por el método.

Por último, el método ".pop()" es una herramienta esencial para trabajar con diccionarios en Python,
pero su uso debe ir acompañado de una comprensión clara de sus características  y  limitaciones.  De
esta forma, se podrán aprovechar al máximo sus capacidades y evitar posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────