# Enunciado:
"""Los condicionales anidados son estructuras de decisión que  contienen  una  condición  dentro  de
otra. Se usan para evaluar múltiples condiciones  de  forma  jerárquica,  lo  que  permite  ejecutar
diferentes bloques de código según el resultado de cada evaluación. Esto permite evaluar condiciones
adicionales dentro de una condición ya evaluada, creando lógicas más complejas y tomando  decisiones
más específicas en el código.

Los condicionales anidados son útiles cuando se necesita evaluar una condición secundaria solo si se
cumple una condición principal. Sin embargo, es importante  mantener  el  código  legible  y  evitar
anidaciones excesivas.

Se deben usar los condicionales anidados con  moderación,  ya  que  un  exceso  de  anidación  puede
dificultar la comprensión del código. En su lugar, se recomienda considerar alternativas como el uso
de los operadores lógicos "and", "or" y "not" o la  refactorización  del  código  en  funciones  más
pequeñas y modulares."""

# Ejemplo_condicionales_anidados.py

# Explicación:
"""Definimos una variable llamada "x" y le asignamos  el  valor  entero  20.  Luego,  utilizamos  el
condicional "if" para verificar si la variable "x" es mayor que 0. Para ello, escribimos la  palabra
clave "if" seguida de la condición entre paréntesis y terminada con dos puntos (:). La condición  se
compone de la variable "x", el operador mayor que (>) y el valor 0.

Si la condición se cumple (si x es mayor  que  0),  se  evalúa  el  bloque  de  código  asociado  al
condicional "if" principal, que colocamos justo debajo y con  una  indentación  de  cuatro  espacios
desde el margen izquierdo. El bloque de código asociado al condicional "if" principal está compuesto
por un bloque "if...else" anidado.

Dentro de este bloque, utilizamos el condicional "if" para verificar si la variable "x" es menor que
10. Para ello, escribimos la palabra clave "if" seguida de la condición entre paréntesis y terminada
con dos puntos (:). La condición se compone de la variable "x", el operador menor que (<) y el valor
10.

Si la condición se cumple (si x es menor que 10), se imprime un mensaje en la consola utilizando  la
función "print()", el cual corresponde al bloque de código asociado al condicional "if" anidado  que
colocamos justo debajo y con una indentación de cuatro espacios desde  el  propio  condicional  "if"
anidado.

A continuación, utilizamos el condicional "else" para manejar el caso en el que  la  condición  "if"
anidada no se cumpla. Para ello, escribimos la palabra clave "else" seguida de dos puntos (:).

Si la condición "if" anidada no se cumple (si x no es menor que 10), se imprime  un  mensaje  en  la
consola utilizando la función "print()", el  cual  corresponde  al  bloque  de  código  asociado  al
condicional "else" anidado que colocamos justo debajo y con una indentación de cuatro espacios desde
el propio condicional "else" anidado.

Por último, utilizamos un segundo condicional "else" para manejar el caso en que la  condición  "if"
principal no se cumpla. Para ello, escribimos la palabra clave "else" seguida de dos puntos (:).

Si la condición "if" principal no se cumple (si x no es mayor que 0), se imprime un  mensaje  en  la
consola utilizando la función "print()", el  cual  corresponde  al  bloque  de  código  asociado  al
condicional "else" principal que colocamos justo debajo y con una  indentación  de  cuatro  espacios
desde el margen izquierdo.

En este caso específico, como la variable "x" tiene el valor 20,  la  condición  "if"  principal  se
cumple (20 es mayor que 0), pero la condición "if" anidada no se cumple (20 no es menor que 10). Por
lo tanto, se ejecuta el bloque de código asociado al  condicional  "else"  anidado,  imprimiendo  el
mensaje "x es un número positivo mayor que 10" en la consola."""

# Código:
x = 20

if (x > 0):
    if (x < 10):
        print("x es un número positivo entre 0 y 10")
    else:
        print("x es un número positivo mayor que 10")
else:
    print("x es un número negativo")

# Nota Muy Importante:
"""Los condicionales anidados solo deben  utilizarse  cuando  sea  estrictamente  necesario  evaluar
múltiples condiciones de forma jerárquica. Si  las  condiciones  son  independientes  entre  sí,  es
preferible emplear condicionales simples para mantener el código más legible y fácil de entender.

El uso excesivo de condicionales anidados puede dificultar la lectura y el mantenimiento del código,
ya que puede volverse complicado seguir la lógica de  las  decisiones.  Por  ello,  es  recomendable
evaluar si es posible simplificar la lógica o utilizar otras estructuras de control, como  funciones
o clases, para organizar el código de manera más clara y modular.

Además, es fundamental mantener  una  buena  indentación  y  organización  del  código  para  evitar
confusiones y errores al leer y mantener el código. Asimismo, existen otras estructuras  de  control
de flujo, como los bucles "for" y "while",  así  como  las  funciones,  que  pueden  complementar  o
reemplazar el uso de condicionales anidados. Estas estructuras permiten repetir bloques de código  o
encapsular lógica en funciones, mejorando la  legibilidad  y  la  reutilización  del  código.  Estos
aspectos son esenciales para escribir código limpio y mantenible y serán tratados en profundidad  en
secciones posteriores.

En cuanto a la correcta indentación, cabe destacar que: Los  condicionales  principales  se  colocan
pegados al margen izquierdo y su bloque asociado se coloca con una indentación  de  cuatro  espacios
desde el margen izquierdo. Cada condicional anidado se coloca con una indentación de cuatro espacios
desde el margen izquierdo, y cada bloque de código asociado a un condicional anidado se  coloca  con
una indentación adicional de cuatro espacios desde el propio condicional anidado al que pertenece.

Cada vez que asociamos un bloque a un condicional (ya sea principal o anidado), debemos  asegurarnos
de que el bloque de código asociado se coloque justo debajo y respete la indentación  adecuada  para
mantener  la  estructura  jerárquica  del  código.  Esto  es  crucial  para  que  Python  interprete
correctamente la relación entre los condicionales y sus  bloques  de  código  asociados.  Aunque  es
posible dejar espacios en blanco entre los condicionales y sus bloques asociados, es recomendable no
hacerlo para mantener la claridad y la estructura del código.

Por último, es importante tener en cuenta que, en cuanto la condición "if" principal se cumple,  las
demás alternativas del mismo bloque no se evalúan, dando paso a la  evaluación  de  las  condiciones
anidadas. Esto es importante  para  optimizar  el  rendimiento  del  código  y  evitar  evaluaciones
innecesarias."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
