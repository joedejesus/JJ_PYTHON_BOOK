# Enunciado:
""""La instrucción "pass" en Python es una instrucción nula que no realiza ninguna acción cuando  se
ejecuta. Se utiliza como un marcador de posición en bloques de código donde aún no  se  ha  definido
una implementación, como en funciones, clases o bucles. Esto significa que, cuando el intérprete  de
Python encuentra una instrucción "pass", no ejecuta ninguna acción y continúa con la siguiente línea
de código.

Cuando se utiliza "pass" dentro de un bucle "for", esta instrucción no afecta el flujo de  ejecución
del bucle. En lugar de realizar una acción específica, el programa continúa normalmente con el resto
del bloque o, si no hay más instrucciones, con la  siguiente  iteración.  Esto  puede  ser  útil  en
situaciones en las que se necesita estructurar el código, pero aún no  se  ha  decidido  qué  acción
tomar en ciertas condiciones.

En el caso de los bucles "for", "pass" permite dejar temporalmente un  bloque  sin  implementar  sin
interrumpir el flujo general del bucle. Sin embargo, a diferencia de  "continue",  "pass"  no  salta
directamente al inicio de la siguiente iteración, sino que simplemente no ejecuta ninguna acción  en
el bloque donde se encuentra.

Por último, el uso de "pass" es común en el  desarrollo  de  código  cuando  se  desea  mantener  la
estructura del programa mientras se trabaja en otras partes de este. Aunque su uso en  bucles  puede
no ser muy práctico, es útil para entender cómo funciona en diferentes contextos. Por ejemplo, en un
bucle "for", "pass" puede utilizarse para  dejar  temporalmente  sin  implementación  una  condición
específica mientras se continúa iterando sobre los elementos de una tupla."""

# Ejemplo_instruccion_pass_for.py

# Explicación:
"""Definimos una variable llamada "tupla_numeros" y le asignamos una tupla de números del 1  al  10.
Luego, utilizamos un bucle "for" para iterar sobre cada elemento de la tupla. Para ello,  escribimos
la palabra clave "for", seguida de la variable "i", que representa cada elemento de la  secuencia  y
que definimos en este momento, seguida del operador "in" para indicar sobre qué  secuencia  queremos
iterar y el nombre de la secuencia, en este caso "tupla_numeros".  A  continuación,  escribimos  dos
puntos (:) para indicar el final de la expresión y el inicio del bloque de código asociado al  bucle
"for".

Dentro del bucle "for", utilizamos el condicional "if" para evaluar si el valor  actual  de  "i"  es
igual a 7 y, si es así, no realizar ninguna acción. Para ello, escribimos  la  palabra  clave  "if",
seguida de la condición entre paréntesis y terminada con dos puntos (:). La condición se compone  de
la variable "i", el operador de igualdad (==) y el número 7. Colocamos el condicional "if"  con  una
indentación de cuatro espacios desde el margen izquierdo, indicando que pertenece al bucle  "for"  y
debe evaluarse en cada iteración.

A continuación, utilizamos la instrucción "pass" asociada  al  condicional  "if"  para  no  realizar
ninguna acción si la condición se cumple,  es  decir,  cuando  "i"  sea  igual  a  7.  Colocamos  la
instrucción "pass" justo debajo del condicional "if" y con una indentación de cuatro espacios  desde
el propio condicional "if", indicando que esta instrucción debe ejecutarse cuando la  condición  del
"if" se cumpla.

Añadimos un condicional "else" asociado al condicional "if", el cual contiene un  bloque  de  código
que se ejecutará cuando la condición del "if" no se cumpla, es decir, cuando "i" no sea igual  a  7.
Colocamos el condicional "else" con una indentación de cuatro espacios desde  el  margen  izquierdo,
indicando que está asociado al condicional "if". Esto significa que el bloque de código  dentro  del
"else" se ejecutará únicamente cuando la condición del "if" no se cumpla en la iteración actual.

El bloque de código asociado al condicional "else" es una instrucción "print()" que imprime el valor
actual de "i" en cada iteración, siempre que la condición del "if" no se cumpla,  acompañada  de  un
mensaje descriptivo en formato "f-string". Colocamos esta instrucción con una indentación de  cuatro
espacios desde el propio condicional "else", indicando que pertenece a este y debe ejecutarse cuando
la condición del "if" no se cumpla.

Por último, fuera del bucle "for", utilizamos la función  "print()"  para  mostrar  un  mensaje  que
indica que el bucle ha finalizado la impresión de todos los números excepto el número  7.  Colocamos
esta instrucción sin indentación, indicando que no pertenece al bucle "for" y que se  ejecutará  una
vez que el bucle haya finalizado todas sus iteraciones."""

# Código:
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in tupla_numeros:
    if (i == 7):
        pass
    else:
        print(f"Este es el valor actual de i en esta iteración: {i}")

print("El bucle ha finalizado la impresión de todos los números excepto el número 7.")

# Nota Importante:
"""La instrucción "pass" en Python es una instrucción nula que no realiza ninguna acción  cuando  se
ejecuta. Se utiliza como un marcador de posición en bloques de código donde aún no  se  ha  definido
una implementación, como en funciones, clases o bucles. En este contexto, "pass"  no  interrumpe  el
flujo del programa ni afecta el comportamiento del bucle.

En este ejemplo, "pass" se ejecuta cuando el valor de "i" es igual a  7,  pero  no  realiza  ninguna
acción. Esto significa que el programa continúa normalmente después de ejecutar esa instrucción.  Es
importante destacar que "pass" no "ignora" iteraciones, sino  que  simplemente  no  realiza  ninguna
acción en el bloque donde se encuentra  y,  por  tanto,  el  flujo  del  bucle  "for"  continúa  con
normalidad. En este caso, cuando "i" es igual a 7, no se imprime nada y el  bucle  continúa  con  la
siguiente iteración.

Aunque el uso de "pass" en este ejemplo no tiene un propósito práctico,  su  utilidad  se  comprende
mejor en otros contextos, como en la definición de funciones, clases o estructuras  de  control  que
aún no se han implementado por completo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
