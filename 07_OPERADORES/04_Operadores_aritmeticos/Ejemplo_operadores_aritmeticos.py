# Enunciado:
"""Los operadores aritméticos  en  Python  son  herramientas  fundamentales  que  permiten  realizar
cálculos matemáticos y manipular datos  de  manera  eficiente.  Estos  son:  suma  (+),  resta  (-),
multiplicación (*), potencia (**), división (/), división entera (//) y módulo (%).

Usar correctamente  los  operadores  aritméticos  mejora  la  claridad  del  código  y  optimiza  el
rendimiento de los algoritmos al realizar operaciones matemáticas. Para aprovechar al  máximo  estos
operadores, es crucial considerar varios aspectos, como la precisión en cálculos  decimales,  evitar
errores como la división por cero, comprender el orden de precedencia, el orden de evaluación  y  la
regla de asociatividad de operadores, así como el tipado  dinámico  pero  estricto  de  Python  para
evitar errores de tipo. Dominar estos operadores  y  entender  sus  matices  resulta  esencial  para
escribir código robusto y eficiente en Python."""

# Ejemplo_operadores_aritmeticos.py

# Explicación:
"""Definimos una variable llamada "suma" y le asignamos la operación (2 + 3), encerrando el operador
(+) y los valores entre paréntesis (). Finalmente, usamos  la  función  "print()"  para  mostrar  el
resultado de la operación en la consola, concatenado con un mensaje descriptivo. La  operación  suma
dos números y devuelve el resultado. En este caso, 2 más 3 es igual a 5, que es el resultado  de  la
suma."""

# Código:
suma = (2 + 3)
print("El resultado de la suma es =", suma)

# Explicación:
"""Definimos una variable llamada "resta" y le  asignamos  la  operación  (5  -  2),  encerrando  el
operador (-) y los valores entre paréntesis (). Finalmente, usamos la función "print()" para mostrar
el resultado de la operación en la consola, concatenado con un  mensaje  descriptivo.  La  operación
resta dos números y devuelve el resultado. En este caso, 5 menos 2 es igual a 3, que es el resultado
de la resta."""

# Código:
resta = (5 - 2)
print("El resultado de la resta es =", resta)

# Explicación:
"""Definimos una variable llamada "multiplicacion" y le asignamos la operación (2 *  3),  encerrando
el operador (*) y los valores entre paréntesis (). Finalmente,  usamos  la  función  "print()"  para
mostrar el resultado de la operación en la consola,  concatenado  con  un  mensaje  descriptivo.  La
operación multiplica dos números y devuelve el resultado. En este caso, 2 por 3 es igual a 6, que es
el resultado de la multiplicación."""

# Código:
multiplicacion = (2 * 3)
print("El resultado de la multiplicación es =", multiplicacion)

# Explicación:
"""Definimos una variable llamada "potencia" y le asignamos la operación (2  **  3),  encerrando  el
operador (**) y los valores entre paréntesis  ().  Finalmente,  usamos  la  función  "print()"  para
mostrar el resultado de la operación en la consola,  concatenado  con  un  mensaje  descriptivo.  La
operación eleva un número a la potencia de otro y devuelve el resultado. En este caso, 2 elevado a 3
es igual a 8, que es el resultado de la potencia."""

# Código:
potencia = (2 ** 3)
print("El resultado de la potencia es =", potencia)

# Explicación:
"""Definimos una variable llamada "division" y le asignamos la operación  (5  /  2),  encerrando  el
operador (/) y los valores entre paréntesis (). Finalmente, usamos la función "print()" para mostrar
el resultado de la operación en la consola, concatenado con un  mensaje  descriptivo.  La  operación
divide dos números y devuelve el resultado. En este caso, 5 dividido entre 2 es igual a 2.5, que  es
el resultado de la división."""

# Código:
division = (5 / 2)
print("El resultado de la división es =", division)

# Explicación:
"""Definimos una variable llamada "division_entera" y le asignamos la operación (7 // 3), encerrando
el operador (//) y los valores entre paréntesis (). Finalmente, usamos  la  función  "print()"  para
mostrar el resultado de la operación en la consola,  concatenado  con  un  mensaje  descriptivo.  La
operación calcula la división entera entre dos números y devuelve el  resultado.  En  este  caso,  7
dividido entre 3 es igual a 2.3333..., pero como se trata de una división entera, se  devuelve  solo
la parte entera del resultado. Por lo tanto, 7 dividido entre 3 da como resultado 2, que es el valor
de la división entera."""

# Código:
division_entera = (7 // 3)
print("El resultado de la división entera es =", division_entera)

# Explicación:
"""Definimos una variable llamada "modulo" y le asignamos  la  operación  (7  %  2),  encerrando  el
operador (%) y los valores entre paréntesis (). Finalmente, usamos la función "print()" para mostrar
el resultado de la operación en la consola, concatenado con un  mensaje  descriptivo.  La  operación
calcula el residuo de la división entre dos números  y  devuelve  el  resultado.  En  este  caso,  7
dividido entre 2 es igual a 3, con un residuo de 1. Por lo tanto, el resultado del módulo es 1."""

# Código:
modulo = (7 % 2)
print("El resultado del módulo es =", modulo)

# Nota Importante:
"""Los operadores aritméticos siguen la jerarquía de operadores en Python. Dentro de  su  categoría,
el orden de precedencia específico es el siguiente: primero (*, /, //, %) y después (+, -). El orden
de evaluación estará determinado por la jerarquía  de  operadores  en  el  caso  de  operadores  con
diferente precedencia, por la asociatividad en el caso de operadores con igual precedencia y por  el
uso de paréntesis, con los que podemos forzar el orden de precedencia y evaluación. En este caso, la
asociatividad es de izquierda a derecha.

Aunque en este ejemplo hemos incluido la exponenciación, este operador  tiene  su  propia  categoría
dentro de la jerarquía de  operadores.  Su  precedencia  es  más  alta  que  la  de  los  operadores
aritméticos básicos. Esto significa que las operaciones de exponenciación se evaluarán antes que las
operaciones aritméticas, a menos que se utilicen paréntesis para modificar el orden de precedencia y
evaluación. Además, la asociatividad en el caso de la exponenciación es de derecha a izquierda.

Por último, es fundamental recordar que estos operadores pueden aplicarse a variables,  siempre  que
estas representen valores numéricos, lo cual permite realizar cálculos  dinámicos  y  reutilizables.
Para evitar errores inesperados, es buena práctica utilizar paréntesis para dejar claro el orden  de
evaluación de las operaciones, especialmente en expresiones complejas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────