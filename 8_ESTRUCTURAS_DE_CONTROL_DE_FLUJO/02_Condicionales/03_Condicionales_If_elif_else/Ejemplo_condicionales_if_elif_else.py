# Enunciado:
"""Los condicionales "if...elif...else" en Python son estructuras de control de flujo  que  permiten
tomar decisiones en un programa. Se utilizan para ejecutar diferentes bloques  de  código  según  el
resultado de evaluar una o más condiciones.

El condicional "if" evalúa una condición; si esta es verdadera,  se  ejecuta  el  bloque  de  código
asociado. Si la condición es falsa, se evalúan las condiciones "elif" en orden  hasta  encontrar  la
primera condición  verdadera,  ejecutándose  el  bloque  de  código  asociado.  Si  ninguna  de  las
condiciones "elif" es verdadera, se ejecuta  el  bloque  de  código  asociado  al  "else"  (si  está
presente). Es importante que todos los bloques estén correctamente indentados para evitar errores de
sintaxis.

Además, es relevante tener en cuenta que las condiciones se evalúan en el orden en que aparecen. Una
vez que se cumple una condición, el programa ejecuta el código asociado y no evalúa  las  siguientes
condiciones. Esto puede influir en el comportamiento del programa si las condiciones no  están  bien
estructuradas.

Por lo tanto, el orden de los condicionales es crucial y no se puede alterar, ya que hacerlo  podría
cambiar la lógica del programa y producir resultados inesperados. El orden correcto es if -> elif ->
else, donde "elif" y "else" son opcionales. Además, "elif" y "else" no pueden existir  sin  un  "if"
previo, pero "else" puede acompañar a un "if" sin necesidad de usar "elif"."""

# Ejemplo_condicionales_if_elif_else.py

# Explicación:
"""Definimos una variable llamada "numero" y le asignamos el valor entero 156. Luego, utilizamos  el
condicional "if" para verificar si la variable "numero" es mayor que 0.  Para  ello,  escribimos  la
palabra clave "if" seguida de la condición, en este caso  entre  paréntesis,  y  terminada  con  dos
puntos (:). La condición se compone de la variable "numero", el operador mayor que (>) y el valor 0.

Si la condición se cumple (si el número es mayor que  0),  se  imprime  un  mensaje  en  la  consola
utilizando la función "print()", el cual corresponde al bloque de  código  asociado  al  condicional
"if" que colocamos justo debajo y con una indentación de cuatro espacios.

A continuación, utilizamos el condicional "elif" para verificar si la variable "numero" es menor que
0. Para ello, escribimos la palabra clave "elif"  seguida  de  la  condición,  en  este  caso  entre
paréntesis, y terminada con dos puntos (:). La condición se compone  de  la  variable  "numero",  el
operador menor que (<) y el valor 0.

Si la condición se cumple (si el número es menor que  0),  se  imprime  un  mensaje  en  la  consola
utilizando la función "print()", el cual corresponde al bloque de  código  asociado  al  condicional
"elif" que colocamos justo debajo y con una indentación de cuatro espacios.

Por último, utilizamos el condicional "else" para manejar el caso en que las condiciones de  "if"  y
"elif" no se cumplan. Para ello, escribimos la palabra clave "else" seguida de dos puntos (:).

Si las condiciones "if" y "elif" no se cumplen (si el número es igual a 0), se imprime un mensaje en
la consola utilizando la función "print()", el cual corresponde al  bloque  de  código  asociado  al
condicional "else" que colocamos justo debajo y con una indentación de cuatro espacios.

Después del bloque "if...elif...else", se imprime otro mensaje indicando el  fin  del  programa,  el
cual se imprimirá siempre, independientemente de si las condiciones se cumplen o  no,  ya  que  está
fuera del bloque "if...elif...else". En este caso, se imprimirá "El número es positivo"  ya  que  la
variable "numero" tiene un valor de 156, el cual es mayor que 0."""

# Código:
numero = 156

if (numero > 0):
    print("El número es positivo")
elif (numero < 0):
    print("El número es negativo")
else:
    print("El número es cero")

print("Fin del programa")

# Nota Muy Importante:
"""Cabe destacar que es posible incluir tantas condiciones "elif" como se desee, y que la  condición
"else" es opcional. Es fundamental estructurar las condiciones "if", "elif" y  "else"  en  el  orden
correcto para garantizar que el programa evalúe las condiciones de manera  adecuada  y  produzca  el
resultado esperado. 

Es posible asociar múltiples instrucciones a un  mismo  condicional,  siempre  y  cuando  todas  las
instrucciones estén correctamente indentadas. Esto se puede lograr utilizando  un  bloque  de  código
indentado debajo de la condición. Estas instrucciones se ejecutarán si  la  condición  se  cumple  y
pueden ser tan variadas como se necesite, incluyendo operaciones matemáticas, llamadas a  funciones,
entre otras.

Por último, es interesante saber que si no se cumple ninguna de las condiciones "if" o "elif", y  no
se incluye un bloque "else", el programa simplemente continuará su ejecución  sin  realizar  ninguna
acción adicional. Esto puede ser útil en ciertos casos donde no se requiere  una  acción  específica
para el caso en que ninguna condición se cumpla."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
