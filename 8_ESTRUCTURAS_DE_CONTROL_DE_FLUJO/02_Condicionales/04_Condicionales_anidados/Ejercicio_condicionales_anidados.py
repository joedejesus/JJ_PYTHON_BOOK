# Enunciado:
"""Escribe un programa que evalúe si un número entero es positivo, negativo o cero. Si el número  es
positivo, el programa debe indicar si es par o impar. Si es negativo, también debe indicar si es par
o impar. Si el número es cero, el programa debe imprimir "El número es cero".

Utiliza un bloque principal "if...elif...else", condicionales  anidados  y  operadores  comparativos
para resolver el problema. El número a evaluar puede ser cualquier entero, ya sea positivo, negativo
o cero."""

# Ejercicio_condicionales_anidados.py

# Explicación:
"""Definimos una variable llamada "x" y le asignamos  el  valor  entero  13.  Luego,  utilizamos  el
condicional "if" para verificar si la variable "x" es mayor que 0. Si la condición se cumple  (si  x
es mayor que 0), se evalúa el bloque de código asociado al condicional "if" principal, que colocamos
e indentamos correctamente. El bloque de código asociado al condicional "if" principal  contiene  un
bloque "if...else" anidado.

Dentro de este bloque, utilizamos el condicional "if" para verificar si el valor de la variable  "x"
es un número par. Si la condición se cumple (si el residuo de la división de x entre 2  es  igual  a
0), se imprime un mensaje en la consola, el  cual  corresponde  al  bloque  de  código  asociado  al
condicional "if" anidado, que colocamos e indentamos correctamente.

A continuación, utilizamos el condicional "else" para manejar el  caso  en  que  la  condición  "if"
anidada no se cumpla. Si la condición "if" anidada no se cumple (si el residuo de la división  de  x
entre 2 no es igual a 0), se imprime un mensaje en la consola, el  cual  corresponde  al  bloque  de
código asociado al condicional "else" anidado, que colocamos e indentamos correctamente.

Repetimos el mismo proceso para el caso en que la condición "if" principal no se cumpla,  utilizando
un condicional "elif" para verificar si la variable "x" es menor que 0. Si la  condición  se  cumple
(si x es menor que 0), se evalúa el bloque de código asociado al condicional "elif"  principal,  que
colocamos e indentamos correctamente. El bloque de código asociado al condicional  "elif"  principal
contiene otro bloque "if...else" anidado.

Dentro de este bloque, utilizamos el condicional "if" para verificar si el valor de la variable  "x"
es un número impar. Si la condición se cumple (si el residuo de la división de x entre 2 es distinto
de 0), se imprime un mensaje en la consola, el cual corresponde al  bloque  de  código  asociado  al
condicional "if" anidado, que colocamos e indentamos correctamente.

A continuación, utilizamos el condicional "else" para manejar el  caso  en  que  la  condición  "if"
anidada no se cumpla. Si la condición "if" anidada no se cumple (si el residuo de la división  de  x
entre 2 es igual a 0), se imprime un mensaje en la consola, el cual corresponde al bloque de  código
asociado al condicional "else" anidado, que colocamos e indentamos correctamente.

Por último, utilizamos el condicional "else" para manejar el caso en  que  las  condiciones  "if"  y
"elif" principales no se cumplan. Si las condiciones "if" y "elif" principales no se cumplen  (si  x
no es mayor que 0 y si x no es menor  que  0),  se  imprime  un  mensaje  en  la  consola,  el  cual
corresponde al bloque de código asociado al condicional "else" principal, que colocamos e indentamos
correctamente.

En este caso específico, como la variable "x" tiene el valor 13,  la  condición  "if"  principal  se
cumple (13 es mayor que 0), pero la condición "if" anidada no se cumple (el residuo de  la  división
de 13 entre 2 no es igual a 0). Por lo tanto, se ejecuta el bloque de código asociado al condicional
"else" anidado, imprimiendo el mensaje "El número es positivo e impar." en la consola."""

# Código:
x = 13

if (x > 0):
    if (x % 2 == 0):
        print("El número es positivo y par.")
    else:
        print("El número es positivo e impar.")
elif (x < 0):
    if (x % 2 != 0):
        print("El número es negativo e impar.")
    else:
        print("El número es negativo y par.")
else:
    print("El número es cero.")

# Nota Importante:
"""En un bloque "if...elif...else", las condiciones son mutuamente  excluyentes.  Una  vez  que  una
condición se evalúa como verdadera, las demás no se evalúan. Esto permite que el programa  tome  una
única dirección según la condición que se cumpla.

El uso de bloques anidados es útil para evaluar condiciones  adicionales  dentro  de  una  condición
principal. Sin embargo, es importante utilizarlos  con  moderación,  ya  que  pueden  dificultar  la
legibilidad del código. Siempre se debe escribir código claro y mantenible.

En este caso, las condiciones están organizadas de manera que evalúan  si  el  número  es  positivo,
negativo o cero, y luego determinan si es par o impar. Esto asegura que las condiciones sean  claras
y no redundantes.

Por  último,  si  fuera  necesario  evaluar  más  condiciones,  se  podrían  añadir  bloques  "elif"
adicionales. Sin embargo, en este ejemplo, las condiciones actuales son suficientes para resolver el
problema."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
