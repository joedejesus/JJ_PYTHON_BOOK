# Enunciado:
"""El bucle "while" en Python permite ejecutar un bloque de código repetidamente mientras se  cumpla
una condición específica. Cuando se combina con las estructuras condicionales "if", "elif" y "else",
toma decisiones en cada iteración, permitiendo ejecutar  diferentes  bloques  de  código  según  las
condiciones definidas, hasta que la condición deje de cumplirse.

Esta combinación es especialmente útil para resolver  problemas  en  los  que  se  requiere  evaluar
múltiples condiciones en cada iteración o realizar operaciones específicas según el estado actual de
las variables, como validar datos  de  entrada,  procesar  elementos  de  una  lista  o  implementar
algoritmos que dependan de condiciones dinámicas.

El condicional "else" asociado al bucle "while" es una  característica  particular  que  se  ejecuta
cuando la condición del bucle deja de cumplirse de manera natural, sin interrupciones,  como  en  el
caso del uso de la instrucción "break". Esto permite manejar el final del bucle de forma  explícita,
lo que puede ser útil para realizar tareas de limpieza, notificaciones  o  cualquier  operación  que
deba ejecutarse al finalizar el bucle.

Es importante tener en cuenta que, cuando se utilizan los condicionales "elif" y "else"  dentro  del
bucle, debe haber un "if" previo, ya que estas estructuras están diseñadas para evaluar  condiciones
adicionales o alternativas. Sin embargo, es posible utilizar  un  condicional  "else"  sin  un  "if"
dentro del bucle "while". Este "else" actúa como una especie de  "finalizador"  del  bucle,  que  se
ejecuta cuando la condición deja de cumplirse.

El bucle "while", en combinación con los condicionales "if", "elif" y "else", también  resulta  útil
para implementar lógica de control en programas interactivos, como menús, validaciones de usuario  o
simulaciones. Su flexibilidad lo convierte en una herramienta poderosa para resolver  problemas  que
requieran iteraciones controladas por condiciones específicas.

Por último, es importante escribir código claro y mantener una buena indentación para  facilitar  la
lectura y su comprensión. Esto es especialmente relevante cuando se combinan bucles y condicionales,
ya que un código mal estructurado puede ser difícil de entender y mantener."""

# Ejemplo_bucle_while_if_elif_else.py

# Explicación:
"""Definimos una variable llamada "numero" y le asignamos el  valor  inicial  de  0.  Esta  variable
controla el número de iteraciones del bucle "while" y contiene el valor actual de "numero"  en  cada
iteración.

Utilizamos el bucle "while" para ejecutar un bloque de código  mientras  se  cumpla  una  condición.
Escribimos la palabra clave "while", seguida de la condición entre paréntesis y  terminada  con  dos
puntos (:). La condición, en este caso, es que el valor de "numero" sea menor o igual que  10.  Esta
condición se compone de la variable "numero", el operador de comparación (<=) y el valor entero  10.
Si la condición se cumple (si "numero" es menor o igual que 10), se  ejecuta  el  bloque  de  código
asociado al bucle "while" hasta que la condición deje de cumplirse.

Dentro del bucle "while", definimos una estructura condicional que utiliza los condicionales "if"  y
"elif" para verificar si el número es par o impar, a medida que la variable "numero" cambia su valor
dinámicamente hasta que la condición deja de cumplirse, y un condicional "else" para manejar el caso
en que el número sea mayor que 10.  Este  actúa  como  un  "finalizador"  del  bucle  "while".  Este
condicional se ejecuta cuando la condición del bucle deja de cumplirse de manera natural y sirve, en
este caso, para notificar que la variable "numero" ha superado el valor de 10 y que la condición  ya
no es verdadera.

Comprobamos si "numero" es par. Escribimos la palabra clave  "if"  seguida  de  la  condición  entre
paréntesis y terminada con dos puntos (:). La condición se  compone  de  la  variable  "numero",  el
operador módulo (%) y el valor entero 2. Si la condición se cumple (si "numero" es par), se  imprime
un mensaje en formato "f-string" en la consola utilizando la función "print()", el cual  corresponde
al bloque de código asociado al condicional "if", que colocamos justo debajo y con  una  indentación
de cuatro espacios desde el propio condicional "if".

Comprobamos si "numero" es impar. Escribimos la palabra clave "elif" seguida de la  condición  entre
paréntesis y terminada con dos puntos (:). La condición se  compone  de  la  variable  "numero",  el
operador módulo (%) y el valor entero 2. Si la condición  se  cumple  (si  "numero"  es  impar),  se
imprime un mensaje en formato "f-string" en la consola utilizando  la  función  "print()",  el  cual
corresponde al bloque de código asociado al condicional "elif", que colocamos justo debajo y con una
indentación de cuatro espacios desde el propio condicional "elif".

Para los dos casos, "if" y "elif", aplicamos una indentación de  cuatro  espacios  desde  el  margen
izquierdo para indicar que estos bloques de código pertenecen al bucle "while" y se evalúan en  cada
iteración del bucle.

A continuación, incrementamos el valor de "numero" en 1 hasta que la condición  del  bucle  deje  de
cumplirse ("numero > 10"). Utilizamos la expresión de incremento "numero += 1",  que  es  una  forma
concisa de escribir "numero = numero + 1". De esta forma, sumamos 1 al valor actual de  la  variable
en cada iteración y asignamos el resultado a la misma variable.

Este paso debe realizarse después del bloque condicional "if...elif" y con la misma indentación  que
estos bloques, es decir, con cuatro  espacios  desde  el  margen  izquierdo.  Esto  asegura  que  la
expresión de incremento se ejecute en cada iteración del bucle "while", permitiendo que la  variable
"numero" cambie su valor dinámicamente hasta que la condición deje de cumplirse.

Después del bloque condicional "if...elif" y de la expresión de incremento "numero += 1", usamos  de
nuevo el condicional "else" asociado  al  bucle  "while".  El  bloque  de  código  asociado  a  este
condicional se ejecuta una vez que la condición del bucle "while" se vuelve falsa. En este caso,  se
imprime otro mensaje en formato "f-string" indicando que el número es mayor que 10, el cual  muestra
el valor de "numero" una vez que la condición del bucle ya no se cumple.  Colocamos  el  condicional
"else" alineado con la palabra clave "while" para  indicar  que  debe  ejecutarse  una  vez  que  la
condición del bucle ya no se cumpla, y no en cada iteración del bucle.

Por último, después del bloque de código asociado al bucle "while", se imprime un mensaje  indicando
que el bucle ha terminado. Este mensaje se imprimirá una vez que la condición del  bucle  ya  no  se
cumpla (cuando "numero" sea mayor que 10) y se coloca sin indentación, es decir, al mismo nivel  que
la palabra clave "while"."""

# Código:
numero = 0

while (numero <= 10):
    if (numero % 2 == 0):
        print(f"El número {numero} es par")
    elif (numero % 2 != 0):
        print(f"El número {numero} es impar")
    numero += 1
else:
    print(f"El número {numero} es mayor que 10")

print("Bucle terminado")

# Nota Importante:
"""Para utilizar el bucle "while" de manera efectiva y evitar  problemas,  es  importante  tener  en
cuenta varias recomendaciones. Primero, hay que asegurarse de que la  condición  asociada  al  bucle
"while" eventualmente se vuelva falsa. Esto se logra verificando que las variables  involucradas  en
la condición cambien adecuadamente dentro del bucle, evitando así bucles infinitos.

Además, es recomendable mantener el código dentro del bucle lo más simple  y  legible  posible  para
facilitar su comprensión y mantenimiento. Si el  código  se  vuelve  complejo,  se  debe  considerar
dividirlo en funciones más pequeñas. También es importante evitar el uso excesivo  de  condicionales
anidados, ya que pueden dificultar la lectura del código. En su lugar, se debe tratar de simplificar
la lógica, estructurando el flujo de manera clara y utilizando funciones cuando sea necesario.

El uso de las instrucciones "break" y "continue" debe ser cuidadoso, ya que un uso inadecuado  puede
hacer que el flujo del programa sea difícil de seguir.  Asimismo,  es  preciso  considerar  cómo  se
quiere que el bucle y las condiciones interactúen entre sí, ya que el orden en que  se  colocan  las
estructuras de control es crucial para garantizar que el programa funcione como se espera. El uso de
estas instrucciones se abordará en las siguientes secciones.

Es importante tener en cuenta que, en este ejemplo, lo que tenemos es una estructura "while...else",
donde el "else" se ejecuta cuando la condición del "while" deja  de  cumplirse  de  manera  natural.
Dentro del bloque del "while" tenemos una estructura "if...elif" para evaluar diferentes condiciones
en cada iteración del bucle, siempre que la condición del "while" sea verdadera.

Por último, siempre es una buena práctica probar y depurar el código para garantizar que el bucle  y
las condiciones funcionen correctamente en todos los casos  posibles.  De  esta  forma,  los  bucles
"while" serán más robustos, legibles y fáciles de mantener."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
