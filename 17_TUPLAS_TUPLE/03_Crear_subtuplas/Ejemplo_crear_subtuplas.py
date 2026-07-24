# Enunciado:
"""La creación de subtuplas es una técnica útil para la manipulación de tuplas  en  Python.  Permite
extraer partes específicas de una tupla original, lo  que  resulta  útil  en  aplicaciones  como  el
procesamiento de datos, la limpieza de información y la generación de reportes.

Esta técnica se logra utilizando  índices  para  seleccionar  los  elementos  deseados  mediante  la
sintaxis de "slicing" o rebanado.  El  "slicing"  utiliza  operadores  de  indexación  que  permiten
especificar el inicio, el final y, opcionalmente,  el  paso  del  segmento  que  se  desea  extraer,
proporcionando una forma eficiente y flexible de trabajar con tuplas. Además, esta funcionalidad  es
compatible con índices negativos, lo que facilita el acceso a los elementos desde  el  final  de  la
tupla hacia el principio."""

# Ejemplo_crear_subtuplas.py

# Explicación:
"""Definimos una variable llamada "tupla" y le asignamos una  tupla  de  elementos.  Esta  tupla  se
utilizará para crear subtuplas mediante la técnica de "slicing" o rebanado.

En primer lugar, definimos una variable llamada "sub_tupla_1" y le asignamos el resultado de aplicar
el operador de indexación "[:5]" a la  variable  "tupla".  Para  ello,  utilizamos  el  operador  de
indexación "[:5]" precedido de la variable "tupla", lo que indica que queremos obtener los elementos
desde el inicio hasta el índice "4". De esta forma, se extraen los elementos desde el inicio  de  la
tupla hasta el índice "4" (excluyendo el índice "5").

En segundo lugar, definimos una variable llamada  "sub_tupla_2"  y  le  asignamos  el  resultado  de
aplicar el operador de indexación "[:-4]" a la variable "tupla". Para ello, utilizamos  el  operador
de indexación "[:-4]" precedido de la variable "tupla", lo  que  indica  que  queremos  obtener  los
elementos desde el inicio hasta el elemento ubicado 4 posiciones antes del final. De esta forma,  se
extraen los elementos desde el inicio de la tupla hasta ese punto, excluyendo el índice "-4".

En cada caso, utilizamos la función "print()" para mostrar el resultado de las subtuplas creadas  en
la consola, acompañadas de un mensaje descriptivo en formato "f-string" que indica qué  subtupla  se
ha creado y qué elementos contiene."""

# Código:
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

sub_tupla_1 = tupla[:5]
print(f"Subtupla que contiene los primeros 5 elementos: {sub_tupla_1}")

sub_tupla_2 = tupla[:-4]
print(f"Subtupla que contiene los elementos desde el inicio hasta 4 elementos antes del final: {sub_tupla_2}")

# Nota Importante:
"""En Python, los índices comienzan en 0, lo que significa que el primer elemento de una tupla tiene
el índice "0", el segundo elemento tiene el índice "1" y así sucesivamente.

Al usar "slicing", el índice de inicio se incluye  en  el  resultado,  mientras  que  el  índice  de
finalización se excluye. Por ejemplo, si se especifica  "tupla[0:3]",  se  obtendrán  los  elementos
desde el índice "0" hasta el índice "2", pero no el elemento ubicado en  el  índice  "3".  Lo  mismo
ocurre con los índices negativos, donde el índice de inicio se incluye y el índice  de  finalización
se excluye. Por ejemplo, si se especifica "tupla[:-2]", se obtendrán los elementos desde  el  inicio
de la tupla hasta el índice que se encuentra 2 posiciones antes  del  final,  excluyendo  el  índice
"-2".

Es importante destacar que los índices negativos permiten contar desde el final de la tupla hacia el
inicio, siendo "-1" el índice del último elemento. Esto añade una capa adicional de flexibilidad  al
trabajar con tuplas, ya que se pueden combinar índices positivos y negativos para obtener resultados
específicos.

Por último, es fundamental tener en cuenta que el uso de índices fuera del  rango  de  la  tupla  no
generará un error, sino que simplemente devolverá una subtupla vacía o el segmento disponible  hasta
el final de la tupla, dependiendo de la dirección  del  "slicing".  Esto  hace  que  la  técnica  de
"slicing" sea robusta y fácil de usar para manipular tuplas en Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
