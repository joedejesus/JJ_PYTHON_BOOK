# Enunciado:
"""El método ".isprintable()" en Python se utiliza para verificar si todos  los  caracteres  de  una
cadena de texto son imprimibles. Este método  devuelve  un  valor  booleano:  "True"  si  todos  los
caracteres son imprimibles y "False" en caso contrario.

Los caracteres imprimibles son aquellos que pueden representarse visualmente, es decir, aquellos que
pueden mostrarse en la pantalla o en papel, como letras, números,  símbolos  y  espacios.  Por  otro
lado, los caracteres de control, como los saltos de línea  (\n)  o  las  tabulaciones  (\t),  no  se
consideran imprimibles porque no tienen una representación visual directa y su función es  controlar
el formato del texto en lugar de formar parte del contenido visible.

El método ".isprintable()" toma una  cadena  de  texto  y  verifica  si  todos  sus  caracteres  son
imprimibles. Si la cadena cumple con esta condición, el método devuelve  "True";  de  lo  contrario,
devuelve "False". Además, si la cadena está vacía, el método devuelve "True",  ya  que  no  contiene
caracteres no imprimibles.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, de una variable que contenga texto o incluso como resultado de una expresión  que  devuelva
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve un valor booleano como resultado de la verificación. Si  se  desea
conservar el resultado de la verificación, es necesario asignarlo a  una  nueva  variable  o  usarlo
directamente en una operación posterior.

El método ".isprintable()" no requiere ningún argumento adicional para funcionar, ya que su  función
principal es verificar la composición de la cadena de texto.

Por último, el método ".isprintable()" es una herramienta sencilla y  eficiente  para  verificar  si
todos los caracteres de una cadena son imprimibles, lo que lo hace útil en diversas aplicaciones  de
validación y procesamiento de texto, como validar entradas de usuario, asegurarse de que una  cadena
no contenga caracteres de control y realizar verificaciones rápidas en cadenas de texto."""

# Ejemplo_9_metodo_isprintable.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene caracteres
imprimibles y no imprimibles. Esta cadena de texto se utilizará para demostrar el funcionamiento del
método ".isprintable()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".isprintable()" a la variable "texto" sin argumentos. Para  ello,  escribimos  el
nombre de la variable "texto" seguido del método ".isprintable()" con los paréntesis vacíos, ya  que
este método no requiere argumentos adicionales.

Además, utilizamos la función "print()" para mostrar el resultado en la  consola  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica si  todos  los  caracteres  de  la  cadena  son
imprimibles o no.

De esta forma, verificamos si todos los caracteres de la cadena son imprimibles y obtenemos un valor
booleano almacenado en la variable "resultado", que indica el resultado de la verificación. En  este
caso, el resultado es "False",  ya  que  en  la  cadena  "python\ttensorflow"  hay  un  carácter  no
imprimible: el tabulador (\t).

Por último, también mostramos el resultado directamente aplicando el método  ".isprintable()"  a  la
variable "texto" dentro de la función "print()", de esta forma:  "print(texto.isprintable())",  para
verificar el resultado de manera inmediata sin necesidad de almacenar el valor en una  variable,  lo
que puede ser útil para validaciones rápidas o para  obtener  una  respuesta  directa  sin  realizar
operaciones adicionales con el resultado."""

# Código:
texto = "python\ttensorflow"
resultado = texto.isprintable()
print(f"¿Todos los caracteres de la cadena de texto '{texto}' son imprimibles? {resultado}")

print(texto.isprintable())

# Nota Importante:
"""Este método no modifica la cadena original, ya que las cadenas en  Python  son  inmutables.  Esto
significa que siempre devuelve un valor booleano como resultado de su aplicación, dejando intacta la
cadena original.

Es fundamental tener en cuenta que el método ".isprintable()" considera imprimibles  los  caracteres
alfabéticos, numéricos, símbolos y espacios, pero no los caracteres de control  como  (\n),  (\t)  o
cualquier otro carácter que no tenga una representación visual directa. Por lo tanto, si  la  cadena
de texto contiene alguno de estos caracteres no imprimibles, el método devolverá "False".

Además, este método solo devuelve "True" si todos los caracteres de la cadena son imprimibles  o  si
la cadena está vacía, ya que en ese caso no contiene caracteres no imprimibles.

Por último, hay que tener en cuenta que este método es ideal para validaciones rápidas en cadenas de
texto, como verificar si una entrada de usuario no contiene caracteres de control  o  asegurarse  de
que una cadena sea completamente imprimible, lo que puede  ser  útil  en  diversas  aplicaciones  de
procesamiento de texto y validación de datos, como contraseñas,  nombres  de  usuario  y  etiquetas,
entre otros."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
