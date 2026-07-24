# Enunciado:
""""La instrucción "pass" en Python es una instrucción nula que no realiza ninguna acción cuando  se
ejecuta. Se utiliza como un marcador de posición en bloques de código donde aún no  se  ha  definido
una implementación, como en funciones, clases o bucles. Esto significa que, cuando el intérprete  de
Python encuentra una instrucción "pass", simplemente la ignora y continúa con la siguiente línea  de
código.

Cuando se utiliza "pass" dentro de un bucle "while", este no afecta el flujo de ejecución del bucle.
En lugar de realizar una acción específica, el programa simplemente continúa evaluando la  condición
del bucle y ejecutando las siguientes iteraciones. Esto puede  ser  útil  en  situaciones  donde  se
necesita estructurar el código, pero aún no se ha decidido qué acción tomar en ciertas condiciones.

En el caso de bucles "while", "pass" permite que el programa ignore temporalmente la  implementación
de un bloque de código sin interrumpir el flujo general  del  bucle.  A  diferencia  de  "continue",
"pass" no salta directamente al inicio de la siguiente iteración, sino que  simplemente  no  ejecuta
ninguna acción en el bloque donde se encuentra. Es importante destacar que "pass" no  interrumpe  el
flujo del programa ni modifica el comportamiento del bucle.

Por último, el uso de "pass" es común en  el  desarrollo  de  código  donde  se  desea  mantener  la
estructura del programa mientras se trabaja en otras partes del mismo. Aunque su uso en bucles puede
no ser muy práctico, es útil para entender cómo funciona en diferentes contextos. Por ejemplo, en un
bucle "while", "pass" puede ser  utilizado  para  omitir  temporalmente  la  implementación  de  una
condición específica mientras se continúa evaluando la condición del bucle."""

# Ejemplo_instruccion_pass_while.py

# Explicación:
"""Definimos una variable llamada "contenedor" y le asignamos el valor inicial de 0.  Esta  variable
controla el número de iteraciones del bucle "while" y almacena su valor actual en cada iteración.

Utilizamos el bucle "while" para ejecutar un bloque de código mientras se cumpla una condición. Para
ello, escribimos la palabra clave "while", seguida de la condición entre paréntesis y terminada  con
dos puntos (:). La condición en este caso es que el valor de "contenedor" sea menor  o  igual  a  5.
Esta condición se compone de: la variable "contenedor", el operador de comparación (<=) y  el  valor
entero 5. Si la condición se cumple (si "contenedor" es menor o igual a 5), se ejecuta el bloque  de
código asociado al bucle "while".

Dentro del bucle "while", utilizamos el  condicional  "if"  para  evaluar  si  el  valor  actual  de
"contenedor" es un número par (contenedor % 2 == 0) y, si es así, no realizar ninguna  acción.  Para
ello, escribimos la palabra clave "if", seguida de la condición entre paréntesis y terminada con dos
puntos (:). La condición se compone de la variable "contenedor", el operador módulo (%),  el  número
entero 2, el operador de comparación (==) y el valor entero 0. Colocamos el condicional "if" con una
indentación de cuatro espacios desde el margen izquierdo, indicando que pertenece al bucle "while" y
debe evaluarse en cada iteración del bucle.

A continuación, utilizamos la instrucción "pass" asociada  al  condicional  "if"  para  no  realizar
ninguna acción si la condición se cumple, es decir, cuando el valor de "contenedor"  sea  un  número
par. Colocamos la instrucción "pass" justo debajo del condicional "if"  y  con  una  indentación  de
cuatro espacios desde el propio condicional "if", indicando que esta instrucción  se  debe  ejecutar
cuando la condición "if" se cumpla y no en cada iteración del bucle. Es importante darse  cuenta  de
que "pass" no afecta el valor de "contenedor" ni el flujo del bucle.

De esta forma, si el valor iterado es un número par,  se  ejecuta  la  instrucción  "pass",  que  no
realiza ninguna acción y permite que el flujo del bucle continúe con normalidad.

Añadimos un condicional "else" asociado al condicional "if", el cual contiene un  bloque  de  código
que se ejecutará cuando la condición del "if" no se cumpla, es decir, cuando "contenedor" no sea  un
número par. Colocamos el condicional "else" con una indentación de cuatro espacios desde  el  margen
izquierdo, indicando que está asociado al condicional "if". Esto significa que el bloque  de  código
dentro del "else" se ejecutará únicamente cuando la condición del "if" no se cumpla en la  iteración
actual.

El bloque de código  asociado  al  condicional  "else"  es  una  instrucción  "print()"  en  formato
"f-string" que imprime el valor actual de "contenedor" en cada iteración siempre  que  la  condición
del "if" no se cumpla. Colocamos esta instrucción justo debajo del  condicional  "else"  y  con  una
indentación de cuatro espacios desde el propio condicional "else", indicando que pertenece a este  y
debe ejecutarse cuando la condición del "if" no se cumpla.

A continuación, incrementamos el valor de "contenedor" en 1 hasta que la condición del bucle deje de
cumplirse (contenedor > 5). Para ello, utilizamos la expresión de incremento "contenedor += 1",  que
es una forma abreviada de escribir "contenedor = contenedor + 1". De esta forma, sumamos 1 al  valor
actual de la variable en cada iteración y asignamos el resultado a la misma variable.  Esto  asegura
que la condición  del  bucle  eventualmente  se  vuelva  falsa,  permitiendo  así  que  la  variable
"contenedor" se actualice en cada iteración.

Por último, después del bloque de código asociado al bucle "while", utilizamos la función  "print()"
para imprimir un mensaje indicando que el bucle ha finalizado. Este mensaje se ejecutará una vez que
el bucle finalice, es decir, cuando la condición del bucle "while" deje de cumplirse.  Este  mensaje
se coloca sin indentación, es decir, al mismo nivel que la palabra clave "while."""

# Código:
contenedor = 0

while (contenedor <= 5):
    if (contenedor % 2 == 0):
        pass
    else:
        print(f"números impares: {contenedor}")
    contenedor += 1

print("El bucle ha finalizado.")

# Nota Importante:
"""En este ejemplo, la instrucción "pass" se utiliza para  omitir  la  impresión  de  números  pares
dentro del bucle "while". Cuando el valor de "contenedor" es un número par, la instrucción "pass" se
ejecuta, lo que significa que no se realiza ninguna acción y  el  programa  continúa  con  el  flujo
normal del bucle. Por otro lado, cuando el valor de "contenedor" es un número impar, se  imprime  en
la consola.

Es por ello que es importante colocar  un  condicional  "else"  asociado  al  condicional  "if"  que
contiene la instrucción "pass"; de lo contrario, no se ejecutaría ninguna acción en las  iteraciones
donde "contenedor" es un número impar y no se imprimiría nada en la consola.

Por último, en este caso, el incremento se realiza al final, ya que el valor inicial de "contenedor"
es 0 (un número par). Si el incremento se realizara al principio del bucle, el primer valor evaluado
sería 1 (un número impar) y se imprimiría en la consola en la primera iteración, tras  evaluarse  la
condición del "if". En ese caso, la instrucción "pass" dejaría de aplicarse al valor inicial 0,  por
lo que el ejemplo perdería parte de su intención didáctica."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
