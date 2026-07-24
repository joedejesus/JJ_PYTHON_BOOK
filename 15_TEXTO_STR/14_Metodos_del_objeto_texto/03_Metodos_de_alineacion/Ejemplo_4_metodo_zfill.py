# Enunciado:
"""El método ".zfill()" en Python se utiliza para rellenar una  cadena  de  texto  con  ceros  a  la
izquierda hasta alcanzar una longitud total especificada. Este método es útil en situaciones en  las
que se requiere un formato numérico uniforme o alinear cadenas de texto de manera consistente.

Este método toma una cadena de texto y devuelve una nueva cadena con ceros añadidos a la  izquierda.
Además, puede aplicarse a cualquier objeto de tipo texto, ya sea una variable, una cadena literal  o
el resultado de una expresión que genere una cadena de texto. La  cadena  utilizada  puede  contener
cualquier tipo de caracteres, incluyendo letras, números y símbolos, ya  que  el  método  se  centra
únicamente en el relleno con ceros a la izquierda. Si la cadena comienza con  un  signo  positivo  o
negativo, los ceros se insertan después de dicho signo.

El método ".zfill()" toma solo un argumento: el ancho total de la cadena resultante. Este  argumento
debe ser un número entero que especifica la  longitud  total  deseada  para  la  cadena  resultante,
incluyendo el texto original y los ceros añadidos. Si la longitud de la cadena original es  mayor  o
igual al ancho especificado, el método  devuelve  la  cadena  original  sin  modificaciones.  Si  la
longitud de la cadena original es menor, se agregan ceros a la izquierda  hasta  alcanzar  el  ancho
deseado.

Es importante destacar que este método no altera la cadena original, ya que las  cadenas  en  Python
son inmutables. En su lugar, genera y devuelve una nueva cadena  con  los  cambios  aplicados.  Esto
significa que cualquier transformación realizada con este método debe ser almacenada  en  una  nueva
variable o sobrescribir la variable existente si se desea conservar el resultado.

En resumen, el método ".zfill()" es una herramienta sencilla y eficiente para rellenar  cadenas  con
ceros a la izquierda, permitiendo un control preciso sobre el formato y la presentación  de  cadenas
de texto. Su facilidad de uso lo convierte en una opción ideal para tareas de  formateo  en  Python,
siempre y cuando se comprenda su funcionamiento y se utilice  de  manera  adecuada  en  el  contexto
correcto."""

# Ejemplo_4_metodo_zfill.py

# Explicación:
"""Definimos una variable llamada "numero" y le asignamos una cadena  de  texto  que  representa  un
número. Esta cadena de texto se utilizará para demostrar el funcionamiento del método ".zfill()".

A continuación, definimos una nueva variable llamada "numero_relleno" y le asignamos el resultado de
aplicar el método ".zfill()" a la variable "numero". Especificamos un ancho total de 15  caracteres.
Para ello, escribimos el nombre de la variable seguido del nombre del método ".zfill()", y dentro de
los paréntesis, pasamos el ancho total (15) como argumento.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" para indicar que se trata del resultado de  aplicar  el
método al texto contenido en la variable "numero".

De esta forma, hemos rellenado la cadena de texto original con ceros a la izquierda  hasta  alcanzar
un ancho de 15 caracteres totales."""

# Código:
numero = "12345"
numero_relleno = numero.zfill(15)
print(f"Este es el resultado de aplicar el método al texto: '{numero_relleno}'")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".zfill()" no realiza cambios en la cadena original,
ya que las cadenas en Python son inmutables. Esto significa que cada vez que se aplica este  método,
se genera una nueva cadena como resultado, dejando intacta la cadena original.  Este  comportamiento
asegura que las  operaciones  realizadas  sobre  cadenas  sean  seguras  y  no  introduzcan  efectos
secundarios inesperados en otras partes del programa.

Si se desea conservar el resultado del método ".zfill()", es necesario  asignarlo  explícitamente  a
una nueva variable o sobrescribir la  variable  original.  De  lo  contrario,  el  resultado  de  la
transformación se perderá, ya que no se almacena  automáticamente.  Este  detalle  es  crucial  para
evitar errores comunes al trabajar con cadenas en Python.

En cuanto al ancho total, este se refiere a la longitud total de la cadena resultante,  incluido  el
texto original y los ceros agregados. Por ejemplo, si tenemos una cadena de texto con  una  longitud
de 5 caracteres y queremos rellenarla hasta un ancho total de  15  caracteres,  usaremos  el  método
".zfill()" con un argumento de 15, lo que agregará 10 ceros a la izquierda y dejará un total  de  15
caracteres en la cadena resultante.

Aunque este método es extremadamente útil para rellenar cadenas con ceros, es importante  considerar
el contexto en el que se utiliza. Por ejemplo, en aplicaciones donde el formato numérico es  crítico
o donde se requiere un formato uniforme, este método es ideal. Sin embargo, debe usarse con  cuidado
para garantizar que el resultado sea adecuado para el propósito deseado.

En resumen, el método ".zfill()" es una herramienta sencilla y eficiente para el formateo  de  texto
en Python, pero su uso debe ser acompañado  de  una  comprensión  clara  de  sus  características  y
limitaciones. Esto permitirá aprovechar al máximo sus capacidades y evitar  posibles  inconvenientes
en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
