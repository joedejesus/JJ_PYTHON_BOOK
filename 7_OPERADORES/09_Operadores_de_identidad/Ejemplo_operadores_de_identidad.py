# Enunciado:
"""Los operadores de identidad en Python son herramientas que permiten verificar  si  dos  variables
apuntan al mismo objeto en memoria, devolviendo un valor booleano (True o False) como resultado.

Estos operadores son: "is" e "is not". El operador "is" verifica si dos variables apuntan  al  mismo
objeto, mientras que el operador "is not" verifica si dos variables no apuntan al mismo objeto.

La equivalencia semántica de los operadores de identidad en español es: (is = es) y  (is  not  =  no es).

Además, es posible aplicar los operadores "is" e "is not" a cualquier tipo de objeto en  Python,  no
solo a números o cadenas. Esto incluye listas, diccionarios, instancias  de  clases  personalizadas,
entre otros.

Estos operadores son útiles para verificar si dos variables hacen referencia  al  mismo  objeto,  en
lugar de comparar sus valores. Es importante destacar que, aunque dos objetos puedan tener el  mismo
valor, no necesariamente son el mismo objeto en memoria.

Los operadores de identidad son esenciales en la programación porque permiten realizar comparaciones
precisas entre objetos, lo que resulta útil en estructuras de control como los  condicionales  "if",
"elif" y "else", así como en otros contextos donde  es  necesario  verificar  la  identidad  de  los
objetos.

Por último, dominar los operadores de  identidad  permite  escribir  código  más  robusto  y  claro,
facilitando el control del flujo según las necesidades. Además, su uso adecuado contribuye a  evitar
errores lógicos relacionados con la comparación de objetos en memoria. Esto ayuda a comprender  cómo
Python gestiona las referencias y la memoria."""

# Ejemplo_operadores_de_identidad.py

# Explicación:
"""Definimos dos variables, "x" e "y", y les asignamos, respectivamente, una lista  con  los  mismos
elementos. Luego, verificamos la identidad entre las variables "x" e "y". Para  ello,  colocamos  el
operador "is" entre las dos variables, encerramos la verificación entre paréntesis  y  asignamos  el
resultado de la verificación a una variable con un nombre descriptivo.

Por último, usamos la función "print()" para mostrar el resultado de la verificación  acompañado  de
un mensaje descriptivo. En este caso, el resultado de la verificación es (False), ya que "x"  e  "y"
no son el mismo objeto en memoria.

A continuación, asignamos "x" a "z" de esta forma (z = x). Colocamos primero la nueva variable "z" y
luego le asignamos la referencia de "x",  ya  que  "z"  no  está  definida  previamente.  Con  esto,
conseguimos que "z" apunte al mismo objeto que "x".

Realizamos una segunda verificación de identidad, esta vez entre las variables "x" y "z". Para ello,
colocamos el operador "is not" entre las dos variables, encerramos la verificación entre  paréntesis
y asignamos el resultado de la verificación a una variable con un nombre  descriptivo.  Por  último,
usamos la función "print()" para mostrar el resultado de la verificación acompañado  de  un  mensaje
descriptivo. En este caso, el resultado de la verificación es (False), ya que "x" y "z" son el mismo
objeto en memoria.

Finalmente, usamos la función "print()" para mostrar el valor de la variable "z" en la  consola.  El
valor es [1, 2, 3], ya que "z" apunta al mismo objeto que "x"."""

# Código:
x = [1, 2, 3]
y = [1, 2, 3]

verificacion_1 = (x is y)
print("El resultado de la verificación 1 es:", verificacion_1)

z = x

verificacion_2 = (x is not z)
print("El resultado de la verificación 2 es:", verificacion_2)

print("El valor de z es:", z)

# Nota Muy Importante:
"""En Python, al asignar una variable a otra (z = x), no se crea un nuevo objeto. En su lugar, ambas
variables apuntan al mismo objeto en memoria. Por lo tanto, cualquier cambio realizado en el  objeto
a través de una variable será visible a través de la otra.

Es recomendable usar nombres descriptivos y únicos  para  las  variables,  ya  que  esto  mejora  la
legibilidad del código y reduce la posibilidad de errores. Sin embargo, en algunos casos,  compartir
referencias entre variables puede ser necesario y útil, siempre que se haga de manera  consciente  y
controlada.

Los operadores de identidad siguen la jerarquía de operadores en Python.  Dentro  de  su  categoría,
todos los operadores tienen la misma precedencia, lo que significa que  se  evaluarán  en  el  mismo
nivel de prioridad. El orden de evaluación estará determinado por la jerarquía de operadores  en  el
caso de operadores con diferente precedencia, por la asociatividad en el caso de los  operadores  de
igual precedencia y por el uso de paréntesis, con los que podemos forzar el orden de  precedencia  y
evaluación. En este caso, la asociatividad es de izquierda a derecha.

Cabe destacar que los operadores de identidad comparten categoría con los operadores de pertenencia.
Esto significa que, en presencia de ambos, se evaluarán en el mismo nivel de prioridad y se aplicará
la misma lógica de evaluación.

Técnicamente, Python sí permite encadenar operadores de identidad dentro de la misma expresión, pero
el resultado puede ser confuso y no es habitual, por lo que se recomienda separar las expresiones o,
en su defecto, encadenarlas con operadores lógicos.

Por último, es importante recordar que los operadores de identidad no  deben  usarse  para  comparar
valores. Para comparar valores, se deben usar los operadores de igualdad (==) y desigualdad (!=)."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────