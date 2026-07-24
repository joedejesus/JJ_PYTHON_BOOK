# Enunciado:
"""El método ".rstrip()" en Python se utiliza para eliminar los caracteres en blanco al final de una
cadena de texto, incluidos los espacios, las tabulaciones y los saltos de línea.  También  se  puede
usar para eliminar caracteres específicos al final de una cadena de texto si  se  proporcionan  como
argumento.

El método ".rstrip()" toma una cadena de texto y devuelve una nueva cadena con  los  caracteres,  ya
sean espacios en blanco o específicos,  eliminados  al  final  de  la  cadena  original.  Si  no  se
especifica ningún carácter como argumento, el método eliminará los espacios y  otros  caracteres  en
blanco al final de la cadena, dejando intactos los caracteres internos y los que están al principio.

Es importante destacar que este método no modifica la cadena original, ya que las cadenas en  Python
son inmutables; en su lugar, genera una nueva  cadena  con  los  cambios  aplicados.  Además,  puede
aplicarse a cualquier objeto de tipo texto en Python, como textos literales, variables  de  texto  o
resultados de otras operaciones que devuelvan texto.

Este método puede tomar como argumento una cadena de caracteres que se desea eliminar al final de la
cadena original. Los argumentos  pueden  ser  cualquier  combinación  de  caracteres  que  se  desee
eliminar, y el método eliminará todos los caracteres especificados como argumento  al  final  de  la
cadena.

Estos argumentos deben ir en forma de cadena de texto dentro de los paréntesis del  método  y  entre
comillas para indicar que se trata de una cadena de caracteres. Además, este método no afecta a  los
caracteres internos ni a los que están al principio de la cadena, solo a los que están al final.

Si se especifica como argumento una cadena de caracteres que no está presente al final de la  cadena
original, el método no realizará ningún cambio y devolverá la cadena  original  sin  modificaciones.
Por otro lado, si los caracteres a eliminar se encuentran en el medio o al principio de  la  cadena,
el método ".rstrip()" no los eliminará, ya que solo se enfoca en  los  caracteres  al  final  de  la
cadena.

De igual forma, si los caracteres en cuestión, ya sean espacios u otros caracteres, están  repetidos
varias veces al final de la cadena, el método ".rstrip()" eliminará todas las  ocurrencias  de  esos
caracteres al final de la cadena hasta que no queden más caracteres coincidentes al final.

En resumen, el método ".rstrip()" es útil en situaciones donde se necesita limpiar cadenas de  texto
eliminando espacios o caracteres no deseados al final de la cadena."""

# Ejemplo_3_metodo_rstrip.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto con espacios al  final,
así como algunos caracteres especiales.  Esta  cadena  de  texto  se  utilizará  para  demostrar  el
funcionamiento del método ".rstrip()".

A continuación, definimos una nueva variable llamada "texto_rstrip" y le asignamos el  resultado  de
aplicar el método ".rstrip()" a la variable "texto" de forma  encadenada  dos  veces:  primero  para
eliminar los espacios en blanco al final y luego para eliminar los caracteres "$" también del  final
de la cadena. Para ello, escribimos  el  nombre  de  la  variable  seguido  del  nombre  del  método
".rstrip()" sin argumentos adicionales, seguido del método ".rstrip()" con el  argumento  "$"  entre
comillas y dentro de los paréntesis.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar que se trata del resultado de aplicar los
métodos al texto contenido en la variable "texto".

De esta forma, primero hemos eliminado los espacios en  blanco  al  final  de  la  cadena  de  texto
original con la aplicación del método ".rstrip()" sin argumentos y luego hemos eliminado  todas  las
ocurrencias de los caracteres "$" al final de la cadena resultante  con  la  aplicación  del  método
".rstrip()" con el argumento "$", obteniendo así una cadena limpia y lista para su uso."""

# Código:
texto = "Texto con espacios y caracteres especiales al final.$$$   "
texto_rstrip = texto.rstrip().rstrip("$")
print(f"Este es el resultado de aplicar los métodos al texto: '{texto_rstrip}'")

# Nota Importante:
"""Es fundamental tener en cuenta que  el  método  ".rstrip()"  no  realiza  cambios  en  la  cadena
original, ya que las cadenas en Python son inmutables. Esto significa  que  siempre  se  genera  una
nueva cadena como resultado de su aplicación, dejando intacta la cadena original.

Si se desea almacenar el resultado del método  ".rstrip()",  es  necesario  asignarlo  a  una  nueva
variable o sobrescribir la variable original. De lo contrario, el resultado de la transformación  se
perderá.

Es importante tener en cuenta que en Python se pueden encadenar múltiples métodos  aplicados  a  una
misma variable y, de esta forma, realizar varias transformaciones en una sola línea de código.

Por último, aunque el método es útil para limpiar cadenas de texto, no es adecuado para  tareas  que
requieran un control más granular sobre el formato del texto. En esos  casos,  se  deben  considerar
otros métodos  o  combinaciones  de  funciones  disponibles  en  Python  para  lograr  el  resultado
deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
