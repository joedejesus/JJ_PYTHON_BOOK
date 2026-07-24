# Enunciado:
"""El método ".partition()" en Python se utiliza para dividir una cadena en tres  partes:  la  parte
anterior al separador, el separador en sí y la parte posterior al separador.  Este  método  devuelve
una tupla con estas tres partes, lo que permite un control preciso sobre cómo se divide la cadena.

El método ".partition()" toma  una  cadena  de  texto  y  la  divide  en  función  de  un  separador
especificado como argumento, devolviendo una tupla con  las  partes  resultantes.  Si  la  subcadena
especificada como argumento, es decir, el separador, no se  encuentra  en  la  cadena  original,  el
método devuelve una tupla con la cadena original como primer elemento  y  dos  cadenas  vacías  como
segundo y tercer elemento.

Este método toma un argumento obligatorio, que es la subcadena que se desea utilizar como  separador
para dividir la cadena  original.  Este  argumento  debe  ser  una  cadena  de  texto  que  coincida
exactamente con una parte de la cadena original, ya que  el  método  distingue  entre  mayúsculas  y
minúsculas. De otro modo, la separación no se realizará y el resultado no será el esperado.

Además, el método tomará como separador la primera  aparición  de  la  subcadena  especificada  como
argumento, lo que significa que, si la cadena original contiene varias  apariciones  del  separador,
este método solo dividirá la cadena en la primera aparición, dejando  el  resto  de  la  cadena  sin
dividir.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, en una variable que contenga texto o incluso como resultado de una expresión  que  devuelva
un texto. Además, este método no modifica la cadena original, ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve una nueva tupla con las partes resultantes. Si se desea  conservar
el resultado de la división, es necesario asignarlo a una nueva variable o  usarlo  directamente  en
una operación posterior.

Por último, el método ".partition()" es una herramienta especialmente útil para dividir  cadenas  de
texto en partes específicas de  manera  eficiente  y  sencilla,  especialmente  cuando  se  necesita
trabajar con las partes resultantes de la división."""

# Ejemplo_2_metodo_partition.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene  la  frase
"Antes y Después". Esta cadena de texto se utilizará para demostrar  el  funcionamiento  del  método
".partition()".

A continuación, definimos una nueva variable llamada "tupla" y le asignamos el resultado de  aplicar
el método ".partition()" a la variable "texto" con un argumento. Para ello, escribimos el nombre  de
la variable "texto", seguido del método ".partition()" y, entre los paréntesis del  método,  pasamos
como argumento el separador que queremos utilizar para dividir la cadena; en este caso, la subcadena
"y", entre comillas, para indicar que es una cadena de texto.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" que indica cómo se ha dividido la  cadena  original  en
las partes resultantes de la tupla.

El método buscará la primera aparición de la subcadena especificada  como  argumento  en  la  cadena
original y dividirá la cadena en tres partes: la parte anterior al separador, el separador en  sí  y
la parte posterior al separador. De esta forma, hemos dividido la cadena original  en  tres  partes,
basándonos en la primera aparición de la  subcadena  "y",  y  obtenido  una  tupla  con  las  partes
resultantes."""

# Código:
texto = "Antes y Después"
tupla = texto.partition("y")
print(f"El texto original: {texto}\nSe ha dividido en las siguientes partes de una tupla: {tupla}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".partition()"  no  realiza  cambios  en  la  cadena
original, ya que las cadenas en Python son inmutables. Esto significa  que  siempre  se  genera  una
nueva tupla como resultado de su aplicación, dejando intacta la cadena original.

Si se desea almacenar el resultado del método ".partition()", es necesario  asignarlo  a  una  nueva
variable o usar directamente el resultado en una operación posterior. De lo contrario, el  resultado
de la operación se perderá.

El método ".partition()" devuelve una tupla con las partes resultantes de la división, por lo que es
importante recordar que las tuplas son estructuras de datos inmutables  en  Python.  Esto  significa
que, una vez creada la tupla, no se pueden modificar sus  elementos.  Por  lo  tanto,  si  se  desea
trabajar con las partes resultantes de la división, es necesario acceder a ellas mediante índices  o
desempaquetado de tuplas.

Además, si el separador no se encuentra en la cadena original, el método devolverá una tupla con  la
cadena original como primer elemento y dos cadenas vacías  como  segundo  y  tercer  elemento.  Esto
permite manejar de manera sencilla y predecible los casos en los que el separador no está presente.

En cuanto a los espacios en blanco, el método ".partition()" no los elimina automáticamente.  Si  el
separador incluye espacios, estos se considerarán parte del separador y se  incluirán  en  la  parte
correspondiente de la tupla resultante. Por otro lado, si la cadena original contiene espacios antes
o después del separador, estos se mantendrán en las partes anterior y posterior al separador  en  la
tupla resultante. Por lo tanto, es importante tener en cuenta cómo se manejan los espacios en blanco
al utilizar el método ".partition()" para evitar resultados inesperados.

Por último, es importante destacar  que  el  método  ".partition()"  distingue  entre  mayúsculas  y
minúsculas, lo que significa que, si se proporciona un separador que no coincida exactamente con  la
cadena original, el método no realizará la división.  Por  lo  tanto,  el  argumento  debe  ser  una
subcadena que se encuentre exactamente en la cadena original. Si se proporciona un separador que  no
coincida exactamente, el método no realizará la división."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
