# Enunciado:
"""La creación de subrangos es una técnica útil para manipular rangos  en  Python.  Permite  extraer
partes específicas de un rango original, lo que resulta útil en aplicaciones como  el  procesamiento
de datos, la limpieza de información y la generación de reportes.

Esta técnica se logra utilizando  índices  para  seleccionar  los  elementos  deseados  mediante  la
sintaxis de "slicing" o  rebanado.  El  "slicing"  emplea  operadores  de  indexación  que  permiten
especificar el inicio, el final y, opcionalmente, el paso del segmento que se desea extraer, lo  que
proporciona una forma eficiente y flexible de trabajar con secuencias. Además, esta funcionalidad es
compatible con índices negativos, lo que facilita el acceso a los elementos desde  el  final  de  la
secuencia hacia el principio."""

# Ejemplo_crear_subrangos.py

# Explicación:
"""Definimos una variable llamada "rango" y le asignamos un rango que genera números enteros desde 1
hasta 10. Para ello,  utilizamos  el  constructor  "range()"  con  los  argumentos  correspondientes
separados por comas; en este caso, el valor inicial "1" y el límite superior  "11".  Este  rango  se
utilizará para crear subrangos mediante la técnica de "slicing" o rebanado.

En primer lugar, definimos una variable llamada "sub_rango_1" y le asignamos el resultado de aplicar
el operador de indexación "[:5]" a la  variable  "rango".  Para  ello,  utilizamos  el  operador  de
indexación "[:5]" precedido por la  variable  "rango",  lo  que  indica  que  queremos  obtener  los
elementos desde el inicio hasta el índice "4". De esta forma, se  extraen  los  elementos  desde  el
inicio del rango hasta el índice "4" (excluyendo el índice "5").

En segundo lugar, definimos una variable llamada  "sub_rango_2"  y  le  asignamos  el  resultado  de
aplicar el operador de indexación "[:-4]" a la variable "rango". Para ello, utilizamos  el  operador
de indexación "[:-4]" precedido por la variable "rango", lo que  indica  que  queremos  obtener  los
elementos desde el inicio hasta el índice ubicado 4 posiciones antes del final sin incluirlo.

En este caso, el último elemento del rango es el número "10", ya que  el  valor  final  indicado  en
"range()" no se incluye. Por ello, el índice "-4" se refiere al cuarto  elemento  contado  desde  el
final, que corresponde al número "7".

Por último, utilizamos la función "print()" para mostrar el contenido de los subrangos en  forma  de
lista en la consola, acompañados de un mensaje descriptivo  en  formato  "f-string"  que  indica  el
contenido de cada subrango. Para ello, utilizamos el constructor "list()"  dentro  de  la  expresión
"f-string" para convertir los subrangos en listas  y,  de  esta  forma,  visualizar  claramente  los
números generados por cada subrango en lugar de  la  representación  del  objeto  rango,  es  decir,
"range(start, stop, step)".

De esta forma, hemos creado dos subrangos a partir del  rango  original  utilizando  la  técnica  de
"slicing", lo que nos permite extraer partes específicas del rango original de  manera  eficiente  y
flexible."""

# Código:
rango = range(1, 11)

sub_rango_1 = rango[:5]
print(f"Subrango que contiene los primeros 5 elementos: {list(sub_rango_1)}")

sub_rango_2 = rango[:-4]
print(f"Subrango que contiene los elementos desde el inicio hasta 4 elementos antes del final: {list(sub_rango_2)}")

# Nota Importante:
"""En Python, los índices comienzan en 0, lo que significa que el primer elemento de un rango  tiene
el índice "0", el segundo elemento tiene el índice "1" y así sucesivamente.

Al usar "slicing", el índice de inicio se incluye  en  el  resultado,  mientras  que  el  índice  de
finalización se excluye. Por ejemplo, si se especifica  "rango[0:3]",  se  obtendrán  los  elementos
desde el índice "0" hasta el índice "2", pero no el elemento ubicado en  el  índice  "3".  Lo  mismo
ocurre con los índices negativos, donde el índice de inicio se incluye y el índice  de  finalización
se excluye. Por ejemplo, si se especifica "rango[:-2]", se obtendrán los elementos desde  el  inicio
del rango hasta el índice ubicado 2 posiciones antes del final, sin incluirlo.

Es importante destacar que los índices negativos permiten contar desde  el  final  de  la  secuencia
hacia el inicio, siendo "-1" el índice del último elemento. Además, en el caso de los rangos, no  se
debe tomar en cuenta el valor final indicado al definir el rango, ya que este no se  incluye  en  el
resultado.

Por ejemplo, si se tiene un rango definido como "range(1, 11)", el número "11" no se incluye  en  el
rango. Por lo tanto, al usar índices negativos y aplicar "slicing", el índice "-1"  se  referirá  al
número "10", el índice "-2" se referirá al número "9", y así sucesivamente.

También es importante destacar que, si se utilizan rangos con paso, el comportamiento de los índices
sigue siendo el mismo, pero se debe tener en cuenta  que  el  paso  puede  afectar  la  cantidad  de
elementos obtenidos en el subrango, ya que determina qué posiciones se seleccionan. Por ejemplo,  si
se tiene un rango definido como "range(1, 11,  2)"  y  se  aplica  "rango[0:4]",  se  obtendrán  los
elementos desde el índice "0" hasta el índice "3" (excluyendo el  índice  "4").  En  este  caso,  el
resultado será "1", "3", "5" y "7", porque esos son los valores almacenados en esas  posiciones  del
rango.

Por último, es fundamental tener en cuenta que el uso de índices fuera  del  rango  no  generará  un
error, sino que simplemente devolverá un subrango vacío o el segmento disponible hasta el  final  de
la secuencia, dependiendo de la dirección del "slicing". Esto hace que la técnica de  "slicing"  sea
robusta y fácil de usar para manipular secuencias en Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────