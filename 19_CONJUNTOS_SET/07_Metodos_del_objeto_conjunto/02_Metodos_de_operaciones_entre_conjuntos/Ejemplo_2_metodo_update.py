# Enunciado:
"""El método ".update()" en Python se utiliza para añadir al conjunto original todos  los  elementos
presentes en los conjuntos o iterables proporcionados como argumentos. Los conjuntos no mantienen un
orden específico en sus elementos, por  lo  que  el  conjunto  resultante  contendrá  los  elementos
añadidos sin una posición determinada ni predecible.

Este método modifica el conjunto original directamente, incorporando los elementos que se encuentran
en los conjuntos o iterables proporcionados como argumentos, por lo que es una herramienta útil para
trabajar con conjuntos dinámicos, ya que permite actualizarlos  de  manera  directa  y  mantiene  la
propiedad de contener elementos únicos.

El método ".update()" puede aplicarse a cualquier objeto de tipo (set)  en  Python,  como  conjuntos
literales, variables que contienen conjuntos o incluso resultados de otras operaciones  que  generan
conjuntos. Este método modifica el conjunto original, lo que significa que no es  necesario  asignar
el resultado de la aplicación del método a una nueva variable, ya que no devuelve un  nuevo  objeto,
sino que altera el objeto existente. Este comportamiento es consistente con la naturaleza mutable de
los conjuntos en Python.

El método ".update()" toma uno o varios argumentos: los conjuntos o  iterables  cuyos  elementos  se
desean añadir al conjunto original. Si no se proporcionan  argumentos,  el  método  no  modifica  el
conjunto original, ya que no hay elementos que añadir.

Estos argumentos deben ser objetos iterables, lo que significa que  pueden  ser  cualquier  tipo  de
objeto que se pueda recorrer, como listas, tuplas, conjuntos,  diccionarios  o  incluso  cadenas  de
texto, siempre y cuando sus elementos sean inmutables. En el caso de  los  diccionarios,  el  método
toma sus claves como referencia, no sus valores; y en el caso de las  cadenas  de  texto,  toma  sus
caracteres como elementos individuales para realizar la operación.

Sin embargo, estos argumentos no pueden ser valores individuales que  no  sean  iterables,  como  un
número entero o decimal, ya que el método ".update()" espera recibir uno o varios objetos iterables.

Además, si algún elemento aparece repetido en cualquiera de los conjuntos o  iterables  involucrados
en la operación de actualización, este no se duplicará en el resultado final, ya que  los  conjuntos
no permiten elementos duplicados. Esto significa que el  conjunto  actualizado  seguirá  conteniendo
elementos únicos.

Por último, el método ".update()" es una herramienta eficiente para añadir elementos a un  conjunto,
ya que permite una manipulación directa y flexible de datos en estructuras de tipo (set),  alterando
el conjunto original."""

# Ejemplo_2_metodo_update.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".update()".

A continuación, aplicamos el método ".update()" a la variable "conjunto". Para ello,  escribimos  el
nombre de la variable "conjunto", seguido del  nombre  del  método  ".update()"  y,  dentro  de  los
paréntesis, pasamos como argumentos los  iterables  cuyos  elementos  deseamos  añadir  al  conjunto
original, separados por comas; en este caso, un conjunto  literal  de  números  enteros,  una  lista
literal de números enteros y una tupla literal de números enteros.

Por último, utilizamos la función "print()" para mostrar el contenido del conjunto resultante en  la
consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que  se  trata  del
resultado de aplicar el método al conjunto original.

De esta forma, hemos añadido varios elementos al conjunto original, modificándolo directamente. Como
resultado, este contiene los elementos que estaban originalmente presentes  en  él,  junto  con  los
elementos que se encuentran en los iterables proporcionados  como  argumentos,  los  cuales  se  han
añadido al conjunto original."""

# Código:
conjunto = {1, 2, 3, 4, 5}

conjunto.update({6, 7}, [8, 9], (10, 11))
print(f"Este es el resultado de aplicar el método al conjunto original: {conjunto}")

# Nota Muy Importante:
"""Es fundamental  tener  en  cuenta  que  el  método  ".update()"  modifica  el  conjunto  original
directamente, ya que los conjuntos en Python son  mutables.  Esto  significa  que  cualquier  cambio
realizado en el conjunto afecta al objeto original, lo que puede ser  útil  en  muchos  casos,  pero
también puede provocar errores si no se maneja con cuidado.

Es importante aclarar que este método toma uno o varios argumentos: los conjuntos o iterables  cuyos
elementos se desean añadir al conjunto original,  y  modifica  directamente  el  conjunto  original,
incorporando los elementos que están presentes en los  conjuntos  o  iterables  proporcionados  como
argumentos.

La diferencia entre el método ".update()" y el método ".union()" radica en que el  primero  modifica
el conjunto original directamente, mientras que el segundo devuelve un nuevo conjunto con la  unión,
sin alterar el conjunto original.

En este caso, hablamos de añadir y no de combinar, porque el método ".update()" añade los  elementos
al conjunto original, modificándolo directamente, lo que significa que el conjunto  original  se  ve
afectado por la operación.

El método ".update()" es una opción eficiente si se desea añadir elementos a  un  conjunto,  ya  que
altera el conjunto original. Además, es importante recordar que  el  método  ".update()"  opera  con
elementos únicos, ya que los conjuntos no admiten elementos duplicados.

Por último, el método ".update()" es una herramienta esencial para trabajar con conjuntos en Python,
pero su uso debe ir acompañado de una comprensión clara de sus características y limitaciones.  Esto
permitirá  aprovechar  al  máximo  sus  capacidades  y  evitar   posibles   inconvenientes   en   su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────