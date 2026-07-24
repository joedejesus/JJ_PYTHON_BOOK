# Enunciado:
"""El método ".symmetric_difference_update()" en Python  se  utiliza  para  actualizar  el  conjunto
original con los elementos que están presentes en él o en el iterable proporcionado como  argumento,
pero no en ambos al mismo tiempo. Es decir, conserva únicamente los elementos no comunes  entre  los
conjuntos involucrados. Los conjuntos no mantienen un orden específico en sus elementos, por lo  que
el conjunto resultante contendrá los elementos obtenidos sin una posición determinada ni predecible.

Este método modifica el conjunto original directamente, reemplazando su contenido por  el  resultado
de la diferencia simétrica. Esto lo convierte en una herramienta útil para  trabajar  con  conjuntos
dinámicos, ya que permite actualizarlos de manera  directa  y  mantiene  la  propiedad  de  contener
elementos únicos.

El método ".symmetric_difference_update()" puede aplicarse a  cualquier  objeto  de  tipo  (set)  en
Python, como conjuntos literales, variables que contienen conjuntos o incluso  resultados  de  otras
operaciones que generan conjuntos. Este método modifica el conjunto original, lo que  significa  que
no es necesario asignar el resultado de la aplicación del método a una nueva  variable,  ya  que  no
devuelve un nuevo objeto, sino que altera el objeto existente. Este  comportamiento  es  consistente
con la naturaleza mutable de los conjuntos en Python.

El método ".symmetric_difference_update()" toma un único argumento: un  conjunto  o  iterable  cuyos
elementos se compararán con los del conjunto original para conservar  únicamente  los  elementos  no
comunes. Si no se proporciona este argumento, se producirá un  error,  ya  que  el  método  requiere
exactamente un iterable.

Este argumento debe ser un objeto iterable, lo que significa que puede ser cualquier tipo de  objeto
que se pueda recorrer, como listas, tuplas, conjuntos, diccionarios  o  incluso  cadenas  de  texto,
siempre y cuando sus elementos sean inmutables. En el caso de los diccionarios, el método  toma  sus
claves como referencia, no sus valores; y, en el caso de las cadenas de texto, toma  sus  caracteres
como elementos individuales para calcular la diferencia simétrica.

Sin embargo, este argumento no puede ser un valor individual que no sea  iterable,  como  un  número
entero o un número decimal, ya que el  método  ".symmetric_difference_update()"  espera  recibir  un
objeto iterable.

Además, si algún elemento aparece repetido en cualquiera de los conjuntos o  iterables  involucrados
en la operación de diferencia simétrica, este no se duplicará en el  resultado  final,  ya  que  los
conjuntos no permiten elementos duplicados. Esto significa que el resultado  será  un  conjunto  con
elementos únicos.

Por último, el método ".symmetric_difference_update()" es una herramienta eficiente para calcular la
diferencia simétrica entre conjuntos, lo que permite una manipulación directa y flexible de datos en
estructuras de tipo (set), alterando el conjunto original."""

# Ejemplo_8_metodo_symmetric_difference_update.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".symmetric_difference_update()".

A continuación, aplicamos el método ".symmetric_difference_update()" a la variable "conjunto".  Para
ello,  escribimos  el  nombre  de  la  variable  "conjunto",   seguido   del   nombre   del   método
".symmetric_difference_update()" y, dentro de los paréntesis, pasamos  como  argumento  un  iterable
cuyos elementos se compararán con los del conjunto original para conservar únicamente los  elementos
no comunes.

Por último, utilizamos la función "print()" para mostrar el contenido del conjunto resultante en  la
consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que  se  trata  del
resultado de aplicar el método sobre el conjunto original.

De esta forma, hemos actualizado el conjunto original,  conservando  únicamente  los  elementos  que
están presentes en uno u otro conjunto, pero no en ambos simultáneamente."""

# Código:
conjunto = {1, 2, 3, 4, 5, 6}

conjunto.symmetric_difference_update({4, 5, 6, 7, 8})
print(f"Este es el resultado de aplicar el método al conjunto original: {conjunto}")

# Nota Muy Importante:
"""Es fundamental tener  en  cuenta  que  el  método  ".symmetric_difference_update()"  modifica  el
conjunto original directamente, ya que los conjuntos en Python  son  mutables.  Esto  significa  que
cualquier cambio realizado en el conjunto afecta al objeto original, lo que puede ser útil en muchos
casos, pero también puede provocar errores si no se maneja con cuidado.

Es importante aclarar que este método  toma  un  único  argumento:  el  conjunto  o  iterable  cuyos
elementos se compararán con los del conjunto original para conservar  únicamente  los  elementos  no
comunes.

La diferencia entre el método ".symmetric_difference_update()" y el método ".symmetric_difference()"
radica en que el primero modifica  el  conjunto  original  directamente,  mientras  que  el  segundo
devuelve un nuevo conjunto con la diferencia simétrica, sin alterar el conjunto original.

En   este   caso,   hablamos   de   actualizar   y    no    de    excluir,    porque    el    método
".symmetric_difference_update()" reemplaza el contenido del conjunto original por los  elementos  no
comunes entre los conjuntos involucrados, lo que significa que el conjunto original se  ve  afectado
por la operación.

El método  ".symmetric_difference_update()"  es  una  opción  eficiente  si  se  desea  calcular  la
diferencia simétrica entre conjuntos, alterando el conjunto original. Además, es importante recordar
que este método opera con elementos únicos, ya que los conjuntos no admiten elementos duplicados.

Por último, el método ".symmetric_difference_update()" es una herramienta esencial para trabajar con
conjuntos en Python, pero su uso debe ir acompañado de una comprensión clara de sus  características
y limitaciones. Esto permitirá aprovechar al máximo sus capacidades y evitar posibles inconvenientes
en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────