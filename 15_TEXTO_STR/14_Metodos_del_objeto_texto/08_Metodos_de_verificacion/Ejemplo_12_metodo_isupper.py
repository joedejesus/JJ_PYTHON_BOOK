# Enunciado:
"""El método ".isupper()" en Python se utiliza para verificar si todos los caracteres alfabéticos de
una cadena de texto están en mayúsculas. Este método devuelve un valor booleano: "True" si todos los
caracteres alfabéticos están en mayúsculas y la cadena contiene al menos un carácter  alfabético,  y
"False" en caso contrario.

Los caracteres alfabéticos  incluyen  tanto  letras  mayúsculas  como  minúsculas,  pero  el  método
".isupper()" solo verifica los caracteres alfabéticos e ignora  los  números,  los  espacios  y  los
caracteres especiales.

Es decir, solo verifica las letras del alfabeto, por lo que, si la cadena contiene números, espacios
o caracteres especiales, el método los ignorará en su verificación. Si la cadena contiene caracteres
alfabéticos en minúsculas, el método devolverá "False", ya que no todos los  caracteres  alfabéticos
están en mayúsculas. Si la cadena no contiene caracteres alfabéticos, el  método  devuelve  "False".
Además, el método ".isupper()" devuelve "False" si se aplica a una  cadena  vacía,  pero  no  genera
ningún error.

El método ".isupper()" toma una cadena de texto y verifica si todos los caracteres alfabéticos están
en mayúsculas. Si la cadena cumple con esta condición, el método devuelve "True"; de  lo  contrario,
devuelve "False".

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, a una variable que contenga texto o incluso al resultado  de  una  expresión  que  devuelva
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve un valor booleano como resultado de la verificación. Si  se  desea
conservar el resultado de la verificación, es necesario asignarlo a  una  nueva  variable  o  usarlo
directamente en una operación posterior.

El método ".isupper()" no requiere ningún argumento adicional para  su  funcionamiento,  ya  que  su
función principal es verificar la composición de la cadena de texto.

Por último, el método ".isupper()" es una herramienta sencilla y eficiente para verificar  si  todos
los caracteres alfabéticos de una cadena están en mayúsculas,  lo  que  lo  hace  útil  en  diversas
aplicaciones de validación y procesamiento de texto, como validar entradas de usuario, asegurarse de
que una cadena no contenga caracteres alfabéticos en minúsculas y realizar verificaciones rápidas en
cadenas de texto."""

# Ejemplo_12_metodo_isupper.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene caracteres
alfabéticos en mayúsculas, además de caracteres especiales y  espacios.  Esta  cadena  de  texto  se
utilizará para demostrar el funcionamiento del método ".isupper()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".isupper()" a la variable "texto",  sin  argumentos.  Para  ello,  escribimos  el
nombre de la variable "texto" seguido del nombre del método ".isupper()" con los paréntesis  vacíos,
ya que este método no requiere argumentos adicionales.

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica si  todos  los  caracteres  alfabéticos  de  la
cadena están en mayúsculas o no.

De esta forma, verificamos si todos los caracteres alfabéticos de la cadena están  en  mayúsculas  y
obtenemos un valor booleano almacenado en la variable "resultado", que indica  el  resultado  de  la
verificación. En este caso, el resultado es "True", ya que en la cadena "PYTHON 3.13  &  TENSORFLOW"
todos los caracteres alfabéticos están en mayúsculas.

Por último, también mostramos el resultado directamente al  aplicar  el  método  ".isupper()"  a  la
variable "texto" dentro de la función  "print()",  de  esta  forma:  "print(texto.isupper())",  para
verificar el resultado de manera inmediata sin necesidad de almacenar el valor en una  variable,  lo
que puede ser útil para validaciones rápidas o para obtener una respuesta directa sin  necesidad  de
realizar operaciones adicionales con el resultado."""

# Código:
texto = "PYTHON 3.13 & TENSORFLOW"
resultado = texto.isupper()
print(f"¿Todos los caracteres alfabéticos de la cadena de texto '{texto}' están en mayúsculas? {resultado}")

print(texto.isupper())

# Nota Importante:
"""Este método no modifica la cadena original, ya que las cadenas en  Python  son  inmutables.  Esto
significa que siempre genera un valor booleano como resultado de su aplicación  y  deja  intacta  la
cadena original.

Es fundamental tener en cuenta que el método ".isupper()" no considera los números, los espacios  ni
los caracteres especiales como caracteres alfabéticos, por lo que, si la cadena contiene  alguno  de
estos elementos, el método los  ignorará  en  su  verificación  y  se  centrará  únicamente  en  los
caracteres alfabéticos para determinar si todos están en mayúsculas o no.

Además, este método solo devuelve "True" si todos los caracteres alfabéticos de la cadena  están  en
mayúsculas y la cadena contiene al menos un carácter alfabético. Si  la  cadena  contiene  cualquier
carácter alfabético en minúsculas o no contiene caracteres alfabéticos, el método devolverá "False".
Si la cadena está vacía, también devolverá "False", ya que no cumple con la  condición  de  contener
caracteres alfabéticos en mayúsculas.

Por último, hay que tener en cuenta que este método es ideal para validaciones rápidas en cadenas de
texto, como verificar si una entrada de usuario está en mayúsculas o asegurarse de que una cadena no
contiene caracteres alfabéticos en minúsculas, lo que puede ser útil  en  diversas  aplicaciones  de
procesamiento de texto y validación de datos, como contraseñas,  nombres  de  usuario  y  etiquetas,
entre otros."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
