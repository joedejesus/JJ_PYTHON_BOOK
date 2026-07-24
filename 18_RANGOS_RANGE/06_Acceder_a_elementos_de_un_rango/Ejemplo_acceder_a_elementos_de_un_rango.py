# Enunciado:
"""Para acceder a elementos de un rango en Python, se utiliza el índice del rango. El índice  es  un
número entero que identifica la posición de un elemento en un rango. Los  índices  en  Python,  para
cualquier secuencia ordenada, comienzan desde 0. Esto significa que el primer elemento de  un  rango
tiene el índice 0, el segundo elemento tiene el índice 1,  y  así  sucesivamente.  Este  sistema  de
indexación es fundamental para trabajar con secuencias en Python, ya que permite acceder  de  manera
directa a cualquier elemento de la secuencia utilizando su posición.

Los rangos en Python son secuencias ordenadas de números, y cada número tiene  un  índice  asociado.
Los rangos son inmutables, lo que significa que no es posible modificar sus  elementos  directamente
una vez que han sido creados. Además, los rangos son iterables, lo que permite recorrer o acceder  a
cada elemento individualmente utilizando su índice u otros métodos de iteración.

Esta técnica es muy útil para inspeccionar partes específicas de un rango, ya que cada número  tiene
una posición definida dentro del rango. Además, el uso de índices negativos permite  acceder  a  los
elementos desde el final del rango, donde el índice "-1" corresponde al último elemento,  el  índice
"-2" al penúltimo, y así sucesivamente. Esta flexibilidad hace que el manejo de rangos en Python sea
muy versátil y potente.

Por último, es importante destacar que, al trabajar con rangos, el número final del  rango  definido
no se incluye en el resultado. Esto significa que, si intentamos acceder a un índice igual  o  mayor
que la longitud del rango, se generará un error de tipo "IndexError", ya que  ese  índice  no  forma
parte del rango."""

# Ejemplo_acceder_a_elementos_de_un_rango.py

# Explicación:
"""Definimos una variable llamada "rango" y le asignamos un rango que genera números enteros desde 1
hasta 20. Este rango se utilizará para acceder a sus elementos mediante sus índices.

A continuación, definimos una variable llamada "elemento" y le asignamos el resultado de aplicar  el
operador de indexación "[]" a la variable "rango" con el índice 5. Para ello, utilizamos el operador
de indexación con el número cinco en su interior, "[5]", precedido de la variable "rango", donde  el
número dentro de los corchetes representa el índice del elemento al que queremos acceder.

De esta forma, obtenemos el elemento que se encuentra en la sexta posición del rango,  que  es  "6",
correspondiente al índice 5.

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string", que indica que el elemento corresponde al  índice  5  del
rango.

Por último, accedemos a otros dos elementos del rango directamente utilizando la  función  "print()"
en formato "f-string" y el operador de indexación "[]" con los índices correspondientes. Para  ello,
utilizamos el operador de indexación con el número dieciocho en su interior, "[18]", precedido de la
variable "rango" para acceder al décimo noveno elemento del rango, que es "19",  y  el  operador  de
indexación con el número menos doce en su interior, "[-12]", precedido de la variable  "rango"  para
acceder al octavo elemento del rango, que es "8".

En ambos casos, las operaciones se realizan dentro de las llaves {} de las expresiones de la  cadena
"f-string" para mostrar  el  resultado  sin  necesidad  de  asignarlo  a  una  variable  intermedia,
acompañadas de un mensaje descriptivo que indica que los elementos corresponden al índice  18  y  al
índice -12 del rango, respectivamente."""

# Código:
rango = range(1, 21)

elemento = rango[5]
print(f"Este es el elemento correspondiente al índice 5 del rango: {elemento}")

print(f"Este es el décimo noveno elemento del rango: {rango[18]}")
print(f"Este es el octavo elemento desde el inicio del rango: {rango[-12]}")

# Nota Importante:
"""Es fundamental tener en cuenta que los índices en Python comienzan desde 0, lo que significa  que
el primer elemento de un rango está  en  la  posición  0,  el  segundo  en  la  posición  1,  y  así
sucesivamente.

Python también permite el uso de índices negativos para acceder a los elementos desde el  final  del
rango. Los índices negativos permiten contar desde el final de la secuencia hacia el inicio,  siendo
"-1" el índice del último elemento. Además, en el caso de los rangos, no se debe tener en cuenta  el
número final del rango definido, ya que este no se incluye en el resultado.

Por ejemplo, si se tiene un rango definido como "range(1, 11)", el número "11" no se incluye  en  el
rango, por lo que, al usar índices negativos, el número final del rango no se considerará como parte
del resultado al aplicar los operadores de indexación. Por lo tanto, el índice "-1" se  referirá  al
número "10", el índice "-2" se referirá al número "9", y así sucesivamente.

Además, es importante destacar  que,  si  se  utilizan  rangos  con  pasos,  la  indexación  seguirá
funcionando sobre los elementos que realmente formen parte del rango. Esto significa que los índices
no representan los valores numéricos originales, sino las posiciones de los elementos generados.

Por ejemplo, si se tiene un rango definido como  "range(0,  11,  2)"  y  se  accede  al  índice  "5"
utilizando "rango[5]", el resultado será "10", porque ese es el sexto elemento del rango generado.

Por último, intentar acceder a un índice fuera del rango generará un error de tipo "IndexError", por
lo que es importante asegurarse de que el índice esté dentro de los límites del rango.  Para  evitar
este error, se puede utilizar la función "len()" para determinar la longitud del rango y  garantizar
que los índices utilizados estén dentro del rango válido. Estas características hacen que el  manejo
de índices en Python sea una herramienta poderosa para trabajar con rangos  de  manera  eficiente  y
segura."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
