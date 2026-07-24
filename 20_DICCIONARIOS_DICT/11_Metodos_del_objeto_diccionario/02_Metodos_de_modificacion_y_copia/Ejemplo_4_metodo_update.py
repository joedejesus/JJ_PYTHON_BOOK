# Enunciado:
"""El método ".update()" en Python se utiliza para modificar un diccionario añadiendo  nuevos  pares
clave-valor o actualizando los valores de claves existentes. Este  método  modifica  el  diccionario
original directamente, incorporando los cambios proporcionados a través de otro diccionario,  de  un
iterable de pares clave-valor o de argumentos con nombre.

Este método puede aplicarse a cualquier objeto de tipo  diccionario  en  Python,  como  diccionarios
literales, variables que contienen diccionarios  o  incluso  resultados  de  otras  operaciones  que
generan diccionarios. Este método modifica el diccionario original directamente,  lo  que  significa
que no es necesario asignar el resultado de la aplicación del método a una nueva  variable,  ya  que
altera el objeto existente. Este comportamiento es consistente con  la  naturaleza  mutable  de  los
diccionarios en Python.

El método ".update()" toma un único argumento opcional, que puede ser otro diccionario, un  iterable
de pares clave-valor o una serie de argumentos con nombre. Si una clave ya existe en el diccionario,
su valor será reemplazado por el nuevo valor proporcionado. Si la clave no existe, será  añadida  al
diccionario.

Además, este argumento puede pasarse en forma de diccionario literal, de una variable  que  contenga
un diccionario, de una lista de tuplas o incluso como argumentos con nombre utilizando  la  sintaxis
"clave=valor".

Por último, el método ".update()" es una herramienta poderosa y flexible para modificar diccionarios
en Python, ya que permite añadir o actualizar información de manera eficiente y controlada."""

# Ejemplo_4_metodo_update.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con  varias  claves  y
valores. Este diccionario se utilizará para demostrar el funcionamiento del método ".update()".

A continuación, aplicamos el método ".update()" a la variable "diccionario". Para  ello,  escribimos
el nombre de la variable seguido del método ".update()", y  dentro  de  los  paréntesis  pasamos  un
diccionario literal que contiene las claves y los valores que deseamos añadir o actualizar; en  este
caso, {"b": 20, "e": 5}.

Por último, utilizamos la función "print()" para mostrar el contenido del diccionario en la consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método al diccionario.

De esta forma, actualizamos el valor de la clave "b" y añadimos una nueva clave "e", modificando  el
diccionario original directamente con el método ".update()"."""

# Código:
diccionario = {"a": 1, "b": 2, "c": 3}

diccionario.update({"b": 20, "e": 5})
print(f"Este es el resultado de aplicar el método al diccionario: {diccionario}")

# Nota Importante:
"""Es fundamental tener en cuenta  que  el  método  ".update()"  modifica  el  diccionario  original
directamente, ya que los diccionarios en Python son mutables. Esto significa  que  cualquier  cambio
realizado en el diccionario afecta al objeto original, lo que puede ser útil en muchos  casos,  pero
también puede provocar errores si no se maneja con cuidado.

El método ".update()" es ideal para fusionar diccionarios, añadir nuevas claves o actualizar valores
existentes. También permite utilizar listas de tuplas o argumentos con nombre, lo que  lo  convierte
en una herramienta muy flexible.

Además, si se desea realizar una actualización  sin  modificar  el  diccionario  original,  se  debe
trabajar con una copia del diccionario utilizando el método ".copy()" antes  de  aplicar  el  método
".update()".

Por último, el método ".update()" es una herramienta esencial  para  trabajar  con  diccionarios  en
Python, ya que permite añadir o modificar información de manera clara, eficiente y controlada."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────