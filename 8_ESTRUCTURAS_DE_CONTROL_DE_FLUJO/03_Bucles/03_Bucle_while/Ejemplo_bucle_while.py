# Enunciado:
"""El bucle "while" es una estructura de control de flujo en Python que ejecuta un bloque de  código
mientras una condición sea verdadera.

El bucle evalúa la condición antes de cada iteración y, si esta es verdadera, ejecuta el  bloque  de
código asociado, repitiendo el proceso hasta que la condición se vuelva falsa. Si  la  condición  es
falsa desde el inicio, el bucle no se ejecutará ni una sola vez. Esto lo diferencia de otros bucles,
como el "for", que itera sobre una secuencia predefinida.

Es muy importante asegurarse de que la condición del bucle "while" eventualmente se vuelva falsa. De
lo contrario, se producirá un bucle infinito, lo que puede  hacer  que  el  programa  se  bloquee  o
consuma recursos innecesarios. Para  evitar  esto,  es  preciso  asegurarse  de  que  las  variables
utilizadas en la condición cambien dentro del bloque  del  bucle,  así  como  usar  herramientas  de
depuración para verificar el flujo del programa e implementar  condiciones  de  salida  adicionales,
como el uso de la instrucción "break" en casos específicos.

Por último, el bucle "while" es especialmente útil cuando no se conoce de antemano el número  exacto
de iteraciones necesarias, como en casos en los que se espera una entrada del usuario o  se  realiza
una operación hasta que se cumpla una condición  dinámica.  Además,  también  puede  emplearse  para
realizar tareas de monitoreo continuo, como verificar el estado de un  sistemao  esperar  un  evento
específico antes de continuar con la ejecución del programa."""

# Ejemplo_bucle_while.py

# Explicación:
"""Definimos una variable llamada "contenedor" y le asignamos el valor inicial de 0.  Esta  variable
controla el número de iteraciones del bucle "while" y almacena el valor actual  de  "contenedor"  en
cada iteración.

A continuación, utilizamos el bucle "while" para ejecutar un bloque de código mientras se cumpla una
condición. Para ello, escribimos la palabra clave "while", seguida de la condición entre  paréntesis
y terminada con dos puntos (:). La condición, en este caso, es que  el  valor  de  "contenedor"  sea
menor o igual que 10.

Esta condición se compone de la variable "contenedor", el operador de comparación (<=)  y  el  valor
entero 10. Si la condición se cumple (si "contenedor" es menor o igual a 10), se ejecuta  el  bloque
de código asociado al bucle "while".

Dentro del bucle "while", utilizamos la función "print()"  para  mostrar  el  estado  actual  de  la
variable "contenedor" en cada iteración, acompañado de un mensaje descriptivo en formato "f-string".
Colocamos esta instrucción justo debajo de la expresión  "while",  con  una  indentación  de  cuatro
espacios desde el margen izquierdo. Es  importante  realizar  este  paso  antes  de  incrementar  la
variable, para que su valor actual se imprima antes de ser incrementado en cada iteración del  bucle
y el resultado sea el esperado.

Luego, incrementamos el valor de "contenedor" en  1  hasta  que  la  condición  del  bucle  deje  de
cumplirse ("contenedor > 10"). Para ello, utilizamos la expresión de incremento "contenedor  +=  1",
que es una forma concisa de escribir "contenedor = contenedor + 1". De  esta  forma,  sumamos  1  al
valor actual de la variable en cada iteración y asignamos el resultado a la misma variable.

Esto asegura que la condición del bucle  eventualmente  se  vuelva  falsa,  evitando  así  un  bucle
infinito. Las instrucciones "print()" y "contenedor += 1" forman el bloque  de  código  asociado  al
bucle "while", y ambas tendrán la misma indentación, cuatro espacios desde el margen izquierdo.

Por último, después del bloque de código asociado al bucle "while", imprimimos un mensaje  indicando
que el bucle ha terminado. Este mensaje se ejecutará una vez que la condición del  bucle  ya  no  se
cumpla (cuando "contenedor" sea mayor a 10) y se coloca sin indentación, es decir,  al  mismo  nivel
que la palabra clave "while"."""

# Codigo:
contenedor = 0         

while (contenedor <= 10):
    print(f"Este es el estado actual del contenedor: {contenedor}")
    contenedor += 1

print("Bucle terminado")    

# Nota Importante:
"""El orden de las instrucciones dentro del bucle es  crucial.  Si  incrementamos  el  valor  de  la
variable antes de imprimirlo, el bucle mostrará los números del 1 al  10,  ya  que  la  variable  se
incrementa antes de mostrarse, lo que puede no ser el resultado esperado. Además, en este  caso,  no
es necesario usar la instrucción "break", ya que el bucle  se  detendrá  automáticamente  cuando  la
condición se vuelva falsa (cuando el valor de "contenedor" sea mayor que 10). Sin embargo,  hay  que
ser cuidadoso al ejecutar este código con una condición que nunca  deje  de  cumplirse,  ya  que  el
código dentro del bloque se ejecutará para siempre.

Se recomienda no modificar variables externas al bucle dentro de este, ya que esto puede  dificultar
la depuración. Usar comentarios para explicar la lógica del bucle,  especialmente  si  es  compleja,
puede ser de gran ayuda. También es aconsejable establecer un  límite  máximo  de  iteraciones  para
evitar bucles infinitos y utilizar herramientas de depuración para analizar  el  comportamiento  del
bucle en tiempo de ejecución.

En cuanto a las condiciones asociadas al bucle,  es  recomendable  utilizar  condiciones  simples  y
directas quesean fáciles de  evaluar  y  evitar  condiciones  complejas  que  puedan  dificultar  la
comprensión del flujo del programa. Aunque es posible  usar  múltiples  condiciones  combinadas  con
operadores lógicos "and", "or" y "not", es  preferible  mantener  la  simplicidad  siempre  que  sea
posible.

Por último, es posible utilizar diferentes tipos de datos en  las  condiciones  asociadas  al  bucle
"while", como números, cadenas de texto o booleanos. En estos casos, los tipos de  datos  deben  ser
compatibles para evitar errores de ejecución."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
