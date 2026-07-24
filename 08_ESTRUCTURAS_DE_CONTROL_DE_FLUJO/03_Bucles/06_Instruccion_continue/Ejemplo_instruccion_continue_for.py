# Enunciado:
""""La instrucción "continue" en Python permite omitir la ejecución del resto del código  dentro  de
un bucle para la iteración actual y pasar directamente a la siguiente iteración. Esto es útil cuando
se desea evitar que ciertas condiciones específicas ejecuten el bloque  de  código  restante  en  el
bucle.

Cuando la condición asociada a la instrucción "continue" se  evalúa  como  verdadera,  el  flujo  de
ejecución salta inmediatamente al inicio del bucle para la siguiente iteración, ignorando  cualquier
código que se encuentre después de la instrucción "continue" en esa iteración.

"Continue" en español significa "continuar", y su función principal es proporcionar un  control  más
preciso sobre el flujo de ejecución dentro de un bucle.

Además, la instrucción "continue" puede ser utilizada tanto en bucles "for" como en bucles  "while".
En el caso de bucles anidados, "continue" solo afecta al bucle en el que se encuentra, sin  impactar
a los bucles externos. Esto es  útil  para  manejar  estructuras  de  control  complejas  de  manera
eficiente.

El uso de "continue" es común en situaciones donde se necesita  omitir  ciertas  iteraciones  de  un
bucle basándose en una condición específica. Por ejemplo, se puede utilizar para saltar elementos no
deseados en una lista o para evitar ejecutar código innecesario en ciertas iteraciones.

Por último,  es  importante  tener  en  cuenta  que  el  uso  de  "continue"  debe  ser  considerado
cuidadosamente, ya que puede hacer que el flujo de ejecución sea menos predecible si no  se  utiliza
de manera clara y justificada."""

# Ejemplo_instruccion_continue_for.py

# Explicación:
"""Definimos una variable llamada "lista_numeros" y le asignamos una lista de números del  0  al  9.
Luego, utilizamos un bucle "for" para iterar sobre cada elemento de la lista. Para ello,  escribimos
la palabra clave "for", seguida de la variable "i", que representa cada elemento de la  secuencia  y
la cual definimos en este momento, seguida del operador "in" para  indicar  dónde  queremos  que  se
realice la iteración y el nombre de la  secuencia  sobre  la  que  queremos  iterar,  en  este  caso
"lista_numeros". A continuación, escribimos dos puntos (:) para indicar el final de la  expresión  y
el inicio del bloque de código asociado al bucle "for".

Dentro del bucle "for", utilizamos el condicional "if" para evaluar si el elemento actual  "i"  está
en el subconjunto (5, 6, 7) y, si es así,  continuar  con  la  siguiente  iteración  del  bucle  sin
ejecutar el resto del código dentro del bucle para esa iteración. Para ello, escribimos  la  palabra
clave "if", seguida de la condición entre paréntesis y terminada con dos puntos (:). La condición se
compone de la variable "i", el operador de pertenencia "in" y el subconjunto (5, 6, 7). Colocamos el
condicional "if" con una indentación de cuatro espacios desde el  margen  izquierdo,  indicando  que
pertenece al bucle "for" y debe evaluarse en cada iteración del bucle.

A continuación, utilizamos la instrucción "continue" asociada al condicional "if" para continuar con
la siguiente iteración del bucle sin ejecutar  el  resto  del  código  dentro  del  bucle  para  esa
iteración si la condición se cumple, es decir,  cuando  "i"  esté  en  el  subconjunto  (5,  6,  7).
Colocamos la instrucción "continue" justo debajo del condicional  "if"  y  con  una  indentación  de
cuatro espacios desde el propio condicional "if", indicando que esta instrucción  se  debe  ejecutar
solo cuando la condición "if" se cumpla y no en cada iteración del bucle.

De esta forma, si el elemento iterado está en el subconjunto (5, 6, 7), se  ejecuta  la  instrucción
"continue", que omite el resto del código dentro del bucle para esa iteración y pasa directamente  a
la siguiente iteración del bucle.

Por último, utilizamos  la  función  "print()"  para  imprimir  un  mensaje  en  formato  "f-string"
acompañado del valor actual de "i" en cada iteración del bucle. Colocamos esta instrucción  con  una
indentación de cuatro espacios desde el margen izquierdo, indicando que pertenece al bucle  "for"  y
debe ejecutarse en cada iteración del bucle excepto cuando la condición "if" se  cumpla,  se  omitan
las iteraciones correspondientes y se pase a la siguiente iteración del  bucle  con  la  instrucción
"continue" para seguir iterando sobre el resto de elementos del conjunto "lista_numeros".

El bucle comienza a iterar sobre cada elemento  de  la  lista.  En  cada  iteración,  se  evalúa  la
condición del condicional "if". Si esta condición se cumple (i está en  5,  6,  7),  se  ejecuta  la
instrucción "continue", omitiendo el resto del código que cumpla esa condición dentro del bucle para
esa iteración y pasando directamente a la siguiente iteración del bucle.

Cuando la condición deje de cumplirse (i no está en 5, 6, 7), el bucle sigue iterando normalmente  y
se continúa ejecutando la instrucción "print()" e imprimiendo el valor actual de "i"  hasta  que  el
conjunto se acabe. Como resultado, se imprimen los números del 0 al 4, además del 8 y  9,  pero  los
números 5, 6 y 7 no se imprimen, ya que la instrucción "continue" se ejecuta antes de la  llamada  a
la función "print()"."""

# Codigo:
lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in lista_numeros:
    if (i in (5, 6, 7)):
        continue
    print(f"Este es el valor de i en este momento: {i}")

print("El bucle se completó correctamente omitiendo los valores 5, 6 y 7.")

# Nota Importante:
"""En este ejemplo, se utiliza el operador de pertenencia "in" para verificar si  el  valor  de  "i"
está en el subconjunto (5, 6, 7). De  esta  forma  vemos  cómo  se  puede  utilizar  la  instrucción
"continue" para omitir múltiples valores específicos dentro de un bucle "for".

Además, cuando la instrucción "continue" se ejecuta, el flujo de ejecución salta directamente  a  la
siguiente iteración del bucle, ignorando cualquier código que se encuentre después de la instrucción
"continue" en esa iteración.

Cuando decimos que salta al principio del bucle, nos referimos a que el flujo de ejecución  continúa
desde el siguiente elemento del conjunto iterable  "lista_numeros"  que  no  está  contenido  en  el
subconjunto (5, 6, 7).

Es importante tener en cuenta que el uso excesivo de la instrucción "continue" puede  dificultar  la
legibilidad del código, especialmente en bucles  complejos  o  anidados.  Por  ello,  se  recomienda
utilizarla únicamente cuando sea estrictamente necesaria y cuando mejore la claridad  del  flujo  de
control.

Una buena práctica es asegurarse de que las condiciones asociadas a la instrucción  "continue"  sean
claras y fáciles de entender. Esto ayuda a evitar errores lógicos y facilita  el  mantenimiento  del
código. Además, es preferible documentar adecuadamente el propósito de la instrucción "continue"  en
el contexto del bucle para que otros desarrolladores puedan comprender su uso.

También se debe tener precaución al utilizar  "continue"  en  bucles  que  dependen  de  condiciones
específicas para finalizar, como los bucles "while".  Un  uso  incorrecto  podría  llevar  a  bucles
infinitos si no se garantiza que la condición de salida se evalúe correctamente en cada iteración.

Por último, es recomendable evitar el uso de "continue" en situaciones donde el mismo  resultado  se
pueda lograr con una estructura de control más simple o con una  lógica  alternativa,  ya  que  esto
puede hacer que el código sea más limpio y fácil de seguir."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────