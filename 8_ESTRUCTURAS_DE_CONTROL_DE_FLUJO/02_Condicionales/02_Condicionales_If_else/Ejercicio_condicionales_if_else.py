# Enunciado:
"""Escribe un programa que verifique el valor de una variable llamada "numero" e imprima un  mensaje
dependiendo de si el valor de la variable "numero" es par o impar. Si el valor es par,  el  programa
debe imprimir el mensaje "El número es par". En caso contrario, el programa debe imprimir el mensaje
"El número es impar".

Por último, el programa debe imprimir un mensaje que diga "Fin del programa"  independientemente  de
las condiciones. Los bloques deben estar correctamente indentados y el valor de la variable "numero"
puede ser cualquier número entero. Además, usa el operador aritmético (%) para crear  la  condición,
teniendo en cuenta que este devuelve el residuo de la división entre dos números."""

# Ejercicio_condicionales_if_else.py

# Explicación:
"""Definimos una variable llamada "numero" y le asignamos el valor entero -189. Luego, utilizamos el
condicional "if" para verificar si el valor de la variable "numero" es par. Para ello, escribimos la
palabra clave "if", seguida de la condición entre paréntesis y terminada  con  dos  puntos  (:).  La
condición se compone de la variable "numero", el operador módulo (%), el valor  2,  el  operador  de
igualdad (==) y el valor 0.

Si la condición se cumple (si el residuo de la división de "numero" entre 2 es  0),  se  imprime  un
mensaje en la consola utilizando la función "print()", el  cual  corresponde  al  bloque  de  código
asociado al condicional "if" que colocamos justo debajo y con una indentación de cuatro espacios.

A continuación, utilizamos el condicional "else" para manejar el caso en que la condición  del  "if"
no se cumpla. Para ello, escribimos la palabra clave "else" seguida de dos puntos (:).

Si la condición del "if" no se cumple (si el residuo de la división de "numero" entre 2 no es 0), se
imprime un mensaje en la consola utilizando la función "print()", el cual corresponde al  bloque  de
código asociado al condicional "else" que colocamos justo debajo y con  una  indentación  de  cuatro
espacios.

Después del bloque "if...else", se imprime otro mensaje indicando el fin del programa,  el  cual  se
imprimirá siempre, independientemente de si la condición se cumple o  no,  ya  que  está  fuera  del
bloque "if...else". En este caso, se imprimirá "El número es impar", ya  que  la  variable  "numero"
tiene un valor de -189, y el residuo de la división de -189 entre 2 es 1, por lo tanto, es un número
impar."""

# Código:
numero = -189

if (numero % 2 == 0):
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")

print("Fin del programa")

# Nota Importante:
"""Dado que el operador aritmético (%) devuelve el residuo de la división, podemos usarlo dentro  de
la condición para saber si un número es par o impar. Si el residuo de la división del número que  se
va a verificar entre 2 es 0, entonces el número es par; de lo contrario, es impar.

Para comprobar si un número es par, se recomienda usar siempre como valor dentro de la condición  el
número 2, ya que es  el  número  par  más  pequeño  y  el  que  mejor  se  adapta  a  este  tipo  de
verificaciones.

Es importante saber que podemos utilizar el operador de desigualdad (!=) para obtener una  respuesta
opuesta a la que nos da el operador de igualdad. Por ejemplo, en lugar de usar "if (numero  %  2  == 0):" 
para verificar si un número es par, podríamos usar "if (numero % 2 != 0):" para verificar si un número 
es impar."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
