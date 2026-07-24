# Lista_de_la_jerarquia_de_las_excepciones.py

# Código:
lista_de_la_jerarquia_de_las_excepciones = [

    "    1. BaseException",  # Clase base de todas las excepciones.
    "        1.1 SystemExit",  # Señala la salida del intérprete.
    "        1.2 KeyboardInterrupt",  # Interrupción del programa por parte del usuario (Ctrl+C).
    "        1.3 GeneratorExit",  # Señala el cierre de un generador.
    "        1.4 Exception",  # Clase base para la mayoría de las excepciones.
    "        1.4.1 ArithmeticError",  # Errores en operaciones matemáticas.
    "            1.4.1.1 FloatingPointError",  # Error en operaciones con números de punto flotante.
    "            1.4.1.2 OverflowError",  # Resultado matemático demasiado grande para representarse.
    "            1.4.1.3 ZeroDivisionError",  # División por cero.
    "        1.4.2 AttributeError",  # Atributo no encontrado en un objeto.
    "        1.4.3 BufferError",  # Error relacionado con búferes.
    "        1.4.4 EOFError",  # Fin inesperado de la entrada.
    "        1.4.5 ImportError",  # Fallo al importar un módulo.
    "            1.4.5.1 ModuleNotFoundError",  # Módulo no encontrado.
    "        1.4.6 LookupError",  # Error en búsquedas (índices o claves).
    "            1.4.6.1 IndexError",  # Índice fuera de rango.
    "            1.4.6.2 KeyError",  # Clave no encontrada en un diccionario.
    "        1.4.7 MemoryError",  # Memoria insuficiente.
    "        1.4.8 NameError",  # Nombre no definido.    
    "            1.4.8.1 UnboundLocalError",  # Variable local referenciada antes de ser asignada.
    "        1.4.9 OSError",  # Error del sistema operativo.
    "            1.4.9.1 FileNotFoundError",  # Archivo o directorio no encontrado.
    "            1.4.9.2 PermissionError",  # Permiso denegado.
    "            1.4.9.3 TimeoutError",  # Operación que excedió el tiempo límite.
    "        1.4.10 ReferenceError",  # Referencia débil a un objeto ya eliminado.
    "        1.4.11 RuntimeError",  # Error general en tiempo de ejecución.
    "            1.4.11.1 NotImplementedError",  # Función o método no implementado.
    "            1.4.11.2 RecursionError",  # Límite de recursión excedido.
    "        1.4.12 SyntaxError",  # Error de sintaxis en el código.
    "            1.4.12.1 IndentationError",  # Error en la indentación.
    "                1.4.12.1.1 TabError",  # Mezcla de tabuladores y espacios.
    "        1.4.13 TypeError",  # Operación con tipos incompatibles.
    "        1.4.14 ValueError",  # Valor inválido para una operación.
    "            1.4.14.1 UnicodeError",  # Error relacionado con Unicode.
    "                1.4.14.1.1 UnicodeDecodeError",  # Error al decodificar Unicode.
    "                1.4.14.1.2 UnicodeEncodeError",  # Error al codificar Unicode.
    "                1.4.14.1.3 UnicodeTranslateError",  # Error al traducir Unicode.
    "        1.4.15 Warning",  # Clase base para advertencias.
    "            1.4.15.1 DeprecationWarning",  # Advertencia sobre características obsoletas.
    "            1.4.15.2 PendingDeprecationWarning",  # Advertencia sobre características próximas a quedar obsoletas.  
    "            1.4.15.3 RuntimeWarning",  # Advertencia en tiempo de ejecución.
    "            1.4.15.4 SyntaxWarning",  # Advertencia de sintaxis.
    "            1.4.15.5 UserWarning",  # Advertencia definida por el usuario.
    "            1.4.15.6 FutureWarning",  # Advertencia de cambios futuros.
    "            1.4.15.7 ImportWarning",  # Advertencia al importar módulos.
    "            1.4.15.8 UnicodeWarning",  # Advertencia relacionada con Unicode.
    "            1.4.15.9 BytesWarning",  # Advertencia relacionada con bytes.
    "            1.4.15.10 ResourceWarning",  # Advertencia sobre recursos no liberados.
]

# Explicación:
"""La jerarquía de excepciones en Python sigue una estructura  de  herencia  en  la  que  todas  las
excepciones derivan de la clase base "BaseException", como se muestra en  la  lista  anterior.  Esta
organización permite manejar las excepciones de forma jerárquica, capturando primero las excepciones
más específicas y luego las más generales. Esto es útil para evitar capturar errores que no deberían
manejarse en ciertos contextos, como "SystemExit" o "KeyboardInterrupt", que no representan  errores
en sí mismos, sino eventos especiales.

En esta lista se numeran las clases de excepciones y sus subclases, indicando la relación jerárquica
entre ellas. Cada nivel de indentación representa una subclase que hereda de la clase ubicada en  el
nivel superior. Por ejemplo, "ArithmeticError" es una subclase de  "Exception"  que  agrupa  errores
relacionados con operaciones matemáticas,  mientras  que  "ZeroDivisionError"  es  una  subclase  de
"ArithmeticError" que se produce específicamente cuando se intenta dividir entre cero.

La lista de la jerarquía de las excepciones muestra cómo las clases de excepciones en  Python  están
organizadas en una estructura jerárquica. Esta jerarquía se basa en la herencia de clases, donde las
clases más específicas heredan de clases más generales. Esto permite manejar excepciones  de  manera
flexible y eficiente, ya que se pueden capturar errores específicos o agruparlos bajo una clase base
común.

La estructura de la jerarquía es la siguiente:

- "BaseException": Es la clase base de todas las excepciones en Python. Todas las demás excepciones
  derivan de esta clase. Aunque es posible capturar esta clase directamente, no es  recomendable  en
  la mayoría de los casos, ya que también  incluye  excepciones  que  no  deberían  manejarse,  como
  "SystemExit" o "KeyboardInterrupt".

- "Exception": Es una subclase de "BaseException" y la clase base para la mayoría de las excepciones
  comunes que aparecen en los programas. Capturar esta clase permite manejar errores generales, pero
  es mejor capturar subclases más específicas siempre que sea posible.

- "Clases específicas": Estas son subclases de "Exception" que representan errores más concretos,
  como "FileNotFoundError", que es una subclase de "OSError" y se produce cuando no se encuentra  un
  archivo o  directorio.  Esto  permite  manejar  errores  relacionados  de  manera  más  precisa  y
  eficiente."""

# Nota Muy Importante:
"""Las clases de excepciones son objetos que representan errores o eventos excepcionales que ocurren
durante la ejecución de un programa. Estas clases permiten capturar  y  manejar  errores  de  manera
controlada utilizando bloques "try-except". Al hacerlo, podemos evitar que los  errores  interrumpan
la ejecución del programa y, en su lugar, tomar medidas para resolverlos o informar  al  usuario  de
manera adecuada.

El manejo correcto de excepciones mediante esta jerarquía permite atender errores específicos  antes
que los generales. Esto es importante porque manejar excepciones específicas permite  identificar  y
resolver problemas concretos, mientras que  manejar  excepciones  generales  puede  ocultar  errores
inesperados  o  no  relacionados.  Por  ejemplo,  capturar   "ZeroDivisionError"   permite   manejar
específicamente el caso de una división entre cero, mientras que capturar "Exception" podría atrapar
otros errores no relacionados, dificultando la depuración.

Además, la jerarquía de excepciones facilita la depuración y el mantenimiento  del  código,  ya  que
permite organizar el manejo de errores de manera lógica y estructurada. Esto mejora la robustez  del
programa al anticipar y manejar errores de manera controlada, reduciendo la probabilidad  de  fallos
inesperados. También nos permite escribir código más claro y fácil de entender, ya que el manejo  de
errores se realiza de manera explícita y bien definida.

Por último, es muy importante saber que cada clase de excepción tiene un propósito específico  y  se
utiliza para manejar distintos tipos de errores que  pueden  ocurrir  durante  la  ejecución  de  un
programa. Por ejemplo, "FileNotFoundError" se utiliza para manejar casos en los que no se  encuentra
un archivo, mientras que "ValueError" se utiliza para manejar valores inválidos en una operación.

Al capturar y manejar estas excepciones, es posible crear programas más  robustos  y  resistentes  a
fallos, mejorando la experiencia del  usuario  y  reduciendo  el  riesgo  de  errores  críticos.  Es
importante afianzar el concepto de excepciones base y específicas o derivadas para lograr una  mejor
comprensión y un manejo adecuado de errores en Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
