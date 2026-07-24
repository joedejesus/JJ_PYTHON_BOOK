# Enunciado:
"""El método ".isnumeric()" en Python se utiliza para verificar  si  todos  los  caracteres  de  una
cadena de texto son numéricos.  Este  método  devuelve  un  valor  booleano:  "True"  si  todos  los
caracteres son numéricos y "False" en caso contrario.

Los caracteres considerados numéricos incluyen los números del 0 al 9,  además  de  caracteres  como
subíndices, superíndices, fracciones, números romanos y caracteres numéricos en diferentes  idiomas,
entre otros. Sin embargo, este conjunto no incluye caracteres como  letras,  espacios  o  caracteres
especiales que no sean numéricos.

Este método es similar al método ".isdigit()", pero es más general, ya que abarca  un  conjunto  más
amplio de caracteres que pueden ser considerados numéricos en ciertos contextos. Por  lo  tanto,  el
método ".isnumeric()" es más amplio en su definición de caracteres numéricos en comparación  con  el
método ".isdigit()".

Además, el método ".isnumeric()" toma una cadena de texto y verifica si todos los caracteres de  esa
cadena son numéricos. Si la cadena cumple con esta condición,  el  método  devuelve  "True";  de  lo
contrario, devuelve "False".

Es importante tener en cuenta que el método ".isnumeric()" devuelve  "False"  si  se  aplica  a  una
cadena vacía, ya que no contiene caracteres numéricos. Este comportamiento es diferente del de otros
métodos, como ".isascii()", que devuelven "True" para cadenas vacías.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, a una variable que contenga texto o incluso como resultado de una  expresión  que  devuelva
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve un valor booleano como resultado de la verificación. Si  se  desea
conservar el resultado de la verificación, es necesario asignarlo a  una  nueva  variable  o  usarlo
directamente en una operación posterior.

El método ".isnumeric()" no requiere ningún argumento adicional para su funcionamiento,  ya  que  su
función principal es verificar la composición de la cadena de texto.

Por último, el método ".isnumeric()" es una herramienta sencilla y eficiente para verificar  si  una
cadena está compuesta únicamente  por  caracteres  numéricos,  lo  que  lo  hace  útil  en  diversas
aplicaciones de validación y procesamiento de texto, como validar entradas de usuario, asegurarse de
que una cadena contiene únicamente números y realizar verificaciones rápidas en cadenas de texto."""

# Ejemplo_8_metodo_isnumeric.py

# Explicación:
"""Definimos una variable llamada "texto"  y  le  asignamos  una  cadena  de  texto  con  caracteres
numéricos, como números enteros, subíndices, superíndices, fracciones y números romanos. Esta cadena
de texto se utilizará para demostrar el funcionamiento del método ".isnumeric()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".isnumeric()" a la variable "texto" sin  argumentos.  Para  ello,  escribimos  el
nombre de la variable "texto", seguido del nombre  del  método  ".isnumeric()"  con  los  paréntesis
vacíos, ya que este método no requiere argumentos adicionales.

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica si la  cadena  contiene  únicamente  caracteres
numéricos o no.

De esta forma, hemos verificado si la cadena está compuesta  únicamente  por  caracteres  numéricos,
obteniendo un valor booleano almacenado en la variable "resultado", que indica el  resultado  de  la
verificación. En este caso, el resultado  es  "True",  ya  que  la  cadena  "ⅩⅬⅡ14584²³₂⅕"  contiene
únicamente caracteres numéricos.

Por último, también mostramos el resultado directamente aplicando  el  método  ".isnumeric()"  a  la
variable "texto" dentro de la función "print()"; de esta forma,  "print(texto.isnumeric())"  permite
verificar el resultado de manera inmediata sin necesidad de almacenar el valor en una  variable,  lo
que puede ser útil para validaciones rápidas o para  obtener  una  respuesta  directa  sin  realizar
operaciones adicionales con el resultado."""

# Código:
texto = "ⅩⅬⅡ14584²³₂⅕"
resultado = texto.isnumeric()
print(f"¿La cadena de texto '{texto}' contiene únicamente caracteres numéricos? {resultado}")

print(texto.isnumeric())

# Nota Importante:
"""Este método no modifica la cadena original, ya que las cadenas en  Python  son  inmutables.  Esto
significa que siempre genera un valor booleano como resultado de su aplicación, dejando  intacta  la
cadena original.

Este método es similar al método ".isdigit()", pero es más general, ya que abarca  un  conjunto  más
amplio de caracteres que pueden ser considerados numéricos en  ciertos  contextos  como  subíndices,
superíndices, fracciones, números romanos o caracteres numéricos en diferentes idiomas, entre otros.

Es fundamental tener en cuenta que el método ".isnumeric()" considera inválidas las cadenas  vacías,
devolviendo "False" en estos casos. Por ejemplo, la cadena "" (vacía) no es considerada  válida,  ya
que no contiene caracteres numéricos.

Además, este método solo devuelve "True" si todos los caracteres de la cadena son numéricos.  Si  la
cadena contiene cualquier otro tipo de carácter, como letras, espacios o caracteres  especiales  que
no son numéricos, entonces el método devolverá "False".

Por último, hay que tener en cuenta que este método es ideal  para  validaciones  rápidas,  pero  no
resulta apropiado para análisis más complejos  dentro  de  una  cadena.  En  esos  casos,  se  deben
considerar otros métodos o expresiones regulares para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
