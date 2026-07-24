# Enunciado:
"""Los operadores lógicos en Python son herramientas que permiten realizar  evaluaciones  de  lógica
booleana entre dos o más valores booleanos  y  devolver  un  valor  booleano  (True  o  False)  como
resultado.

También permiten realizar evaluaciones de lógica booleana más complejas, siempre que el resultado de
cada expresión sea un valor booleano.

Estos operadores son: "and", que devuelve (True) si ambas  condiciones  son  verdaderas;  "or",  que
devuelve (True) si al menos una condición es verdadera; y "not", que invierte el valor  booleano  de
la expresión a su derecha, es decir, convierte (True) en (False) y viceversa.

El operador "not" es diferente de los otros, ya que solo requiere una expresión  para  funcionar,  a
diferencia de "and" y "or", que requieren dos. Por lo tanto, "not" es un operador  unario,  mientras
que "and" y "or" son operadores binarios. Python evalúa  "not"  antes  que  "and"  y  "or",  lo  que
facilita validaciones y negaciones más complejas.

La equivalencia semántica de los operadores lógicos en español es: (and = y), (or = o) y (not = no).

Los operadores lógicos se usan para controlar el flujo de ejecución en estructuras de  control  como
"if" o "while" y para  tomar  decisiones  basadas  en  condiciones  complejas.  Evalúan  expresiones
aritméticas, comparativas, de pertenencia, de identidad, de indexación y otros tipos de  expresiones
que produzcan valores booleanos. Gracias al "cortocircuito", "and" y "or" evitan evaluar expresiones
innecesarias, lo que mejora la eficiencia del código.

La tabla de verdad  de  los  operadores  lógicos,  que  se  presenta  a  continuación,  facilita  la
comprensión de su funcionamiento y permite evaluar todas las condiciones posibles. Esta tabla se lee
de izquierda a  derecha,  considerando  los  valores  a  evaluar  y  aplicando  el  operador  lógico
correspondiente.

|---------|---------|---------|---------|--------|
| Valor X | Valor Y | X and Y | X or Y  | not X  |
|---------|---------|---------|---------|--------|
| True    | True    | True    | True    | False  |
| True    | False   | False   | True    | False  |
| False   | True    | False   | True    | True   |
| False   | False   | False   | False   | True   |
|---------|---------|---------|---------|--------|"""

# Ejemplo_operadores_logicos.py

# Explicación:
"""Definimos dos variables llamadas "a" y  "b"  y  les  asignamos  los  valores  enteros  5  y  -10,
respectivamente. Luego, definimos una variable llamada "evaluacion_and" y le asignamos el  resultado
de una expresión lógica que combina dos  expresiones  comparativas  utilizando  el  operador  lógico
"and".

Primero, comparamos si "a" es mayor que 0, usando el operador comparativo (>) entre los dos  valores
y encerrando la expresión entre paréntesis. Luego, comparamos si "b"  es  mayor  que  0,  usando  el
operador comparativo (>)  entre  los  dos  valores  y  encerrando  la  expresión  entre  paréntesis.
Encerramos ambas expresiones entre paréntesis  y  las  combinamos  con  el  operador  lógico  "and",
colocándolo entre las dos expresiones. Por último, usamos  la  función  "print()"  para  mostrar  el
resultado de la evaluación en la consola acompañado de un mensaje descriptivo.

El operador lógico "and" evalúa si ambas condiciones son verdaderas y devuelve (True). Si  al  menos
una de ellas es falsa, el resultado será (False). En este caso, el resultado  de  la  evaluación  es
(False), ya que "b" es menor que 0."""

# Código:
a = 5
b = -10

evaluacion_and = ((a > 0) and (b > 0))
print("El resultado de la evaluación con el operador \"and\" es:", evaluacion_and)

# Explicación:
"""Definimos dos variables llamadas "c" y "d" y  les  asignamos  los  valores  enteros  158  y  568,
respectivamente. Luego, definimos una variable llamada "evaluacion_or" y le asignamos  el  resultado
de una expresión lógica que combina dos expresiones comparativas utilizando el operador lógico "or".

Primero, comparamos si "c" es mayor que 0, usando el operador comparativo (>) entre los dos  valores
y encerrando la expresión entre paréntesis. Luego, comparamos si "d"  es  mayor  que  0,  usando  el
operador comparativo (>)  entre  los  dos  valores  y  encerrando  la  expresión  entre  paréntesis.
Encerramos ambas expresiones entre  paréntesis  y  las  combinamos  con  el  operador  lógico  "or",
colocándolo entre las dos expresiones. Por último, usamos  la  función  "print()"  para  mostrar  el
resultado de la evaluación en la consola acompañado de un mensaje descriptivo.

El operador lógico "or" evalúa si al menos una de las condiciones es verdadera y devuelve (True). Si
ambas son falsas, el resultado será (False). En este caso, el resultado de la evaluación es  (True),
ya que tanto "c" como "d" son mayores que 0."""

# Código:
c = 158
d = 568

evaluacion_or = ((c > 0) or (d > 0))
print("El resultado de la evaluación con el operador \"or\" es:", evaluacion_or)

# Explicación:
"""Definimos dos variables llamadas "e" y "f" y les  asignamos  los  valores  enteros  489  y  -789,
respectivamente. Luego, definimos una variable llamada "evaluacion_not" y le asignamos el  resultado
de una expresión lógica que combina dos expresiones comparativas utilizando los  operadores  lógicos
"not" y "and".

Primero, comparamos si "e" es mayor que 0, usando el operador comparativo (>) entre los dos  valores
y encerrando la expresión entre paréntesis. Luego, comparamos si "f"  es  menor  que  0,  usando  el
operador comparativo (<)  entre  los  dos  valores  y  encerrando  la  expresión  entre  paréntesis.
Encerramos ambas expresiones entre paréntesis  y  las  combinamos  con  el  operador  lógico  "and",
colocándolo entre las dos expresiones. Además, colocamos el operador lógico "not" al principio de la
expresión, fuera del paréntesis, para invertir su valor. Por último,  usamos  la  función  "print()"
para mostrar el resultado de la evaluación en la consola acompañado de un mensaje descriptivo.

El operador lógico "not" invierte el valor booleano de la expresión a su derecha.  Si  es  verdadera
(True), la convierte en falsa (False) y viceversa. En este caso, el resultado de la  evaluación  con
el operador lógico "and" sería (True), ya que "e" es mayor que 0 y "f" es menor que 0. Sin  embargo,
al aplicar el operador lógico "not", cambiamos el valor de la expresión a su derecha a  su  opuesto,
por lo que el resultado final de la evaluación es (False)."""

# Código:
e = 489
f = -789

evaluacion_not = not ((e > 0) and (f < 0))
print("El resultado de la evaluación con el operador \"not\" es:", evaluacion_not)

# Explicación:
"""Definimos dos variables llamadas "g" y "h"  y  les  asignamos  los  valores  booleanos  (True)  y
(False),   respectivamente.   Luego,   definimos   tres   variables   llamadas   "evaluacion_and_2",
"evaluacion_or_2" y "evaluacion_not_2" y a cada una de  ellas  le  asignamos  el  resultado  de  una
expresión lógica.

En el primer caso, usamos el operador "and" para evaluar las variables "g"  y  "h".  En  el  segundo
caso, usamos el operador "or" para evaluar las variables "g" y "h" y en el  tercer  caso  usamos  el
operador "not" para invertir el valor de la variable "g". Por último, usamos  la  función  "print()"
para mostrar el resultado de cada evaluación en la consola acompañado de un mensaje descriptivo.

En este caso, el resultado de la evaluación con el operador "and" es (False), ya que "g" es (True) y
"h" es (False). El resultado de la evaluación con el operador "or" es (True), ya que "g" es (True) y
"h" es (False), y el resultado de la evaluación con el operador "not" es  (False),  ya  que  "g"  es
(True).

En este último caso, vemos cómo es posible usar los operadores lógicos con variables  que  contienen
valores booleanos  directamente,  pudiendo  guiarnos  por  la  tabla  de  verdad  para  predecir  el
resultado."""

# Código:
g = True
h = False

evaluacion_and_2 = (g) and (h)
print("El resultado de la evaluación con el operador \"and\" es:", evaluacion_and_2)

evaluacion_or_2 = (g) or (h)
print("El resultado de la evaluación con el operador \"or\" es:", evaluacion_or_2)

evaluacion_not_2 = not (g)
print("El resultado de la evaluación con el operador \"not\" es:", evaluacion_not_2)

# Nota Muy Importante:
"""Los operadores lógicos siguen la jerarquía de operadores en Python. Dentro de  su  categoría,  el
orden de precedencia específico es el siguiente: (not, and y or).  El  orden  de  evaluación  estará
determinado por la jerarquía de operadores en el caso de operadores con diferente  precedencia,  por
la asociatividad en el caso de los operadores de igual precedencia y por el uso de  paréntesis,  con
los que podemos forzar el orden de precedencia y evaluación. En este caso, la  asociatividad  es  de
izquierda a derecha.

Por otra parte, el "cortocircuito" es una característica de los operadores  lógicos  "and"  y  "or".
Significa que si la primera condición de una expresión es suficiente para determinar  el  resultado,
el resto no se evalúa. Por ejemplo, con "and", si la primera condición es falsa, el  resultado  será
(False), ya no importa lo demás; y con "or", si la primera condición es verdadera, el resultado será
(True) sin  necesidad  de  comprobar  el  resto.  Por  otro  lado,  el  operador  "not"  no  utiliza
cortocircuito, ya que invierte el valor de la expresión  a  su  derecha  antes  de  evaluarla.  Esto
optimiza el código y evita evaluaciones innecesarias."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
