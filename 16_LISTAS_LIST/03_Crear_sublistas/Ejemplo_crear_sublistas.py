# Enunciado:
"""La creación de sublistas es una técnica fundamental en  la  manipulación  de  listas  en  Python.
Permite extraer partes específicas de una lista original, lo que resulta útil en una amplia variedad
de aplicaciones, como el procesamiento de datos, la limpieza  de  información  y  la  generación  de
informes.

Esta técnica se logra utilizando  índices  para  seleccionar  los  elementos  deseados  mediante  la
sintaxis de "slicing" o rebanado.  El  "slicing"  utiliza  operadores  de  indexación  que  permiten
especificar el inicio, el final y, opcionalmente, el paso del segmento que se desea extraer, lo  que
proporciona una forma eficiente y flexible de trabajar con listas.

Además, esta funcionalidad escompatible con índices negativos, lo  que  facilita  el  acceso  a  los
elementos desde el final de la lista hacia el principio."""

# Ejemplo_crear_sublistas.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una  lista  de  elementos.  Esta  lista  se
utilizará para crear sublistas mediante la técnica de "slicing" o rebanado.

En primer lugar, definimos una variable llamada "sub_lista_1" y le asignamos el resultado de aplicar
el operador de indexación "[:3]" a la  variable  "lista".  Para  ello,  utilizamos  el  operador  de
indexación "[:3]" precedido por la  variable  "lista",  lo  que  indica  que  queremos  obtener  los
elementos desde el inicio hasta el índice "2". De esta forma, se  extraen  los  elementos  desde  el
inicio de la lista hasta el índice "2" (excluyendo el índice "3").

En segundo lugar, definimos una variable llamada  "sub_lista_2"  y  le  asignamos  el  resultado  de
aplicar el operador de indexación "[:-2]" a la variable "lista". Para ello, utilizamos  el  operador
de indexación "[:-2]" precedido por la variable "lista", lo que  indica  que  queremos  obtener  los
elementos desde el inicio hasta el índice "-2". De esta forma, se extraen  los  elementos  desde  el
inicio de la lista hasta el índice que se encuentra dos posiciones antes del  final  (excluyendo  el
índice "-2").

En cada caso, utilizamos la función "print()" para mostrar el resultado de las sublistas creadas  en
la consola, acompañadas de un mensaje descriptivo en formato "f-string" que indica qué  sublista  se
ha creado y qué elementos contiene."""

# Código:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sub_lista_1 = lista[:3]
print(f"Sublista que contiene los primeros 3 elementos: {sub_lista_1}")

sub_lista_2 = lista[:-2]
print(f"Sublista que contiene los elementos desde el inicio hasta 2 elementos antes del final: {sub_lista_2}")

# Nota Importante:
"""En Python, los índices comienzan en 0, lo que significa que el primer elemento de una lista tiene
el índice "0", el segundo elemento tiene el índice "1" y así sucesivamente.

Al usar "slicing", el índice de inicio se incluye  en  el  resultado,  mientras  que  el  índice  de
finalización se excluye. Por ejemplo, si se especifica  "lista[0:3]",  se  obtendrán  los  elementos
desde el índice "0" hasta el índice "2", pero no el elemento en el índice "3".  De  la  misma  forma
ocurre con los índices negativos, donde el índice de inicio se incluye y el índice  de  finalización
se excluye. Por ejemplo, si se especifica "lista[:-2]", se obtendrán los elementos desde  el  inicio
de la lista hasta el índice que se encuentra dos posiciones antes del final  (excluyendo  el  índice
"-2").

Es importante destacar que los índices negativos permiten contar desde el final de la lista hacia el
principio, siendo "-1" el índice del último elemento. Esto añade una capa adicional de  flexibilidad
al trabajar con listas, ya que se  pueden  combinar  índices  positivos  y  negativos  para  obtener
resultados específicos.

Por último, es fundamental tener en cuenta que el uso de índices fuera del  rango  de  la  lista  no
genera un error, sino que simplemente devuelve una sublista vacía o el segmento disponible hasta  el
final de la lista, dependiendo de la dirección del "slicing". Esto hace que la técnica de  "slicing"
sea robusta y fácil de usar para manipular listas en Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
