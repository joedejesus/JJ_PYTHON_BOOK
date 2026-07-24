# Enunciado:
"""La instrucción "break" en Python permite interrumpir de forma inmediata la ejecución de un  bucle
cuando una condición específica se  cumple.  Esto  ocurre  independientemente  de  si  el  bucle  ha
completado todas sus iteraciones previstas o no.

En cuanto la condición asociada a la instrucción "break" se evalúa como  verdadera,  la  instrucción
"break" se ejecuta y el bucle se detiene. El control del programa pasa entonces a la  primera  línea
de código que sigue al bucle, lo que proporciona un control más preciso sobre el flujo de  ejecución
del programa.

"Break" en español significa "romper" o "interrumpir", y su función  principal  es  proporcionar  un
control más preciso sobre el flujo de ejecución del programa.

Además, la instrucción "break" puede ser utilizada tanto en bucles "for" como en bucles "while".  En
el caso de bucles anidados, "break" solo afecta al bucle en el que se encuentra, sin impactar a  los
bucles externos. Esto es útil para manejar estructuras de control complejas de manera eficiente.

El uso de "break" es común en situaciones donde se necesita interrumpir un bucle  basándose  en  una
condición específica. Por ejemplo, se puede utilizar para detener la búsqueda de un elemento en  una
lista una vez que se encuentra, o para salir de un bucle cuando se cumple un criterio en un conjunto
de datos.

Por último, es importante tener en cuenta que el uso de "break" debe ser considerado cuidadosamente,
ya que puede hacer que el flujo de ejecución sea menos predecible si no se utiliza de manera clara y
justificada."""

# Ejemplo_instruccion_break_while.py

# Explicación:
"""Definimos una variable llamada "contenedor" y le asignamos el valor inicial de 0.  Esta  variable
controla el número de iteraciones del bucle "while" y contiene el valor actual  de  "contenedor"  en
cada iteración.

Utilizamos el bucle "while" para ejecutar un bloque de código mientras se cumpla una condición. Para
ello, escribimos la palabra clave "while", seguida de la condición entre paréntesis y terminada  con
dos puntos (:). La condición en este caso es que el valor de "contenedor" sea menor o  igual  a  10.
Esta condición se compone de: la variable "contenedor", el operador de comparación (<=) y  el  valor
entero 10. Si la condición se cumple (si "contenedor" es menor o igual a 10), se ejecuta  el  bloque
de código asociado al bucle "while".

Dentro del bucle "while", utilizamos el  condicional  "if"  para  evaluar  si  el  valor  actual  de
"contenedor" es igual a 5 y, si es así, interrumpir el bucle. Para ello, escribimos la palabra clave
"if", seguida de la condición entre paréntesis y terminada con  dos  puntos  (:).  La  condición  se
compone de la variable "contenedor", el operador de igualdad  (==)  y  el  número  5.  Colocamos  el
condicional "if" justo debajo del "while" y con una indentación de cuatro espacios desde  el  margen
izquierdo, indicando que pertenece al bucle "while" y debe evaluarse en cada iteración del bucle.

A continuación, utilizamos la instrucción "break" asociada al condicional "if" para  interrumpir  el
bucle cuando esta condición se cumpla, es decir, cuando "contenedor" sea igual  a  5.  Colocamos  la
instrucción "break" justo debajo del condicional "if", con una indentación de cuatro espacios  desde
el propio condicional, indicando  que  esta  instrucción  se  ejecuta  únicamente  al  cumplirse  la
condición y no en cada iteración del bucle. De este modo, al cumplirse la  condición  del  "if",  el
bucle se interrumpe inmediatamente mediante "break", garantizando que el ciclo no continúe.

Además, dentro del bucle "while", utilizamos la función "print()" para mostrar el valor actual de la
variable "contenedor" en cada iteración acompañado de un mensaje descriptivo en formato  "f-string".
Colocamos esta instrucción justo debajo de la instrucción "break", con la misma indentación  que  el
condicional "if", ya que está asociada al bloque "while". Es importante realizar este paso antes  de
incrementar la variable, para  que  el  valor  actual  de  la  variable  se  imprima  antes  de  ser
incrementado en cada iteración del bucle y el resultado sea el esperado.

Luego, incrementamos el valor de "contenedor" en  1  hasta  que  la  condición  del  bucle  deje  de
cumplirse (contenedor > 10). Para ello, utilizamos la expresión de incremento "contenedor += 1", que
es una forma concisa de escribir "contenedor = contenedor + 1". De esta forma, sumamos  1  al  valor
actual de la variable en cada iteración y asignamos el resultado a la misma variable.

Esto asegura que la condición del bucle  eventualmente  se  vuelva  falsa,  evitando  así  un  bucle
infinito. Aunque en este caso, el bucle se interrumpirá  antes  de  que  la  condición  asociada  al
"while" deje de cumplirse debido a la instrucción "break" asociada al condicional "if".

Por último, después del bloque de código asociado al bucle "while", utilizamos la función  "print()"
para imprimir un mensaje indicando que el bucle ha terminado debido a la instrucción  "break".  Este
mensaje se ejecutará una vez que el bucle finalice, ya sea porque la  condición  del  bucle  "while"
deje de cumplirse o por la instrucción "break" y se coloca sin indentación, es decir, al mismo nivel
que la palabra clave "while"."""

# Código:
contenedor = 0

while (contenedor <= 10):
    if (contenedor == 5):
        break
    print(f"El valor actual de la variable contenedor es: {contenedor}")
    contenedor += 1

print("El bucle ha terminado debido a la instrucción break.")

# Nota Importante:
"""La instrucción "break" en Python es una herramienta poderosa que  permite  interrumpir  de  forma
inmediata la ejecución de un bucle cuando se cumple una condición específica.  Esto  proporciona  un
control preciso sobre el flujo de ejecución del programa, ya que permite detener el bucle  antes  de
que complete todas sus iteraciones previstas. Es importante destacar  que  "break"  solo  afecta  al
bucle en el que se encuentra, sin impactar a otros bucles externos ni al flujo general del programa.


En este ejemplo, se utiliza un bucle "while" para ejecutar un  bloque  de  código  siempre  que  una
condición se cumpla. Sin embargo, gracias a la instrucción "break", el bucle se  detiene  cuando  la
condición "if" se cumple.  Esto  ocurre  porque,  al  evaluar  la  condición  del  condicional  "if"
(contenedor == 5), esta se cumple y se ejecuta la instrucción "break", saliendo  inmediatamente  del
bucle. Como resultado, el número 5 nunca se imprime, ya que la instrucción "break" se ejecuta  antes
de la llamada a la función "print()".

Además, el uso de "break" es especialmente útil en situaciones  donde  se  necesita  interrumpir  un
bucle basado en una condición específica, como al buscar un elemento en  una  lista  o  al  procesar
datos hasta que se cumpla un  criterio  determinado.  Sin  embargo,  es  fundamental  utilizar  esta
instrucción de manera clara y justificada, ya que un uso inadecuado puede  hacer  que  el  flujo  de
ejecución sea menos predecible y más difícil de entender.

Por último, es importante recordar que "break" no debe ser confundido con "continue".  Mientras  que
"break" detiene por completo la ejecución del bucle, "continue" simplemente  salta  a  la  siguiente
iteración sin finalizar el  bucle.  Comprender  estas  diferencias  es  clave  para  utilizar  estas
herramientas de control de flujo de  manera  efectiva  y  eficiente  en  Python.  Las  instrucciones
"continue" y "pass" se explican en las siguientes secciones."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
