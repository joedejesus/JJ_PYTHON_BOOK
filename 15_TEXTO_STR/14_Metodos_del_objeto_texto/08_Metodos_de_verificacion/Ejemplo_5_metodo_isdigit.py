# Enunciado:
"""El método ".isdigit()" en Python se utiliza para verificar si todos los caracteres de una  cadena
de texto son dígitos. Este método devuelve un valor booleano: "True" si  todos  los  caracteres  son
dígitos y "False" en caso contrario.

Los caracteres considerados como dígitos incluyen los números del 0 al 9, además de otros caracteres
que pueden considerarse dígitos en ciertos contextos, como subíndices,  superíndices  o  dígitos  de
diferentes escrituras. Sin embargo, este conjunto no incluye caracteres como signos  de  puntuación,
letras, espacios o caracteres especiales que no sean dígitos.

Este método es similar al método ".isdecimal()" pero es más general, ya que abarca un  conjunto  más
amplio de caracteres que pueden considerarse dígitos en ciertos contextos. Por lo tanto,  el  método
".isdigit()" es más amplio en su definición de dígitos en comparación con el método  ".isdecimal()",
el cual se limita estrictamente a caracteres decimales específicos usados en distintos  sistemas  de
escritura.

El método ".isdigit()" toma una cadena de texto y verifica si todos los caracteres de esa cadena son
dígitos. Si la cadena cumple con esta  condición,  el  método  devuelve  "True";  de  lo  contrario,
devuelve "False".

Además, es importante tener en cuenta que el método ".isdigit()" devuelve "False" si se aplica a una
cadena vacía, ya que no contiene caracteres dígitos. Este comportamiento es diferente  al  de  otros
métodos como el método ".isascii()", que devuelven "True" para cadenas vacías.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, de una variable que contenga texto o incluso como resultado de una expresión  que  devuelva
un texto. Además, este método no modifica la cadena original, ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve un valor booleano como resultado de la verificación. Si  se  desea
conservar el resultado de la verificación, es necesario asignarlo a  una  nueva  variable  o  usarlo
directamente en una operación posterior.

El método ".isdigit()" no requiere ningún argumento adicional para  su  funcionamiento,  ya  que  su
función principal es verificar la composición de la cadena de texto.

Por último, el método ".isdigit()" es una herramienta sencilla y eficiente  para  verificar  si  una
cadena está  compuesta  únicamente  por  caracteres  dígitos,  lo  que  lo  hace  útil  en  diversas
aplicaciones de validación y procesamiento de texto, como validar entradas de usuario, asegurarse de
que una cadena contiene únicamente números y realizar verificaciones rápidas en cadenas de texto."""

# Ejemplo_5_metodo_isdigit.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto con caracteres dígitos,
además de algunos caracteres especiales considerados dígitos en ciertos contextos. En este caso,  se
añadieron los superíndices (², ³) y un subíndice (₂) a la cadena "14584". Esta cadena  de  texto  se
utilizará para demostrar el funcionamiento del método ".isdigit()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".isdigit()" a la variable "texto" sin argumentos. Para ello, escribimos el nombre
de la variable "texto" seguido del nombre del método ".isdigit()" con los paréntesis vacíos, ya  que
este método no requiere argumentos adicionales.

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica si la  cadena  contiene  únicamente  caracteres
dígitos o no.

De esta forma, hemos verificado si la cadena  está  compuesta  únicamente  por  caracteres  dígitos,
obteniendo un valor booleano almacenado en la variable "resultado" que indica  el  resultado  de  la
verificación. En este caso, el resultado es "True" ya que la cadena "14584²³₂"  contiene  únicamente
caracteres dígitos.

Por último, también mostramos el resultado  directamente  aplicando  el  método  ".isdigit()"  a  la
variable "texto" dentro de la función "print()". De esta forma,  mediante  "print(texto.isdigit())",
verificamos el resultado de manera inmediata sin necesidad de almacenar el valor en una variable, lo
que puede ser útil para validaciones rápidas o para obtener una respuesta directa sin  necesidad  de
realizar operaciones adicionales con el resultado."""

# Código:
texto = "14584²³₂"
resultado = texto.isdigit()
print(f"¿La cadena de texto '{texto}' contiene únicamente caracteres dígitos? {resultado}")

print(texto.isdigit())

# Nota Importante:
"""Este método no modifica la cadena original, ya que las cadenas en  Python  son  inmutables.  Esto
significa que siempre genera un valor booleano como resultado de su aplicación, dejando  intacta  la
cadena original.

Este método es similar al método ".isdecimal()" pero es más general, ya que abarca un  conjunto  más
amplio de caracteres  que  pueden  considerarse  dígitos  en  ciertos  contextos,  como  subíndices,
superíndices o dígitos de diferentes escrituras.

Por lo tanto, el método ".isdigit()" es más amplio en su definición de dígitos en comparación con el
método ".isdecimal()", el cual se limita estrictamente a caracteres decimales específicos usados  en
distintos sistemas de escritura, pero no incluye caracteres como subíndices, superíndices o  algunos
otros símbolos numéricos considerados dígitos por ".isdigit()".

Es fundamental tener en cuenta que el método ".isdigit()" considera inválidas  las  cadenas  vacías,
devolviendo "False" en estos casos. Por ejemplo, la cadena "" (vacía) no es  considerada  válida  ya
que no contiene caracteres dígitos.

Además, este método solo devuelve "True" si todos los caracteres de la cadena  son  dígitos.  Si  la
cadena contiene cualquier otro tipo de carácter, como letras, espacios o caracteres  especiales  que
no son dígitos, entonces el método devolverá "False".

Por último, hay que tener en cuenta que este método es ideal  para  validaciones  rápidas,  pero  no
resulta apropiado para análisis más complejos  dentro  de  una  cadena.  En  esos  casos,  se  deben
considerar otros métodos o expresiones regulares para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
