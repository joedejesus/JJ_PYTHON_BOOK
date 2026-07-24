# Enunciado:
"""El método ".popitem()" en Python se utiliza para eliminar y devolver el  último  par  clave-valor
insertado en un diccionario. Este método modifica el diccionario original directamente,  elimina  el
par más reciente según el orden de inserción y lo devuelve como una tupla formada por la clave y  su
valor asociado.

El método ".popitem()" puede aplicarse a cualquier  objeto  de  tipo  diccionario  en  Python,  como
diccionarios  literales,  variables  que  contienen  diccionarios  o  incluso  resultados  de  otras
operaciones que generan diccionarios.

Este método modifica el diccionario original directamente, lo que  significa  que  no  es  necesario
asignar el resultado de la aplicación del método a una nueva  variable,  ya  que  altera  el  objeto
existente. Sin embargo, este comportamiento mutable implica  que,  si  se  desea  almacenar  el  par
eliminado y devuelto, se puede asignar el resultado de la aplicación del método a una nueva variable
para su uso posterior.  Este  comportamiento  es  consistente  con  la  naturaleza  mutable  de  los
diccionarios en Python.

El método ".popitem()" no toma  argumentos.  Su  función  es  eliminar  el  último  par  clave-valor
insertado en el diccionario. Si el diccionario está vacío, genera un error del tipo "KeyError",  por
lo que es recomendable verificar si el diccionario contiene elementos antes de utilizar este  método
o manejar la excepción en caso de que ocurra.

Por último, el método ".popitem()" es una herramienta sencilla pero poderosa para eliminar y obtener
pares clave-valor de diccionarios en Python, permitiendo una manipulación eficiente  y  flexible  de
datos en estructuras de tipo diccionario."""

# Ejemplo_2_metodo_popitem.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con  varias  claves  y
valores. Este diccionario se utilizará para demostrar el funcionamiento del método ".popitem()".

A continuación, definimos una variable llamada  "par_eliminado"  y  le  asignamos  el  resultado  de
aplicar el método ".popitem()" a la variable "diccionario". Para ello, escribimos el  nombre  de  la
variable "diccionario" seguido del nombre del método ".popitem()", con los paréntesis vacíos, ya que
este método no requiere argumentos para funcionar.

Por último, utilizamos la función "print()" para mostrar el contenido del diccionario en la  consola
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método  al  diccionario.  Además,  también  mostramos  el  par  eliminado  y  devuelto
utilizando de nuevo la función "print()", acompañada de un mensaje descriptivo en formato "f-string"
para indicar que se trata del par clave-valor eliminado del diccionario.

De esta forma, hemos eliminado y almacenado en una variable el último par clave-valor  insertado  en
el diccionario, modificando el diccionario original directamente con el método ".popitem()"."""

# Código:
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

par_eliminado = diccionario.popitem()
print(f"Este es el resultado de aplicar el método al diccionario: {diccionario}")
print(f"Este es el par clave-valor eliminado del diccionario: {par_eliminado}")

# Nota Importante:
"""Es fundamental tener en cuenta que  el  método  ".popitem()"  modifica  el  diccionario  original
directamente, ya que los diccionarios en Python son mutables. Esto significa  que  cualquier  cambio
realizado en el diccionario afecta al objeto original, lo que puede ser útil en muchos  casos,  pero
también puede llevar a errores si no se maneja con cuidado.

Este método elimina y devuelve el  último  par  clave-valor  insertado  en  el  diccionario.  Si  el
diccionario está vacío, se generará un error "KeyError". Por lo tanto, es recomendable verificar  si
el  diccionario  contiene  elementos  antes  de  utilizar  este  método  o  manejar   la   excepción
adecuadamente.

Además, si se desea eliminar varios pares clave-valor, se puede utilizar un bucle  para  aplicar  el
método ".popitem()" repetidamente, según sea necesario. Sin embargo, es importante tener  en  cuenta
que modificar un diccionario mientras se itera sobre él puede llevar a resultados  inesperados,  por
lo que se recomienda trabajar con una copia del diccionario en estos casos.

Por otro lado, en cuanto a los objetos mutables, como los diccionarios, es crucial entender  que  no
es necesario asignar el resultado de la aplicación de un método que modifica el  diccionario  a  una
nueva variable, ya que el método modifica el diccionario original directamente. Sin embargo,  si  el
método aplicado devuelve un valor y si este se desea almacenar, entonces  es  necesario  asignar  el
resultado a una nueva variable, la cual contendrá el valor devuelto por el método.

Por último, el método ".popitem()" es una herramienta esencial para  trabajar  con  diccionarios  en
Python, especialmente cuando se necesita eliminar el último par clave-valor insertado, pero  su  uso
debe ir acompañado de una comprensión clara de sus características y limitaciones."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────