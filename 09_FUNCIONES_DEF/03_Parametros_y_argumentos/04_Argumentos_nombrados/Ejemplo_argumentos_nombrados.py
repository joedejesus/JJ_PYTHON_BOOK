# Enunciado:
"""Los argumentos nombrados en Python son aquellos que se pasan a una función especificando explícitamente el 
nombre del parámetro al que se asigna cada valor. Esto permite que los argumentos se proporcionen en cualquier
orden, ya que el nombre del parámetro asegura que el valor se asigne correctamente, independientemente de su
posición en la llamada a la función.

El uso de argumentos nombrados es especialmente útil cuando una función tiene muchos parámetros o cuando
algunos de ellos tienen valores predeterminados. Esto mejora la claridad del código, ya que el propósito de
cada argumento es explícito, reduciendo el riesgo de errores y facilitando el mantenimiento del código. Además,
los argumentos nombrados permiten omitir parámetros opcionales siempre que estos tengan valores predeterminados
definidos en la función. Esto proporciona flexibilidad al llamar a la función, ya que solo es necesario
especificar los argumentos relevantes para el caso particular.

Cuando en la definición de una función se combinan parámetros obligatorios y parámetros con valores
predeterminados, los parámetros con valores predeterminados deben ir al final de la lista de parámetros. Esto
se debe a que los parámetros sin valores predeterminados son obligatorios y deben especificarse primero. Sin
embargo, al usar argumentos nombrados, es posible sobrescribir esos valores predeterminados si se desea un
comportamiento diferente.

Además, otra ventaja importante es que los argumentos nombrados ayudan a evitar errores comunes, como asignar
valores al parámetro incorrecto debido a la posición de los argumentos. Esto es particularmente útil en
funciones con parámetros que tienen nombres similares o cuando se trabaja con valores que podrían
malinterpretarse si se pasan como argumentos posicionales. Al usar argumentos nombrados, se reduce el riesgo de
asignar accidentalmente un valor al parámetro incorrecto, lo que mejora la robustez del código y reduce errores
en tiempo de ejecución.

En Python, los argumentos nombrados también son ideales para trabajar con funciones que tienen parámetros
opcionales con valores predeterminados. Esto permite que las funciones sean más flexibles y adaptables a
diferentes escenarios, ya que los desarrolladores pueden elegir explícitamente qué parámetros modificar y
cuáles dejar con sus valores por defecto. Además, los argumentos nombrados permiten que las funciones sean más
expresivas, ya que el nombre del parámetro actúa como una especie de documentación implícita, indicando
claramente el propósito de cada valor proporcionado.

Por último, los argumentos nombrados son especialmente útiles en proyectos colaborativos o en código que será
mantenido a largo plazo. Su claridad y flexibilidad los convierten en una herramienta poderosa para escribir
código más robusto, mantenible y fácil de entender. Aunque pueden ser un poco más verbosos que los argumentos
posicionales, su capacidad para evitar errores y mejorar la legibilidad los hace una opción preferida en muchos
casos. En resumen, el uso de argumentos nombrados es una práctica recomendada para mejorar la legibilidad,
evitar confusiones y reducir errores, especialmente en funciones con muchos parámetros. Su claridad y
flexibilidad los convierten en una herramienta poderosa para escribir código más robusto, mantenible y fácil de
entender."""

# Ejemplo_argumentos_nombrados.py

# Explicación:
"""Definimos una función llamada "persona()" que recibe tres parámetros obligatorios llamados "nombre", "edad" 
y "ciudad". Estos parámetros se utilizarán para imprimir un mensaje de saludo personalizado correspondiente a
una persona y serán reemplazados por los valores que se pasen a la función al llamarla. Para ello, utilizamos
la palabra clave "def", seguida del nombre de la función, en este caso "persona()", y de los parámetros
"nombre", "edad" y "ciudad" entre paréntesis, separados por comas. Terminamos con dos puntos (:) para indicar
el inicio del bloque de código asociado a la función.

A continuación, dentro de la función, utilizamos la instrucción "print()" para imprimir un mensaje en la
consola en formato "f-string", el cual incluye los nombres de los parámetros "nombre", "edad" y "ciudad" dentro
del mensaje de saludo. Estos parámetros serán reemplazados por los argumentos pasados al llamar a la función,
ya sean posicionales o nombrados, según se decida al momento de la llamada. Colocamos esta instrucción con una
indentación de cuatro espacios desde el margen izquierdo para indicar que forma parte del cuerpo de la función
y que debe ejecutarse siempre que la función sea llamada.

Luego, llamamos a la función "persona()" con los argumentos correspondientes, en este caso los valores "ana",
"25" y "Asturias", para ejecutar el código asociado dentro de ella. Para llamar a la función, simplemente
escribimos su nombre seguido de paréntesis con los argumentos correspondientes, ya sean posicionales o
nombrados, separados por comas; en este caso, "persona("ana", edad="25", ciudad="Asturias")". Aquí, el primer
argumento "ana" se pasa como argumento posicional, mientras que los otros dos argumentos, "edad" y "ciudad", se
pasan como argumentos nombrados, precedidos por el nombre del parámetro correspondiente, tal como fue definido,
seguido del operador de asignación (=) y del valor del argumento. 

De esta forma, estos valores serán transferidos y asignados a los parámetros correspondientes. En este caso,
"ana" se asigna al parámetro "nombre", "25" al parámetro "edad" y "Asturias" al parámetro "ciudad". Al llamar a
la función, el código dentro de ella se ejecutará y se imprimirá en la consola el mensaje de saludo
personalizado con los valores proporcionados. Colocamos esta línea de código sin indentación, ya que se
encuentra en el nivel principal del código y no forma parte de ninguna otra estructura."""

# Código:
def persona(nombre, edad, ciudad):
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")

persona("ana", edad="25", ciudad="Asturias")

# Nota Muy Importante:
"""En este caso, los argumentos nombrados son "edad" y "ciudad", que se asignan explícitamente a los parámetros 
obligatorios correspondientes de la función. Esto significa que el valor "25" se asigna al parámetro "edad" y
el valor "Asturias" al parámetro "ciudad". Por otro lado, el valor "ana" se asigna al parámetro "nombre" como
argumento posicional, ya que es el único argumento posicional proporcionado en la llamada a la función, y este
se asigna siguiendo el orden de los parámetros en la definición de la función, de izquierda a derecha.

Es crucial entender que los argumentos nombrados mejoran la claridad del código, especialmente en funciones con
múltiples parámetros. Al especificar explícitamente el propósito de cada argumento, se reduce el riesgo de
errores y se facilita el mantenimiento del código. Esto es particularmente útil en funciones complejas o cuando
algunos parámetros tienen valores predeterminados. Además, los argumentos nombrados permiten que el código sea
más legible y autoexplicativo, lo que facilita su comprensión por parte de otros desarrolladores o incluso del
propio autor en el futuro.

El orden de los argumentos nombrados en la llamada a la función no afecta a la asignación de valores a los
parámetros, ya que cada argumento se asigna al parámetro correspondiente según su nombre. Esto significa que
los argumentos nombrados pueden proporcionarse en cualquier orden, lo que brinda flexibilidad al llamar a la
función. Sin embargo, es importante recordar que los argumentos posicionales deben preceder a los argumentos
nombrados en la llamada a la función y deben respetar el orden de los parámetros en la definición de la
función. Esto significa que cualquier argumento posicional debe colocarse antes de los argumentos nombrados
para evitar errores de sintaxis.

Además, los argumentos nombrados en la llamada a la función deben ir siempre después de los argumentos
posicionales, no antes ni entre ellos. Del mismo modo, los parámetros con valores predeterminados en la
definición de la función deben ir siempre después de los parámetros obligatorios sin valores predeterminados,
no antes ni entre ellos. Esto se debe a que los argumentos posicionales se asignan a los parámetros en el orden
en que se definen en la función, mientras que los argumentos nombrados se asignan según el nombre del
parámetro. Colocar argumentos nombrados antes de los argumentos posicionales o mezclarlos puede causar
confusión y errores de sintaxis, ya que Python no podrá determinar correctamente a qué parámetro corresponde
cada argumento.

Es importante tener en cuenta que todos los parámetros obligatorios sin valores predeterminados de una función
deben cubrirse al momento de llamarla, ya sea mediante argumentos posicionales o nombrados. En este ejemplo,
todos los parámetros de la función "persona()" son obligatorios, lo que significa que cada uno debe
proporcionarse de alguna manera, ya sea por nombre o por posición. Si se omite cualquier parámetro en la
llamada a la función, Python generará un error indicando que falta un argumento requerido. Esto subraya la
importancia de comprender la estructura de la función y los requisitos de sus parámetros.

Por último, es fundamental asegurarse de que los tipos de datos de los argumentos nombrados y posicionales
coincidan con los tipos esperados por los parámetros de la función. Esto garantiza que la función se ejecute
correctamente y evita errores en tiempo de ejecución. Además, tener en cuenta el uso que se les dará a estos
datos dentro de la función es esencial para evitar comportamientos inesperados o errores lógicos en el
programa. Los argumentos nombrados, al ser explícitos, también ayudan a documentar el propósito de cada valor,
lo que es especialmente útil en proyectos colaborativos o en código que será mantenido a largo plazo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
