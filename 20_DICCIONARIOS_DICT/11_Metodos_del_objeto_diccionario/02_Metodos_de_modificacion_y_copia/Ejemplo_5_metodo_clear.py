# Enunciado:
"""El método ".clear()" en Python se utiliza para eliminar todos los elementos  de  un  diccionario,
dejándolo vacío. Este método modifica el diccionario original  directamente,  eliminando  todos  los
pares clave-valor y sin devolver ningún valor. Después de aplicar este método, el diccionario  queda
completamente vacío, pero sigue existiendo como objeto.

El método ".clear()" puede aplicarse  a  cualquier  objeto  de  tipo  diccionario  en  Python,  como
diccionarios  literales,  variables  que  contienen  diccionarios  o  incluso  resultados  de  otras
operaciones que generan diccionarios.

Este método modifica el diccionario original directamente, lo que  significa  que  no  es  necesario
asignar el resultado de la aplicación del método a una nueva variable, ya  que  modifica  el  objeto
existente. Este comportamiento es consistente con la  naturaleza  mutable  de  los  diccionarios  en
Python.

El método ".clear()" no toma argumentos, ya que su función es simplemente vaciar el diccionario  por
completo. Si se desea conservar los datos antes de vaciar el diccionario, es  recomendable  realizar
una copia utilizando el método ".copy()" antes de aplicar el método ".clear()".

Por último, el método ".clear()" es una herramienta sencilla pero efectiva para eliminar  todos  los
elementos de un diccionario en Python,  permitiendo  reiniciar  su  contenido  de  manera  rápida  y
controlada."""

# Ejemplo_5_metodo_clear.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con  varias  claves  y
valores. Este diccionario se utilizará para demostrar el funcionamiento del método ".clear()".

A continuación, aplicamos el método ".clear()" a la variable "diccionario". Para ello, escribimos el
nombre de la variable seguido del nombre del método ".clear()", con los paréntesis  vacíos,  ya  que
este método no requiere argumentos para su funcionamiento.

Por último, utilizamos la función "print()" para mostrar el contenido del diccionario en la consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método al diccionario.

De esta forma, hemos eliminado todos los  elementos  del  diccionario,  modificando  el  diccionario
original directamente con el método ".clear()" y dejándolo vacío como un objeto que sigue existiendo
y puede volver a utilizarse añadiendo nuevos pares clave-valor según sea necesario."""

# Código:
diccionario = {"a": 1, "b": 2, "c": 3}

diccionario.clear()
print(f"Este es el resultado de aplicar el método al diccionario: {diccionario}")

# Nota Importante:
"""Es fundamental tener en  cuenta  que  el  método  ".clear()"  modifica  el  diccionario  original
directamente, ya que los diccionarios en Python son mutables. Esto significa  que  cualquier  cambio
realizado en el diccionario afecta al objeto original, lo que puede ser útil en muchos  casos,  pero
también puede llevar a errores si no se maneja con cuidado.

El método ".clear()" es ideal para vaciar completamente un diccionario cuando se desea reiniciar  su
contenido o eliminar todos los datos almacenados. Sin embargo, si se desea conservar  los  elementos
antes de vaciarlo, se debe realizar una copia utilizando el método ".copy()"  antes  de  aplicar  el
método ".clear()".

Por último, es importante recordar que este método elimina todos los elementos del diccionario, pero
no el diccionario en sí. El objeto sigue existiendo y puede volver  a  utilizarse  añadiendo  nuevos
pares clave-valor según sea necesario."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────