# Enunciado:
"""Escribe un programa que pida al usuario que adivine un número secreto entre 1 y 10. Si el usuario
no acierta, el programa debe indicarle que no ha acertado y volver a pedirle que adivine el número.

El programa terminará cuando el usuario acierte el número secreto. En ese  caso,  el  programa  debe
felicitar al usuario. Si el usuario introduce un valor no válido (fuera del rango 1-10), el programa
debe indicarle que el valor no es correcto y volver a pedirle que  adivine  el  número.  Utiliza  un
bucle "while" y los condicionales "if", "elif" y "else" para resolver el ejercicio.

El número secreto debe estar definido en el código y puede  ser  cualquier  número  entre  1  y  10.
Además, debes asegúrarte de que el usuario introduzca un número entero convirtiendo su  entrada  con
el constructor "int()" e indicándole cuál es el valor esperado."""

# Ejercicio_bucle_while_if_elif_else.py

# Explicación:
"""Definimos una variable llamada "numero_secreto" y le asignamos el valor entero 7.  Esta  variable
contiene el número que el usuario debe adivinar. Además, hacemos que el programa imprima un  mensaje
de bienvenida en la consola utilizando la función "print()".

Utilizamos la función "input()" para solicitar al usuario que introduzca su  suposición  del  número
secreto. Para ello, definimos una variable llamada "opcion_usuario", escribimos la función "input()"
seguida de paréntesis (), y dentro de estos incluimos un mensaje con la información  que  se  espera
que el usuario introduzca.

Como la función "input()" devuelve un valor de tipo cadena (str), utilizamos el constructor  "int()"
para convertir esa entrada en un número entero,  encerrando  la  función  "input()"  dentro  de  los
paréntesis del constructor "int()", que colocamos justo antes  de  la  función  "input()".  De  esta
forma, obtenemos un valor de tipo entero (int)  almacenado  en  la  variable  "opcion_usuario",  que
podremos utilizar en el bucle "while" y en el condicional "if".

Es necesario colocar este "input()" antes del bucle "while" para que el usuario pueda introducir  su
primera suposición antes de que comience el bucle. Además, la variable debe estar definida antes  de
usarla en la condición del bucle  "while"  para  evitar  errores  por  referencias  a  variables  no
definidas.

A continuación, utilizamos el bucle "while" para ejecutar un bloque de código mientras se cumpla una
condición. Escribimos la palabra clave "while", seguida de la condición entre paréntesis y terminada
con dos puntos (:). La condición, en este caso, es que el valor de  "numero_secreto"  sea  diferente
del valor de "opcion_usuario". Esta  condición  se  compone  de  la  variable  "numero_secreto",  el
operador de comparación (!=) y la variable "opcion_usuario". Si la condición se cumple, es decir, si
"numero_secreto" es diferente de "opcion_usuario", se ejecuta el bloque de código asociado al  bucle
"while" hasta que la condición deje de cumplirse.

Dentro del bucle "while", definimos una estructura condicional que utiliza el condicional "if"  para
evaluar si el número introducido por el usuario está dentro del rango válido (entre 1  y  10)  y  un
condicional "else" para manejar el caso en que el número introducido por el usuario  esté  fuera  de
ese rango. Ambas condiciones están dentro del bucle "while" y se evalúan en cada  iteración  siempre
que la condición del  bucle  se  cumpla,  es  decir,  mientras  "opcion_usuario"  sea  diferente  de
"numero_secreto".

En cada caso se imprime un mensaje en la consola utilizando la función "print()"  para  informar  al
usuario sobre el resultado de su suposición. Además, en los dos casos, "if" y "else", aplicamos  una
indentación de cuatro espacios desde el margen izquierdo para indicar que estos  bloques  de  código
pertenecen al bucle "while" y se evalúan en cada iteración del bucle.

De nuevo, utilizamos la función "input()" para solicitar al usuario que introduzca su suposición del
número secreto del mismo modo que al principio del programa. Esta instrucción se ejecutará  en  cada
iteración del bucle "while", independientemente de cuál de las dos condiciones, "if"  o  "else",  se
cumpla, hasta que la condición principal del "while" deje  de  cumplirse,  lo  que  permite  que  el
usuario introduzca un nuevo  valor  en  cada  intento.  Colocamos  esta  instrucción  con  la  misma
indentación que las condiciones "if" y "else" para indicar que pertenece al bucle "while".

Por último, después del bloque  condicional  "if...else"  y  de  la  función  "input()",  usamos  el
condicional "else" asociado al bucle "while". El bloque de código asociado  a  este  condicional  se
ejecuta  una  vez  que  la  condición  del  bucle  "while"  se  vuelve  falsa,  es   decir,   cuando
"opcion_usuario" es igual a "numero_secreto". En este caso, se imprime otro mensaje indicando que el
número introducido por el usuario coincide con el  número  secreto  y  felicitando  al  usuario  por
haberlo adivinado. Colocamos el condicional "else"  alineado  con  la  palabra  clave  "while"  para
indicar que debe ejecutarse una vez que la condición del bucle  ya  no  se  cumpla,  y  no  en  cada
iteración del bucle."""

# Código:
numero_secreto = 7

print("¡Bienvenido al juego de adivinar el número secreto!")

opcion_usuario = int(input("Adivina el número secreto (entre 1 y 10): "))

while (opcion_usuario != numero_secreto):
    if (1 <= opcion_usuario <= 10):
        print("No has acertado. Inténtalo de nuevo.")
    else:
        print("Número no válido. Debes introducir un número entre 1 y 10.")
    opcion_usuario = int(input("Adivina el número secreto (entre 1 y 10): "))
else:
    print("¡Felicidades! Has adivinado el número secreto.")

# Nota Muy Importante:
"""En este ejemplo, el bucle  "while"  se  ejecuta  siempre  que  la  condición  "opcion_usuario  !=
numero_secreto" sea verdadera. Dentro del bucle, se evalúan las condiciones del  bloque  condicional
"if" y "else".

Estas dos condiciones, "if" y "else", están anidadas dentro del bucle "while", lo que significa  que
se evalúan en cada iteración del bucle mientras la condición de este se cumpla, es  decir,  mientras
"opcion_usuario" sea diferente de "numero_secreto". Además, independientemente de cuál  de  las  dos
condiciones se cumpla, en cada iteración se ejecuta el "input()" asociado al bucle "while" para  que
el usuario pueda introducir un nuevo valor en cada intento.

La condición "if" se ejecuta cuando el número introducido por el usuario está dentro del rango 1-10,
pero no coincide con el número secreto. Con esta condición, (1 <= opcion_usuario <= 10), conseguimos
verificar que el valor introducido por el usuario está dentro del rango  válido,  ya  que  debe  ser
mayor o igual que 1 y menor o igual que 10. En este caso, el programa informa al usuario de  que  no
ha acertado y le pide que lo intente de nuevo mediante la función "input()". En caso  contrario,  es
decir, cuando el número introducido está  fuera  del  rango  1-10,  se  ejecuta  el  bloque  "else",
indicando que el valor no es válido y solicitando un nuevo intento mediante la función "input()".

Cuando la condición del bucle "while"  deja  de  cumplirse,  es  decir,  cuando  "opcion_usuario  ==
numero_secreto", se ejecuta el bloque "else" asociado al bucle, felicitando  al  usuario  por  haber
adivinado el número secreto. Este enfoque garantiza  que  el  programa  maneje  tanto  los  intentos
incorrectos como las entradas no válidas de manera adecuada.

Por último, en este programa utilizamos dos llamadas a la función "input()"  para  permitir  que  el
usuario introduzca su suposición del número secreto en dos momentos diferentes: una antes de  entrar
en el bucle "while" y otra dentro del bucle para cada intento posterior. De esta manera, el programa
puede evaluar la suposición inicial del usuario y luego continuar  solicitando  nuevas  suposiciones
hasta que el usuario adivine el número secreto o introduzca un valor no válido."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
