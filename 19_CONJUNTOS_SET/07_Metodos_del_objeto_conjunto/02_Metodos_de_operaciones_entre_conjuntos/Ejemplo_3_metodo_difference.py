# Enunciado:
"""El método ".difference()" en Python se utiliza para obtener un nuevo conjunto  que  contiene  los
elementos que están presentes en el  conjunto  original,  pero  no  en  los  conjuntos  o  iterables
proporcionados como argumentos, cuyos elementos  se  excluyen  del  resultado  de  la  operación  de
diferencia. Los conjuntos no mantienen un orden específico en sus elementos, por lo que el resultado
de la diferencia será un nuevo conjunto con los elementos obtenidos, sin una posición determinada ni
predecible.

El método ".difference()" puede aplicarse a cualquier objeto de tipo (set) en Python, como conjuntos
literales, variables que contienen conjuntos o incluso resultados de otras operaciones  que  generan
conjuntos. Este método no modifica el conjunto original y devuelve un nuevo  conjunto  que  contiene
los elementos que están presentes en el conjunto original, pero no  en  los  conjuntos  o  iterables
proporcionados como argumentos los cuales se excluyen del resultado de la operación  de  diferencia.
Este nuevo conjunto se almacena en la variable asignada al resultado de la aplicación del método.

El método ".difference()" toma uno o varios argumentos: los conjuntos o iterables cuyos elementos se
desean excluir del resultado de la operación de diferencia. Si no  se  proporcionan  argumentos,  el
método devuelve una copia del conjunto original, ya que no hay elementos que excluir.

Estos argumentos deben ser objetos iterables, lo que significa que  pueden  ser  cualquier  tipo  de
objeto que se pueda recorrer, como listas, tuplas, conjuntos,  diccionarios  o  incluso  cadenas  de
texto, siempre y cuando sus elementos sean inmutables. En el caso de  los  diccionarios,  el  método
toma sus claves como referencia, no sus valores; y, en el caso de las cadenas  de  texto,  toma  sus
caracteres como elementos individuales para calcular la diferencia.

Sin embargo, estos argumentos no pueden ser valores individuales que  no  sean  iterables,  como  un
número entero o decimal, ya que el método ".difference()" espera recibir uno o varios iterables.

Además, si algún elemento aparece repetido en cualquiera de los conjuntos o  iterables  involucrados
en la operación de diferencia, este no se duplicará en el resultado final, ya que los  conjuntos  no
permiten elementos duplicados. Esto significa que el resultado de la diferencia será un conjunto con
elementos únicos.

Por último, el método ".difference()" es una herramienta eficiente para calcular la diferencia entre
conjuntos, permitiendo una manipulación directa y flexible de datos en estructuras de tipo (set) sin
alterar el conjunto original."""

# Ejemplo_3_metodo_difference.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".difference()".

A continuación, definimos una nueva variable llamada "nuevo_conjunto" y le asignamos el resultado de
aplicar el método ".difference()" a la variable "conjunto". Para ello, escribimos el  nombre  de  la
variable "conjunto", seguido del nombre del método ".difference()"  y,  dentro  de  los  paréntesis,
pasamos como argumentos los iterables cuyos elementos deseamos excluir del resultado de la operación
de diferencia, separados por comas; en este caso, un conjunto literal de números enteros, una  lista
literal de números enteros y una tupla literal de números enteros.

Por último, utilizamos la función "print()" para mostrar el contenido del nuevo conjunto  resultante
en la consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que se  trata
del resultado de aplicar el método al conjunto original.

De esta forma, hemos obtenido un nuevo conjunto que contiene los elementos que están presentes en el
conjunto original, sin modificarlo y excluyendo los elementos que se  encuentran  en  los  iterables
proporcionados  como  argumentos,  los  cuales  se  excluyen  del  resultado  de  la  operación   de
diferencia."""

# Código:
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

nuevo_conjunto = conjunto.difference({2, 4}, [6, 8], (10, 12))
print(f"Este es el resultado de aplicar el método al conjunto original: {nuevo_conjunto}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".difference()" no modifica  el  conjunto  original,
sino que devuelve un nuevo conjunto con los elementos que están presentes en el  conjunto  original,
pero no en los conjuntos o iterables proporcionados como argumentos, cuyos elementos se excluyen del
resultado. Esto significa que el conjunto original permanece sin cambios, lo que puede ser  útil  en
muchos casos, pero también puede provocar errores si no se maneja con cuidado.

Es importante aclarar que este método toma uno o varios argumentos: los conjuntos o iterables  cuyos
elementos se desean excluir del conjunto original, y devuelve un nuevo conjunto  con  los  elementos
que están presentes en el conjunto original, pero no en los  conjuntos  o  iterables  proporcionados
como argumentos, cuyos elementos se excluyen del resultado.

La diferencia entre el método ".difference()" y el método ".difference_update()" radica  en  que  el
primero devuelve un nuevo conjunto con la diferencia, sin alterar el conjunto original, mientras que
el segundo modifica el conjunto original directamente.

En este caso, hablamos de excluir y no de eliminar, porque el método ".difference()" no elimina  los
elementos del conjunto original, sino que los excluye del resultado de la operación  de  diferencia,
lo que significa que el conjunto original no se ve afectado por la operación.

El método ".difference()" es una opción eficiente si se desea calcular la diferencia entre conjuntos
sin alterar el conjunto original. Además, es importante recordar que el método ".difference()" opera
sobre elementos únicos, ya que los conjuntos no admiten elementos duplicados.

Por último, el método ".difference()" es una herramienta esencial para  trabajar  con  conjuntos  en
Python, pero su uso debe estar  acompañado  de  una  comprensión  clara  de  sus  características  y
limitaciones. Esto permitirá aprovechar al máximo sus capacidades y evitar  posibles  inconvenientes
en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ───────────────────────────────────────────────────────────