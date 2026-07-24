# Enunciado:
"""El método ".split()" en Python se utiliza para dividir una  cadena  de  texto  en  una  lista  de
subcadenas, utilizando  un  delimitador  especificado  como  argumento.  Si  no  se  proporciona  un
delimitador como argumento, el método ".split()" utiliza por defecto cualquier secuencia de espacios
en blanco como delimitador, incluyendo tabulaciones y saltos de línea.  Este  método  es  útil  para
separar palabras, frases o cualquier otro contenido delimitado dentro de  una  cadena  de  texto  en
partes más pequeñas, facilitando su manipulación y análisis posterior.

El método toma una cadena de texto y devuelve una lista de subcadenas separadas por  el  delimitador
especificado como argumento o, si no se especifica, utilizando el delimitador por defecto. Cada  vez
que el método encuentra el delimitador en la  cadena,  crea  una  nueva  subcadena  sin  incluir  el
delimitador y la agrega a la lista resultante.

Además, es importante destacar que el delimitador no se incluye en las  subcadenas  resultantes,  ya
que se utiliza únicamente como punto de separación. Esto significa que el delimitador se elimina  de
la cadena generada a partir de la cadena original durante el proceso de división y no formará  parte
de las subcadenas resultantes dentro de la lista. Esto  permite  obtener  una  lista  de  subcadenas
limpias, sin caracteres adicionales que puedan interferir con el  análisis  o  manipulación  de  los
datos obtenidos a partir de la cadena original.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya  sea  una  variable,  una
cadena literal o el resultado de una función que devuelva texto. Además, este método no modifica  la
cadena original, ya que las cadenas en Python son inmutables.

El método ".split()" puede tomar uno  o  dos  argumentos,  los  cuales  son  opcionales.  El  primer
argumento opcional es el delimitador que se utilizará para dividir la cadena de texto, el cual  debe
ser una cadena de  de  texto,  como  una  coma,  un  espacio  o  cualquier  otro  carácter,  y  debe
especificarse entre comillas. Si el delimitador no se encuentra en la cadena de texto  original,  el
método devolverá una lista que contiene la cadena original como único elemento.

El segundo argumento opcional es un número entero que  indica  el  número  máximo  de  divisiones  a
realizar teniendo en cuenta el delimitador especificado. Si no  se  especifica  este  argumento,  el
método dividirá la cadena en todas las ocurrencias del delimitador.

Esto quiere decir que si se especifica un número máximo de divisiones  como  segundo  argumento,  el
método limitará el número de divisiones realizadas a ese número, lo que significa que la  cadena  se
dividirá en un número máximo de partes igual al número de divisiones especificado  más  uno.  Si  el
número máximo de divisiones especificado es mayor que las ocurrencias del delimitador en la  cadena,
el método simplemente dividirá la cadena en todas las ocurrencias del delimitador disponibles.

Por último, el método ".split()" es útil para dividir  cadenas  de  texto  en  partes  más  pequeñas
basadas en un delimitador específico."""

# Ejemplo_1_metodo_split.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que  contiene  palabras
terminadas con puntos y separadas por espacios. Esta cadena de texto se utilizará para demostrar  el
funcionamiento del método ".split()".

A continuación, definimos una nueva variable llamada "lista_palabras" y le asignamos el resultado de
aplicar el método ".split()" a la variable "texto" con dos argumentos: el  delimitador  (".")  y  el
número máximo de divisiones, en este caso 4. Para ello, escribimos el nombre de la variable  seguido
del nombre del método ".split()" y, dentro de los paréntesis, pasamos  el  delimitador  como  primer
argumento en forma de cadena entre comillas y el número máximo de divisiones como segundo  argumento
en forma de número entero, separados por comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola acompañado de un
mensaje descriptivo en formato "f-string" para indicar cómo se dividió  el  texto  contenido  en  la
variable "texto".

De esta forma, hemos dividido la cadena de texto en subcadenas  basadas  en  el  delimitador  ("."),
limitando el número de divisiones a 4 y obteniendo una lista que contiene las partes  de  la  cadena
original excluyendo el delimitador. En este caso, el número de divisiones se ha establecido en 4, lo
que significa que el método dividirá la cadena con un máximo de  4  divisiones,  lo  que  dará  como
resultado una lista con 5 elementos, ya que el número de elementos en la lista resultante  es  igual
al número de divisiones más uno."""

# Código:
texto = "palabra1. palabra2. palabra3. palabra4. palabra5"
lista_palabras = texto.split(".", 4)
print(f"El texto '{texto}' se ha dividido en: {lista_palabras}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".split()" no realiza cambios en la cadena original,
ya que las cadenas en Python son inmutables. Esto significa que siempre se genera  una  nueva  lista
como resultado de su aplicación, dejando intacta la cadena original.

Si se desea almacenar el resultado del  método  ".split()",  es  necesario  asignarlo  a  una  nueva
variable o usar directamente el resultado en una operación posterior. De lo contrario, el  resultado
de la operación se perderá.

En este caso, el primer argumento del método se suele pasar como una cadena de texto  literal,  pero
también se puede pasar como una variable que contenga el  delimitador  deseado  o  incluso  como  el
resultado de una función que devuelva un texto. Esto proporciona flexibilidad al método, permitiendo
su uso en una amplia variedad de situaciones y contextos.

Aunque decimos que el primer argumento es opcional, es lógico utilizarlo ya que si no se  especifica
el delimitador, el uso de este método no  tendría  sentido  en  este  contexto,  ya  que  el  método
utilizará el delimitador por defecto, es decir, cualquier  secuencia  de  espacios  en  blanco  para
dividir la cadena obteniendo una lista de palabras separadas por espacios.

Por último, aunque el método es útil para dividir cadenas de texto, no es adecuado para  tareas  que
requieran un control más granular sobre el formato del texto. En esos  casos,  se  deben  considerar
otros métodos  o  combinaciones  de  funciones  disponibles  en  Python  para  lograr  el  resultado
deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
