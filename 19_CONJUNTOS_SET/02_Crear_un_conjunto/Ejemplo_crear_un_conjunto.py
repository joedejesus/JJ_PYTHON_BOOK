# Enunciado:
"""La forma más común de crear un conjunto (set) en Python es utilizando llaves { }.  Los  conjuntos
son estructuras de datos que permiten almacenar múltiples elementos  en  un  solo  objeto,  pero,  a
diferencia de las  listas  o  tuplas,  no  permiten  elementos  duplicados  ni  mantienen  un  orden
específico. Para crear un conjunto, simplemente se colocan los elementos dentro de las llaves { }  y
se separan con comas (,).

Los conjuntos en Python son colecciones de elementos únicos, no  ordenados,  mutables  e  iterables.
Esto significa que los elementos no pueden repetirse dentro de un conjunto, no tienen un orden fijo,
pueden agregarse o eliminarse después de su creación  y  se  pueden  recorrer  utilizando  bucles  o
funciones de iteración.

Además, los conjuntos pueden contener una combinación de distintos tipos de datos inmutables, lo que
los hace útiles en una amplia gama de aplicaciones. Esto significa que un  conjunto  puede  contener
elementos inmutables, como números, cadenas de texto, tuplas y valores booleanos.  Sin  embargo,  no
puede contener objetos mutables, como listas o diccionarios. Tampoco puede contener otros conjuntos,
a menos que estos sean del tipo "frozenset", que es inmutable y hashable. En el caso de las  tuplas,
estas pueden ser elementos de un conjunto siempre que todos sus componentes sean inmutables, ya  que
las tuplas en sí mismas son inmutables y hashables.

Los elementos de un conjunto no se pueden modificar  directamente,  pero  sí  se  pueden  agregar  o
eliminar elementos del conjunto utilizando métodos específicos, como ".add()" para agregar elementos
y ".remove()" o ".discard()"  para  eliminar  elementos.  Esto  hace  que  los  conjuntos  sean  una
herramienta muy útil para almacenar y manipular datos de manera eficiente, especialmente  cuando  se
necesita garantizar la unicidad de los elementos o realizar operaciones de teoría de conjuntos, como
la unión, la intersección o la diferencia entre conjuntos.

Por otra parte, si se incluyen elementos duplicados al crear  un  conjunto,  Python  automáticamente
eliminará los duplicados y solo mantendrá un elemento único  de  cada  valor.  Por  ejemplo,  si  se
intenta crear un conjunto con los elementos {1, 2, 2, 3}, el resultado será {1, 2,  3},  ya  que  el
valor "2" se repite y solo se mantendrá una instancia de él en el conjunto.

Esto también ocurre con valores que Python considera equivalentes, como 1 y True, o 0  y  False,  ya
que estos pares son tratados como iguales en un conjunto. Por lo  tanto,  si  se  intenta  crear  un
conjunto con los elementos {1, True, 0, False}, el resultado será {0, 1}, ya  que  Python  considera
que 1 y True son equivalentes, al igual que 0 y False.

Por último, es importante ser consistente en el uso de conjuntos dentro de un proyecto, ya que  esto
asegura que el código sea más legible y menos propenso a errores. La consistencia incluye no solo el
estilo de definición de los conjuntos, sino también la forma en que se accede a ellos y se manipulan
sus elementos. Además, los conjuntos  son  muy  versátiles  y  permiten  realizar  operaciones  como
agregar, eliminar o verificar la existencia de elementos, lo que los convierte  en  una  herramienta
esencial para cualquier programador que trabaje con Python."""

# Ejemplo_crear_un_conjunto.py

# Explicación:
"""Definimos una variable llamada "conjunto_1" y le  asignamos  un  conjunto  que  contiene  números
enteros. Luego, definimos otra variable llamada "conjunto_2" y le asignamos un conjunto que contiene
diferentes tipos de datos inmutables.

Para ello, en ambos casos utilizamos llaves { } para crear los conjuntos y separamos  cada  elemento
dentro de ellas con comas  (,).  Para  cada  elemento  de  los  conjuntos,  respetamos  la  sintaxis
correspondiente al tipo de dato que estamos utilizando.

Por último, utilizamos la función "print()" para mostrar los conjuntos en la consola, acompañados de
un mensaje descriptivo en formato "f-string" que indica el contenido de cada conjunto.

De esta forma, hemos creado dos conjuntos en Python: uno con números enteros y otro  con  diferentes
tipos de datos inmutables, demostrando la flexibilidad y utilidad de los conjuntos en Python."""

# Código:
conjunto_1 = {1, 2, 3, 4, 5}
print(f"Este es un conjunto de números: {conjunto_1}")

conjunto_2 = {"a", True, (1, 2)}
print(f"Este es un conjunto de diferentes tipos de datos: {conjunto_2}")

# Nota Muy Importante:
"""Es recomendable ser consistente en el uso de conjuntos dentro  de  un  proyecto.  Esto  significa
elegir un estilo claro para definir y manipular conjuntos,  y  mantenerlo  en  todo  el  código.  La
consistencia no solo mejora la legibilidad del código, sino que también reduce  la  probabilidad  de
errores, especialmente en proyectos colaborativos o de gran escala.

Además de este método para crear conjuntos, existen  otras  formas  de  hacerlo,  como  utilizar  el
constructor "set()" para convertir otros tipos de datos iterables en conjuntos. De  esta  forma,  se
pueden crear conjuntos a partir de listas, tuplas, diccionarios o incluso cadenas de texto. Para  el
caso de los diccionarios, solo se considerarán las claves al convertirlos en conjuntos, ya  que  los
valores no se incluyen en el conjunto resultante.

Los conjuntos pueden contener cualquier objeto inmutable, lo  que  los  hace  útiles  para  eliminar
duplicados y realizar operaciones de teoría de conjuntos. Sin embargo, es importante  tener  cuidado
al mezclar tipos de datos en un conjunto,  ya  que  esto  puede  llevar  a  resultados  inesperados,
especialmente con valores que Python considera equivalentes, como 1 y True, o  0  y  False,  ya  que
estos pares son tratados como iguales en un conjunto.

Por ejemplo, al realizar operaciones sobre  los  elementos  de  un  conjunto,  puede  ser  necesario
verificar el tipo de dato de cada elemento para evitar errores en tiempo de ejecución. Por lo tanto,
aunque los conjuntos permiten mezclar tipos de datos inmutables,  es  una  buena  práctica  mantener
coherencia en los tipos de datos almacenados siempre que sea posible.

Por último, un objeto mutable es aquel que puede ser modificado después de su creación. En  el  caso
de los conjuntos, esto significa que podemos agregar o eliminar elementos del conjunto sin necesidad
de crear un nuevo conjunto cada vez que  queramos  hacer  un  cambio.  Sin  embargo,  los  elementos
individuales del conjunto deben ser inmutables y hashables.

Esta es una de las características más importantes de los conjuntos, ya que nos permite trabajar con
datos de manera eficiente y flexible, sin tener que preocuparnos por la necesidad  de  crear  nuevas
estructuras de datos cada vez que queramos realizar una modificación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ───────────────────────────────────────────────────────────