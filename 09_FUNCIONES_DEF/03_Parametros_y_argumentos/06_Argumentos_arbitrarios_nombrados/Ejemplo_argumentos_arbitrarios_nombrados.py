# Enunciado:
"""Los argumentos arbitrarios nombrados "**kwargs" en Python permiten que una función reciba un número variable 
de argumentos nombrados en forma de diccionario de "pares clave-valor". Esto se logra usando dos asteriscos
(**) antes del nombre del parámetro en la definición de la función. Por convención, se usa "kwargs" como nombre
del parámetro, pero este puede ser cualquier nombre de variable válido en Python. Dentro de la función, los
argumentos arbitrarios nombrados se almacenan como un diccionario (dict), lo que permite procesar cualquier
cantidad de pares "clave-valor" sin necesidad de definir un número fijo de parámetros. Además, dentro de la
función, se omiten los asteriscos al referirse a los argumentos arbitrarios nombrados, ya que estos ya han sido
agrupados en un diccionario al momento de la llamada a la función. Por lo tanto, podemos acceder a los valores
utilizando las claves correspondientes del diccionario "kwargs".

En cierto modo, los argumentos arbitrarios nombrados son similares a los argumentos nombrados, con la
diferencia de que los argumentos nombrados requieren que se definan explícitamente en la definición de la
función como posicionales o predeterminados, mientras que los argumentos arbitrarios nombrados permiten pasar
un número variable de pares "clave-valor" sin necesidad de definirlos previamente. Sin embargo, los argumentos
nombrados se almacenan como parámetros individuales, mientras que los argumentos arbitrarios nombrados se
agrupan en un diccionario. En ambos casos se asocia un nombre a cada valor, pero los argumentos arbitrarios
nombrados ofrecen mayor flexibilidad al no requerir una definición fija de los parámetros.

Además, esto proporciona mayor flexibilidad al permitir que la función maneje diferentes cantidades de datos
según sea necesario. Asimismo, el orden de asignación, en cuanto a la posición de las claves en el diccionario,
es el mismo en el que se definen al llamar a la función. Esto es relevante en cuanto a cómo se presentan los
datos, aunque en un diccionario el orden de los elementos no afecta la forma en que se accede a ellos, pero sí
a cómo se imprimen o muestran.

Es importante que las claves del diccionario en la llamada a la función sean únicas y se definan respetando la
sintaxis de los nombres de variables en Python, ya que estas representan los nombres de los argumentos. Además,
en la definición de la función solo es posible definir un argumento arbitrario nombrado "**kwargs". Al llamar a
la función, se pueden pasar múltiples pares "clave-valor", y los valores asociados a las claves pueden ser de
cualquier tipo de dato válido en Python, como números, cadenas, listas, diccionarios, objetos, entre otros.
Esto hace que los argumentos arbitrarios nombrados sean especialmente útiles para manejar datos estructurados o
configuraciones dinámicas.

Cuando se combinan argumentos arbitrarios nombrados con otros parámetros en la definición de la función, los
argumentos arbitrarios nombrados deben colocarse al final de la lista de parámetros usando la notación
"**kwargs". El orden correcto en la definición de la función es: parámetros obligatorios, parámetros con
valores predeterminados, argumentos arbitrarios "*args" y, finalmente, argumentos arbitrarios nombrados
"**kwargs". Para la llamada a la función, el orden sería: argumentos posicionales, argumentos nombrados,
argumentos arbitrarios "*args" y, por último, argumentos arbitrarios nombrados "**kwargs". Este orden asegura
que los argumentos se asignen correctamente y evita errores de interpretación.

El uso de argumentos arbitrarios nombrados es útil cuando no se sabe de antemano cuántos pares "clave-valor" se
pasarán a la función. Esto proporciona flexibilidad y permite que la función sea más general y adaptable a
diferentes escenarios. Por ejemplo, se pueden usar para configurar opciones dinámicas, manejar configuraciones
complejas o procesar datos estructurados de manera eficiente.

Por último, los argumentos arbitrarios nombrados son una herramienta poderosa para escribir funciones dinámicas
y flexibles. Su capacidad para aceptar un número variable de pares "clave-valor" los hace ideales para
escenarios en los que la cantidad de datos puede variar, mejora la reutilización del código, permite una mayor
modularidad en el diseño del software y facilita la creación de soluciones más robustas y escalables."""

# Ejemplo_argumentos_arbitrarios_nombrados.py

# Explicación:
"""Definimos una función llamada "informacion()" que recibe un argumento arbitrario nombrado representado por 
el nombre "**kwargs". Este parámetro se utilizará para almacenar un número variable de pares "clave-valor" y
permitirá iterar sobre ellos dentro de la función. Los valores serán transferidos y asignados a este parámetro
al llamar a la función, y representarán la información de una persona. Para ello, utilizamos la palabra clave
"def" seguida del nombre de la función, en este caso "informacion()", seguido del nombre del parámetro
"**kwargs" entre paréntesis, y terminamos con dos puntos (:) para indicar el inicio del bloque de código
asociado a la función.

Dentro de la función, utilizamos un bucle "for" para iterar sobre cada par "clave-valor" del diccionario
"kwargs". Para ello, escribimos la palabra clave "for", seguida de las variables "clave" y "valor" separadas
por una coma, las cuales representan cada par "clave-valor" del diccionario y se definen en este momento,
seguida del operador "in" para indicar dónde queremos que se realice la iteración y el nombre de la secuencia
sobre la que queremos iterar, en este caso "kwargs". Además, utilizamos el método de diccionario ".items()"
asociado al diccionario para obtener una vista de los pares "clave-valor". A continuación, escribimos dos
puntos (:) para indicar el final de la expresión y el inicio del bloque de código asociado al bucle "for". La
expresión quedaría de la siguiente manera: "for clave, valor in kwargs.items():". Colocamos esta línea de
código con una indentación de cuatro espacios desde el margen izquierdo para indicar que forma parte del bloque
de código asociado a la función y que debe ejecutarse siempre que la función sea llamada.

Dentro del bucle, utilizamos la instrucción "print()" para imprimir un mensaje en la consola en cada iteración
del bucle en formato "f-string", el cual incluye los nombres de los parámetros "clave" y "valor",
respectivamente. Estos parámetros serán sustituidos por los argumentos arbitrarios nombrados pasados al llamar
a la función, los cuales serán elegidos por nosotros y se utilizarán para formatear el mensaje. Colocamos esta
instrucción con una indentación de cuatro espacios desde el bucle "for" para indicar que forma parte del bucle
y que debe ejecutarse en cada iteración, siempre que la función sea llamada.

Por último, llamamos a la función "informacion()" con los argumentos arbitrarios nombrados, en este caso
"nombre=Ana", "edad=28", "ciudad=Asturias" y "profesion=Ingeniera". Estos pares "clave-valor" son transferidos
a la función y asignados al parámetro "**kwargs" en forma de diccionario. Para llamar a la función, simplemente
escribimos su nombre seguido de paréntesis con los argumentos en forma de pares "clave-valor", con la ayuda del
operador de asignación (=), separados por comas y respetando la sintaxis de los nombres de variables en Python.
Además, los valores se pasan como cadenas de texto (str). Colocamos esta línea de código sin indentación para
indicar que no forma parte de ninguna otra estructura.

En este caso, los pares "clave-valor" definidos al llamar a la función se agrupan en un diccionario dentro de
la función, representado por "**kwargs". Utilizamos un bucle "for" para iterar sobre los elementos del
diccionario "kwargs", con ayuda del método de diccionario ".items()". Este método devuelve una vista de los
pares "clave-valor" del diccionario, lo que permite acceder a cada clave y a su valor correspondiente durante
la iteración. Dentro del bucle, se imprimen las claves y los valores utilizando una cadena formateada
"f-string" para mostrar cada par en el formato "clave: valor" en cada iteración. Esto hace posible la
visualización de los datos almacenados en el diccionario "kwargs"."""

# Código:
def informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

informacion(nombre="Ana", edad="28", ciudad="Asturias", profesion="Ingeniera")

# Nota Importante:
"""Es importante entender que los argumentos arbitrarios nombrados mejoran la flexibilidad del código, ya que 
permiten manejar entradas dinámicas sin necesidad de modificar la definición de la función. Esto asegura que
los argumentos posicionales y nombrados se asignen correctamente antes de capturar los pares "clave-valor"
adicionales en el diccionario de argumentos arbitrarios nombrados.

Además, los argumentos arbitrarios nombrados son ideales para manejar configuraciones dinámicas, ya que
permiten que las funciones acepten opciones adicionales sin necesidad de modificar su definición. Esto mejora
la modularidad y la escalabilidad del código, permitiendo que las funciones se adapten a diferentes escenarios
y requisitos.

Aunque a menudo nos referimos a estos como "argumentos arbitrarios nombrados", técnicamente, en la definición
de la función, estamos hablando de "parámetros con argumentos arbitrarios nombrados". Es decir, los valores que
se pasan al llamar a la función son argumentos, pero lo que se define en la función son parámetros. Usamos el
término "argumentos" y la notación "**kwargs" por convención, por lo que es recomendable entender la distinción
entre ambos términos.

Es importante destacar que los argumentos arbitrarios nombrados se pueden combinar con otros tipos de
parámetros en la definición de la función, como parámetros obligatorios, parámetros con valores predeterminados
y argumentos arbitrarios posicionales.  

Por último, los argumentos arbitrarios nombrados son una herramienta poderosa para escribir funciones dinámicas
y flexibles. Su capacidad para aceptar un número variable de pares "clave-valor" los hace ideales para
escenarios en los que la cantidad de datos puede variar, mejora la reutilización del código, permite una mayor
modularidad en el diseño del software y facilita la creación de soluciones más robustas y escalables."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
