# Enunciado:
"""Los argumentos posicionales en Python son aquellos que se pasan a una función en un orden específico y 
predefinido. El orden en el que se pasan los argumentos es crucial, ya que cada argumento se asigna al
parámetro correspondiente según su posición en la definición de la función. Esto significa que el primer
argumento proporcionado se asignará al primer parámetro definido en la función, el segundo argumento al
segundo parámetro, y así sucesivamente. El orden comienza desde la izquierda, siguiendo la convención de
indexación en Python, donde el índice inicial es cero.

El uso de argumentos posicionales es útil cuando el significado de cada argumento es evidente por su
posición, lo que permite escribir funciones de manera más concisa y directa. Sin embargo, es importante tener
en cuenta que el orden de los argumentos no puede alterarse arbitrariamente, ya que esto podría llevar a
resultados inesperados o errores en la ejecución del programa. Por ejemplo, si una función espera que el
primer argumento sea un número entero y el segundo un número flotante, invertir el orden podría causar
errores de tipo o resultados incorrectos.

En funciones con muchos parámetros, el uso exclusivo de argumentos posicionales puede dificultar la
comprensión del código, especialmente si no está bien documentado. Por esta razón, es recomendable documentar
claramente el propósito de cada argumento y considerar el uso de argumentos nombrados (keyword arguments)
cuando sea necesario. Los argumentos nombrados permiten especificar explícitamente qué valor corresponde a
cada parámetro, independientemente del orden en que se pasen, lo que mejora la legibilidad y reduce el riesgo
de errores.

Por último, los argumentos posicionales son una herramienta poderosa y eficiente para transferir valores a
las funciones, pero requieren atención al orden en que se especifican. Su uso es ideal en funciones simples y
bien definidas, donde el propósito de cada parámetro es claro y no da lugar a confusiones. En casos más
complejos, es recomendable combinar argumentos posicionales con argumentos nombrados para lograr un
equilibrio entre simplicidad, claridad y flexibilidad en el diseño de las funciones."""

# Ejemplo_argumentos_posicionales.py

# Explicación:
"""Definimos una función llamada "calculo_area_rectangulo()" que recibe dos parámetros llamados "base" y 
"altura". Estos parámetros se utilizarán para calcular el área de un rectángulo multiplicando la base por la
altura y serán sustituidos por los valores que se le pasen a la función al llamarla. Para ello, utilizamos la
palabra clave "def" seguida del nombre de la función, en este caso "calculo_area_rectangulo()", seguida del
nombre de los parámetros "base" y "altura" entre paréntesis, separados por una coma, y terminamos con dos
puntos (:) para indicar el inicio del bloque de código asociado a la función.

A continuación, dentro de la función utilizamos la instrucción "return" para devolver el producto de "base" y
"altura" como resultado del cálculo del área del rectángulo. La expresión (base * altura) realiza la
multiplicación de los valores de los dos parámetros y genera el resultado que será devuelto cuando la función
sea llamada. La instrucción "return" indica al intérprete de Python que la función debe finalizar su
ejecución y enviar el valor especificado de vuelta al lugar donde fue llamada. Para ello, escribimos la
palabra clave "return" seguida del valor que queremos devolver, en este caso el resultado de la
multiplicación de (base * altura) utilizando el operador de multiplicación (*). 

En este caso, estamos devolviendo el resultado de una operación aritmética en una sola instrucción en forma
de número entero (int). Colocamos esta línea de código con una indentación de cuatro espacios desde el margen
izquierdo para indicar que forma parte del bloque de código asociado a la función y debe ejecutarse siempre
que la función sea llamada.

Luego, llamamos a la función "calculo_area_rectangulo()" con los argumentos correspondientes, en este caso
los valores 5 y 10 para así ejecutar el código asociado dentro de ella. Para llamar a la función, simplemente
escribimos su nombre seguido de paréntesis con los argumentos correspondientes en el orden en que queramos
que se transfieran, separados por una coma, en este caso "calculo_area_rectangulo(5, 10)". Escribimos los
argumentos como números para indicar que se tratan de números enteros (int) y así hacer que los tipos de
datos sean compatibles. De esta forma, estos valores serán transferidos y asignados a los parámetros "base" y
"altura" respectivamente, ya que la función los recibe en el mismo orden en que son transferidos al ser
argumentos posicionales. Además, asignamos la llamada de la función a una variable llamada "resultado_area"
para almacenar el valor devuelto por la función en la variable en forma de número entero (int). Colocamos
esta línea de código sin indentación, ya que se encuentra en el nivel principal del código y no forma parte
de ninguna otra estructura.

Por último, imprimimos el resultado del cálculo del área del rectángulo. Para ello, utilizamos la función
"print()" en formato "f-string" incluyendo la variable "resultado_area", la cual contiene el valor almacenado
y devuelto por la función. Esto nos permite mostrar el resultado de manera clara y legible en la consola.
Colocamos esta línea de código sin indentación, ya que se encuentra en el nivel principal del código y no
forma parte de ninguna otra estructura."""

# Código:
def calculo_area_rectangulo(base, altura):
    return (base * altura)

resultado_area = calculo_area_rectangulo(5, 10)

print(f"El área del rectángulo es: {resultado_area}")

# Nota Importante:
"""En este caso, los argumentos posicionales son los números enteros 5 y 10, que se asignan a los parámetros 
base y altura respectivamente según su posición en la llamada a la función. Esto significa que el primer
valor "5" se asigna al parámetro "base", y el segundo valor "10" se asigna al parámetro "altura". En este
caso, cambiar el orden de los factores al ser una multiplicación no afectaría el resultado final del cálculo
del área del rectángulo, ya que la multiplicación es conmutativa y el producto de dos números no depende del
orden de los factores, pero en otras operaciones sí podría afectar el resultado final.

Es crucial mantener el orden correcto de los argumentos al llamar a funciones que utilizan argumentos
posicionales, ya que estos están diseñados para situaciones donde el orden de los parámetros es evidente y no
se presta a confusión. Sin embargo, en funciones más complejas o con múltiples parámetros, el uso de
argumentos posicionales puede aumentar el riesgo de errores si no se tiene cuidado. En estos casos, es
recomendable utilizar argumentos nombrados para mejorar la claridad y evitar confusiones. Los argumentos
nombrados permiten especificar explícitamente qué valor corresponde a cada parámetro, independientemente de
su posición, lo que resulta especialmente útil en funciones con muchos parámetros o cuando el orden de los
argumentos no es intuitivo.

Además, el uso de la instrucción "return" en este ejemplo es un aspecto importante a destacar. Al devolver
directamente el resultado de la operación aritmética (base * altura), se evita la necesidad de crear
variables intermedias dentro de la función, lo que hace que el código sea más eficiente y fácil de leer. Este
enfoque es especialmente útil en funciones simples y bien definidas, donde el resultado puede calcularse y
devolverse en una sola línea de código.

Por otro lado, es importante destacar que cuando nos referimos a "posicionales" nos referimos a los
argumentos y no a los parámetros. Los parámetros son las variables definidas en la declaración de la función
que actúan como marcadores de posición para los valores que se pasarán cuando la función sea llamada. Los
argumentos, por otro lado, son los valores reales que se proporcionan a la función al momento de la llamada.
Estas pequeñas pero importantes diferencias terminológicas son esenciales para comprender cómo funcionan las
funciones en Python y cómo se manejan los datos dentro de ellas.

Por último, este ejemplo ilustra cómo los argumentos posicionales pueden ser útiles en funciones simples y
bien definidas, donde el orden de los parámetros es claro y no da lugar a ambigüedades. Sin embargo, en
aplicaciones más complejas, es recomendable combinar argumentos posicionales con argumentos nombrados para
lograr un equilibrio entre simplicidad y legibilidad. Esto asegura que el código sea fácil de entender y
mantener, incluso para otros desarrolladores que trabajen en el mismo proyecto. La elección entre argumentos
posicionales y nombrados dependerá del contexto y de las necesidades específicas de cada función."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
