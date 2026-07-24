# Enunciado:
"""Las "excepciones" en Python son errores que ocurren durante la ejecución de  un  programa.  Estas
excepciones pueden ser manejadas para evitar que el programa se detenga abruptamente. Una  excepción
ocurre cuando el intérprete de Python encuentra una situación inesperada, como intentar  dividir  un
número por cero, acceder a una variable que no existe o convertir un valor no válido a  un  tipo  de
dato específico.

Las "excepciones" son una parte fundamental de la programación  robusta,  ya  que  permiten  manejar
errores de manera controlada y evitar que el programa falle inesperadamente. Python  proporciona  un
mecanismo para capturar y manejar estas excepciones utilizando bloques "try-except". Existen  varios
tipos de excepciones en Python, cada una diseñada para manejar un  tipo  específico  de  error.  Por
ejemplo, "ZeroDivisionError" se lanza cuando se intenta dividir por cero, "ValueError" ocurre cuando
se pasa un valor incorrecto a una función y "KeyError" se lanza cuando  se  intenta  acceder  a  una
clave inexistente en un diccionario.

Además, es posible generar excepciones personalizadas para adaptarse a necesidades específicas. Esto
se logra creando clases que hereden de la clase base "Exception". Las excepciones personalizadas son
útiles para representar errores específicos de la lógica del programa, lo que facilita la depuración
y el mantenimiento del código.

Cuando ocurre un  error,  Python  genera  o  "lanza"  una  excepción  correspondiente.  Los  bloques
"try-except" permiten capturar estas excepciones y manejar el error sin detener el programa.  Dentro
del bloque "try", se coloca el código  que  podría  generar  una  excepción,  y  dentro  del  bloque
"except", se define cómo manejar el error en caso de que ocurra.  También  es  posible  utilizar  un
bloque "else" para ejecutar código si no se lanza ninguna excepción,  y  un  bloque  "finally"  para
especificar código que siempre se ejecutará, independientemente de si ocurrió una excepción o no.

Algunos de los beneficios de manejar excepciones incluyen una mejor experiencia de usuario al evitar
cierres inesperados del programa, la identificación y resolución de errores de manera más eficiente,
y el mantenimiento de la integridad de los datos y del flujo del programa. Entre las más comunes  se
encuentran las excepciones de sintaxis "SyntaxError", las excepciones  de  valor  "ValueError",  las
excepciones de nombre "NameError" y las excepciones de tipo "TypeError". También existen excepciones
relacionadas con operaciones de entrada/salida, como "FileNotFoundError" o  "IOError",  que  ocurren
cuando se intenta acceder a un archivo inexistente o cuando hay problemas al leer o escribir datos.

Por último, es importante destacar que las excepciones no deben usarse como una forma de control  de
flujo normal en un programa, sino como una herramienta para manejar errores inesperados.  Un  manejo
adecuado de excepciones mejora la calidad del software y facilita su mantenimiento."""

# Ejemplo_caracteristicas_de_las_excepciones.py

# Nota Muy Importante:
"""Es fundamental comprender que las excepciones en Python son una herramienta poderosa para manejar
errores de manera controlada. El uso adecuado de bloques "try-except" permite a los  desarrolladores
anticipar posibles errores y proporcionar soluciones alternativas sin interrumpir la  ejecución  del
programa. Esto es especialmente útil en aplicaciones críticas, donde los errores inesperados podrían
tener consecuencias graves.

Además, Python permite manejar excepciones de  manera  jerárquica,  ya  que  todas  las  excepciones
heredan de la clase base "BaseException". Las  excepciones  más  específicas,  como  "ValueError"  o
"TypeError", heredan de la clase "Exception", que a su vez hereda de "BaseException".  Esto  permite
capturar excepciones específicas o manejar todas las excepciones de  manera  general.  Por  ejemplo,
capturar "Exception" permitirá manejar cualquier error que herede de esta clase, pero es  una  buena
práctica capturar excepciones específicas siempre que sea posible para  evitar  manejar  errores  no
deseados.

Cuando nos referimos a la herencia en el contexto de las excepciones, estamos hablando de  cómo  las
clases de excepciones pueden derivar de otras clases. En Python, todas las excepciones heredan de la
clase base "BaseException". La mayoría de las excepciones comunes, como "ValueError", "TypeError"  y
"NameError", heredan de la clase "Exception", que a su vez hereda de "BaseException".

Esto significa que, al capturar una excepción de una clase base, también se capturan las excepciones
de sus clases derivadas. Por ejemplo, capturar "Exception" también capturará "ValueError",  pero  no
capturará excepciones como "KeyboardInterrupt", que heredan directamente de "BaseException".

Es importante destacar que el manejo  adecuado  de  excepciones  no  solo  mejora  la  robustez  del
programa, sino que también facilita la depuración y el  mantenimiento  del  código.  Al  capturar  y
registrar las excepciones, los desarrolladores pueden identificar problemas recurrentes y mejorar la
calidad del software. Además, el uso de excepciones personalizadas permite crear mensajes  de  error
más claros y específicos, lo que ayuda a los usuarios y a los desarrolladores a comprender mejor  el
problema.

Por último, se recomienda utilizar excepciones personalizadas cuando sea necesario para  representar
errores específicos de la lógica  del  programa.  Esto  se  logra  creando  clases  que  hereden  de
"Exception". Por ejemplo, se puede crear una excepción "InvalidInputError" para manejar entradas  no
válidas en un programa. Esto no solo mejora la claridad del código, sino que también permite manejar
errores de manera más precisa y eficiente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
