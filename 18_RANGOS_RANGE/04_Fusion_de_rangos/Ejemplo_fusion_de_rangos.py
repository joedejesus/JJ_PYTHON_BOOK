# Enunciado:
"""La fusión de rangos es una técnica útil en la manipulación de datos en  Python,  ya  que  permite
combinar múltiples rangos en una sola secuencia, lo que resulta práctico  en  aplicaciones  como  la
agregación de datos, la creación de secuencias más complejas y la organización  de  la  información.
Además, facilita la integración de contenidos provenientes de diferentes fuentes y  su  presentación
de manera coherente.

Esta técnica se logra utilizando la función "chain()"  del  módulo  "itertools",  que  permite  unir
iterables de manera eficiente. Dado que los rangos en Python  son  objetos  inmutables  que  generan
secuencias, la fusión de rangos no altera los rangos originales, sino que crea un nuevo iterable que
contiene la combinación de los elementos de los rangos fusionados.

La función "chain()" toma como argumentos los iterables que se desean fusionar y devuelve  un  nuevo
iterable que produce los elementos de cada uno en el orden en que se pasan  como  argumentos.  Estos
argumentos pueden ser tanto variables que contienen  iterables  como  iterables  literales,  lo  que
proporciona flexibilidad en la manipulación de datos.

Esto significa que el resultado de la fusión de  rangos  es  un  iterable  que  contiene  todos  los
elementos de los  rangos  originales,  mientras  que  dichos  rangos  permanecen  intactos  tras  la
operación. Esto ayuda a evitar efectos  no  deseados  y  a  mantener  la  integridad  de  los  datos
originales.

Por último, con esta técnica es posible combinar  rangos  que  contengan  diferentes  intervalos  de
datos, lo que proporciona flexibilidad para la manipulación de datos y  la  creación  de  secuencias
dinámicas.  Esto  permite  adaptar  soluciones  a  necesidades  específicas,  combinando  diferentes
intervalos y estructuras de manera eficiente."""

# Ejemplo_fusion_de_rangos.py

# Explicación:
"""En primer lugar, importamos la función  "chain()"  del  módulo  "itertools",  que  nos  permitirá
fusionar los rangos de manera eficiente. Para ello, utilizamos la sintaxis  "from  itertools  import
chain". De esta forma, ya podemos utilizar la función "chain()" en el código para trabajar  con  los
rangos que deseamos fusionar.

A continuación, definimos dos variables llamadas "rango_1" y "rango_2", y les asignamos  los  rangos
"range(1, 4)" y "range(4, 7)", respectivamente. Estos rangos representan dos conjuntos de datos  que
queremos fusionar para formar una secuencia combinada que contenga  todos  los  elementos  de  ambos
rangos. Adicionalmente, incluimos un tercer rango literal, "range(7, 10)", en la fusión.

Luego, definimos una nueva variable llamada "rango_fusionado" y le asignamos el resultado de  llamar
a la función "chain()" con los rangos que queremos fusionar como argumentos separados por comas.  En
este caso, "rango_1", "rango_2" y el rango literal "range(7, 10)". La  función  "chain()"  toma  los
rangos como argumentos y devuelve un nuevo iterable que produce los elementos de cada  rango  en  el
orden en que se pasan, el cual se almacena en la variable "rango_fusionado".

De esta forma, los rangos "range(1, 4)", "range(4, 7)" y "range(7, 10)" se combinan para  formar  un
nuevo iterable que contiene todos los elementos. Esta combinación se realiza en el orden en  que  se
pasaron los rangos como argumentos a la función "chain()", lo que significa que el resultado  de  la
fusión, después de ser convertido en una lista mediante el constructor "list()", será: [1, 2, 3,  4,
5, 6, 7, 8, 9].

Por último, utilizamos la función "print()" para mostrar el contenido del rango fusionado  en  forma
de lista en la consola, acompañado de un mensaje descriptivo en formato "f-string" que indica que se
trata del resultado de la fusión de los rangos.

Para ello, utilizamos el constructor "list()"  dentro  de  la  expresión  "f-string",  que  toma  el
iterable obtenido como argumento. Esto permite convertir el resultado de la fusión de rangos en  una
lista y, de esta forma, visualizar el rango fusionado como una secuencia de números  y  no  como  la
representación del objeto iterable que devuelve la función "chain()"."""

# Código:
from itertools import chain
rango_1 = range(1, 4)
rango_2 = range(4, 7)

rango_fusionado = chain(rango_1, rango_2, range(7, 10))

print(f"Este es el resultado de la fusión de los rangos: {list(rango_fusionado)}")

# Nota Importante:
"""Es importante destacar que la fusión de rangos no modifica los rangos originales, sino  que  crea
un nuevo iterable que contiene su combinación, ya que los rangos en Python son objetos inmutables.

Los rangos son objetos iterables que generan  sus  elementos  de  manera  perezosa  (lazy),  lo  que
significa que no almacenan todos los valores en memoria, sino que los producen  bajo  demanda.  Esta
característica hace que los rangos sean muy eficientes en términos de uso de memoria, incluso cuando
representan secuencias muy grandes.

En el caso de la fusión de rangos utilizando  la  función  "chain()",  la  conversión  a  una  lista
mediante el constructor "list()" es necesaria para visualizar  los  números  generados,  ya  que  la
función "chain()" devuelve un objeto iterable que  no  se  visualiza  directamente,  sino  que  debe
convertirse explícitamente. Esto se debe a que la función "chain()" genera los elementos  de  manera
perezosa y no almacena todos los valores en memoria, lo que permite una mayor eficiencia en términos
de uso de memoria, especialmente cuando se trabaja con rangos grandes o con múltiples iterables.

Además, el orden de los rangos pasados como argumentos es importante, ya que determina el  resultado
final de la fusión. Si se invierte el orden de los rangos, el resultado sería diferente, por lo  que
es fundamental prestar atención a la secuencia en la que se combinan  los  rangos  para  obtener  el
resultado deseado.

Por último, la fusión de rangos mediante la función "chain()" permite trabajar con secuencias que no
necesariamente tienen que ser consecutivas ni tener el  mismo  tamaño.  Esto  proporciona  una  gran
versatilidad para manejar datos provenientes de diferentes fuentes o con diferentes características,
adaptándose a una amplia variedad de casos de uso."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────