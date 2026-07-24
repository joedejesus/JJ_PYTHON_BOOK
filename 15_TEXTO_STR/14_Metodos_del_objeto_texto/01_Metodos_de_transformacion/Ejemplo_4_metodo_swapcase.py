# Enunciado:
"""El método ".swapcase()" en Python se utiliza para transformar las letras de una cadena de  texto,
invirtiendo su capitalización. Es decir, convierte las letras mayúsculas en minúsculas y las  letras
minúsculas en mayúsculas.

El método ".swapcase()" toma una cadena de texto y devuelve una nueva cadena en  la  que  todas  las
letras mayúsculas se convierten en minúsculas y  todas  las  letras  minúsculas  en  mayúsculas.  Es
importante destacar que este método no modifica la cadena original, ya que las cadenas en Python son
inmutables; en su lugar, genera una nueva cadena con los cambios aplicados.

Este método puede aplicarse a cualquier objeto de tipo texto  en  Python,  como  cadenas  literales,
variables de texto o resultados de otras operaciones que devuelvan texto. Al no requerir  argumentos
adicionales, su uso es directo y fácil de entender, lo que lo convierte en una herramienta accesible
incluso para principiantes en programación. Además, este método no afecta a los  caracteres  que  no
son letras, como números, espacios o símbolos, los cuales permanecen sin cambios.

En cuanto a los caracteres acentuados o especiales, el método  ".swapcase()"  también  invierte  las
letras según las reglas de mayúsculas y minúsculas de Unicode. Por ello, caracteres acentuados  como
"á" o "É" normalmente se transforman correctamente, aunque el resultado  siempre  dependerá  de  los
caracteres presentes en el texto.

En resumen, el método ".swapcase()" es útil en  situaciones  en  las  que  se  necesita  cambiar  la
capitalización de un texto de manera rápida y sencilla, como en el procesamiento de datos  o  en  la
creación de formatos específicos."""

# Ejemplo_4_metodo_swapcase.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto con la primera letra en
minúscula y el resto en mayúsculas, incluyendo caracteres especiales como acentos.  Esta  cadena  de
texto se utilizará para demostrar el funcionamiento del método ".swapcase()".

A continuación, definimos una nueva variable llamada "texto_swapcase" y le asignamos el resultado de
aplicar el método ".swapcase()" a la variable  "texto".  Para  ello,  escribimos  el  nombre  de  la
variable seguido del nombre del método ".swapcase()". En este caso, el método no  recibe  argumentos
adicionales, por lo que los paréntesis se dejan vacíos.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" para indicar que se trata del resultado de  aplicar  el
método al texto contenido en la variable "texto".

De esta forma, hemos invertido la capitalización de las letras  en  la  cadena  de  texto  original.
Además, los caracteres acentuados también se han  transformado  a  su  correspondiente  mayúscula  o
minúscula, mostrando cómo el método maneja los caracteres  especiales  presentes  en  la  cadena  de
texto."""

# Código:
texto = "tEXTO CON CARACTERES ESPECIALES Y ACENTOS: ##, á, é, í, ó, ú, $$."
texto_swapcase = texto.swapcase()
print(f"Este es el resultado de aplicar el método al texto: {texto_swapcase}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método  ".swapcase()"  no  realiza  cambios  en  la  cadena
original, ya que las cadenas en Python son inmutables. Esto significa  que  siempre  se  genera  una
nueva cadena como resultado de su aplicación, dejando intacta la cadena original.

Si se desea almacenar el resultado del método ".swapcase()", es  necesario  asignarlo  a  una  nueva
variable o sobrescribir la variable original. De lo contrario, el resultado de la transformación  se
perderá.

Además, este método aplica la conversión de mayúsculas y minúsculas según las reglas de Unicode, por
lo que su comportamiento depende de  los  caracteres  presentes  en  la  cadena.  Por  ejemplo,  los
caracteres especiales o las letras  con  acentos  también  pueden  verse  afectados  si  tienen  una
correspondencia válida entre mayúsculas y minúsculas.

Por último, aunque el método es útil para invertir la capitalización, no es adecuado para tareas que
requieran un control más preciso sobre el formato del texto,  como  la  capitalización  de  palabras
específicas o la normalización del texto. En  esos  casos,  se  deben  considerar  otros  métodos  o
combinaciones de funciones disponibles en Python para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────