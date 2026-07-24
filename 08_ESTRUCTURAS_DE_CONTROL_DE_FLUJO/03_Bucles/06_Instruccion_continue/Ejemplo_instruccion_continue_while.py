# Enunciado:
""""La instrucción "continue" en Python permite omitir la ejecución del resto del código  dentro  de
un bucle para la iteración actual y pasar directamente a la siguiente iteración. Esto es útil cuando
se desea evitar que ciertas condiciones específicas ejecuten el bloque de código restante del bucle.

Cuando la condición asociada a la instrucción "continue" se  evalúa  como  verdadera,  el  flujo  de
ejecución salta inmediatamente al inicio del bucle para la siguiente iteración, ignorando  cualquier
código que se encuentre después de la instrucción "continue" en esa iteración.

"Continue" en español significa "continuar", y su función principal es proporcionar un  control  más
preciso sobre el flujo de ejecución dentro de un bucle.

Además, la instrucción "continue" puede utilizarse tanto en bucles "for" como en bucles "while".  En
el caso de bucles anidados, "continue" solo afecta al bucle en el que se encuentra, sin  impactar  a
los bucles externos. Esto es útil para manejar estructuras de control complejas de manera eficiente.

El uso de "continue" es común en situaciones en las que se necesita omitir ciertas iteraciones de un
bucle basándose en una condición específica. Por ejemplo, se puede utilizar para saltar elementos no
deseados en una lista o para evitar ejecutar código innecesario en ciertas iteraciones.

Por último, es importante tener en cuenta que el uso de "continue" debe considerarse cuidadosamente,
ya que puede hacer que el flujo de ejecución sea menos predecible si no se utiliza de manera clara y
justificada."""

# Ejemplo_instruccion_continue_while.py

# Explicación:
"""Definimos una variable llamada "contenedor" y le asignamos el valor inicial de 0.  Esta  variable
controla el número de iteraciones del bucle "while" y almacena el valor actual  de  "contenedor"  en
cada iteración.

Utilizamos el bucle "while" para ejecutar un bloque de código mientras se cumpla una condición. Para
ello, escribimos la palabra clave "while", seguida de la condición entre paréntesis y terminada  con
dos puntos (:). La condición en este caso es que el valor de "contenedor" sea menor o  igual  a  10.
Esta condición se compone de: la variable "contenedor", el operador de comparación (<=) y  el  valor
entero 10. Si la condición se cumple (si "contenedor" es menor o igual a 10), se ejecuta  el  bloque
de código asociado al bucle "while".

A continuación, incrementamos el valor de "contenedor" en 1 hasta que la condición del bucle deje de
cumplirse (contenedor > 10). Para ello, utilizamos la expresión de incremento "contenedor += 1", que
es una forma concisa de escribir "contenedor = contenedor + 1". De esta forma, sumamos  1  al  valor
actual de la variable en cada iteración y asignamos el resultado a la misma variable.  Esto  asegura
que la condición del bucle,  eventualmente,  se  vuelva  falsa,  permitiendo  así  que  la  variable
"contenedor" se actualice en cada iteración.

Dentro del bucle "while", utilizamos el  condicional  "if"  para  evaluar  si  el  valor  actual  de
"contenedor" es un número par (contenedor  %  2  ==  0)  y,  si  es  así,  ejecutar  la  instrucción
"continue". Para ello, escribimos la palabra clave "if", seguida de la condición entre paréntesis  y
terminada con dos puntos (:). La condición se compone  de  la  variable  "contenedor",  el  operador
módulo (%), el número entero 2, el operador de comparación (==) y el valor entero  0.  Colocamos  el
condicional "if" con una indentación de cuatro espacios desde el  margen  izquierdo,  indicando  que
pertenece al bucle "while" y debe evaluarse en cada iteración del bucle.

Luego, utilizamos la instrucción "continue" asociada al  condicional  "if"  para  continuar  con  la
siguiente iteración del bucle sin ejecutar el resto del código dentro del bucle en esa iteración, si
la condición se cumple; es decir, cuando el valor de "contenedor" sea un número  par.  Colocamos  la
instrucción "continue" justo debajo del condicional "if" y con una indentación  de  cuatro  espacios
desde el propio condicional "if", indicando que esta instrucción  debe  ejecutarse  solo  cuando  la
condición del "if" se cumpla y no en cada iteración del bucle.

De esta forma, si el elemento iterado es un número par, se ejecuta la  instrucción  "continue",  que
omite el resto del código dentro del bucle para esa iteración y pasa  directamente  a  la  siguiente
iteración del bucle.

Además, dentro del bucle "while", utilizamos la función "print()" para mostrar el valor actual de la
variable "contenedor" en cada iteración, acompañado de un mensaje descriptivo en formato "f-string".
Colocamos esta instrucción justo debajo de la instrucción "continue", con la misma  indentación  que
el condicional "if", indicando que está asociada al bucle "while" y debe ejecutarse siempre  que  la
condición del bucle se cumpla. En este caso, realizamos este paso después de incrementar la variable
para asegurarnos de que solo se impriman los números impares y así obtener el resultado esperado.

Por último, después del bloque de código asociado al bucle "while", utilizamos la función  "print()"
para imprimir un mensaje indicando que el bucle ha finalizado. Este mensaje se ejecutará una vez que
el bucle finalice, es decir, cuando la condición del bucle "while" deje de cumplirse.  Este  mensaje
se coloca sin indentación, es decir, al mismo nivel que la palabra clave "while"."""

# Código:
contenedor = 0

while (contenedor <= 10):
    contenedor += 1
    if (contenedor % 2 == 0):
        continue
    print(f"Este elemento iterado es un número impar: {contenedor}")

print("El bucle ha finalizado correctamente, imprimiendo solo los números impares.")

# Nota Muy Importante:
"""Es importante realizar el  incremento  de  la  variable  "contenedor"  antes  de  la  instrucción
"continue" para evitar que el bucle se detenga prematuramente.  Si  "contenedor"  no  se  incrementa
antes de "continue", el flujo de ejecución volverá al inicio del bucle sin modificar su valor.  Esto
ocurre porque el valor inicial de "contenedor" es 0  (un  número  par),  y  la  condición  del  "if"
(contenedor % 2 == 0) se evalúa como verdadera en la primera iteración. Como resultado,  se  ejecuta
la instrucción "continue" y el incremento nunca se realiza, lo que provoca que el  bucle  no  avance
más allá de la primera iteración.

Al colocar el incremento antes de  la  instrucción  "continue",  garantizamos  que  "contenedor"  se
actualice en cada iteración, permitiendo que  eventualmente  alcance  un  valor  impar  y  el  bucle
continúe ejecutándose correctamente. Esto asegura que el flujo de ejecución sea predecible  y  evita
problemas en el comportamiento del programa.

Por último, en este ejemplo colocamos la instrucción  "print()"  después  del  incremento  y  de  la
instrucción "continue" para asegurarnos de que solo se impriman los números impares y así obtener el
resultado esperado. Sin embargo, en el  código  anterior  (instrucción  "break"  asociada  al  bucle
"while"), este paso se realizó antes del incremento y después de la instrucción "break".  Por  ello,
es importante considerar el orden de las instrucciones dentro del bucle y  del  flujo  de  ejecución
para obtener el comportamiento deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
