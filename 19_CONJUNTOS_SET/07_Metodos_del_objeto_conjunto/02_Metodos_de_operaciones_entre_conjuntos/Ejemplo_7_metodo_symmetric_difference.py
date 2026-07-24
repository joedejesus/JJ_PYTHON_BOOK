# Enunciado:
"""El método ".symmetric_difference()" en Python se utiliza  para  obtener  un  nuevo  conjunto  que
contiene los elementos que están presentes en el conjunto original o en  el  iterable  proporcionado
como argumento, pero no en ambos al mismo tiempo. Es  decir,  devuelve  los  elementos  que  no  son
comunes entre los conjuntos involucrados. Los conjuntos no mantienen  un  orden  específico  de  sus
elementos, por lo que el resultado de la  diferencia  simétrica  será  un  nuevo  conjunto  con  los
elementos obtenidos, sin una posición determinada ni predecible.

El método ".symmetric_difference()" puede aplicarse a cualquier objeto de tipo (set) en Python, como
conjuntos literales, variables que contienen conjuntos o incluso resultados de otras operaciones que
generan conjuntos. Este método no modifica el conjunto original y devuelve  un  nuevo  conjunto  que
contiene los elementos que están presentes en uno u otro conjunto, pero no en ambos simultáneamente.
Este nuevo conjunto se almacena en la variable asignada al resultado de la aplicación del método.

El método ".symmetric_difference()" toma un único argumento: un conjunto o iterable cuyos  elementos
se compararán con los del conjunto original  para  obtener  los  elementos  no  comunes.  Si  no  se
proporciona ningún argumento, el método generará un error, ya  que  espera  recibir  exactamente  un
iterable.

Este argumento debe ser un objeto iterable, lo que significa que puede ser cualquier tipo de  objeto
que se pueda recorrer, como listas, tuplas, conjuntos, diccionarios  o  incluso  cadenas  de  texto,
siempre que sus elementos sean inmutables. En el caso de los diccionarios, el método toma sus claves
como referencia, no sus valores; y, en el caso de las cadenas de texto,  toma  sus  caracteres  como
elementos individuales para calcular la diferencia simétrica.

Sin embargo, este argumento no puede ser un valor individual que no sea  iterable,  como  un  número
entero o decimal, ya que el método ".symmetric_difference()" espera recibir un iterable.

Además, si algún elemento aparece repetido en cualquiera de los conjuntos o  iterables  involucrados
en la operación de diferencia simétrica, este no se duplicará en el  resultado  final,  ya  que  los
conjuntos no permiten elementos duplicados. Esto significa que el resultado  será  un  conjunto  con
elementos únicos.

Por último, el método ".symmetric_difference()"  es  una  herramienta  eficiente  para  calcular  la
diferencia simétrica entre conjuntos, lo que permite una manipulación directa y flexible de datos en
estructuras de tipo (set) sin alterar el conjunto original."""

# Ejemplo_7_metodo_symmetric_difference.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".symmetric_difference()".

A continuación, definimos una nueva variable llamada "nuevo_conjunto" y le asignamos el resultado de
aplicar el método ".symmetric_difference()" a la  variable  "conjunto".  Para  ello,  escribimos  el
nombre de la variable "conjunto", seguido del nombre del método ".symmetric_difference()" y,  dentro
de los paréntesis, pasamos como argumento un iterable cuyos elementos  se  compararán  con  los  del
conjunto original para obtener los elementos no comunes.

Por último, utilizamos la función "print()" para mostrar el contenido del nuevo conjunto  resultante
en la consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que se  trata
del resultado de aplicar el método al conjunto original.

De esta forma, obtenemos un nuevo conjunto que contiene los elementos que están presentes en  uno  u
otro conjunto, pero no en ambos simultáneamente, sin modificar el conjunto original."""

# Código:
conjunto = {1, 2, 3, 4, 5, 6}

nuevo_conjunto = conjunto.symmetric_difference({4, 5, 6, 7, 8})
print(f"Este es el resultado de aplicar el método al conjunto original: {nuevo_conjunto}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".symmetric_difference()" no  modifica  el  conjunto
original, sino que devuelve un nuevo conjunto con los elementos que están presentes en  uno  u  otro
conjunto, pero no en ambos simultáneamente. Esto significa que el conjunto  original  permanece  sin
cambios, lo que puede ser útil en muchos casos, pero también puede provocar errores si no se  maneja
con cuidado.

Es importante aclarar que este método  toma  un  único  argumento:  el  conjunto  o  iterable  cuyos
elementos se compararán con los del conjunto original para obtener los elementos no comunes.

La diferencia entre el método ".symmetric_difference()" y el método ".symmetric_difference_update()"
radica en que el primero devuelve un nuevo conjunto con la  diferencia  simétrica,  sin  alterar  el
conjunto original, mientras que el segundo modifica el conjunto original directamente.

El método ".symmetric_difference()" es una opción eficiente  si  se  desea  calcular  la  diferencia
simétrica entre conjuntos sin alterar el conjunto original. Además, es importante recordar que  este
método opera sobre elementos únicos, ya que los conjuntos no admiten elementos duplicados.

Por último, el método ".symmetric_difference()"  es  una  herramienta  esencial  para  trabajar  con
conjuntos  en  Python,  pero  su  uso  debe  estar  acompañado  de  una  comprensión  clara  de  sus
características y limitaciones. Esto  permitirá  aprovechar  al  máximo  sus  capacidades  y  evitar
posibles inconvenientes en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────