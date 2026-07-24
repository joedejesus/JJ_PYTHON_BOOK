# Enunciado:
"""En Python, además de  los  conjuntos  mutables  (set),  existe  una  variante  inmutable  llamada
"frozenset". Un frozenset es una colección de elementos únicos, inmutables y no ordenados, similar a
un conjunto, pero, a diferencia de este, no permite modificar su contenido después de  su  creación;
es decir, es inmutable.

Para crear un frozenset, se utiliza el constructor "frozenset()" y se  le  pasa  como  argumento  un
iterable, como una lista, una tupla o un conjunto, ya sea de  forma  literal  o  almacenado  en  una
variable. El resultado es un objeto  frozenset  que  contiene  los  elementos  únicos  del  iterable
proporcionado. Al ser inmutable, no se pueden agregar ni eliminar elementos una vez creado,  lo  que
lo hace útil en situaciones donde se requiere una colección de elementos únicos que no debe cambiar,
como elemento de otros conjuntos o para ciertas operaciones de teoría de conjuntos.

Los frozenset pueden contener cualquier tipo de dato inmutable y hashable, como números, cadenas  de
texto, tuplas (siempre que sus elementos también sean inmutables), valores booleanos,  entre  otros.
Sin embargo, no pueden contener objetos mutables como listas o diccionarios. Además,  los  frozenset
pueden ser elementos de otros conjuntos, ya que son inmutables y  hashables,  a  diferencia  de  los
conjuntos normales, que no pueden ser elementos de otros conjuntos por ser mutables.

Al igual que los conjuntos, los frozenset eliminan automáticamente los  elementos  duplicados  y  no
mantienen un orden específico. Si se incluyen elementos duplicados en el iterable de origen, solo se
conservará una instancia de cada valor en el frozenset  resultante.  Por  ejemplo,  si  se  crea  un
frozenset con los elementos [1, 2, 2, 3], el resultado será "frozenset({1, 2, 3})", ya que el  valor
"2" se repite y solo se mantendrá una instancia de este en el conjunto,  por  lo  que  no  aparecerá
repetido en el resultado final.

Esto también ocurre con valores que Python considera equivalentes, como 1 y True, o 0  y  False,  ya
que estos pares son tratados como iguales en un conjunto. Por lo  tanto,  si  se  intenta  crear  un
frozenset con los elementos [1, True, 0, False], el  resultado  será  "frozenset({0,  1})",  ya  que
Python considera que 1 y True son equivalentes, al igual que 0 y False.

Otra característica importante es que, al ser inmutables, los frozenset no disponen de métodos  para
agregar o eliminar elementos, como  ".add()"  o  ".remove()".  Sin  embargo,  sí  permiten  realizar
operaciones de teoría de conjuntos, como unión, intersección,  diferencia  y  diferencia  simétrica,
devolviendo siempre un nuevo conjunto como resultado, sin modificar el frozenset original.

Por último, los frozenset son útiles cuando se necesita una colección de  elementos  únicos  que  no
debe modificarse, y pueden utilizarse como claves en diccionarios o elementos de otros conjuntos. Su
inmutabilidad y capacidad de ser hashables los hacen ideales para estos casos."""

# Ejemplo_crear_un_frozenset.py

# Explicación:
"""Definimos una variable llamada "conjunto_original"  y  le  asignamos  un  conjunto  que  contiene
números enteros del 1 al 5. Para ello, utilizamos llaves {} y separamos sus elementos con comas (,).

A continuación, definimos una variable llamada "conjunto_congelado"  y  le  asignamos  un  frozenset
creado a partir del conjunto original. Para ello, utilizamos el  constructor  "frozenset()"  con  el
argumento correspondiente entre paréntesis; en  este  caso,  la  variable  "conjunto_original",  que
contiene el conjunto de números enteros a partir del cual queremos crear el frozenset.

Utilizamos la función "print()" para mostrar el frozenset en la consola, acompañado  de  un  mensaje
descriptivo en formato "f-string" que indica que se trata  de  un  frozenset  creado  a  partir  del
conjunto original.

Además, creamos un frozenset a partir de  una  lista  literal  con  números  enteros  utilizando  el
constructor "frozenset()" directamente con la lista literal como argumento.

Para ello, definimos una variable llamada "conjunto_congelado_2" y le asignamos un frozenset  creado
a partir de una lista literal. Para ello, utilizamos el constructor "frozenset()" con  el  argumento
correspondiente entre paréntesis; en este caso, la lista literal "[1,  2,  2,  2,  3,  4,  5]",  que
contiene los números enteros a partir de los cuales queremos crear el frozenset.  Algunos  de  estos
números se repiten para demostrar que el frozenset eliminará los duplicados automáticamente.

Por último, utilizamos la función "print()" para mostrar el frozenset en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" que indica que se trata de un frozenset creado a partir
de una lista literal sin los elementos duplicados.

De esta forma, hemos creado dos frozenset: uno a partir de un conjunto y otro a partir de una  lista
literal con elementos duplicados, demostrando  la  flexibilidad  y  utilidad  de  los  frozenset  en
Python."""

# Código:
conjunto_original = {1, 2, 3, 4, 5}

conjunto_congelado = frozenset(conjunto_original)
print(f"frozenset creado a partir del conjunto original: {conjunto_congelado}")

conjunto_congelado_2 = frozenset([1, 2, 2, 2, 3, 4, 5])
print(f"frozenset creado a partir de una lista literal sin los elementos duplicados: {conjunto_congelado_2}")

# Nota Muy Importante:
"""Es recomendable ser consistente en el uso de frozenset dentro  de  un  proyecto.  Esto  significa
elegir un estilo claro para definir y manipular frozenset,  y  mantenerlo  en  todo  el  código.  La
consistencia no solo mejora la legibilidad del código, sino que también reduce  la  probabilidad  de
errores, especialmente en proyectos colaborativos o de gran escala.

Además de este método para crear frozenset, estos se pueden crear a partir  de  cualquier  iterable,
como listas, tuplas, conjuntos o incluso cadenas de texto, utilizando el constructor  "frozenset()",
ya estén definidos en  variables  o  como  elementos  literales,  siempre  que  los  elementos  sean
inmutables. En el caso de los diccionarios, solo se  considerarán  las  claves  al  convertirlos  en
frozenset, ya que los valores no se incluyen en el conjunto resultante.

Los frozenset pueden contener cualquier objeto inmutable y hashable, lo que  los  hace  útiles  para
eliminar duplicados, realizar operaciones de teoría de conjuntos y ser  utilizados  como  claves  en
diccionarios o elementos de otros conjuntos. Sin embargo, es importante  tener  cuidado  al  mezclar
tipos de datos en un frozenset, ya que esto puede llevar a resultados inesperados, especialmente con
valores que Python considera equivalentes, como 1 y True, o 0  y  False,  ya  que  estos  pares  son
tratados como iguales en un conjunto.

Por ejemplo, al realizar operaciones sobre los  elementos  de  un  frozenset,  puede  ser  necesario
verificar el tipo de dato de cada elemento para evitar errores en tiempo de ejecución. Por lo tanto,
aunque los frozenset permiten mezclar tipos de datos inmutables,  es  una  buena  práctica  mantener
coherencia en los tipos de datos almacenados siempre que sea posible.

Por último, un objeto inmutable es aquel que no puede ser modificado después de su creación.  En  el
caso de los frozenset, esto significa que no podemos agregar ni eliminar elementos del conjunto  una
vez creado. Esta inmutabilidad es una de las características más importantes de  los  frozenset,  ya
que nos permite trabajar con datos de manera eficiente y segura, especialmente  cuando  se  requiere
que la colección de elementos permanezca constante a lo largo del tiempo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────