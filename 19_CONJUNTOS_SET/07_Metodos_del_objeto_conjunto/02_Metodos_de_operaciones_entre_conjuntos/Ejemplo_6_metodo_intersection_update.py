# Enunciado:
"""El método ".intersection_update()" en Python se utiliza para conservar en  el  conjunto  original
únicamente los  elementos  que  también  estén  presentes  en  los  conjuntos  o  en  los  iterables
proporcionados como argumentos. Los conjuntos no mantienen un orden específico de sus elementos, por
lo que el conjunto resultante contendrá los elementos  comunes,  sin  una  posición  determinada  ni
predecible.

Este método modifica el conjunto original  directamente,  conservando  solo  los  elementos  que  se
encuentran tanto en él como en los conjuntos o iterables proporcionados como argumentos, por lo  que
es una herramienta útil para trabajar con conjuntos  dinámicos,  ya  que  permite  actualizarlos  de
manera directa y mantiene la propiedad de contener elementos únicos.

El método ".intersection_update()" puede aplicarse a cualquier objeto de tipo (set) en Python,  como
conjuntos literales, variables que contienen conjuntos o incluso resultados de otras operaciones que
generan conjuntos. Este método modifica el conjunto original, lo que significa que no  es  necesario
asignar el resultado de la aplicación del método a una nueva variable, ya que no devuelve  un  nuevo
objeto, sino que altera el objeto existente. Este comportamiento es consistente  con  la  naturaleza
mutable de los conjuntos en Python.

El método ".intersection_update()" toma uno o varios argumentos: los  conjuntos  o  iterables  cuyos
elementos se desean comparar con el  conjunto  original  para  conservar  únicamente  los  elementos
comunes. Si no se proporcionan argumentos, el método no modifica el conjunto original, ya que no hay
elementos con los que comparar.

Estos argumentos deben ser objetos iterables, lo que significa que  pueden  ser  cualquier  tipo  de
objeto que se pueda recorrer, como listas, tuplas, conjuntos,  diccionarios  o  incluso  cadenas  de
texto, siempre y cuando sus elementos sean inmutables. En el caso de  los  diccionarios,  el  método
toma sus claves como referencia, no sus valores; y, en el caso de las cadenas  de  texto,  toma  sus
caracteres como elementos individuales para calcular la intersección.

Sin embargo, estos argumentos no pueden ser valores individuales que  no  sean  iterables,  como  un
número entero o decimal, ya que el método  ".intersection_update()"  espera  recibir  uno  o  varios
objetos iterables.

Además, si algún elemento aparece repetido en cualquiera de los conjuntos o  iterables  involucrados
en la operación de intersección, este no se duplicará en el resultado final, ya que los conjuntos no
admiten elementos duplicados. Esto significa que el resultado de la intersección  será  un  conjunto
con elementos únicos.

Por último, el método  ".intersection_update()"  es  una  herramienta  eficiente  para  calcular  la
intersección  entre  conjuntos,  permitiendo  una  manipulación  directa  y  flexible  de  datos  en
estructuras de tipo (set), alterando el conjunto original."""

# Ejemplo_6_metodo_intersection_update.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".intersection_update()".

A continuación, aplicamos el método ".intersection_update()" a la variable  "conjunto".  Para  ello,
escribimos   el   nombre   de   la   variable   "conjunto",   seguido   del   nombre   del    método
".intersection_update()" y, dentro de los paréntesis, pasamos como argumentos  los  iterables  cuyos
elementos deben coincidir con los del conjunto original para conservarse en él, separados por comas;
en este caso, un conjunto literal de números enteros, una lista literal de  números  enteros  y  una
tupla literal de números enteros.

Por último, utilizamos la función "print()" para mostrar el contenido del conjunto resultante en  la
consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que  se  trata  del
resultado de aplicar el método al conjunto original.

De esta forma, hemos conservado únicamente los elementos que están presentes tanto  en  el  conjunto
original como en los iterables proporcionados como argumentos, modificando directamente el  conjunto
original.  Como  resultado,  este  contiene  únicamente  los  elementos  comunes  entre  todos   los
iterables."""

# Código:
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

conjunto.intersection_update({2, 4, 6, 8}, [4, 6, 8], (6, 12))
print(f"Este es el resultado de aplicar el método al conjunto original: {conjunto}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta  que  el  método  ".intersection_update()"  modifica  el  conjunto
original directamente, ya que los conjuntos en Python son mutables.  Esto  significa  que  cualquier
cambio realizado en el conjunto afecta al objeto original, lo que puede ser útil  en  muchos  casos,
pero también puede provocar errores si no se maneja con cuidado.

Es importante aclarar que este método toma uno o varios argumentos: los conjuntos o iterables  cuyos
elementos se desean comparar con el conjunto original, y modifica directamente el conjunto original,
conservando únicamente los elementos  que  están  presentes  en  todos  los  conjuntos  o  iterables
proporcionados como argumentos.

La diferencia entre el método ".intersection_update()" y el método ".intersection()" radica  en  que
el primero modifica el conjunto original directamente, mientras que el  segundo  devuelve  un  nuevo
conjunto con la intersección, sin alterar el conjunto original.

En este caso hablamos de conservar y no de excluir, porque  el  método  ".intersection_update()"  no
elimina elementos del conjunto original de manera arbitraria, sino que mantiene únicamente  aquellos
que coinciden en todos los iterables  proporcionados  como  argumentos,  lo  que  significa  que  el
conjunto original se ve afectado por la operación.

El método ".intersection_update()" es una opción eficiente si  se  desea  calcular  la  intersección
entre conjuntos, alterando el conjunto original.  Además,  es  importante  recordar  que  el  método
".intersection_update()" opera sobre elementos únicos, ya que los  conjuntos  no  admiten  elementos
duplicados.

Por último, el método  ".intersection_update()"  es  una  herramienta  esencial  para  trabajar  con
conjuntos en Python, pero su uso debe ir acompañado de una comprensión clara de sus  características
y limitaciones. Esto permitirá aprovechar al máximo sus capacidades y evitar posibles inconvenientes
en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────