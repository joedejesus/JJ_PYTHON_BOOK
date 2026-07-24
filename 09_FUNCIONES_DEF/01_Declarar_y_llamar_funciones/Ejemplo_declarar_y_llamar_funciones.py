# Enunciado:
"""Las funciones en Python son bloques de código que realizan una  tarea  específica  y  pueden  ser
reutilizadas en diferentes partes de un programa. Se  definen  utilizando  la  palabra  clave  "def"
seguida del nombre  de  la  función  y  paréntesis  (),  los  cuales  pueden  contener  "parámetros"
opcionales. Estos "parámetros" son variables que se asocian  a  la  función  en  el  momento  de  su
definición y permiten transferir datos a la función cuando esta es llamada.

El nombre de la función debe ser descriptivo para indicar claramente su propósito, y los  paréntesis
que siguen al nombre pueden contener "parámetros" que la función puede recibir. Si no  se  necesitan
"parámetros", los paréntesis se dejan vacíos. Estos "parámetros" son opcionales y  permiten  que  la
función trabaje con datos específicos transferidos  en  el  momento  de  su  llamada.  Estos  datos,
transferidos en el momento de la llamada a la función, se conocen como "argumentos".

Además, el uso de funciones permite estructurar el código en partes reutilizables, lo  que  facilita
su mantenimiento, comprensión y depuración. Además, las funciones ayudan a evitar la  repetición  de
código, ya que, una vez definidas, se pueden llamar tantas veces como sea  necesario  en  diferentes
partes del programa. Esto promueve la modularidad y la claridad en el diseño del software.

El flujo de trabajo de una función generalmente sigue tres pasos principales: Definición, llamada  y
retorno  (opcional).  La  definición  establece  qué  hace  la  función,  especificando  su  nombre,
"parámetros" (si los hay) y el bloque de código asociado que se  ejecutará  cuando  la  función  sea
llamada. La llamada ejecuta esa función en  el  punto  del  programa  donde  se  necesite,  pudiendo
transferirle "argumentos" si la función los requiere.

En algunos casos, a  esta  llamada  se  la  conoce  como  invocación.  En  cualquier  caso,  estamos
requiriendo que se ejecute la función definida en otra  parte  del  código  escribiendo  su  nombre.
Finalmente, el retorno (si se utiliza) finaliza la ejecución de la función devolviendo un  valor  al
lugar desde donde se llamó la función. Esto se consigue con la palabra clave "return". No todas  las
funciones necesitan un retorno, pero, cuando se utiliza,  permite  que  la  función  proporcione  un
resultado específico en un punto determinado del programa.

Por último, el bloque de código asociado a una función puede incluir cualquier instrucción válida de
Python, como bloques condicionales, bucles, operaciones matemáticas y manipulación de  datos,  entre
otras. Esto permite que las funciones realicen tareas complejas y específicas dentro de un programa.
Esto es una ventaja enorme, ya que es posible crear una función para cada tarea y, de  esta  manera,
construir programas más grandes y complejos combinándolas entre sí.  Por  ello,  las  funciones  son
fundamentales para escribir código modular, claro y eficiente, y son ampliamente  utilizadas  en  la
programación para resolver problemas de manera estructurada, organizada y escalable."""

# Ejemplo_declarar_y_llamar_funciones.py

# Explicación:
"""Definimos una función llamada "saludar()" que no recibe  parámetros.  Para  ello,  utilizamos  la
palabra clave "def" seguida del nombre de la función, en este caso "saludar", seguido de  paréntesis
vacíos (), ya que no recibe parámetros, y terminamos con dos puntos (:) para indicar el  inicio  del
bloque de código asociado a la función.

Dentro de la función, utilizamos la instrucción "print()" para mostrar un mensaje de  saludo  en  la
consola. Colocamos esta instrucción con una indentación de cuatro espacios desde el margen izquierdo
para indicar que forma parte del cuerpo de la función y debe ejecutarse siempre que la  función  sea
llamada.

Por último, llamamos a la función "saludar()" para ejecutar el código asociado dentro de ella.  Para
llamar a la función, simplemente escribimos su nombre  seguido  de  paréntesis  vacíos,  ya  que  no
requiere argumentos, en este caso "saludar()". Esto indica al intérprete que debe ejecutar el bloque
de código asociado a la función, mostrando así el mensaje de saludo  en  la  consola  gracias  a  la
instrucción "print()" dentro de la función. Colocamos la llamada a la función  sin  indentación,  ya
que se encuentra en el nivel principal del código y no forma parte de ninguna otra estructura."""

# Código:
def saludar():
    print("¡Hola! ¿Cómo estás?")

saludar()

# Nota Importante:
"""Es importante recordar que una función debe definirse antes de  ser  llamada  en  el  código.  Si
intentamos llamar a una función antes de  su  definición,  Python  generará  un  error,  ya  que  el
intérprete procesa el código de forma secuencial, es decir, de arriba hacia  abajo.  Esto  significa
que el intérprete necesita conocer la existencia de la función antes de que se intente ejecutar. Por
lo tanto, siempre es recomendable organizar el código colocando las  definiciones  de  funciones  al
inicio del archivo o en un lugar lógico que facilite su lectura y mantenimiento.

Es muy importante destacar que hay muchas posibilidades de llamar a una función, incluyendo  el  uso
de "argumentos", manejo de valores de retorno, asignación a variables y la combinación de  funciones
dentro de otras funciones. Estas técnicas permiten una mayor flexibilidad y modularidad en el diseño
del código, facilitando la reutilización y la organización de las tareas específicas  dentro  de  un
programa. Por otro lado, si no llamamos a la función definida, el código dentro de la función no  se
ejecutará y no veremos ningún resultado en la consola.

No obstante, es importante tener en cuenta que las funciones pueden ser mucho más complejas y pueden
incluir "parámetros", valores de retorno y otras características avanzadas que podrían confundir  al
lector. Por ello, es recomendable documentar el código adecuadamente para mejorar su  comprensión  y
no dejar lugar a dudas sobre su funcionamiento. Para ello,  se  utilizan  cadenas  de  documentación
(docstrings) para describir su propósito, "parámetros" y valores de retorno, si los hay. Esto mejora
la legibilidad del código y facilita su uso por otros desarrolladores o por el propio  autor  en  el
futuro. Una organización adecuada y el uso de comentarios claros contribuyen a un código más limpio,
estructurado y fácil de entender.

Por último, no se deben confundir estas  funciones  definidas  por  el  usuario  con  las  funciones
integradas de Python "built-in", que son funciones predefinidas disponibles para  su  uso  inmediato
sin necesidad de definición previa. Estas funciones integradas, como "print()",  "len()",  "type()",
entre otras, proporcionan funcionalidades comunes y útiles que facilitan la programación en  Python.
De la misma forma, no se deben confundir las funciones incorporadas "built-in" con  los  métodos  de
objetos, que son  funciones  asociadas  a  objetos  específicos  y  se  utilizan  para  manipular  o
interactuar con esos objetos. Las funciones incorporadas y los métodos de objetos  se  abordarán  en
secciones posteriores de esta biblioteca."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
