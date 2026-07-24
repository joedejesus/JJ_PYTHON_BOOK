# Enunciado:
"""El método ".intersection()" en Python se utiliza para obtener un nuevo conjunto que contiene  los
elementos que están presentes tanto en el conjunto original como en todos los conjuntos o  iterables
proporcionados como argumentos. Sus elementos deben coincidir para formar parte del resultado de  la
operación de intersección. Los conjuntos no mantienen un orden específico en sus elementos,  por  lo
que el resultado de la intersección será un nuevo conjunto con  los  elementos  obtenidos,  sin  una
posición determinada ni predecible.

El método ".intersection()" puede aplicarse a  cualquier  objeto  de  tipo  (set)  en  Python,  como
conjuntos literales, variables que contienen conjuntos o incluso resultados de otras operaciones que
generan conjuntos. Este método no modifica el conjunto original y devuelve  un  nuevo  conjunto  que
contiene los elementos que están presentes tanto en el conjunto original como  en  los  conjuntos  o
iterables proporcionados como argumentos. Sus  elementos  deben  coincidir  para  formar  parte  del
resultado de la operación de intersección. Este nuevo conjunto se almacena en la  variable  asignada
al resultado de la aplicación del método.

El método ".intersection()" toma uno o varios argumentos: los conjuntos o iterables cuyos  elementos
se desean comparar con el conjunto original para obtener únicamente los elementos comunes. Si no  se
proporciona ningún argumento, el método devuelve una copia del conjunto  original,  ya  que  no  hay
otros elementos con los cuales comparar.

Estos argumentos deben ser objetos iterables, lo que significa que  pueden  ser  cualquier  tipo  de
objeto que se pueda recorrer, como listas, tuplas, conjuntos,  diccionarios  o  incluso  cadenas  de
texto, siempre y cuando sus elementos sean inmutables. En el caso de  los  diccionarios,  el  método
toma sus claves como referencia, no sus valores; y, en el caso de las cadenas  de  texto,  toma  sus
caracteres como elementos individuales para calcular la intersección.

Sin embargo, estos argumentos no pueden ser valores individuales que  no  sean  iterables,  como  un
número entero o de punto flotante, ya que el método ".intersection()" espera recibir  uno  o  varios
iterables.

Además, si algún elemento aparece repetido en cualquiera de los conjuntos o  iterables  involucrados
en la operación de intersección, este no se duplicará en el resultado final, ya que los conjuntos no
permiten elementos duplicados. Esto significa que el resultado de la intersección será  un  conjunto
con elementos únicos.

Por último, el método ".intersection()" es una herramienta eficiente para calcular  la  intersección
entre conjuntos, lo que permite una manipulación directa y flexible de datos en estructuras de  tipo
(set) sin alterar el conjunto original."""

# Ejemplo_5_metodo_intersection.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".intersection()".

A continuación, definimos una nueva variable llamada "nuevo_conjunto" y le asignamos el resultado de
aplicar el método ".intersection()" a la variable "conjunto". Para ello, escribimos el nombre de  la
variable "conjunto", seguido del nombre del método ".intersection()" y, dentro  de  los  paréntesis,
pasamos como argumentos los iterables cuyos elementos deben coincidir con los del conjunto  original
para formar parte del resultado de la operación de intersección, separados por comas. En este  caso,
un conjunto literal de números enteros, una lista literal de números enteros y una tupla literal  de
números enteros.

Por último, utilizamos la función "print()" para mostrar el contenido del nuevo conjunto  resultante
en la consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que se  trata
del resultado de aplicar el método al conjunto original.

De esta forma, obtenemos un nuevo conjunto que contiene únicamente los elementos que están presentes
tanto en el conjunto original como en los iterables proporcionados como argumentos, sin modificar el
conjunto original y conservando solo los elementos comunes."""

# Código:
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

nuevo_conjunto = conjunto.intersection({2, 4, 6, 8}, [4, 6, 8], (6, 12))
print(f"Este es el resultado de aplicar el método al conjunto original: {nuevo_conjunto}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".intersection()" no modifica el conjunto  original,
sino que devuelve un nuevo conjunto con los elementos que  están  presentes  tanto  en  el  conjunto
original como en los conjuntos o iterables  proporcionados  como  argumentos.  Sus  elementos  deben
coincidir para formar parte del resultado. Esto significa que el  conjunto  original  permanece  sin
cambios, lo cual puede ser útil en muchos casos, pero también puede provocar errores si no se maneja
con cuidado.

Es importante aclarar que este método toma uno o varios argumentos: los conjuntos o iterables  cuyos
elementos se desean comparar con el  conjunto  original,  y  devuelve  un  nuevo  conjunto  con  los
elementos que están presentes en todos los conjuntos o  iterables  proporcionados  como  argumentos,
conservando únicamente los elementos comunes.

La diferencia entre el método ".intersection()" y el método ".intersection_update()" radica  en  que
el primero devuelve un nuevo conjunto  con  la  intersección,  sin  alterar  el  conjunto  original,
mientras que el segundo modifica el conjunto original directamente.

En este caso, hablamos de conservar y no de eliminar, porque el método ".intersection()" no  elimina
elementos del conjunto original, sino que selecciona únicamente los elementos que coinciden en todos
los iterables proporcionados como argumentos, lo que significa que el conjunto  original  no  se  ve
afectado por la operación.

El método ".intersection()" es una opción eficiente si  se  desea  calcular  la  intersección  entre
conjuntos  sin  alterar  el  conjunto  original.  Además,  es  importante  recordar  que  el  método
".intersection()" opera con elementos únicos, ya que los conjuntos no admiten elementos duplicados.

Por último, el método ".intersection()" es una herramienta esencial para trabajar con  conjuntos  en
Python, pero su uso debe estar  acompañado  de  una  comprensión  clara  de  sus  características  y
limitaciones. Esto permitirá aprovechar al máximo sus capacidades y evitar  posibles  inconvenientes
en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────