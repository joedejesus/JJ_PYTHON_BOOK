# Enunciado:
"""El método ".center()" en Python se utiliza para centrar una cadena de texto dentro  de  un  ancho
total especificado, rellenando los espacios adicionales a  la  derecha  y  a  la  izquierda  con  un
carácter opcional o un espacio en blanco  por  defecto.  Este  método  es  particularmente  útil  en
situaciones donde se requiere presentar texto de manera  alineada  o  formateada,  como  en  tablas,
reportes o interfaces de usuario.

El método ".center()" toma una cadena de texto y devuelve una nueva cadena centrada dentro del ancho
especificado. Este método puede aplicarse a cualquier objeto de tipo (str) en Python,  como  cadenas
literales, variables que contienen texto o incluso  resultados  de  otras  operaciones  que  generan
texto.

El método toma dos argumentos principales: el ancho total de la cadena resultante y,  opcionalmente,
un carácter de relleno. El ancho total debe ser un número entero que indique la longitud deseada  de
la cadena final, mientras que el carácter de relleno, si se especifica, debe ser una  cadena  de  un
solo carácter.

Si no se proporciona un carácter de relleno, el método utiliza un espacio en blanco por defecto.  Es
importante destacar que si el ancho especificado es menor que la longitud de la cadena original,  el
método devuelve la cadena original sin modificaciones, ya que no puede reducir su tamaño.

Además, el método ".center()" no altera la cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, genera y  devuelve  una  nueva  cadena  con  los  cambios  aplicados.  Esto
significa que cualquier transformación realizada con este  método  debe  almacenarse  en  una  nueva
variable  o  sobrescribir  la  variable  existente  si  se  desea  conservar  el   resultado.   Este
comportamiento es consistente con la filosofía de diseño de Python, que prioriza la seguridad  y  la
predictibilidad en el manejo de datos.

Por último, el método ".center()" es una herramienta  poderosa  para  centrar  texto  dentro  de  un
espacio definido, permitiendo un control preciso sobre el formato y la presentación  de  cadenas  de
texto. Su flexibilidad y facilidad de uso lo convierten en una opción ideal para tareas de  formateo
en Python, siempre que se utilice con un entendimiento claro de sus parámetros y limitaciones."""

# Ejemplo_1_metodo_center.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto. Esta cadena  de  texto
se utilizará para demostrar el funcionamiento del método ".center()".

A continuación, definimos una nueva variable llamada "texto_centrado" y le asignamos el resultado de
aplicar el método ".center()" a la variable "texto". Especificamos un ancho total de 20 caracteres y
utilizamos el carácter (*) como relleno. Para ello, escribimos el nombre de la variable seguido  del
nombre del método ".center()", y dentro de los paréntesis, pasamos el ancho total (20)  como  primer
argumento y el carácter de relleno  (*)  entre  comillas  y  separado  por  una  coma  como  segundo
argumento.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola acompañado de un
mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado  de  aplicar  el
método al texto contenido en la variable "texto".

De esta forma, hemos centrado la cadena de texto original  dentro  de  un  ancho  de  20  caracteres
totales y hemos rellenado los espacios adicionales a la derecha y a la  izquierda  con  el  carácter
(*)."""

# Código:
texto = "Texto centrado"
texto_centrado = texto.center(20, "*")
print(f"Este es el resultado de aplicar el método al texto: '{texto_centrado}'")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que  el  método  ".center()"  no  realiza  cambios  en  la  cadena
original, ya que las cadenas en Python son inmutables. Esto significa que cada  vez  que  se  aplica
este método, se genera una nueva cadena como resultado, dejando intacta  la  cadena  original.  Este
comportamiento asegura que las operaciones realizadas sobre cadenas sean seguras  y  no  introduzcan
efectos secundarios inesperados en otras partes del programa.

Si se desea conservar el resultado del método ".center()", es necesario asignarlo  explícitamente  a
una nueva variable o sobrescribir la  variable  original.  De  lo  contrario,  el  resultado  de  la
transformación se perderá, ya que no se almacena  automáticamente.  Este  detalle  es  crucial  para
evitar errores comunes al trabajar con cadenas en Python.

En cuanto al ancho total, este se refiere a la longitud total de la cadena resultante, incluyendo el
texto original y los caracteres de relleno. Los caracteres  de  relleno  se  distribuyen  de  manera
equitativa a ambos lados; estos se obtienen de la diferencia entre el ancho total especificado y  la
longitud del texto original. Si el número de caracteres de relleno es impar, el  carácter  adicional
se coloca a la derecha.

Por ejemplo, si tenemos una cadena de texto con una longitud de 14 caracteres y  queremos  centrarla
dentro de un ancho total de 20 caracteres, el método ".center()" agregará 3 caracteres de relleno  a
la izquierda y 3 caracteres de relleno a la derecha, dejando un total de 20 caracteres en la  cadena
resultante.

Aunque este método es extremadamente útil para centrar cadenas de texto, es importante considerar el
contexto en el que se utiliza. Por ejemplo, en aplicaciones donde el espacio es limitado o donde  se
requiere un formato más complejo, puede ser necesario combinar este método con otras herramientas de
formateo. Además, el uso de caracteres de relleno debe ser cuidadosamente evaluado  para  garantizar
que el resultado sea visualmente coherente y adecuado para el propósito deseado.

Por último, el método ".center()" es una herramienta versátil y eficiente para el formateo de  texto
en Python, pero su uso debe ser acompañado  de  una  comprensión  clara  de  sus  características  y
limitaciones. Esto permitirá aprovechar al máximo sus capacidades y evitar  posibles  inconvenientes
en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────