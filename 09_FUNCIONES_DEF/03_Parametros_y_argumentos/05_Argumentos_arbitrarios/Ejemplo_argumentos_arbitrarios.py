# Enunciado:
"""Los argumentos arbitrarios "*args" en Python permiten que una función reciba un número variable de 
argumentos. Esto se logra usando un asterisco (*) antes del nombre del parámetro en la definición de la
función. Comúnmente se usa "args" por convención, pero el nombre del parámetro puede ser cualquier nombre de
variable válido en Python, siempre que se añada el asterisco antes. Dentro de la función, los valores
correspondientes a los argumentos arbitrarios se almacenan como una tupla (tuple), lo que permite procesar
cualquier cantidad de valores sin necesidad de definir un número fijo de parámetros. Dentro de la función, se
omite el asterisco (*) al referirse a los argumentos arbitrarios, ya que estos ya han sido capturados como una
tupla durante la llamada a la función.

Es recomendable que la variable que almacena la tupla de argumentos arbitrarios contenga valores del mismo tipo
de dato para facilitar su procesamiento dentro de la función. Además, es muy importante saber que en la
definición de la función solo se puede definir un argumento arbitrario "*args", pero este puede recibir tantos
valores como sea necesario. Al momento de llamar a la función, se pueden pasar múltiples tipos de datos
diferentes. Python no impone restricciones sobre los tipos de datos que se pueden pasar como argumentos
arbitrarios, lo que permite una gran flexibilidad. Por ejemplo, se pueden pasar números, cadenas, listas u
otros tipos de datos como argumentos arbitrarios, ya sea de forma literal o contenidos en variables.

Es importante destacar que los argumentos arbitrarios siempre se reciben en forma de tupla, a menos que se
transformen a otro tipo de dato dentro de la función. Además, si usamos la instrucción "return" para devolver
valores, los datos serán devueltos en su tipo original y, si se devuelven múltiples valores, estos se
devolverán como una tupla (tuple). Esto es relevante si se combinan diferentes tipos de parámetros en la
definición de la función. Además, garantiza que la salida de valores sea predecible y consistente.

El uso de argumentos arbitrarios es especialmente útil cuando no se sabe de antemano cuántos valores se pasarán
a la función. Esto proporciona flexibilidad y permite que la función sea más general y adaptable a diferentes
escenarios. Por ejemplo, se pueden usar para sumar una cantidad variable de números, concatenar cadenas o
realizar operaciones con listas de longitud desconocida.

Además, cuando se combinan argumentos arbitrarios con otros parámetros, los arbitrarios deben colocarse al
final de la lista de parámetros usando la notación "*args". Si se combinan con parámetros con valores
predeterminados, estos deben ir antes de los argumentos arbitrarios en la definición de la función. Al llamar a
la función, los argumentos posicionales y nombrados deben proporcionarse antes de los argumentos arbitrarios.

Esto asegura que los argumentos posicionales se asignen correctamente antes de capturar los valores adicionales
en la tupla de argumentos arbitrarios. El orden en la definición de la función sería el siguiente: parámetros
obligatorios, parámetros con valores predeterminados y, finalmente, argumentos arbitrarios. El orden al llamar
a la función sería: argumentos posicionales, argumentos nombrados y, finalmente, argumentos arbitrarios.

Otra ventaja importante de los argumentos arbitrarios es que permiten escribir funciones más dinámicas y
reutilizables. En lugar de limitarse a un número fijo de parámetros, las funciones pueden aceptar cualquier
cantidad de entradas, lo que las hace más versátiles y adecuadas para una variedad de casos de uso.

En Python, los argumentos arbitrarios también se pueden combinar con argumentos nombrados y argumentos
arbitrarios nombrados (**kwargs), lo que permite una mayor flexibilidad al definir funciones. Por ejemplo, se
pueden usar "*args" para capturar valores posicionales adicionales y "**kwargs" para capturar pares
"clave-valor" adicionales, lo que permite una personalización más avanzada de las funciones.

Por último, los argumentos arbitrarios son una herramienta poderosa para escribir funciones flexibles y
adaptables. Su capacidad para aceptar un número variable de entradas los hace ideales para escenarios donde la
cantidad de datos puede variar, mejorando la reutilización del código y permitiendo una mayor modularidad en el
diseño del software."""

# Ejemplo_argumentos_arbitrarios.py

# Explicación:
"""Definimos una función llamada "sumar_numeros()" que recibe un parámetro obligatorio llamado "lista" y un 
parámetro arbitrario representado por el nombre "*args" como segundo parámetro. Estos parámetros se utilizarán
para realizar una operación de suma entre los elementos de una lista y los valores pasados como argumentos
arbitrarios en forma de tupla, y serán sustituidos por los valores que se le pasen a la función al llamarla.
Para ello, utilizamos la palabra clave "def" seguida del nombre de la función, en este caso "sumar_numeros()",
seguida de los nombres de los parámetros "lista" y "*args" entre paréntesis, separados por una coma, y
terminamos con dos puntos (:) para indicar el inicio del bloque de código asociado a la función.

Dentro de la función, utilizamos la instrucción "print()" para imprimir dos mensajes en la consola en formato
"f-string", los cuales incluyen los nombres de los parámetros "lista" y "args", respectivamente. Estos
parámetros serán sustituidos por los argumentos pasados al llamar a la función, ya sean posicionales o
arbitrarios, los cuales serán de nuestra elección y se utilizarán para formatear el mensaje. Colocamos estas
instrucciones con una indentación de cuatro espacios desde el margen izquierdo para indicar que forman parte
del cuerpo de la función y deben ejecutarse siempre que la función sea llamada.

Estos mensajes permiten visualizar los valores recibidos por la función, mostrando cómo el argumento posicional
se almacena en una lista y cómo los argumentos arbitrarios se almacenan en una tupla. Esto es útil para
entender cómo se manejan los diferentes tipos de argumentos dentro de la función.

A continuación, dentro de la función utilizamos la instrucción "return" para devolver el resultado de la suma
de los elementos de la lista y los valores pasados como argumentos arbitrarios en forma de tupla. Esto se logra
utilizando la función incorporada "sum()" para calcular la suma de los elementos de la lista y la suma de los
valores de la tupla de argumentos arbitrarios "args". La función "sum()" recibe un iterable como argumento y
devuelve la suma de sus elementos. Los resultados devueltos por la función "sum()" luego se suman entre sí
utilizando el operador de suma (+) para obtener el resultado final. La instrucción "return" indica al
intérprete de Python que la función debe finalizar su ejecución y enviar el valor especificado de vuelta al
lugar donde fue llamada, en este caso, el resultado de la suma de los elementos de la lista y los valores
pasados como argumentos arbitrarios.

Para ello, escribimos la palabra clave "return" seguida del valor que queremos devolver, en este caso, el
resultado de la suma de "sum(lista) + sum(args)" utilizando el operador de suma (+) y encerrando toda la
operación entre paréntesis. Además, pasamos como argumento a la función "sum()" tanto el parámetro "lista" como
el parámetro "args" dentro de los paréntesis de la propia función para calcular la suma de sus elementos. En
este caso, estamos devolviendo el resultado de una operación aritmética en una sola instrucción en forma de
número entero (int). Colocamos esta línea de código con una indentación de cuatro espacios desde el margen
izquierdo para indicar que forma parte del bloque de código asociado a la función y debe ejecutarse siempre que
la función sea llamada.

Luego, llamamos a la función "sumar_numeros()" con los argumentos correspondientes, en este caso una lista
literal "[1, 2, 3]" como argumento posicional y los valores "10", "15" y "20" como argumentos arbitrarios en
forma de tupla. Estos valores serán transferidos a la función y asignados a los parámetros correspondientes.

Para llamar a la función, simplemente escribimos su nombre seguido de paréntesis con los argumentos
correspondientes, ya sean posicionales o arbitrarios, separados por una coma, en este caso "sumar_numeros ([1,
2, 3], 10, 15, 20)", respetando el orden de los argumentos, primero el posicional y luego los arbitrarios.
Además, asignamos la llamada de la función a una variable llamada "resultado" para almacenar el valor devuelto
por la función. Tanto los valores de la lista literal como los valores pasados como argumentos arbitrarios son
números enteros (int); de esta forma, nos aseguramos de que la operación aritmética reciba los valores del tipo
de dato esperado y así garantizar que la operación de suma se realice correctamente. Colocamos esta línea de
código sin indentación para indicar que no forma parte de ninguna otra estructura.

Por último, utilizamos la instrucción "print()" para imprimir un mensaje con el resultado final de la suma en
la consola en formato "f-string". Este mensaje incluye el valor almacenado en la variable "resultado",
acompañado de un mensaje descriptivo. Colocamos esta línea de código sin indentación para indicar que no forma
parte de ninguna otra estructura."""

# Código:
def sumar_numeros(lista, *args):
    print(f"Argumentos posicionales recibidos como lista: {lista}")
    print(f"Argumentos arbitrarios recibidos como tupla: {args}")
    return (sum(lista) + sum(args))

resultado = sumar_numeros([1, 2, 3], 10, 15, 20)

print(f"El resultado final de la suma es: {resultado}")

# Nota Importante:
"""En este caso, los argumentos arbitrarios permiten que la función acepte un número variable de entradas: 
una lista literal y varios números enteros como argumentos arbitrarios. Dentro de la función, los argumentos
arbitrarios se reciben como una tupla y la lista literal como una lista. Esto significa que la función puede
procesar cualquier cantidad de valores sin necesidad de definir un número fijo de parámetros.

Es crucial entender que los argumentos arbitrarios mejoran la flexibilidad del código, ya que permiten manejar
entradas dinámicas sin necesidad de modificar la definición de la función. Esto es especialmente útil en
escenarios donde no se conoce de antemano cuántos valores se pasarán a la función.

Cuando se combinan argumentos arbitrarios con otros parámetros, es importante que los argumentos arbitrarios se
definan al final de la lista de parámetros de la función. Esto asegura que los argumentos posicionales se
asignen correctamente antes de capturar los valores adicionales en la tupla de argumentos arbitrarios.

Aunque a menudo nos referimos a estos como "argumentos arbitrarios", técnicamente, en la definición de la
función, estamos hablando de "parámetros con argumentos arbitrarios". Es decir, los valores que se pasan al
llamar a la función son argumentos, pero lo que se define en la función son parámetros. Usamos el término
"argumentos" y la notación "*args" por convención, por lo que es recomendable entender la distinción entre
ambos términos.

Por último, los argumentos arbitrarios son una herramienta poderosa para escribir funciones dinámicas y
flexibles. Su capacidad para aceptar un número variable de entradas los hace ideales para escenarios donde la
cantidad de datos puede variar, mejorando la reutilización del código y permitiendo una mayor modularidad en el
diseño del software."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
