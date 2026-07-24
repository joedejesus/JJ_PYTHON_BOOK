# Enunciado:
"""Crea una variable "global" llamada "contador" e inicialízala con el valor 0. Escribe un  programa
que utilice funciones para modificar esta variable. La primera función debe incrementar el valor  de
"contador" en 1 cada vez que se llame. La segunda función debe restablecer el valor de "contador"  a
0 cuando se llame.

Finalmente, el programa debe llamar a la función de incremento 5 veces y luego llamar a  la  función
de reseteo 1 vez. Verifica que el valor de "contador" se restablezca correctamente al  final  de  la
ejecución del código. No olvides usar la palabra clave "global" para hacer referencia a la  variable
"contador" desde dentro de los ámbitos internos de ambas funciones. Además,  usa  dos  bucles  "for"
para llamar a las funciones tantas veces como sea necesario."""

# Ejercicio_palabra_clave_global.py

# Explicación:
"""Definimos una variable global llamada "contador" y le asignamos  el  valor  inicial  de  0.  Esta
variable contiene el valor actual del "contador" y será modificada e incrementada por las  funciones
definidas posteriormente en el código hasta que se reinicie y adquiera el  valor  de  0  nuevamente.
Esta variable es accesible desde cualquier parte del código, incluso desde dentro de las  funciones.
Sin embargo, su valor solo podrá ser modificado desde un ámbito local si se  declara  explícitamente
como global utilizando la palabra clave "global", evitando así crear una nueva variable local con el
mismo nombre dentro del ámbito de la función.

Definimos una  función  llamada  "incrementar_contador()"  que  no  recibe  parámetros.  Para  ello,
utilizamos  la  palabra  clave  "def"  seguida  del   nombre   de   la   función,   en   este   caso
"incrementar_contador", seguido de paréntesis vacíos () ya que no recibe  parámetros,  y  terminamos
con dos puntos (:) para indicar el inicio del bloque de código asociado a la función.  Esta  función
se encargará de incrementar el valor de la variable global "contador" en 1 cada vez que sea llamada.

Dentro de la función, hacemos referencia a la variable global "contador", la  cual  tiene  el  valor
inicial "0". Para ello, utilizamos la palabra clave "global" seguida del nombre de la  variable,  en
este caso "contador". De esta forma indicamos al intérprete que queremos trabajar  con  la  variable
global en lugar de crear una nueva variable local con el mismo nombre ya que se encuentra dentro del
ámbito de la función y queremos trabajar con la  variable  global  definida  fuera  de  la  función.
Colocamos esta línea de código con una indentación de cuatro espacios desde el margen izquierdo para
indicar que forma parte del cuerpo de la función y  debe  ejecutarse  siempre  que  la  función  sea
llamada.

A continuación, incrementamos el valor de la variable global "contador" en 1 cada vez que se llama a
la función, hasta completar las cinco llamadas previstas antes de restablecerlo a 0 con  la  función
"resetear_contador()". Para ello utilizamos la expresión "contador +=  1".  Esta  expresión  es  una
forma abreviada de escribir "contador = contador + 1", lo que significa que estamos tomando el valor
actual de "contador", sumándole 1 y luego asignando el  resultado  a  la  propia  variable  en  cada
llamada a la función. Al haber declarado  "contador"  como  global  previamente,  esta  modificación
afectará el valor de "contador" en el ámbito global.

De esta forma, cada vez que se llame a la función "incrementar_contador()", el valor  de  "contador"
se incrementará en 1 tanto dentro como fuera  de  la  función,  es  decir,  en  todos  los  ámbitos.
Colocamos esta línea de código con una indentación de cuatro espacios desde el margen izquierdo para
indicar que forma parte del cuerpo de la función y  debe  ejecutarse  siempre  que  la  función  sea
llamada.

Además, utilizamos la instrucción "return" para devolver el valor actualizado de "contador" cada vez
que se llame a la función "incrementar_contador()". La instrucción "return" indica al intérprete que
la función debe finalizar su ejecución y enviar los valores especificados de vuelta al  lugar  donde
fue llamada. Para ello escribimos la palabra clave  "return"  seguida  del  nombre  de  la  variable
"contador". En este caso, estamos devolviendo el resultado en  una  sola  instrucción  en  forma  de
número  entero  (int),  que  representa  el  valor  actual  de  "contador"  después  de  haber  sido
incrementado. Colocamos esta línea de código con una indentación de cuatro espacios desde el  margen
izquierdo para indicar que forma parte del bloque de código asociado a la función y debe  ejecutarse
siempre que la función sea llamada.

Luego, utilizamos un bucle "for" para llamar a la función "incrementar_contador()" 5 veces cada  vez
que se ejecute el código. Esto nos permite incrementar el valor de  la  variable  global  "contador"
tantas veces como llamemos a la función y sea necesario, en este caso 5, en una sola  ejecución  del
código.

Para ello, escribimos la palabra clave "for", seguida  de  la  variable  "i",  que  representa  cada
iteración o elemento de la secuencia y la cual definimos en este momento, seguida del operador  "in"
para indicar dónde queremos que se realice la iteración y el nombre de la  secuencia  sobre  la  que
queremos iterar, en este caso "range(5)". Este rango representa una secuencia de números enteros que
va desde 0 hasta 4 (excluyendo el 5). De esta forma, el bucle se ejecutará y llamará  a  la  función
cinco veces, una por cada número en la secuencia generada por "range(5)". A continuación, escribimos
dos puntos (:) para indicar el final de la expresión y el inicio del bloque de  código  asociado  al
bucle "for".

Dentro  del  bucle   "for",   igualamos   la   variable   "i"   a   la   llamada   de   la   función
"incrementar_contador()" para que en cada iteración del bucle se llame a la función y se  incremente
el valor de "contador" en 1. Para ello, escribimos el nombre de la variable "i" y  le  asignamos  la
llamada a la función  "incrementar_contador()"  utilizando  el  operador  de  asignación  (=).  Esto
significa que en cada iteración del bucle, "i" tomará el valor actualizado de "contador" después  de
haber sido incrementado por la función y devuelto por la instrucción "return" desde la función.

Por último, dentro del bucle "for", utilizamos la función "print()" para mostrar el valor actual  de
"contador", en este caso representado por la variable "i", después de cada incremento, acompañado de
un mensaje descriptivo en formato "f-string". De esta forma, podemos ver cómo el valor de "contador"
cambia con cada llamada a la función "incrementar_contador()" en cada iteración del bucle.

Colocamos el código asociado al bucle "for" con una indentación de cuatro espacios desde  el  margen
izquierdo para indicar que forma parte del bloque de código asociado al bucle y debe  ejecutarse  en
cada iteración del mismo.

Repetimos los procesos anteriores para definir una segunda función llamada  "resetear_contador()"  y
un bucle "for" que llame a esta función una vez  para  restablecer  el  valor  de  "contador"  a  0.
Simplemente cambiamos el nombre de la función y el cuerpo  de  la  función  para  que  en  lugar  de
incrementar "contador", lo restablezca a 0.

En el bucle "for", cambiamos el rango a 1 para que la función se llame solo una vez y, en la función
"resetear_ contador()", asignamos el valor 0 a la variable global "contador" utilizando la expresión
"contador = 0". De esta forma, al final de la ejecución  del  código,  el  valor  de  "contador"  se
restablecerá correctamente a 0 después de haber sido incrementado 5 veces."""

# Código:
contador = 0

def incrementar_contador():
    global contador
    contador += 1
    return contador

for i in range(5):
    i = incrementar_contador()
    print(f"Contador después de incrementar: {i}")

def resetear_contador():
    global contador
    contador = 0
    return contador

for i in range(1):
    i = resetear_contador()
    print(f"Contador después de resetear: {i}")

# Nota Importante:
"""El bucle "for" se utiliza aquí para llamar varias veces a las funciones "incrementar_contador"  y
"resetear_contador".  En  el  primer   caso,   el   bucle   se   ejecuta   5   veces,   llamando   a
"incrementar_contador" en cada iteración. Esto permite incrementar el valor de  la  variable  global
"contador" de forma repetida. En el segundo caso, aunque el  bucle  se  ejecuta  solo  una  vez,  se
utiliza  para  demostrar  cómo  se  puede  restablecer  el  valor  de  "contador"  a  0  llamando  a
"resetear_contador".

La palabra clave "global" en Python permite que una función acceda y modifique una variable definida
en el ámbito global del programa. Esto es útil cuando se necesita que una variable sea compartida  y
manipulada por múltiples funciones. En este caso,  se  utiliza  "global"  para  garantizar  que  las
funciones puedan modificar directamente el valor de "contador" definido fuera de  su  ámbito  local.
Este enfoque es importante para comprender cómo gestionar el estado global en un programa y cómo las
funciones pueden interactuar con variables globales de manera controlada.

Las variables globales son accesibles  desde  cualquier  parte  del  código,  incluyendo  dentro  de
funciones y bucles. Sin embargo, para modificar su valor o trabajar con ellas dentro de una  función
es necesario declarar la variable como global utilizando la palabra clave "global".  Esto  evita  la
creación de una nueva variable local con el mismo nombre y  permite  que  la  función  modifique  la
variable global existente.

Por último, es importante destacar que el uso de variables globales  puede  ser  útil  en  programas
pequeños o simples, como en este caso, pero en programas más grandes puede  llevar  a  problemas  de
mantenimiento y errores difíciles de depurar. Por ello, se recomienda limitar su  uso  y  considerar
alternativas como el paso de parámetros o el uso de clases para encapsular el estado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
