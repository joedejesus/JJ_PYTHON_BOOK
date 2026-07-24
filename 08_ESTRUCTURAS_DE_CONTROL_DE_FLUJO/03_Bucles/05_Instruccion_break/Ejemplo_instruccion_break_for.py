# Enunciado:
"""La instrucción "break" en Python permite interrumpir de forma inmediata la ejecución de un  bucle
cuando se cumple una condición  específica.  Esto  ocurre  independientemente  de  si  el  bucle  ha
completado todas sus iteraciones previstas o no.

En cuanto la condición asociada a la instrucción "break" se evalúa como  verdadera,  la  instrucción
"break" se ejecuta y el bucle se detiene. El control del programa pasa entonces a la  primera  línea
de código que sigue al bucle, lo que proporciona un control más preciso sobre el flujo de  ejecución
del programa.

"Break" en español significa "romper" o "interrumpir", y su función  principal  es  proporcionar  un
control más preciso sobre el flujo de ejecución del programa.

La instrucción "break" puede ser utilizada tanto en bucles "for" como en bucles "while". En el  caso
de bucles anidados, "break" solo afecta al bucle en el que se encuentra, sin impactar a  los  bucles
externos. Esto es útil para manejar estructuras de control complejas de manera eficiente.

El uso de "break" es común en situaciones donde se necesita  interrumpir  un  bucle  basado  en  una
condición específica. Por ejemplo, se puede utilizar para detener la búsqueda de un elemento en  una
lista una vez que se encuentra, o para salir de un bucle cuando se cumple un criterio en un conjunto
de datos.

Por último, es importante tener en cuenta que el uso de "break" debe considerarse cuidadosamente, ya
que puede hacer que el flujo de ejecución sea menos predecible si no se utiliza de  manera  clara  y
justificada."""

# Ejemplo_instruccion_break_for.py

# Explicación:
"""Definimos una variable llamada "lista_numeros" y le asignamos una lista de números del 1  al  10.
Luego, utilizamos un bucle "for" para iterar sobre cada elemento de la lista. Para ello,  escribimos
la palabra clave "for", seguida de la variable "i", que representa cada elemento de la  secuencia  y
que definimos en este momento, seguida del operador "in" para indicar sobre qué  secuencia  queremos
que se realice la iteración y el nombre de la secuencia sobre la que queremos iterar, en  este  caso
"lista_numeros". A continuación, escribimos dos puntos (:) para indicar el final de la  expresión  y
el inicio del bloque de código asociado al bucle "for".

Dentro del bucle "for", utilizamos el condicional "if" para evaluar si el valor  actual  de  "i"  es
igual a 5 y, si es así, interrumpir el bucle. Para ello, escribimos la palabra clave  "if",  seguida
de la condición entre paréntesis y terminada con dos puntos (:).  La  condición  se  compone  de  la
variable "i", el operador de igualdad (==) y el número 5. Colocamos  el  condicional  "if"  con  una
indentación de cuatro espacios desde el margen izquierdo, indicando que pertenece al bucle  "for"  y
debe evaluarse en cada iteración del bucle.

A continuación, utilizamos la instrucción "break" asociada al condicional "if" para  interrumpir  el
bucle si la condición se cumple, es decir, cuando "i"  sea  igual  a  5.  Colocamos  la  instrucción
"break" justo debajo del condicional "if" y con una indentación de cuatro espacios desde  el  propio
condicional "if", indicando que esta instrucción se debe ejecutar cuando la condición "if" se cumpla
y no en cada iteración del bucle.

Utilizamos la función "print()" para imprimir un mensaje en formato "f-string" acompañado del  valor
actual de "i" en cada iteración del bucle. Colocamos esta instrucción con una indentación de  cuatro
espacios desde el margen izquierdo, indicando que pertenece al bucle "for" y debe ejecutarse en cada
iteración del bucle hasta que la  condición  "if"  se  cumpla  y  el  bucle  se  interrumpa  con  la
instrucción "break".

Por último, añadimos un condicional "else" asociado al bucle "for", el cual contiene  un  bloque  de
código que se ejecutará si el bucle se completa sin interrupciones, cosa que  no  ocurrirá  en  este
caso debido a la presencia de la instrucción "break". De esta forma  demostramos  que  el  bucle  se
interrumpe antes de completarse.

Además, colocamos el condicional "else" al mismo nivel de indentación que el bucle "for",  indicando
que está asociado a este bucle y no al condicional "if", y debe evaluarse una vez que el bucle  haya
finalizado todas sus iteraciones. El bloque de código asociado a este condicional es una instrucción
"print()" que imprime un mensaje indicando que el bucle se ha completado sin interrupciones.

El bucle comienza a iterar sobre cada elemento  de  la  lista.  En  cada  iteración,  se  evalúa  la
condición del condicional "if". Si esta condición no se cumple (i no es  igual  a  5),  se  continúa
ejecutando la instrucción "print()" e imprimiendo el valor actual de "i" hasta que la  condición  se
cumpla (i == 5). Cuando esto ocurre, se ejecuta la instrucción  "break",  dejando  de  iterar  y  de
imprimir el valor de "i".

Como resultado, se imprimen los números del 1 al 4, sin embargo, el número 5 nunca  se  imprime,  ya
que la instrucción "break" se ejecuta antes de la llamada a la función "print()". Además, el  bloque
de código dentro del condicional "else" no se ejecuta, ya  que  el  bucle  se  interrumpe  antes  de
completarse."""

# Código:
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista_numeros:
    if (i == 5):
        break
    print(f"Este es el valor de i en este momento: {i}")
else:
    print("El bucle se ha completado sin interrupciones.")

# Nota Importante:
"""La instrucción "break" en Python es una herramienta poderosa que  permite  interrumpir  de  forma
inmediata la ejecución de un bucle cuando se cumple una condición específica.  Esto  proporciona  un
control preciso sobre el flujo de ejecución del programa, ya que permite detener el bucle  antes  de
que complete todas sus iteraciones previstas. Es importante destacar  que  "break"  solo  afecta  al
bucle en el que se encuentra, sin impactar a otros bucles externos ni al flujo general del programa.

En este ejemplo, usamos un bucle "for" para iterar sobre una lista de  números  del  1  al  10.  Sin
embargo, gracias a la instrucción "break", el bucle se detiene antes de llegar  al  número  5.  Esto
ocurre porque, al evaluar la condición del condicional "if" (i == 5), esta se cumple y se ejecuta la
instrucción "break", saliendo inmediatamente del  bucle.  Como  resultado,  el  número  5  nunca  se
imprime, ya que la instrucción "break" se ejecuta antes  de  la  llamada  a  la  función  "print()".
Además, el bloque de código dentro del condicional  "else"  no  se  ejecuta,  ya  que  el  bucle  se
interrumpe antes de completarse.

El uso de "break" es especialmente útil en situaciones donde se necesita interrumpir un bucle basado
en una condición específica, como al buscar un elemento en una lista o al procesar datos  hasta  que
se cumpla un criterio determinado. Sin embargo, es fundamental utilizar esta instrucción  de  manera
clara y justificada, ya que un uso inadecuado puede hacer  que  el  flujo  de  ejecución  sea  menos
predecible y más difícil de entender.

Por último, es importante recordar que "break" no debe ser confundido con "continue".  Mientras  que
"break" detiene por completo la ejecución del bucle, "continue" simplemente  salta  a  la  siguiente
iteración sin finalizar el  bucle.  Comprender  estas  diferencias  es  clave  para  utilizar  estas
herramientas de control de flujo de  manera  efectiva  y  eficiente  en  Python.  Las  instrucciones
"continue" y "pass" se explican en las siguientes secciones."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
