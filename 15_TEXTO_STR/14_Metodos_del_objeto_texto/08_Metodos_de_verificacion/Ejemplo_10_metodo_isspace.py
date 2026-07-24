# Enunciado:
"""El método ".isspace()" en Python se utiliza para verificar si todos los caracteres de una  cadena
son espacios en blanco. Este método devuelve un valor booleano: "True" si todos los  caracteres  son
espacios en blanco y "False" en caso contrario.

Los espacios en blanco incluyen caracteres como el espacio  estándar,  las  tabulaciones  (\t),  los
saltos de línea (\n), además de otros caracteres que se  consideran  espacios  en  blanco  según  la
definición de "Unicode", como el espacio de no separación, el espacio "em" y el espacio "en",  entre
otros.

El método ".isspace()" toma una cadena de texto y verifica si todos los caracteres son  espacios  en
blanco. Si la cadena cumple con esta condición, el método devuelve "True"; de lo contrario, devuelve
"False". Además, si la cadena está vacía, el método devuelve "False", ya que no contiene  caracteres
de espacio en blanco.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, una variable que contenga texto o incluso como resultado de una expresión que  devuelva  un
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve un valor booleano como resultado de la verificación. Si  se  desea
conservar el resultado de la verificación, es necesario asignarlo a  una  nueva  variable  o  usarlo
directamente en una operación posterior.

El método ".isspace()" no requiere ningún argumento adicional para  su  funcionamiento,  ya  que  su
función principal es verificar la composición de la cadena de texto.

Por último, el método ".isspace()" es una herramienta sencilla y eficiente para comprobar  si  todos
los caracteres de una cadena son espacios en blanco, lo que lo hace útil en diversas aplicaciones de
validación y procesamiento de texto, como validar entradas de usuario, asegurarse de que una  cadena
contiene solo espacios en blanco y realizar verificaciones rápidas en cadenas de texto."""

# Ejemplo_10_metodo_isspace.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene caracteres
de espacio en blanco estándar, además de una tabulación (\t) y un salto de línea  (\n),  los  cuales
son considerados espacios en blanco por el método ".isspace()". Esta cadena de  texto  se  utilizará
para demostrar el funcionamiento del método ".isspace()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".isspace()" a la variable "texto" sin argumentos. Para ello, escribimos el nombre
de la variable "texto" seguido del nombre del método ".isspace()" con los paréntesis vacíos, ya  que
este método no requiere argumentos adicionales.

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica si  todos  los  caracteres  de  la  cadena  son
espacios en blanco o no.

De esta forma, hemos verificado si todos los  caracteres  de  la  cadena  son  espacios  en  blanco,
obteniendo un valor booleano almacenado en la variable "resultado" que indica  el  resultado  de  la
verificación. En este caso, el resultado es "True", ya que  en  la  cadena  "  \t  \n  "  todos  los
caracteres son espacios en blanco, incluyendo el espacio estándar,  la  tabulación  y  el  salto  de
línea.

Por último, también mostramos el resultado directamente al  aplicar  el  método  ".isspace()"  a  la
variable "texto" dentro de la función  "print()",  de  esta  forma:  "print(texto.isspace())",  para
verificar el resultado de manera inmediata sin necesidad de almacenar el valor en una  variable,  lo
que puede ser útil para validaciones rápidas o para obtener una respuesta directa sin  necesidad  de
realizar operaciones adicionales con el resultado."""

# Código:
texto = " \t \n "
resultado = texto.isspace()
print(f"¿Todos los caracteres de la cadena de texto '{texto}' son espacios en blanco? {resultado}")

print(texto.isspace())

# Nota Importante:
"""Este método no modifica la cadena original, ya que las cadenas en  Python  son  inmutables.  Esto
significa que siempre genera un valor booleano como resultado de su aplicación, dejando  intacta  la
cadena original.

Es fundamental tener en cuenta que el método ".isspace()" considera espacios  en  blanco  caracteres
como el espacio estándar, las tabulaciones (\t), los saltos de línea  (\n)  y  otros  caracteres  de
espacio en blanco definidos por "Unicode" como el espacio de no separación, el espacio de "em" y  el
espacio de "en", entre otros. Por lo tanto, si la cadena de texto contiene al menos un carácter  que
no sea un espacio en blanco, el método devolverá "False".

Además, este método solo devuelve "True" si todos los caracteres de la cadena son espacios en blanco
y la cadena no está vacía.

Por último, hay que tener en cuenta que este método es ideal para validaciones rápidas en cadenas de
texto, como verificar si una entrada de usuario contiene solo espacios en blanco o asegurarse de que
una cadena está compuesta únicamente por espacios en blanco, lo  que  puede  ser  útil  en  diversas
aplicaciones de procesamiento de texto  y  validación  de  datos,  como  contraseñas  y  nombres  de
usuario."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
