# Enunciado:
"""El método ".isdecimal()" en Python se utiliza para verificar  si  todos  los  caracteres  de  una
cadena de texto son caracteres decimales. Este método devuelve un valor booleano:  "True"  si  todos
los caracteres son decimales, y "False" en caso contrario.

Los caracteres decimales incluyen  los  dígitos  del  0  al  9  y  otros  caracteres  numéricos  que
representan números decimales en otros  sistemas  de  escritura.  Por  ejemplo,  en  el  sistema  de
numeración arábigo-índico, los caracteres decimales son "٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨",
"٩". Sin embargo, los caracteres decimales no incluyen signos  de  puntuación,  letras,  espacios  o
caracteres especiales.

El método ".isdecimal()" toma una cadena de texto y verifica si todos los caracteres de  esa  cadena
son decimales. Si la cadena cumple con esta condición, el método devuelve "True"; de  lo  contrario,
devuelve "False".

Además, es importante tener en cuenta que el método ".isdecimal()" devuelve "False" si se  aplica  a
una cadena vacía, ya que no contiene caracteres decimales. Este comportamiento es  diferente  al  de
otros métodos como ".isascii()", que devuelven "True" para cadenas vacías.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, una variable que contenga texto o incluso como resultado de una expresión que  devuelva  un
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve un valor booleano como resultado de la verificación. Si  se  desea
conservar el resultado de la verificación, es necesario asignarlo a  una  nueva  variable  o  usarlo
directamente en una operación posterior.

El método ".isdecimal()" no requiere ningún argumento adicional para su funcionamiento,  ya  que  su
función principal es verificar la composición de la cadena de texto.

Por último, el método ".isdecimal()" es una herramienta sencilla y eficiente para verificar  si  una
cadena está compuesta únicamente  por  caracteres  decimales,  lo  que  lo  hace  útil  en  diversas
aplicaciones de validación y procesamiento de texto, como validar entradas de usuario, asegurarse de
que una cadena contiene únicamente números decimales y realizar verificaciones rápidas en cadenas de
texto."""

# Ejemplo_4_metodo_isdecimal.py

# Explicación:
"""Definimos una variable llamada "texto"  y  le  asignamos  una  cadena  de  texto  únicamente  con
caracteres decimales. Esta cadena de texto se utilizará para demostrar el funcionamiento del  método
".isdecimal()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".isdecimal()" a la variable "texto" sin  argumentos.  Para  ello,  escribimos  el
nombre de la variable "texto" seguido del  nombre  del  método  ".isdecimal()"  con  los  paréntesis
vacíos, ya que este método no requiere argumentos adicionales.

Además, utilizamos la función "print()" para mostrar el resultado en la  consola  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica si la  cadena  contiene  únicamente  caracteres
decimales o no.

De esta forma, hemos verificado si la cadena está compuesta  únicamente  por  caracteres  decimales,
obteniendo un valor booleano almacenado en la variable "resultado" que indica  el  resultado  de  la
verificación. En este caso, el resultado es "True", ya que la cadena  "012345"  contiene  únicamente
caracteres decimales.

Por último, también mostramos el resultado directamente aplicando  el  método  ".isdecimal()"  a  la
variable "texto" dentro de la función "print()", de  esta  forma:  "print(texto.isdecimal())",  para
verificar el resultado de manera inmediata sin necesidad de almacenar el valor en una  variable,  lo
que puede ser útil para validaciones rápidas o para obtener una respuesta directa sin  necesidad  de
realizar operaciones adicionales."""

# Código:
texto = "012345"
resultado = texto.isdecimal()
print(f"¿La cadena de texto '{texto}' contiene únicamente caracteres decimales? {resultado}")

print(texto.isdecimal())

# Nota Importante:
"""Este método no modifica la cadena original, ya que las cadenas en  Python  son  inmutables.  Esto
significa que siempre genera un valor booleano como resultado de su aplicación, dejando  intacta  la
cadena original.

Los caracteres decimales incluyen  los  dígitos  del  0  al  9  y  otros  caracteres  numéricos  que
representan números decimales en otros sistemas de escritura, como el sistema arábigo-índico. Por lo
tanto, si la cadena contiene caracteres fuera de este conjunto, como letras, espacios  o  caracteres
especiales, el método devolverá "False".

Es fundamental tener en cuenta que el método ".isdecimal()" considera inválidas las cadenas  vacías,
devolviendo "False" en estos casos. Por ejemplo, la cadena "" (vacía) no se  considera  decimal,  ya
que no contiene caracteres decimales.

Además, este método solo devuelve "True" si todos los caracteres de la cadena son decimales.  Si  la
cadena contiene cualquier otro tipo de carácter, como letras, espacios o caracteres  especiales,  el
método devolverá "False".

Por último, hay que tener en cuenta que este método es ideal para validaciones rápidas, pero  no  es
apropiado para análisis más complejos dentro de una cadena. En esos casos, se deben considerar otros
métodos o expresiones regulares para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
