# Enunciado:
"""En Python, los operadores de asignación son herramientas fundamentales que permiten modificar  el
valor de una variable aplicando una operación matemática y almacenando  el  resultado  en  la  misma
variable, todo en una sola instrucción. Los principales operadores son: asignación simple (=),  suma
(+=), resta (-=), multiplicación (*=), potencia (**=), división (/=), división entera (//=) y módulo
(%=).

Dominar su uso mejora la legibilidad del código y evita redundancias. Para aplicarlos correctamente,
es importante respetar la jerarquía de operadores, comprender que Python permite cambiar el tipo  de
las variables durante la ejecución y prevenir errores frecuentes, como  operar  con  valores  nulos,
como "None", o con variables no inicializadas.

Estos operadores son especialmente útiles para optimizar el código dentro de  bucles,  facilitar  el
uso de contenedores y simplificar operaciones frecuentes, como incrementar, decrementar  o  acumular
valores contenidos en variables.

Además, permiten manipular índices o elementos de listas y realizar cálculos  y  actualizaciones  en
estructuras de datos de manera eficiente.

Por último, cabe destacar que existen otros operadores de asignación mucho menos  comunes,  como  el
operador de desplazamiento a la izquierda (<<=), el desplazamiento a la derecha (>>=), AND (&=), XOR
(^=) y OR (|=), los cuales permiten realizar operaciones bit a bit de manera  más  concisa.  Por  su
complejidad, se abordarán en las secciones correspondientes a bits y bytes."""

# Ejemplo_operadores_de_asignacion.py

# Explicación:
"""Definimos una variable llamada "a" y le asignamos el valor 5 utilizando el operador de asignación
simple (=), que asigna el valor a la variable situada  a  la  izquierda  del  operador.  Finalmente,
imprimimos el valor de la variable "a" usando la función "print()" para mostrar el resultado  de  la
asignación en la consola, acompañado de un mensaje descriptivo."""

# Código:
a = 5
print("El valor de a es =", a)

# Explicación:
"""Definimos una variable llamada "b" y le asignamos el valor 5 utilizando el operador de asignación
simple (=), que asigna el valor a la variable situada a la izquierda del operador. Luego,  aplicamos
el operador de asignación de suma (+=) para actualizar el valor de "b", sumándole 5. Esto equivale a
escribir "b = b + 5", lo cual, dado que "b = 5", produce el resultado "b  +  5  =  10".  Finalmente,
usamos la función "print()" para mostrar el nuevo valor de la variable "b" en la consola, acompañado
de un mensaje descriptivo."""

# Código:
b = 5
b += 5
print("La suma de (b + 5) es =", b)

# Explicación:
"""Definimos una variable llamada "c" y le asignamos el valor 5 utilizando el operador de asignación
simple (=), que asigna el valor a la variable situada a la izquierda del operador. Luego,  aplicamos
el operador de asignación de resta (-=) para actualizar el valor de "c", restándole 2. Esto equivale
a escribir "c = c - 2", lo cual, dado que "c = 5", produce el resultado "c -  2  =  3".  Finalmente,
usamos la función "print()" para mostrar el nuevo valor de la variable "c" en la consola, acompañado
de un mensaje descriptivo."""

# Código:
c = 5
c -= 2
print("La resta de (c - 2) es =", c)

# Explicación:
"""Definimos una variable llamada "d" y le asignamos el valor 5 utilizando el operador de asignación
simple (=), que asigna el valor a la variable situada a la izquierda del operador. Luego,  aplicamos
el operador de asignación de multiplicación (*=) para actualizar el valor  de  "d",  multiplicándolo
por 5. Esto equivale a escribir "d = d * 5", lo cual, dado que "d = 5", produce el resultado "d *  5
= 25". Finalmente, usamos la función "print()" para mostrar el nuevo valor de la variable "d" en  la
consola, acompañado de un mensaje descriptivo."""

# Código:
d = 5
d *= 5
print("La multiplicación de (d * 5) es =", d)

# Explicación:
"""Definimos una variable llamada "e" y le asignamos el valor 5 utilizando el operador de asignación
simple (=), que asigna el valor a la variable situada a la izquierda del operador. Luego,  aplicamos
el operador de asignación de potencia (**=) para actualizar el valor de "e", elevándolo a la  quinta
potencia. Esto equivale a escribir "e = e ** 5", lo cual, dado que "e =  5",  produce  el  resultado
"e** 5 = 3125". Finalmente, usamos la función "print()" para mostrar el nuevo valor de  la  variable
"e" en la consola, acompañado de un mensaje descriptivo."""

# Código:
e = 5
e **= 5
print("La quinta potencia de (e) es =", e)

# Explicación:
"""Definimos una variable llamada "f" y le asignamos el valor 5 utilizando el operador de asignación
simple (=), que asigna el valor a la variable situada a la izquierda del operador. Luego,  aplicamos
el operador de asignación de división (/=) para actualizar el valor de "f", dividiéndolo por 5. Esto
equivale a escribir "f = f / 5", lo cual, dado que "f = 5", produce el resultado  "f  /  5  =  1.0".
Finalmente, usamos la función "print()" para mostrar el  nuevo  valor  de  la  variable  "f"  en  la
consola, acompañado de un mensaje descriptivo."""

# Código:
f = 5
f /= 5
print("La división de (f / 5) es =", f)

# Explicación:
"""Definimos una variable llamada "g" y le asignamos el valor 7 utilizando el operador de asignación
simple (=), que asigna el valor a la variable situada a la izquierda del operador. Luego,  aplicamos
el operador de asignación de división entera (//=) para actualizar el valor de  "g",  calculando  la
parte entera de la división de "g" entre 2. Esto equivale a escribir "g = g // 2", lo cual, dado que
"g = 7", produce el resultado "g // 2 = 3", que es la parte entera de la  división  de  7  entre  2.
Finalmente, usamos la función "print()" para mostrar el  nuevo  valor  de  la  variable  "g"  en  la
consola, acompañado de un mensaje descriptivo."""

# Código:
g = 7
g //= 2
print("La parte entera de la división de (g // 2) es =", g)

# Explicación:
"""Definimos una variable llamada "h" y le asignamos el valor 7 utilizando el operador de asignación
simple (=), que asigna el valor a la variable situada a la izquierda del operador. Luego,  aplicamos
el operador de asignación de módulo (%=) para actualizar el valor de "h", calculando el  residuo  de
la división de "h" entre 2. Esto equivale a escribir "h = h % 2", lo cual, dado que "h = 7", produce
el resultado "h % 2 = 1", que es el residuo de la división de  7  entre  2.  Finalmente,  usamos  la
función "print()" para mostrar el nuevo valor de la variable "h" en la  consola,  acompañado  de  un
mensaje descriptivo."""

# Código:
h = 7
h %= 2
print("El residuo de (h % 2) es =", h)

# Nota Importante:
"""Los operadores de asignación siguen la jerarquía de operadores en Python. Dentro de su categoría,
todos los operadores tienen la misma precedencia, lo que significa que se evalúan en el mismo  nivel
de prioridad. El orden de evaluación está determinado por la jerarquía de operadores en el  caso  de
operadores con diferente precedencia, por la asociatividad en el caso de los  operadores  con  igual
precedencia y por el uso de paréntesis, con los  que  podemos  forzar  el  orden  de  precedencia  y
evaluación. En este caso, la asociatividad es de derecha a izquierda.

Estos operadores permiten asignar valores directamente a una  variable.  Estos  valores  pueden  ser
numéricos, otras variables o incluso el resultado de expresiones más complejas que se  ubican  a  la
derecha del signo de asignación, lo que permite guardar el resultado  de  una  operación  matemática
directamente en la variable, evitando la necesidad de crear una variable temporal. Esto facilita  la
reutilización de dicho valor, lo que aporta eficiencia y claridad al código.

Es importante recordar que el operador  de  asignación  simple  (=)  no  realiza  ninguna  operación
aritmética; su función es únicamente  asignar  un  valor  a  una  variable.  En  cambio,  los  demás
operadores combinan la asignación con una operación matemática, lo que  actualiza  el  valor  de  la
variable de forma directa y legible."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
