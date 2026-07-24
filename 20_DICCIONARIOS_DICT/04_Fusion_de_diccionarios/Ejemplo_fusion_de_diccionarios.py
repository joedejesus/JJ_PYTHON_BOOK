# Enunciado:
"""La fusión de diccionarios es una técnica fundamental en  la  manipulación  de  datos  en  Python.
Permite combinar múltiples diccionarios en uno solo, lo que resulta útil en una amplia  variedad  de
aplicaciones, como la agregación de datos, la creación de estructuras de datos más  complejas  y  la
organización de la información. Además, es una herramienta esencial para el procesamiento de  datos,
ya que facilita la integración de contenidos provenientes de diferentes fuentes y su presentación de
manera coherente y estructurada.

Esta técnica se logra utilizando el operador de unión (|), introducido en Python  3.9,  que  permite
unir diccionarios de manera eficiente y flexible.  El  operador  (|)  es  ideal  para  combinaciones
simples y rápidas, aunque puede  generar  un  mayor  consumo  de  memoria,  ya  que  crea  un  nuevo
diccionario cada vez que se realiza una fusión, en lugar de modificar los diccionarios existentes.

Sin embargo, esta característica también  garantiza  que  los  diccionarios  originales  permanezcan
intactos, lo que puede ser beneficioso para evitar efectos secundarios no  deseados  y  mantener  la
integridad de los datos originales, teniendo en cuenta que los diccionarios en  Python  son  objetos
mutables.

Por último, es importante destacar que  con  esta  técnica  es  posible  combinar  diccionarios  que
contengan diferentes tipos de datos, ya sea  mediante  variables  o  directamente  con  diccionarios
literales, lo que proporciona una gran flexibilidad para la manipulación de datos y la  creación  de
estructuras dinámicas.

Además, esto nos permite adaptar nuestras soluciones a las necesidades  específicas  de  cada  caso,
combinando diferentes tipos de datos y estructuras  de  manera  eficiente  y  efectiva,  lo  que  es
fundamental para el desarrollo de programas robustos y versátiles en Python."""

# Ejemplo_fusion_de_diccionarios.py

# Explicación:
"""Definimos  dos  variables  llamadas  "diccionario_1"  y  "diccionario_2",  y  les  asignamos  los
diccionarios {"a": 1, "b": 2} y {"c": 3, "d": 4}, respectivamente.  Estos  diccionarios  representan
dos conjuntos de datos que queremos fusionar para formar un diccionario combinado que contenga todos
los pares clave-valor de  ambos  diccionarios,  además  de  los  pares  de  un  diccionario  literal
adicional.

Luego, definimos una nueva variable llamada "diccionario_fusionado" y le asignamos el  resultado  de
la fusión de "diccionario_1", "diccionario_2" y el diccionario literal {"e": 5, "f":  6}  utilizando
el operador de unión (|). Para ello, colocamos ambas variables y el diccionario literal en el  orden
deseado de fusión, entre paréntesis para mejorar la legibilidad y separadas por el operador (|).

Por último, utilizamos la función "print()" para mostrar el resultado de la fusión  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" que indica que se trata del resultado  de
la fusión de los diccionarios.

De esta forma, los diccionarios {"a": 1, "b": 2}, {"c": 3, "d": 4} y {"e": 5, "f":  6}  se  combinan
para formar un nuevo diccionario que contiene todos  los  pares  clave:valor.  Esta  combinación  se
realiza en el orden en que se encuentran las variables y el  diccionario  literal,  por  lo  que  el
resultado de la fusión será el diccionario: {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}."""

# Código:
diccionario_1 = {"a": 1, "b": 2}
diccionario_2 = {"c": 3, "d": 4}

diccionario_fusionado = (diccionario_1 | diccionario_2 | {"e": 5, "f": 6})
print(f"Este es el resultado de la fusión de los diccionarios: {diccionario_fusionado}")

# Nota Importante:
"""Es importante destacar que la fusión de diccionarios no  modifica  los  diccionarios  originales,
sino que crea un nuevo diccionario que contiene la combinación de los diccionarios originales.  Esto
se debe a que, aunque los diccionarios en Python son objetos mutables, el  operador  (|)  genera  un
nuevo diccionario en lugar de modificar los existentes. Por lo  tanto,  cada  vez  que  se  fusionan
diccionarios, se genera un nuevo diccionario que contiene el resultado de la  fusión,  mientras  que
los diccionarios originales permanecen sin cambios.

Esta característica garantiza la seguridad y consistencia de los  datos,  ya  que  los  diccionarios
originales no se ven afectados por operaciones posteriores. Sin embargo, también es importante tener
en cuenta que la creación de nuevos diccionarios puede tener un impacto en el rendimiento cuando  se
trabaja con grandes volúmenes de datos, por lo que es  recomendable  utilizar  métodos  alternativos
como ".update()" si se busca modificar un diccionario existente y optimizar el uso de memoria.

El método ".update()" permite agregar los pares clave-valor de un diccionario a otro  sin  crear  un
nuevo diccionario, lo que puede ser más eficiente en términos de memoria  y  rendimiento  cuando  se
trabaja con grandes volúmenes  de  datos.  Sin  embargo,  el  operador  (|)  es  más  adecuado  para
combinaciones simples y rápidas, especialmente cuando se desea mantener los diccionarios  originales
sin modificaciones. Por lo tanto, la  elección  entre  el  operador  (|)  y  el  método  ".update()"
dependerá del contexto específico y de las necesidades del programa, teniendo en cuenta las ventajas
y desventajas de cada enfoque para lograr la fusión de diccionarios de manera eficiente y efectiva.

Por otro lado, el uso de paréntesis en este caso no es necesario y no  tiene  ningún  efecto  en  la
operación, pero puede ayudar a mejorar la legibilidad del código al indicar claramente que  se  está
realizando una operación de fusión de diccionarios. Además, el orden de los diccionarios  puede  ser
importante cuando existen claves repetidas, ya que determina qué valor  prevalece  en  el  resultado
final. En este ejemplo, como no hay claves duplicadas, invertir el orden no cambiaría el  resultado,
aunque sí es fundamental prestar atención a la secuencia en la  que  se  combinan  los  diccionarios
cuando hay coincidencias de claves.

Por último, destacar que en realidad lo que estamos haciendo es unir los diccionarios con ayuda  del
operador (|), pero utilizamos el  término  "fusión"  para  describir  el  proceso  de  combinar  los
diccionarios en uno solo, ya que el término "fusión" se utiliza comúnmente  para  referirse  a  este
proceso en un contexto más amplio y descriptivo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────