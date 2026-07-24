# Enunciado:
"""Escribe un programa que verifique el valor de una variable llamada "edad" e  imprima  un  mensaje
diferente dependiendo de si la edad es mayor o igual a 18 años o menor de 18 años.  Si  la  edad  es
mayor o igual a 18  años,  el  programa  debe  imprimir  el  mensaje  "Eres  mayor  de  edad,  estás
autorizado". En caso contrario, el programa debe imprimir el mensaje "Eres menor de edad,  no  estás
autorizado".

Por último, el programa debe imprimir un mensaje que diga "Fin del programa", independientemente  de
la edad. Los bloques deben estar correctamente indentados y el valor de la variable "edad" puede ser
cualquier número entero entre 0 y 100."""

# Ejercicio_condicional_if.py

# Explicación:
"""Definimos una variable llamada "edad"  y  le  asignamos  un  valor;  en  este  caso,  20.  Luego,
utilizamos dos estructuras condicionales "if" para verificar si la edad es mayor o igual a 18 años o
menor de 18 años.

En el primer caso, utilizamos el condicional "if" para verificar si la edad es mayor o igual  a  18.
Para ello, escribimos la palabra clave "if", seguida de la condición entre  paréntesis  y  terminada
con dos puntos (:). La condición se compone de la variable "edad", el operador comparativo (>=) y el
valor 18.

Si la primera condición se cumple (si "edad" es mayor o igual a 18), se imprime  un  mensaje  en  la
consola utilizando la función "print()", el  cual  corresponde  al  bloque  de  código  asociado  al
condicional "if", que colocamos justo debajo con una indentación de cuatro espacios.

En el segundo caso, utilizamos el condicional "if" para verificar si la edad es menor  de  18.  Para
ello, escribimos la palabra clave "if", seguida de la condición entre paréntesis y terminada con dos
puntos (:). La condición se compone de la variable "edad", el operador comparativo (<)  y  el  valor
18.

Si la segunda condición se cumple (si "edad" es menor de 18), se imprime un mensaje  en  la  consola
utilizando la función "print()", el cual corresponde al bloque de  código  asociado  al  condicional
"if", que colocamos justo debajo con una indentación de cuatro espacios.

Después de los bloques "if", se imprime otro mensaje indicando el  fin  del  programa,  el  cual  se
mostrará siempre, independientemente de si las condiciones se cumplen o no, ya que está fuera de los
bloques "if".

En este caso, el programa imprime "Eres mayor de edad, estás  autorizado"  porque  el  valor  de  la
variable "edad" es 20, que es mayor o igual a 18."""

# Código:
edad = 20

if (edad >= 18):
    print("Eres mayor de edad, estás autorizado")
if (edad < 18):
    print("Eres menor de edad, no estás autorizado")

print("Fin del programa")

# Nota Importante:
"""En este caso, se utilizan dos estructuras  condicionales  "if"  independientes  en  lugar  de  un
"if-else", lo cual no sería lo más adecuado. Esto significa que ambas  condiciones  se  evalúan  por
separado. Si la edad es exactamente 18 o mayor, solo se ejecutará el primer bloque "if". Si la  edad
es menor de 18, solo se ejecutará el segundo bloque "if".

Es importante destacar que el uso de dos bloques "if" independientes puede ser útil  en  situaciones
en las que se requiera  evaluar  múltiples  condiciones  de  forma  separada,  pero,  en  este  caso
particular, un "if-else" sería más eficiente y claro, ya que  las  dos  condiciones  son  mutuamente
excluyentes. Estos condicionales se verán en  las  próximas  secciones  para  seguir  una  curva  de
aprendizaje progresiva y no mezclar conceptos."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
