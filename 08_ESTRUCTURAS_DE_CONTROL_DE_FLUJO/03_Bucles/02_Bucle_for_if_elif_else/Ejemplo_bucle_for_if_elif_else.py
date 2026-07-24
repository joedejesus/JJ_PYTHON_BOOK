# Enunciado:
"""El bucle "for" en Python permite iterar  sobre  una  secuencia  o  cualquier  objeto  iterable  y
ejecutar un bloque de  código  para  cada  elemento  iterado.  Este  bucle  es  útil  para  recorrer
estructuras de datos y realizar operaciones sobre cada elemento.

La combinación del bucle "for" con las estructuras condicionales "if", "elif" y "else" permite tomar
decisiones basadas en el valor de cada elemento iterado y  ejecutar  diferentes  bloques  de  código
dependiendo de si se cumple o no una condición específica.

Este enfoque es útil para procesar listas, tuplas, cadenas u otras estructuras  de  datos  donde  se
requiere realizar operaciones condicionales en cada iteración del bucle. Además, es  posible  anidar
bucles "for" y combinar condicionales "if", "elif" y "else" para manejar estructuras  más  complejas
de datos y realizar operaciones más sofisticadas. Sin embargo, es importante mantener la legibilidad
del código al usar estas combinaciones."""

# Ejemplo_bucle_for_if_elif_else.py

# Explicación:
"""Definimos una variable llamada "tupla_variada" que contiene una tupla  con  diferentes  tipos  de
datos: enteros, flotantes y cadenas.

Utilizamos un bucle "for" para iterar sobre cada elemento de la  tupla.  Para  ello,  escribimos  la
palabra clave "for", seguida de la variable "i", que representa cada elemento de la secuencia y  que
definimos en este momento, seguida del operador "in" para indicar dónde queremos que se  realice  la
iteración y el nombre de la secuencia sobre la que queremos iterar, en este caso "tupla_variada".  A
continuación, escribimos dos puntos (:) para indicar el final de la expresión y el inicio del bloque
de código asociado al bucle "for".

Dentro del bucle "for", definimos una estructura condicional que  utiliza  los  condicionales  "if",
"elif" y "else" para verificar el tipo de cada elemento "i" de la tupla, y que  será  el  bloque  de
código asociado al bucle "for".

Comprobamos si "i" es un entero utilizando la  función  "isinstance()".  Para  ello,  escribimos  la
palabra clave "if" seguida de la condición entre paréntesis y  terminada  con  dos  puntos  (:).  La
condición se compone de la función "isinstance()", que toma como argumentos el  elemento  "i"  y  el
tipo "int" separados por una coma y entre los paréntesis propios de la función.

Si la condición se cumple (si "i" es una instancia de la  clase  int),  se  imprime  un  mensaje  en
formato "f-string" en la consola utilizando la función "print()", el cual corresponde al  bloque  de
código asociado al condicional "if" que colocamos justo debajo  y  con  una  indentación  de  cuatro
espacios desde el propio condicional "if".

A continuación, comprobamos si "i" es un flotante utilizando también la función "isinstance()". Para
ello, escribimos la palabra clave "elif" seguida de la condición entre paréntesis  y  terminada  con
dos puntos (:). La condición se compone de la función "isinstance()", que toma  como  argumentos  el
elemento "i" y el tipo "float" separados por una coma y entre los paréntesis propios de la función.

Si la condición se cumple (si "i" es una instancia de la clase float),  se  imprime  un  mensaje  en
formato "f-string" en la consola utilizando la función "print()", el cual corresponde al  bloque  de
código asociado al condicional "elif" que colocamos justo debajo y con  una  indentación  de  cuatro
espacios desde el propio condicional "elif".

Luego, utilizamos el condicional "else" para manejar el caso en  que  las  condiciones  del  "if"  y
"elif" no se cumplan. Para ello, escribimos la palabra clave "else" seguida de dos  puntos  (:).  Si
las condiciones "if" y "elif" no se cumplen, se imprime un  mensaje  en  formato  "f-string"  en  la
consola utilizando la función "print()", el  cual  corresponde  al  bloque  de  código  asociado  al
condicional "else" que colocamos justo debajo y con una indentación  de  cuatro  espacios  desde  el
propio condicional "else".

Para los tres casos "if", "elif" y "else" aplicamos una indentación  de  cuatro  espacios  desde  el
margen izquierdo para indicar que estos bloques de código pertenecen al bucle "for" y se evalúan  en
cada iteración del bucle.

Por último, después del bloque condicional "if...elif...else", usamos de nuevo el condicional "else"
asociado al bucle "for". Este condicional se ejecuta una vez al finalizar todas las iteraciones  del
bucle.

En este caso, se imprime otro mensaje indicando que la iteración está completa, el cual se imprimirá
siempre, independientemente de si las condiciones se cumplen o no, ya  que  está  fuera  del  bloque
"if...elif...else". Colocamos el condicional "else" alineado con la palabra clave "for" para indicar
que este bloque de código no pertenece al bloque condicional  "if...elif...else"  y  evitar  que  se
ejecute en cada iteración del bucle."""

# Código:
tupla_variada = (1, 2.14, "3", 4, 5.11, "6")

for i in tupla_variada:
    if (isinstance(i, int)):
        print(f"El elemento {i} es de tipo int.")
    elif (isinstance(i, float)):
        print(f"El elemento {i} es de tipo float.")
    else:
        print(f"El elemento {i} es de tipo str.")
else:
    print("Iteración completa.")

# Nota Importante:
"""El condicional "else" asociado a un bucle "for"  se  ejecuta  una  vez  al  finalizar  todas  las
iteraciones, siempre que el bucle no haya sido interrumpido con la instrucción "break". Esto permite
realizar tareas adicionales o manejar casos específicos al final  del  bucle.  Es  común  usar  este
condicional para verificar si se recorrió toda la  secuencia  sin  interrupciones  o  para  realizar
acciones adicionales después de completar el bucle.

El bloque de código dentro del bucle "for" y los bloques de los condicionales "if", "elif" y  "else"
deben estar correctamente indentados para evitar errores de sintaxis. En  el  caso  del  condicional
"else" asociado a un bucle "for", este debe estar alineado con la palabra clave "for"  para  que  su
bloque de código no se ejecute en  cada  iteración,  sino  solo  una  vez  al  finalizar  todas  las
iteraciones.

En este contexto, el nombre genérico "i" se utiliza para referirse a cada elemento de  la  secuencia
iterada. Esto es una práctica común, pero el nombre puede  ser  cualquier  identificador  válido  en
Python. Además, "i" puede representar cualquier tipo de dato (int, float, str, etc.), dependiendo de
los elementos de la secuencia iterada.

Además, es importante respetar  las  reglas  de  uso  de  condicionales  vistas  en  la  sección  de
condicionales. Esto asegura que el código sea claro, legible y funcional. Además, al combinar bucles
"for" con condicionales "if", "elif" y "else", se pueden manejar estructuras más complejas de  datos
y realizar operaciones más sofisticadas, siempre manteniendo la legibilidad del código.

Por último, en este ejemplo usamos  la  función  "isinstance()"  para  comprobar  el  tipo  de  cada
elemento, ya que es más  segura  y  adecuada  que  convertir  los  elementos  directamente  con  los
constructores "int()" o "float()". La función "isinstance()" es una función  incorporada  en  Python
que se utiliza para verificar si un objeto es una instancia de una clase o de una tupla de clases.

Por lo que en este ejemplo se usa para comprobar si un elemento es de tipo "int"  o  "float"  y,  en
consecuencia,  verificar  las  condiciones  del  condicional  "if"  y  "elif"  respectivamente.  Las
condiciones se cumplirán si el elemento es efectivamente del tipo especificado, permitiendo ejecutar
el bloque de código correspondiente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
