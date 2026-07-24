# Enunciado:
"""Escribe un programa que dé la bienvenida al usuario y le pida ingresar dos números enteros. Si el
usuario ingresa un valor no numérico o diferente de un entero (int), el  programa  debe  mostrar  un
mensaje de error específico y solicitar al usuario ingresar los números nuevamente.

Si el usuario intenta dividir entre cero, el programa debe mostrar un mensaje de error específico  y
solicitar al usuario ingresar los números nuevamente. Una vez que el  usuario  ingrese  dos  números
válidos, el programa debe realizar la división de los dos números.  Por  último,  el  programa  debe
mostrar el resultado de la división.

Usa un bucle "while True" acompañado de la estructura "try-except" y la instrucción "break" para que
el programa no se detenga abruptamente y siga solicitando los números hasta que se ingresen  valores
válidos. Los números deben ser convertidos a enteros (int) y  pueden  ser  cualquier  número  entero
positivo o negativo."""

# Ejercicio_bloque_try_except.py

# Explicación:
"""Utilizamos el bucle "while" para ejecutar un bloque de código mientras se cumpla  una  condición.
Para ello, escribimos la palabra clave "while", seguida de la condición entre paréntesis y terminada
con dos puntos (:). La condición, en este caso, es el valor booleano "True", lo que significa que el
bucle se ejecutará indefinidamente hasta que se encuentre una instrucción "break" dentro del  bloque
de código asociado al bucle. La instrucción "break" se  utiliza  para  salir  del  bucle  cuando  se
cumplen ciertas condiciones; en este caso, esas condiciones se darán cuando el usuario  ingrese  dos
números válidos y la división se realice sin errores.

Dentro del bucle "while", utilizamos la función "print()" para mostrar un mensaje de  bienvenida  en
la consola. Colocamos esta instrucción con una  indentación  de  cuatro  espacios  desde  el  margen
izquierdo para indicar que pertenece al bloque de código asociado al bucle "while" y debe ejecutarse
en cada iteración del bucle.

Además, también dentro del bucle "while", utilizamos un bloque "try-except"  para  manejar  posibles
errores al solicitar al usuario que ingrese dos números enteros (int) y dividirlos  entre  sí.  Para
ello, utilizamos la palabra clave "try", seguida de dos puntos (:), para iniciar el bloque de código
que intentaremos ejecutar. Colocamos la palabra clave "try" con una indentación de  cuatro  espacios
desde el margen izquierdo para indicar que pertenece al bloque de código asociado al bucle "while" y
debe ejecutarse en cada iteración del bucle.

Dentro del bloque "try", utilizamos la función "input()" para solicitar al usuario  que  ingrese  el
primer número entero (int), el cual será el "dividendo" y  será  dividido  entre  el  segundo  valor
ingresado. Para ello, definimos una variable llamada "opcion_usuario_1", escribimos la palabra clave
"input" seguida de paréntesis () y, dentro de estos, incluimos un mensaje o "prompt",  el  cual,  al
ejecutar el código, se mostrará en la consola indicando al usuario qué tipo de información se espera
que ingrese. De esta forma, lo que el usuario ingrese se guarda en  la  variable  "opcion_usuario_1"
como una cadena de texto (str) y podremos usarlo en el resto del código.

A continuación, utilizamos de nuevo la función "input()" para solicitar al usuario  que  ingrese  el
segundo número entero (int), el cual será el "divisor" del primer valor. Para  ello,  definimos  una
variable llamada "opcion_usuario_2", escribimos la palabra clave "input" seguida de paréntesis () y,
dentro de estos, incluimos un mensaje o "prompt", el cual, al ejecutar el código, se mostrará en  la
consola indicando al usuario qué tipo de información se espera que ingrese. De esta forma, lo que el
usuario ingrese se guarda en la variable  "opcion_usuario_2"  como  una  cadena  de  texto  (str)  y
podremos usarlo en el resto del código.

Luego, definimos una variable llamada "resultado", a la cual asignamos el resultado de la  operación
de  división  entre  los  dos  valores  ingresados   por   el   usuario.   Para   ello,   escribimos
int(opcion_usuario_1), el cual será el dividendo, seguido del operador aritmético (/) y del  divisor
"int(opcion_usuario_2)". Además, encerramos toda la operación entre paréntesis  ().  El  constructor
"int()" toma como argumento, en cada caso, las variables  "opcion_usuario_1"  y  "opcion_usuario_2",
las cuales contendrán el valor introducido por  el  usuario  convertido  a  entero  (int).  Esto  es
necesario porque la función "input()" devuelve una  cadena  de  texto  (str),  y  para  realizar  la
división necesitamos un número, en este caso, un número entero (int).

Además, utilizamos la función "print()" para mostrar el resultado de  la  división  en  la  consola,
acompañado de un mensaje en formato de "f-string" que da las gracias  al  usuario  por  utilizar  el
programa.

Para cerrar el bloque "try", utilizamos la  instrucción  "break",  asociada  a  dicho  bloque,  para
interrumpir el bucle cuando se complete con éxito la ejecución del bloque "try"; es decir, cuando no
se genere ninguna excepción. Esto evita que el bucle se ejecute indefinidamente una vez  que  se  ha
obtenido un resultado válido. Colocamos todo el contenido del bloque "try" con  una  indentación  de
cuatro espacios desde la palabra clave "try" para  indicar  que  pertenece  a  este  bloque  y  debe
ejecutarse en cada iteración del bucle, siempre que no se genere ninguna excepción.

Después del bloque "try", utilizamos dos bloques "except"  para  manejar  posibles  excepciones  que
puedan ocurrir durante la ejecución del código dentro del bloque "try".

En el primer bloque "except", capturamos la excepción "ValueError", que puede ocurrir si el  usuario
ingresa un valor no numérico, como letras o símbolos, o un valor  numérico  distinto  de  un  entero
(int). Esta excepción es una subclase de <class 'Exception'> y es una excepción específica para este
tipo de error. Para ello, escribimos la palabra clave "except" seguida del nombre de  la  excepción,
en este caso, "ValueError", seguido de la expresión  "as  e"  y  dos  puntos  (:).  De  esta  forma,
capturamos la excepción y la asignamos a la variable "e", la cual definimos en este momento, lo  que
nos permite acceder al mensaje de error asociado a la excepción. Colocamos el  bloque  "except"  con
una indentación de cuatro espacios desde el margen izquierdo para indicar que pertenece al bloque de
código asociado al bucle "while" y debe ejecutarse en cada iteración del bucle  cuando  se  generela
excepción "ValueError".

Si se genera esta excepción, se ejecuta el bloque de  código  asociado  a  este  "except",  el  cual
contiene una instrucción "print()" que muestra un mensaje de error en formato "f-string", acompañado
de la variable "e", la cual contendrá el error, indicando así al usuario que debe ingresar un  valor
numérico válido. Colocamos esta instrucción con una indentación de cuatro espacios desde la  palabra
clave "except" para indicar que pertenece a este bloque y debe  ejecutarse  solo  si  se  genera  la
excepción "ValueError".

Por último, en el segundo bloque "except", capturamos la excepción  "ZeroDivisionError",  que  puede
ocurrir si el usuario ingresa el valor "cero". Esta excepción es una subclase de <class 'Exception'>
y es una excepción específica para este error. Para  ello,  escribimos  la  palabra  clave  "except"
seguida del nombre de la excepción, en este caso, "ZeroDivisionError", seguida de la  expresión  "as
f" y dos puntos (:). De esta forma, capturamos la excepción y la asignamos a  la  variable  "f",  la
cual definimos en este momento, lo que nos permite  acceder  al  mensaje  de  error  asociado  a  la
excepción. Colocamos el bloque "except" con una indentación  de  cuatro  espacios  desde  el  margen
izquierdo para indicar que pertenece al bloque de código asociado al bucle "while" y debe ejecutarse
en cada iteración del bucle cuando se genere la excepción "ZeroDivisionError".

Si se genera esta excepción, se ejecuta el bloque de  código  asociado  a  este  "except",  el  cual
contiene una instrucción "print()" que muestra un mensaje de error en formato "f-string", acompañado
de la variable "f", la cual contendrá el error, indicando así al usuario que no es  posible  dividir
entre cero. Colocamos esta instrucción con una indentación de cuatro espacios desde la palabra clave
"except" para indicar que pertenece a este bloque y debe ejecutarse solo si se genera  la  excepción
"ZeroDivisionError"."""

# Código:
while (True):
    print("Bienvenido al programa de división de dos números enteros.")
    try:
        opcion_usuario_1 = input("Ingresa el primer número (dividendo). Debe ser un numero entero: ")
        opcion_usuario_2 = input("Ingresa el segundo número (divisor). Debe ser un numero entero: ")
        resultado = (int(opcion_usuario_1) / int(opcion_usuario_2))
        print(f"El resultado de la división es: {resultado}. Gracias por utilizar el programa.")
        break

    except ValueError as e:
        print(f"Error: {e}. Ingresa un valor numérico válido.")

    except ZeroDivisionError as f:
        print(f"Error: {f}. No es posible dividir entre cero.")

# Nota Importante:
"""La instrucción "break" se ejecutará únicamente si no ocurre ninguna excepción.  En  caso  de  que
ocurra una excepción, el programa mostrará un mensaje de error y solicitará al usuario  que  ingrese
los números nuevamente gracias al bucle "while True". Este bucle continuará ejecutándose  hasta  que
el usuario ingrese dos números válidos.

En este tipo de código, el flujo de ejecución puede tomar diferentes caminos dependiendo  de  si  se
generan o no excepciones. Si no se generan excepciones, el flujo seguirá el camino del bloque  "try"
y se ejecutará la instrucción "break" para  salir  del  bucle.  Por  el  contrario,  si  se  generan
excepciones, el flujo seguirá el camino del bloque "except" correspondiente, evitando que se ejecute
la instrucción "break". Esto hará que el bucle continúe  solicitando  al  usuario  que  ingrese  los
números nuevamente hasta que se rompa con la instrucción "break" al ingresar valores válidos.

Es importante destacar que la estructura "try-except" puede aplicarse de manera anidada;  es  decir,
dentro de un bloque "try" se puede incluir otro bloque "try-except". Además, encerrar todo el código
dentro de un bucle "while True" garantiza que el programa no se detenga al momento  de  ingresar  un
valor no numérico o al intentar dividir entre cero, sino que  vuelva  a  solicitar  al  usuario  que
ingrese los números nuevamente.

Por último, también es posible añadir tantos bloques "except" como se desee para manejar  diferentes
tipos de excepciones. Sin embargo, no es una buena práctica abusar  de  estructuras  anidadas  o  de
múltiples bloques "except", ya que esto puede dificultar la lectura y el mantenimiento  del  código.
Por otro lado, es recomendable utilizar mensajes de error claros y específicos para que  el  usuario
entienda qué tipo de error ha ocurrido y cómo puede solucionarlo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
