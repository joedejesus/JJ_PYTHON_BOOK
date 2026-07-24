# Enunciado:
"""El método ".isalnum()" en Python se utiliza para verificar si todos los caracteres de una  cadena
de texto son alfanuméricos, es decir, si están compuestos únicamente por letras  y/o  números.  Este
método devuelve un valor booleano: "True" si todos los caracteres son alfanuméricos,  la  cadena  no
está vacía y no contiene espacios ni caracteres especiales; en caso contrario, devuelve "False".

Los caracteres alfanuméricos incluyen letras, ya sean mayúsculas o minúsculas, y dígitos  numéricos,
pero no incluyen espacios, caracteres especiales ni signos de puntuación.

El método ".isalnum()" se aplica a una cadena de texto  y  verifica  si  todos  sus  caracteres  son
alfanuméricos. Si la cadena cumple con esta condición, el método devuelve "True"; de  lo  contrario,
devuelve "False".

Además, es importante tener en cuenta que el método ".isalnum()" devuelve "False" si se aplica a una
cadena vacía, pero no genera un error. Del mismo modo, si la cadena contiene espacios  o  caracteres
especiales, el método devolverá "False", ya que estos no se consideran caracteres alfanuméricos.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, una variable que contenga texto o incluso como resultado  de  una  expresión  que  devuelva
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve un valor booleano como resultado de la verificación. Si  se  desea
conservar ese resultado, es necesario asignarlo a una nueva variable o usarlo  directamente  en  una
operación posterior.

El método ".isalnum()" no requiere ningún argumento adicional para  su  funcionamiento,  ya  que  su
función principal es verificar la composición de la cadena de texto.

Por último, el método ".isalnum()" es una herramienta sencilla y eficiente  para  verificar  si  una
cadena está compuesta únicamente por caracteres alfanuméricos, lo  que  lo  hace  útil  en  diversas
aplicaciones de validación y procesamiento de texto, como validar entradas de usuario, asegurarse de
que una cadena no contenga caracteres especiales o espacios, y realizar  verificaciones  rápidas  en
cadenas de texto."""

# Ejemplo_1_metodo_isalnum.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene  letras  y
números combinados. Esta cadena de texto se utilizará para demostrar el  funcionamiento  del  método
".isalnum()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".isalnum()" a la variable "texto",  sin  argumentos.  Para  ello,  escribimos  el
nombre de la variable "texto" seguido del nombre del método ".isalnum()" con los paréntesis  vacíos,
ya que este método no requiere argumentos adicionales.

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica si la cadena es alfanumérica o no.

De esta forma, verificamos si la cadena está  compuesta  únicamente  por  caracteres  alfanuméricos,
obteniendo un valor booleano almacenado en la variable "resultado", que indica el  resultado  de  la
verificación. En este caso, el resultado es "True", ya que la cadena "Python3"  contiene  únicamente
letras y números, sin espacios ni caracteres especiales.

Por último, también mostramos el resultado directamente utilizando el método dentro  de  la  función
"print()", de esta forma: "print(texto.isalnum())", para verificar el resultado de manera  inmediata
sin necesidad de almacenar el valor en una variable, lo que puede ser útil para validaciones rápidas
o para obtener una respuesta directa sin  necesidad  de  realizar  operaciones  adicionales  con  el
resultado."""

# Código:
texto = "Python3"
resultado = texto.isalnum()
print(f"¿La cadena de texto '{texto}' es alfanumérica? {resultado}")

print(texto.isalnum())

# Nota Importante:
"""Este método no modifica la cadena original, ya que las cadenas en  Python  son  inmutables.  Esto
significa que siempre devuelve un valor booleano como resultado de su aplicación, dejando intacta la
cadena original.

Es fundamental tener en cuenta que el método ".isalnum()" no considera los espacios como  caracteres
alfanuméricos, por lo que una cadena que contenga espacios devolverá "False". Por ejemplo, la cadena
"Python 3" no se considera alfanumérica debido al espacio entre "Python" y "3".

Además, este método solo devuelve "True" si todos los caracteres de la cadena son alfanuméricos y la
cadena no está vacía. Si la  cadena  contiene  cualquier  otro  tipo  de  carácter,  como  espacios,
caracteres especiales o signos de puntuación, el método devolverá "False". Si la cadena está  vacía,
también devolverá "False", ya que no cumple con la condición de contener caracteres alfanuméricos.

Por último, hay que tener en cuenta que este método es ideal para validaciones rápidas, pero  no  es
apropiado para análisis más complejos  del  contenido  de  una  cadena.  En  esos  casos,  se  deben
considerar otros métodos o expresiones regulares para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
