# Enunciado:
"""El método ".strip()" en Python se utiliza para eliminar los caracteres en blanco al  principio  y
al final de una cadena de texto, incluidos los espacios, las tabulaciones y  los  saltos  de  línea.
También se puede usar para eliminar caracteres específicos al principio y al final de una cadena  de
texto si se proporcionan como argumento.

El método ".strip()" toma una cadena de texto y devuelve una nueva cadena  con  los  caracteres,  ya
sean en blanco o específicos, eliminados del principio y del final de la cadena original. Si  no  se
especifica ningún carácter como argumento, el método eliminará los espacios y  otros  caracteres  en
blanco al principio y al final de la cadena, dejando intactos los caracteres internos.

Es importante destacar que este método no modifica la cadena original, ya que las cadenas en  Python
son inmutables; en su lugar, genera una nueva  cadena  con  los  cambios  aplicados.  Además,  puede
aplicarse a cualquier objeto de tipo texto en Python, como cadenas literales, variables de  texto  o
resultados de otras operaciones que devuelvan texto.

Este método puede tomar como argumento una cadena de caracteres que se desee eliminar al principio y
al final de la cadena original. Los argumentos pueden ser cualquier combinación de caracteres que se
desee eliminar, y el método eliminará todos los caracteres especificados como argumento al principio
y al final de la cadena.

Estos argumentos deben ir en forma de cadena de texto dentro de los paréntesis del  método  y  entre
comillas para indicar que se trata de una cadena de caracteres. Además, este método  no  afecta  los
caracteres internos de la cadena, solo los que están al principio y al final.

Si se especifica como argumento una cadena de caracteres que no está presente en la cadena original,
el método no realizará ningún cambio y devolverá la cadena original  sin  modificaciones.  Por  otro
lado, si los caracteres a eliminar se encuentran en el medio de la cadena, el método  ".strip()"  no
los eliminará, ya que solo se enfoca en los caracteres del principio  y  del  final  de  la  cadena.
Además, si el carácter especificado como argumento solo se encuentra en un extremo de la cadena,  el
método solo eliminará ese carácter en ese extremo específico.

De igual forma, si los caracteres en cuestión, ya sean espacios u otros caracteres, están  repetidos
varias veces al principio o al final  de  la  cadena,  el  método  ".strip()"  eliminará  todas  las
ocurrencias de esos caracteres en ambos extremos de la cadena hasta que  no  queden  más  caracteres
coincidentes al principio o al final.

En resumen, el método ".strip()" es útil en situaciones en las que se necesita  limpiar  cadenas  de
texto eliminando espacios o caracteres no deseados al principio y al final de la cadena."""

# Ejemplo_1_metodo_strip.py

# Explicación:
"""Definimos una variable llamada "texto" y le  asignamos  una  cadena  de  texto  con  espacios  al
principio y al final, así como algunos caracteres especiales. Esta cadena de texto se utilizará para
demostrar el funcionamiento del método ".strip()".

A continuación, definimos una nueva variable llamada "texto_strip" y le asignamos  el  resultado  de
aplicar el método ".strip()" a la variable "texto" dos  veces  de  forma  encadenada:  primero  para
eliminar los espacios en blanco y luego para eliminar los caracteres "$". Para ello,  escribimos  el
nombre de la variable seguido del método ".strip()" sin argumentos adicionales, seguido  del  método
".strip()" con el argumento "$" entre comillas y dentro de los paréntesis.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" para indicar que se trata del resultado de aplicar  los
métodos al texto contenido en la variable "texto".

De esta forma, primero hemos eliminado los espacios en blanco al principio y al final de  la  cadena
de texto original con la aplicación del método ".strip()" sin argumentos y, luego,  hemos  eliminado
todas las ocurrencias de los caracteres "$" al principio y al final de la cadena resultante  con  la
aplicación del método ".strip()" con el argumento "$", obteniendo así una cadena limpia y lista para
su uso."""

# Código:
texto = "   $$$Texto con espacios y caracteres especiales al principio y al final$$$   "
texto_strip = texto.strip().strip("$")
print(f"Este es el resultado de aplicar los métodos al texto: '{texto_strip}'")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".strip()" no realiza cambios en la cadena original,
ya que las cadenas en Python son inmutables. Esto significa que siempre se genera una  nueva  cadena
como resultado de su aplicación, dejando intacta la cadena original.

Si se desea almacenar el resultado del  método  ".strip()",  es  necesario  asignarlo  a  una  nueva
variable o sobrescribir la variable original. De lo contrario, el resultado de la transformación  se
perderá.

Es importante tener presente que en Python se pueden encadenar múltiples  métodos  aplicados  a  una
misma variable y, de esta forma, realizar varias transformaciones en una sola línea de código.

Por último, aunque el método es útil para limpiar cadenas de texto, no es adecuado para  tareas  que
requieran un control más preciso sobre el formato del texto. En  esos  casos,  se  deben  considerar
otros métodos  o  combinaciones  de  funciones  disponibles  en  Python  para  lograr  el  resultado
deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
