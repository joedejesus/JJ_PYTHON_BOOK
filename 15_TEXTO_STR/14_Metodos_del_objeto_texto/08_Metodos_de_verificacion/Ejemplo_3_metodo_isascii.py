# Enunciado:
"""El método ".isascii()" en Python se utiliza para verificar si todos los caracteres de una  cadena
de texto pertenecen al conjunto "ASCII", es decir, si está compuesta únicamente por  caracteres  con
valores "ASCII". Este método devuelve un valor booleano: "True" si todos los  caracteres  pertenecen
al conjunto "ASCII" y "False" en caso contrario.

Los caracteres "ASCII" son aquellos que se encuentran dentro del rango de valores numéricos entre  0
y 127 de la tabla "ASCII". Estos caracteres incluyen letras mayúsculas y minúsculas, números, signos
de puntuación, espacios y caracteres de control. Sin embargo,  no  incluyen  caracteres  acentuados,
caracteres de idiomas distintos del inglés ni caracteres especiales que no pertenezcan  al  conjunto
"ASCII".

El método ".isascii()" toma una cadena de texto y verifica si todos los  caracteres  de  esa  cadena
pertenecen al conjunto "ASCII". Si la cadena cumple con esta condición, el método  devuelve  "True";
de lo contrario, devuelve "False".

Además, es importante tener en cuenta que el método ".isascii()" devuelve "True" si se aplica a  una
cadena vacía, ya que no  contiene  caracteres  fuera  del  rango  "ASCII".  Este  comportamiento  es
diferente del de otros métodos, como ".isalpha()", que devuelven "False" para cadenas vacías.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, en una variable que contenga texto o incluso como resultado de una expresión  que  devuelva
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve un valor booleano como resultado de la verificación. Si  se  desea
conservar el resultado de la verificación, es necesario asignarlo a  una  nueva  variable  o  usarlo
directamente en una operación posterior.

El método ".isascii()" no requiere ningún argumento adicional para  su  funcionamiento,  ya  que  su
función principal es verificar la composición de la cadena de texto.

Por último, el método ".isascii()" es una herramienta sencilla y eficiente  para  verificar  si  una
cadena está  compuesta  únicamente  por  caracteres  "ASCII",  lo  que  lo  hace  útil  en  diversas
aplicaciones de validación y procesamiento de texto, como validar entradas de usuario, asegurarse de
que una cadena no contenga caracteres "Unicode" y realizar  verificaciones  rápidas  en  cadenas  de
texto."""

# Ejemplo_3_metodo_isascii.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de  texto  compuesta  únicamente
"por caracteres ASCII". Esta cadena de texto se  utilizará  para  demostrar  el  funcionamiento  del
"método ".isascii()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".isascii()" a la variable "texto". Para ello, escribimos el nombre de la variable
"texto" seguido del nombre del método ".isascii()" con los paréntesis vacíos, ya que este método  no
requiere argumentos adicionales.

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica si la  cadena  contiene  únicamente  caracteres
"ASCII".

De esta forma, verificamos si la cadena está compuesta únicamente por caracteres "ASCII" y obtenemos
un valor booleano almacenado en la variable "resultado", que indica el resultado de la verificación.
En este caso, el resultado es "True", ya que la cadena "Python 3.13" contiene únicamente  caracteres
"ASCII".

Por último, también mostramos el resultado directamente al  aplicar  el  método  ".isascii()"  a  la
variable "texto" dentro de la función  "print()",  de  esta  forma:  "print(texto.isascii())",  para
verificar el resultado de manera inmediata sin necesidad de almacenarlo  en  una  variable,  lo  que
puede ser útil para  validaciones  rápidas  o  para  obtener  una  respuesta  directa  sin  realizar
operaciones adicionales con el resultado."""

# Código:
texto = "Python 3.13"
resultado = texto.isascii()
print(f"¿La cadena de texto '{texto}' contiene únicamente caracteres 'ASCII'? {resultado}")

print(texto.isascii())

# Nota Importante:
"""Este método no modifica la cadena original, ya que las cadenas en  Python  son  inmutables.  Esto
significa que siempre devuelve un valor booleano como resultado de su aplicación, dejando intacta la
cadena original.

Los caracteres "ASCII" incluyen letras mayúsculas  y  minúsculas,  números,  signos  de  puntuación,
espacios y caracteres de control. Por lo tanto, si la  cadena  contiene  caracteres  fuera  de  este
conjunto, como caracteres "Unicode", el método devolverá "False". Por ejemplo, si la cadena contiene
caracteres acentuados o caracteres de idiomas distintos del inglés, el método devolverá "False",  ya
que estos caracteres no pertenecen al conjunto "ASCII".

Es fundamental tener en cuenta que el método ".isascii()" considera válidas  las  cadenas  vacías  y
devuelve "True" en estos casos. Por ejemplo, la cadena "" (vacía) se considera "ASCII",  ya  que  no
contiene caracteres fuera del rango "ASCII".

Además, este método solo devuelve "True" si todos los caracteres de la cadena pertenecen al conjunto
"ASCII" o si la cadena está vacía. Si la cadena contiene  cualquier  otro  tipo  de  carácter,  como
caracteres "Unicode", el método devolverá "False".

Por último, hay que tener en cuenta que este método es ideal  para  validaciones  rápidas,  pero  no
resulta apropiado para análisis más complejos del contenido de una cadena. En esos casos,  se  deben
considerar otros métodos o expresiones regulares para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
