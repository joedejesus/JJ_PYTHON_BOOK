# Enunciado:
"""El bloque "try-except-finally" en Python es una  estructura  de  control  de  flujo  que  permite
manejar excepciones y asegurar que ciertas acciones se realicen siempre,  independientemente  de  si
ocurre un error o no.

El bloque "try" encapsula el código que puede generar una excepción, mientras que el bloque "except"
captura y maneja dichas excepciones. Si no se genera ningún error, el bloque "except" no se ejecuta.
Sin embargo, el bloque "finally" se ejecuta siempre, ocurra o no una excepción, lo que lo hace ideal
para realizar tareas de limpieza, liberar recursos o ejecutar acciones  que  deban  garantizarse  en
cualquier circunstancia.

El bloque "finally" es especialmente útil en programas que interactúan con archivos,  conexiones  de
red o bases de datos, ya que asegura que estos recursos  se  cierren  o  se  liberen  correctamente,
incluso si ocurre un error durante  la  ejecución  del  programa.  Esto  mejora  la  robustez  y  la
confiabilidad del código, evitando fugas de recursos o comportamientos inesperados.

Por ejemplo, si un programa abre un archivo para lectura o  escritura,  el  bloque  "finally"  puede
garantizar que el archivo se cierre correctamente,  incluso  si  ocurre  una  excepción  durante  su
procesamiento. Esto asegura que el sistema no quede en un estado inconsistente y que los recursos se
liberen adecuadamente.

Además, el bloque de código asociado al bloque "finally" puede contener cualquier instrucción válida
en Python, como llamadas a funciones, operaciones  aritméticas,  asignaciones  de  variables,  entre
otras. Sin embargo, su uso más común es realizar tareas de limpieza o liberar recursos, como  cerrar
archivos, liberar memoria o cerrar conexiones de red.

Por último, el uso del bloque "finally" no solo mejora la  calidad  del  código,  sino  que  también
facilita el manejo de errores de manera controlada y eficiente. Esto es especialmente importante  en
aplicaciones críticas, donde la liberación de recursos o la ejecución de  tareas  finales  no  puede
quedar al azar, ya que podría comprometer la estabilidad del sistema o la integridad de  los  datos.
Por lo tanto, el bloque "finally" es una herramienta indispensable para escribir programas  robustos
y confiables."""

# Ejemplo_bloque_try_except_finally.py

# Explicación:
"""Definimos una variable llamada "a", a la cual asignamos como valor una cadena de texto (str),  en
este caso "cien".

Utilizamos un bloque "try-except-finally" para manejar posibles errores al solicitar al usuario  que
ingrese un número entero (int) y restar  ese  número  al  valor  de  la  variable  "a".  Para  ello,
utilizamos la palabra clave "try" seguida de dos puntos (:) para iniciar el  bloque  de  código  que
intentaremos ejecutar.

Dentro del bloque "try", utilizamos la función "input()" para solicitar al usuario  que  ingrese  un
número entero (int) para restar ese número al valor de la variable "a".  Para  ello,  definimos  una
variable llamada "opcion_usuario", escribimos la palabra clave "input" seguida de  paréntesis  ()  y
dentro de estos incluimos un mensaje o "prompt", el cual, al ejecutar el código, se mostrará  en  la
consola indicando al usuario qué tipo de información se espera que ingrese. De esta forma, lo que el
usuario ingrese se guarda en la variable "opcion_usuario" como una cadena de texto (str) y  podremos
usarlo en el resto del código.

A continuación, definimos una variable llamada "resultado", a la cual asignamos el resultado  de  la
operación de resta entre el valor de la variable "a" y el valor ingresado por el usuario. Para ello,
escribimos el nombre de la variable "a", el cual será el minuendo, seguido del  operador  aritmético
(-) y seguido del sustraendo "int(opcion_usuario)", que en este caso es el valor  ingresado  por  el
usuario, el cual  convertimos  a  un  número  entero  utilizando  el  constructor  "int()".  Además,
encerramos toda la operación entre paréntesis ().

El constructor toma como  argumento  la  variable  "opcion_usuario",  la  cual  contendrá  el  valor
introducido por el usuario, convertido a entero (int). Esto es necesario porque la función "input()"
devuelve una cadena de texto (str), y para realizar la resta necesitamos un número, en este caso  un
número entero (int).

Además, utilizamos la función "print()" para mostrar  el  resultado  de  la  resta  en  la  consola,
acompañado de un mensaje en formato "f-string" para formatear la salida. Colocamos todo el contenido
del bloque "try" con una indentación de cuatro espacios desde el margen izquierdo para  indicar  que
pertenece a este bloque y debe ejecutarse siempre que no se genere ninguna excepción.

Después del bloque "try", utilizamos dos bloques "except"  para  manejar  posibles  excepciones  que
puedan ocurrir durante la ejecución del código dentro del bloque "try".

En el primer bloque "except", capturamos la excepción "ValueError", que puede ocurrir si el  usuario
ingresa un valor no numérico como letras o símbolos, o un  valor  numérico  distinto  de  un  entero
(int). Esta excepción es una subclase de <class 'Exception'> y es una excepción específica para este
error. Para ello, escribimos la palabra clave "except" seguida del nombre de la excepción,  en  este
caso "ValueError", seguido de la terminación "as e" y dos puntos (:). De esta forma,  capturamos  la
excepción y la asignamos a la variable "e", la cual definimos en este momento, lo  que  nos  permite
acceder al mensaje de error asociado a la excepción.

Si se genera esta excepción, se ejecuta el bloque de código asociado a este bloque "except", el cual
es una instrucción "print()" que muestra un mensaje de error en formato "f-string" acompañado de  la
variable "e", la cual contendrá el error, indicando así al  usuario  que  debe  ingresar  un  número
válido y los detalles del error. Colocamos esta instrucción con una indentación de  cuatro  espacios
desde el margen izquierdo para indicar que pertenece a este bloque y  debe  ejecutarse  solo  si  se
genera la excepción "ValueError".

En el segundo bloque "except", capturamos la excepción "TypeError", que puede ocurrir si  intentamos
realizar una operación con tipos de datos incompatibles, como intentar restar una  cadena  de  texto
(str) con un número entero (int), como en este caso, donde la variable "a" es una  cadena  de  texto
(str) y el valor ingresado por el usuario es un número entero (int). Esta excepción es una  subclase
de <class 'Exception'> y es una excepción específica para  este  error.  Para  ello,  escribimos  la
palabra clave "except" seguida del nombre de la excepción, en este caso "TypeError", seguido  de  la
terminación "as f" y dos puntos (:). De esta forma capturamos la  excepción  y  la  asignamos  a  la
variable "f", la cual definimos en este momento, lo que nos permite  acceder  al  mensaje  de  error
asociado a la excepción.

Si se genera esta excepción, se ejecuta el bloque de código asociado a este bloque "except", el cual
es una instrucción "print()" que muestra un mensaje de error en formato "f-string" acompañado de  la
variable "f", la cual contendrá el error, indicando así al  usuario  que  los  tipos  de  datos  son
incompatibles y los detalles del error. Colocamos esta instrucción con  una  indentación  de  cuatro
espacios desde el margen izquierdo para indicar que pertenece a este bloque y debe  ejecutarse  solo
si se genera la excepción "TypeError".

Por último, utilizamos el bloque "finally" para  definir  un  bloque  de  código  que  se  ejecutará
siempre, independientemente de si ocurrió una excepción o no. Para ello, escribimos la palabra clave
"finally" seguida de dos puntos (:). Dentro de este bloque, utilizamos  la  función  "print()"  para
mostrar un mensaje en la consola indicando que este bloque se ejecuta siempre. Colocamos este bloque
sin indentación, para indicar que debe ejecutarse  siempre  independientemente  de  si  ocurrió  una
excepción o no.

En este caso se ejecutará la excepción "TypeError" ya que estamos intentando restar  una  cadena  de
texto (str) con un número entero (int), lo cual no es válido en Python. Por lo tanto, se mostrará el
mensaje de error correspondiente y luego se ejecutará el bloque "finally" mostrando su mensaje."""

# Código:
a = "cien"

try:
    opcion_usuario = input("Ingresa un número entero para restarle a 'cien' ese número: ")
    resultado = ((a) - int(opcion_usuario))
    print(f"El resultado es: {resultado}")

except ValueError as e:
    print(f"Error: Debes ingresar un número válido. Detalles del error: {e}")

except TypeError as f:
    print(f"Error: Los tipos de datos son incompatibles. Detalles del error: {f}")

finally:
    print("Este bloque finally se ejecuta siempre, independientemente de si ocurrió una excepción o no.")

# Nota Importante:
"""El bloque "finally" es esencial para garantizar que ciertas acciones se  realicen  siempre,  como
liberar recursos o realizar tareas de limpieza, independientemente de si ocurrió una excepción o no.
Esto asegura que el programa no quede en un estado inconsistente y que los recursos utilizados, como
archivos abiertos, conexiones de red o memoria asignada, se liberen  correctamente.  Sin  el  bloque
"finally", existe el riesgo de que un error interrumpa la ejecución del programa y deje recursos sin
liberar, lo que podría causar problemas como fugas de memoria, bloqueos  de  archivos  o  conexiones
abiertas innecesarias.

Los recursos no liberados  pueden  llevar  a  un  rendimiento  deficiente  del  sistema,  a  errores
inesperados o incluso fallos críticos en aplicaciones más grandes y complejas. Estos  son  problemas
que pueden ser difíciles de diagnosticar y resolver, especialmente en entornos de  producción  donde
la estabilidad y confiabilidad del software son cruciales. Estos recursos son  simplemente  datos  o
elementos que un programa utiliza durante su ejecución, como archivos abiertos, conexiones  de  red,
memoria asignada, entre otros.

Por lo tanto, el bloque "finally" no solo es una buena práctica, sino que también es una herramienta
clave para garantizar la estabilidad y el correcto funcionamiento de los programas, especialmente en
entornos  donde  la  gestión  adecuada  de  recursos  es  crítica  para  evitar  errores  graves   o
comportamientos inesperados. Aunque este ejemplo no es el uso más común  del  bloque  "finally",  su
propósito principal es garantizar que ciertas acciones se realicen siempre, independientemente de si
ocurrió una excepción o no. Su verdadero valor radica en situaciones donde es  crucial  asegurar  la
liberación de recursos o la ejecución de tareas finales, como cerrar  archivos,  liberar  memoria  o
cerrar conexiones de red.

Se muestra este ejemplo y no otro más acorde con el uso del bloque "finally", ya que tendríamos  que
hacer uso de funciones, métodos o manejo de archivos en Python, aspectos que aún no se han visto, lo
que podría confundir al lector. No obstante, la puesta en práctica de esta estructura sería  similar
en el manejo de archivos o recursos.

Por último, es preciso destacar que solo es posible tener un bloque "finally" por cada bloque  "try"
y este debe ir al final de la estructura "try-except-finally". Sin embargo,  puede  haber  múltiples
bloques "except" para manejar diferentes tipos de excepciones que puedan surgir  dentro  del  bloque
"try"."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
