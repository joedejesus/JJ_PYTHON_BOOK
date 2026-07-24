# Enunciado:
"""La fusión de tuplas es una técnica muy útil para la manipulación  de  datos  en  Python.  Permite
combinar múltiples tuplas en una sola, lo que resulta práctico en aplicaciones como la agregación de
datos, la creación de estructuras de datos más  complejas  y  la  organización  de  la  información.
Además, facilita la integración de contenidos provenientes de diferentes fuentes y  su  presentación
de manera coherente.

Esta técnica se logra utilizando el operador aritmético (+),  que  permite  unir  tuplas  de  manera
eficiente. Dado que las tuplas en Python son objetos inmutables, las  tuplas  originales  permanecen
intactas tras la operación. Esto ayuda a evitar efectos no deseados y a mantener  la  integridad  de
los datos originales.

Por último, con esta técnica es posible combinar tuplas que contengan diferentes tipos de datos,  ya
sea en forma de variables o directamente como tuplas literales, lo que proporciona flexibilidad para
la manipulación de datos y la creación de estructuras dinámicas. Esto permite adaptar  soluciones  a
necesidades específicas, combinando diferentes tipos de datos y estructuras de  manera  eficiente  y
efectiva."""

# Ejemplo_fusion_de_tuplas.py

# Explicación:
"""Definimos dos variables llamadas "tupla_1" y "tupla_2", y les asignamos las tuplas (1,  2,  3)  y
(4, 5, 6), respectivamente. Estas tuplas representan dos conjuntos de datos  que  queremos  fusionar
para formar una tupla combinada que contenga todos los elementos de  ambas  tuplas,  además  de  los
elementos de una tupla literal adicional.

Luego, definimos una nueva variable llamada "tupla_fusionada" y le  asignamos  el  resultado  de  la
fusión de "tupla_1", "tupla_2" y la tupla literal "(7, 8, 9)" utilizando el operador aritmético (+).
Para ello, colocamos ambas variables y la tupla  literal  en  el  orden  deseado  de  fusión,  entre
paréntesis para mejorar la legibilidad y separadas por el operador aritmético (+).

De esta forma, las tuplas (1, 2, 3) y (4, 5, 6), contenidas en las variables "tupla_1" y  "tupla_2",
junto con la tupla literal "(7, 8, 9)", se combinan para formar una nueva tupla que  contiene  todos
los elementos. Esta combinación se realiza en el orden en que se encuentran las variables y la tupla
literal, por lo que el resultado de la fusión será la tupla: (1, 2, 3, 4, 5, 6, 7, 8, 9).

Por último, utilizamos la función "print()" para mostrar el resultado de la fusión  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" que indica que se trata del resultado  de
la fusión de las tuplas."""

# Código:
tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)

tupla_fusionada = (tupla_1 + tupla_2 + (7, 8, 9))
print(f"Este es el resultado de la fusión de las tuplas: {tupla_fusionada}")

# Nota Importante:
"""Es importante destacar que la fusión de tuplas no modifica las tuplas originales, sino  que  crea
una nueva tupla que contiene la combinación de las tuplas originales. Esto se debe a que las  tuplas
en Python son objetos inmutables y el operador (+) no  modifica  las  tuplas  existentes,  sino  que
genera una nueva tupla. Por lo tanto, cada vez que se fusionan tuplas, se genera una nueva tupla que
contiene el resultado de la fusión, mientras que las tuplas originales permanecen sin cambios.

Esta característica, combinada con la inmutabilidad de las  tuplas,  garantiza  la  seguridad  y  la
consistencia de los datos, ya que  las  tuplas  originales  no  se  ven  afectadas  por  operaciones
posteriores. Sin embargo, también es importante tener en cuenta que la  creación  de  nuevas  tuplas
puede tener un impacto en el rendimiento cuando se trabaja con grandes volúmenes de datos.

El uso de paréntesis en este caso no es necesario y no tiene ningún efecto  en  la  operación,  pero
puede ayudar a mejorar la legibilidad del código al indicar claramente que se  está  realizando  una
operación de fusión de tuplas. Además, el orden de las tuplas es importante,  ya  que  determina  el
resultado final de la fusión. Si se invierte el orden de las tuplas, el resultado  sería  diferente,
por lo que es fundamental prestar atención a la secuencia en la que  se  combinan  las  tuplas  para
obtener el resultado deseado.

Por último, cabe destacar que, en realidad, lo que estamos haciendo es  concatenar  las  tuplas  con
ayuda del operador aritmético (+), pero utilizamos el término "fusión" para describir el proceso  de
combinar las tuplas en una sola, ya que este término se utiliza comúnmente  para  referirse  a  este
proceso en un contexto más amplio y descriptivo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
