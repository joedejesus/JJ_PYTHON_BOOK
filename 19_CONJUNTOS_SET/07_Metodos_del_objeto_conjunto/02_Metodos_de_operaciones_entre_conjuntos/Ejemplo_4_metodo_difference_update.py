# Enunciado:
"""El método ".difference_update()" en Python se utiliza para eliminar  del  conjunto  original  los
elementos que también estén presentes en los  conjuntos  o  en  los  iterables  proporcionados  como
argumentos. Los conjuntos no mantienen un orden específico de sus elementos, por lo que el  conjunto
resultante contendrá los elementos restantes sin una posición determinada ni predecible.

Este método modifica el conjunto original directamente, eliminando los elementos que  se  encuentran
en los conjuntos o en los iterables proporcionados como argumentos, por lo que  es  una  herramienta
útil para trabajar con conjuntos dinámicos,  ya  que  permite  actualizarlos  de  manera  directa  y
mantiene la propiedad de contener elementos únicos.

El método ".difference_update()" puede aplicarse a cualquier objeto de tipo (set)  en  Python,  como
conjuntos literales, variables que contienen conjuntos o incluso resultados de otras operaciones que
generan conjuntos. Este método modifica el conjunto original, lo que significa que no  es  necesario
asignar el resultado de la aplicación del método a una nueva variable, ya que no devuelve  un  nuevo
objeto, sino que altera el objeto existente. Este comportamiento es consistente  con  la  naturaleza
mutable de los conjuntos en Python.

El método ".difference_update()" toma uno o varios  argumentos:  los  conjuntos  o  iterables  cuyos
elementos se desean eliminar del conjunto original. Si no se proporcionan argumentos, el  método  no
modifica el conjunto original, ya que no hay elementos que eliminar.

Estos argumentos deben ser objetos iterables, lo que significa que  pueden  ser  cualquier  tipo  de
objeto que se pueda recorrer, como listas, tuplas, conjuntos,  diccionarios  o  incluso  cadenas  de
texto, siempre y cuando sus elementos sean inmutables. En el caso de  los  diccionarios,  el  método
toma sus claves como referencia, no sus valores; y, en el caso de las cadenas  de  texto,  toma  sus
caracteres como elementos individuales para calcular la diferencia.

Sin embargo, estos argumentos no pueden ser valores individuales que  no  sean  iterables,  como  un
número entero o decimal, ya que el método ".difference_update()" espera recibir uno o varios objetos
iterables.

Además, si algún elemento aparece repetido en cualquiera de los conjuntos o  iterables  involucrados
en la operación de diferencia, este no se duplicará en el resultado final, ya que los  conjuntos  no
permiten elementos duplicados. Esto significa que el resultado de la diferencia será un conjunto con
elementos únicos.

Por último,  el  método  ".difference_update()"  es  una  herramienta  eficiente  para  calcular  la
diferencia entre conjuntos, permitiendo una manipulación directa y flexible de datos en  estructuras
de tipo (set), alterando el conjunto original."""

# Ejemplo_4_metodo_difference_update.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".difference_update()".

A continuación, aplicamos el método ".difference_update()" a  la  variable  "conjunto".  Para  ello,
escribimos el nombre de la variable "conjunto", seguido del nombre del método ".difference_update()"
y, dentro de los paréntesis, pasamos como argumentos los iterables cuyos elementos deseamos eliminar
del conjunto original, separados por comas; en este caso, un conjunto literal  de  números  enteros,
una lista literal de números enteros y una tupla literal de números enteros.

Por último, utilizamos la función "print()" para mostrar en la consola  el  contenido  del  conjunto
resultante, acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata del
resultado de aplicar el método al conjunto original.

De esta forma, hemos eliminado varios elementos del conjunto original,  modificándolo  directamente.
Como resultado, este contiene los elementos que  estaban  originalmente  presentes  en  él,  excepto
aquellos que se encuentran en los iterables proporcionados como  argumentos,  los  cuales  han  sido
eliminados del conjunto original."""

# Código:
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

conjunto.difference_update({2, 4}, [6, 8], (10, 12))
print(f"Este es el resultado de aplicar el método al conjunto original: {conjunto}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".difference_update()" modifica el conjunto original
directamente, ya que los conjuntos en Python son  mutables.  Esto  significa  que  cualquier  cambio
realizado en el conjunto afecta al objeto original, lo que puede ser  útil  en  muchos  casos,  pero
también puede provocar errores si no se maneja con cuidado.

Es importante aclarar que este método toma uno o varios argumentos: los conjuntos o iterables  cuyos
elementos se desean eliminar del conjunto original, y modifica directamente  el  conjunto  original,
eliminando los elementos que están presentes en los conjuntos o en los iterables proporcionados como
argumentos.

La diferencia entre el método ".difference_update()" y el método ".difference()" radica  en  que  el
primero modifica el conjunto original directamente,  mientras  que  el  segundo  devuelve  un  nuevo
conjunto con la diferencia, sin alterar el conjunto original.

En este caso, hablamos de eliminar y no de excluir, porque el método ".difference_update()"  elimina
los elementos del conjunto original, modificándolo directamente, lo que significa  que  el  conjunto
original se ve afectado por la operación.

El método ".difference_update()" es una opción eficiente si se desea calcular  la  diferencia  entre
conjuntos,  alterando  el  conjunto  original.  Además,  es  importante  recordar  que   el   método
".difference_update()" opera con elementos  únicos,  ya  que  los  conjuntos  no  admiten  elementos
duplicados.

Por último, el método ".difference_update()" es una herramienta esencial para trabajar con conjuntos
en Python, pero su uso debe ir  acompañado  de  una  comprensión  clara  de  sus  características  y
limitaciones. Esto permitirá aprovechar al máximo sus capacidades y evitar  posibles  inconvenientes
en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────