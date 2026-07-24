# Enunciado:
"""La creación de subtextos es una técnica fundamental en la manipulación de  cadenas  de  texto  en
Python. Permite extraer partes específicas de un texto original, lo que resulta útil en  una  amplia
variedad de aplicaciones, como el procesamiento de datos, la limpieza de información y la generación
de informes.

Esta técnica se logra utilizando índices  para  seleccionar  los  caracteres  deseados  mediante  la
sintaxis de "slicing" o rebanado.  El  "slicing"  utiliza  operadores  de  indexación  que  permiten
especificar el inicio, el final y, opcionalmente, el paso del segmento que se desea extraer, lo  que
proporciona una forma  eficiente  y  flexible  de  trabajar  con  cadenas  de  texto.  Además,  esta
funcionalidad es compatible con índices negativos, lo que facilita el acceso a los caracteres  desde
el final de la cadena hacia el principio."""

# Ejemplo_crear_subtextos.py

# Explicación:
"""Definimos una variable llamada "texto" y le  asignamos  una  cadena  de  texto.  Esta  cadena  se
utilizará para crear subtextos mediante la técnica de "slicing" o rebanado.

En primer lugar, definimos una variable llamada "sub_texto_1" y le asignamos el resultado de aplicar
el operador de indexación "[:5]" a la  variable  "texto".  Para  ello,  utilizamos  el  operador  de
indexación "[:5]" precedido por la  variable  "texto",  lo  que  indica  que  queremos  obtener  los
caracteres desde el inicio hasta el índice "4". De esta forma, se extraen los  caracteres  desde  el
inicio del texto hasta el índice "4" (excluyendo el índice "5").

En segundo lugar, definimos una variable llamada  "sub_texto_2"  y  le  asignamos  el  resultado  de
aplicar el operador de indexación "[:-5]" a la variable "texto". Para ello, utilizamos  el  operador
de indexación "[:-5]" precedido por la variable "texto", lo que  indica  que  queremos  obtener  los
caracteres desde el inicio hasta la posición ubicada 5 caracteres antes del final. De esta forma, se
extraen los caracteres desde el inicio del texto hasta esa posición (excluyendo el índice "-5").

En cada caso, utilizamos la función "print()" para mostrar el resultado de los subtextos creados  en
la consola, acompañados de un mensaje descriptivo en formato "f-string" que indica qué  subtexto  se
ha creado y qué caracteres contiene."""

# Código:
texto = "Texto de ejemplo para crear subtextos en Python."

sub_texto_1 = texto[:5]
print(f"Subtexto que contiene los primeros 5 caracteres: {sub_texto_1}")

sub_texto_2 = texto[:-5]
print(f"Subtexto que contiene los caracteres desde el inicio hasta 5 caracteres antes del final: {sub_texto_2}")

# Nota Importante:
"""En Python, los índices comienzan en 0, lo que significa que el primer carácter de un texto  tiene
"el índice 0", el segundo carácter tiene el índice "1" y así sucesivamente.

Al usar "slicing", el índice de inicio se incluye  en  el  resultado,  mientras  que  el  índice  de
finalización se excluye. Por ejemplo, si se especifica "texto[0:5]",  se  obtendrán  los  caracteres
desde el índice "0" hasta el índice "4", pero no el carácter en el índice "5". Lo mismo  ocurre  con
los índices negativos, donde el índice de inicio se incluye y el índice de finalización se  excluye.
Por ejemplo, si se especifica "texto[:-5]", se obtendrán los caracteres desde el  inicio  del  texto
hasta la posición ubicada 5 posiciones antes del final (excluyendo el índice "-5").

Es importante destacar que los índices negativos permiten contar desde el final de la  cadena  hacia
el principio, siendo "-1"  el  índice  del  último  carácter.  Esto  añade  una  capa  adicional  de
flexibilidad al trabajar con cadenas de texto,  ya  que  se  pueden  combinar  índices  positivos  y
negativos para obtener resultados específicos.

Por último, es fundamental tener en cuenta que el uso de índices fuera del rango  de  la  cadena  no
generará un error, sino que simplemente devolverá una subcadena vacía o el segmento disponible hasta
el final de la cadena, dependiendo de la dirección del  "slicing".  Esto  hace  que  la  técnica  de
"slicing" sea robusta y fácil de usar para manipular cadenas de texto en Python.

Además, las comillas utilizadas para definir cadenas no se incluyen en el resultado  del  "slicing",
lo que significa que, al crear subtextos, solo se extraen los caracteres dentro de las comillas, sin
incluir las comillas en sí. Esto es importante para entender cómo se manipulan las cadenas de  texto
y cómo se crean subtextos en Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────