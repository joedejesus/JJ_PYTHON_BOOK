# Enunciado:
"""Define dos variables y asígnales respectivamente una  lista  con  números  diferentes  entre  sí.
Escribe un programa que verifique si un número de tu elección está  presente  en  cada  una  de  las
listas e imprima un mensaje adecuado para cada  caso.  El  número  a  verificar  puede  estar  o  no
presente.

Por último, el programa debe imprimir un mensaje que diga "Fin de la verificación  del  elemento  en
las listas", independientemente de las condiciones. Además, los bloques  deben  estar  correctamente
indentados."""

# Ejercicio_condicionales_if_elif_else.py

# Explicación:
"""Definimos dos variables llamadas "lista_1" y "lista_2" y les asignamos respectivamente una  lista
con números diferentes entre sí. En este caso, el número elegido será el 4 para  verificar  si  está
presente en alguna de las listas.

En primer lugar, utilizamos el condicional "if" para verificar si el número 4 está  presente  en  la
"lista_1". Para ello, escribimos la palabra clave "if" seguida de la condición  entre  paréntesis  y
terminada con dos puntos (:). La condición se compone del valor 4, el operador de pertenencia "in" y
la variable "lista_1".

Si la condición se cumple (si el número 4 está presente en la lista_1), se imprime un mensaje en  la
consola utilizando la función "print()", el  cual  corresponde  al  bloque  de  código  asociado  al
condicional "if" que colocamos justo debajo y con una indentación de cuatro espacios.

A continuación, utilizamos el condicional "elif" para verificar si el número 4 está presente  en  la
"lista_2". Para ello, escribimos la palabra clave "elif" seguida de la condición entre paréntesis  y
terminada con dos puntos (:). La condición se compone del valor 4, el operador de pertenencia "in" y
la variable "lista_2".

Si la condición se cumple (si el número 4 está presente en la lista_2), se imprime un mensaje en  la
consola utilizando la función "print()", el  cual  corresponde  al  bloque  de  código  asociado  al
condicional "elif" que colocamos justo debajo y con una indentación de cuatro espacios.

Por último, utilizamos el condicional "else" para manejar el caso en que las condiciones del "if"  y
"elif" no se cumplan. Para ello, escribimos la palabra clave "else" seguida de dos  puntos  (:).  Si
las condiciones "if" y "elif" no se cumplen, se imprime un  mensaje  en  la  consola  utilizando  la
función "print()", el cual corresponde al bloque  de  código  asociado  al  condicional  "else"  que
colocamos justo debajo y con una indentación de cuatro espacios.

Después del bloque "if...elif...else", se imprime otro mensaje indicando el fin de la  verificación,
el cual se imprimirá siempre, independientemente de si la condición se cumple  o  no,  ya  que  está
fuera del bloque "if...elif...else". En este caso, se imprimirá "El número 4  está  presente  en  la
lista_1", ya que el número 4 está presente en la "lista_1"."""

# Código:
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [11, 12, 13, 14, 15]

if (4 in lista_1):
    print("El número 4 está presente en la lista_1")
elif (4 in lista_2):
    print("El número 4 está presente en la lista_2")
else:
    print("El número 4 no está presente en ninguna de las listas")

print("Fin de la verificación del elemento en las listas")

# Nota Importante:
"""Es importante saber que si el número elegido estuviera presente en ambas listas, el programa solo
imprimiría el mensaje del primer condicional ya que en cuanto se cumple una condición, el  resto  de
condiciones no se evalúan.

Además, es posible definir el número a verificar como una variable, por ejemplo: "numero  =  4".  De
este modo, introduciríamos la variable en las condiciones del "if"  y  "elif"  obteniendo  el  mismo
resultado.

Esto ocurre porque Python evalúa el valor  de  la  variable  en  el  momento  de  la  ejecución  del
condicional y, al coincidir con el valor que estamos buscando, la condición  se  cumple  ya  que  el
valor de la variable es igual al valor que estamos verificando en las listas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
