# Enunciado:
"""El condicional "if" en Python es una estructura de control de flujo  que  ejecuta  un  bloque  de
código solo si una condición se evalúa como verdadera. Es uno de los  pilares  fundamentales  de  la
programación condicional y tiene una sintaxis sencilla y legible. La estructura básica  consiste  en
escribir la palabra clave "if" seguida de una condición. Si la condición se evalúa  como  verdadera,
se ejecuta el bloque de código asociado, que debe estar correctamente indentado. Si la condición  es
falsa, el bloque se omite.

La equivalencia semántica del condicional "if" al español es "si". Por ejemplo,  "if  x  >  10:"  se
traduce como "si x es mayor que 10: haz esto".

Además, los condicionales pueden extenderse con "elif"  (abreviatura  de  "else  if")  para  evaluar
condiciones adicionales y con "else" para definir un  bloque  que  se  ejecuta  si  ninguna  de  las
condiciones previas es verdadera. Python utiliza la indentación para definir los bloques de  código,
lo que asegura claridad y legibilidad. Es posible combinar condiciones utilizando operadores lógicos
como "and", "or" y "not" para crear expresiones más complejas.

En Python, cualquier valor que no sea "0", "vacío" o "None" se evalúa como verdadero,  mientras  que
"0", "vacío" o "None" se evalúan como falsos. Para comprobar esto, basta con escribir el valor o  la
variable que lo contiene seguido de un condicional "if". Si el valor es verdadero, se  ejecutará  el
bloque de código asociado; de lo contrario, se omitirá."""

# Ejemplo_condicional_if.py

# Explicación:
"""Definimos dos variables, "x" y "z", y les asignamos los valores enteros 10 y 5,  respectivamente.
Luego, utilizamos el condicional "if" para verificar si la variable "x" es igual a  10.  Para  ello,
escribimos la palabra clave "if" seguida de la condición entre paréntesis y terminada con dos puntos
(:). La condición se compone de la variable "x", el operador de igualdad (==) y el valor 10.

Si la condición se cumple (si x es igual a 10), se imprime un mensaje en la  consola  utilizando  la
función "print()", el cual corresponde  al  bloque  de  código  asociado  al  condicional  "if"  que
colocamos justo debajo y con una indentación de cuatro espacios. Después del bloque "if", se imprime
otro mensaje indicando el fin del programa, el cual se imprimirá siempre, independientemente  de  si
la condición se cumple o no, ya que está fuera del bloque "if".

Realizamos una segunda verificación. Esta vez utilizamos el condicional "if" para  verificar  si  la
variable "x" es igual a 10 y la variable "z" es igual a 5. Para ello, escribimos  la  palabra  clave
"if" seguida de las condiciones  entre  paréntesis,  separadas  por  el  operador  lógico  "and",  y
terminadas con dos puntos (:). La primera condición se compone de la variable "x",  el  operador  de
igualdad (==) y el valor 10. La segunda condición se compone de la  variable  "z",  el  operador  de
igualdad (==) y el valor 5.

Si ambas condiciones se cumplen (si x es igual a 10 y z es igual a 5), se imprime un mensaje  en  la
consola utilizando la función "print()", el  cual  corresponde  al  bloque  de  código  asociado  al
condicional "if" que colocamos justo debajo y con una indentación de cuatro  espacios.  Después  del
bloque "if", se imprime otro mensaje indicando el fin del programa, el cual  se  imprimirá  siempre,
independientemente de si la condición se cumple o no, ya que está fuera del bloque "if".

En estos casos, se imprimirán ambos mensajes, ya que las variables "x" y "z" tienen los valores 10 y
5, respectivamente, y ambas condiciones se cumplen."""

# Código:
x = 10
z = 5

if (x == 10):
    print("La variable es igual a 10")

print("Fin del programa")

if (x == 10) and (z == 5):
    print("Ambas condiciones son verdaderas")

print("Fin del programa")

# Nota Importante:
"""El uso correcto de la indentación es fundamental en Python,  ya  que  define  la  estructura  del
código. Para asociar un bloque de código a un condicional "if", se  debe  utilizar  una  indentación
consistente. La convención más común es usar  cuatro  espacios  por  nivel  de  indentación.  Si  la
indentación no es correcta, se producirá un error de sintaxis.

Se pueden usar  paréntesis  en  las  condiciones  para  mejorar  la  legibilidad,  especialmente  al
combinarlas con operadores lógicos como "and" y "or". Esto ayuda a evitar confusiones sobre el orden
de evaluación, ya que Python sigue las reglas de precedencia de operadores.

Además, el condicional "if" puede evaluar cualquier expresión que devuelva un valor  booleano.  Esto
incluye comparaciones entre números, cadenas de texto, listas, entre otros. También puede evaluar la
presencia o ausencia de elementos en una colección o si una  variable  está  definida.  Los  valores
vacíos como cadenas (""), listas ([]), tuplas  (()),  diccionarios  ({}),  y  conjuntos  (set())  se
evalúan como falsos. Esto está definido en las reglas de evaluación de valores booleanos en Python.

Es posible anidar estructuras "if" dentro de otras, pero  esto  puede  afectar  la  legibilidad  del
código. Por ello, se recomienda usar esta técnica con moderación. Si se tienen múltiples condiciones
similares, es preferible simplificar el código utilizando estructuras como  listas,  diccionarios  o
bucles en lugar de múltiples condicionales "if".

Por último, escribir condiciones claras y usar comentarios para explicar la  lógica  detrás  de  las
decisiones es una buena práctica que mejora la comprensión y el mantenimiento del código."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────