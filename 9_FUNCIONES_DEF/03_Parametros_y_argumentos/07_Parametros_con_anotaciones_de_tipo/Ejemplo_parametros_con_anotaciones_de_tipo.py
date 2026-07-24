# Enunciado:
"""Las anotaciones de tipo en Python permiten especificar el tipo de datos esperado para los parámetros de 
una función y el tipo de dato que esta devuelve. Aunque Python es un lenguaje de tipado dinámico y no requiere
declarar tipos explícitamente, el uso de anotaciones de tipo mejora la legibilidad del código y ayuda a
prevenir errores al proporcionar información adicional sobre cómo se espera que funcione una función. Además,
las anotaciones sirven como una guía para el programador, pero no condicionan el tipo de dato que se le pase a
la función; es decir, se pueden pasar datos de cualquier tipo.

El uso de anotaciones de tipo es útil en proyectos grandes o colaborativos, donde la claridad y la consistencia
son esenciales. También facilita la comprensión del código por parte de otros desarrolladores, ya que
proporciona una documentación implícita sobre los tipos de datos esperados. Esto es particularmente valioso
cuando se trabaja en equipos o cuando el código debe ser mantenido a largo plazo. Además, las anotaciones de
tipo son compatibles con herramientas como "mypy", que permiten realizar comprobaciones estáticas de tipos en
el código. Esto ayuda a identificar errores potenciales antes de ejecutar el programa, lo que resulta
especialmente útil en sistemas críticos o aplicaciones complejas. Por lo tanto, su uso fomenta buenas prácticas
de programación y permite aprovechar al máximo las capacidades de las herramientas modernas de desarrollo.

Es posible combinar las anotaciones de tipo con cualquier tipo de parámetro: parámetros obligatorios,
parámetros con valores predeterminados, "*args" o "**kwargs". Esto permite que las funciones sean más flexibles
y sigan siendo claras en cuanto a los tipos de datos esperados. Por ejemplo, se puede anotar un parámetro con
un valor por defecto o especificar el tipo de dato de los argumentos variables. Además, se pueden anotar
parámetros de cualquier tipo, incluyendo listas, diccionarios, tuplas, clases personalizadas, entre otros. Sin
embargo, es importante recordar que las anotaciones de tipo no reemplazan las validaciones en tiempo de
ejecución. Aunque pueden indicar qué tipos de datos se esperan, no evitan que se pasen valores de tipos
incorrectos. Por esta razón, es recomendable combinar las anotaciones de tipo con validaciones explícitas
dentro de la función, si es necesario. Por ejemplo, se pueden usar estructuras condicionales o excepciones para
verificar que los datos cumplen con los requisitos esperados.

Por último, es importante saber que las anotaciones de tipo son una herramienta poderosa para mejorar la
calidad del código. Al especificar los tipos de datos esperados, se reduce el riesgo de errores, se mejora la
legibilidad y se facilita el mantenimiento del código, especialmente en proyectos complejos o colaborativos.
Además, su uso fomenta buenas prácticas de programación y permite aprovechar al máximo las capacidades de las
herramientas modernas de desarrollo."""

# Ejemplo_parametros_con_anotaciones_de_tipo.py

# Explicación:
"""Definimos una función llamada "sumar()" que recibe dos parámetros obligatorios con anotaciones de tipo 
llamados "a" y "b". Estos parámetros se utilizarán para realizar una operación de suma entre ellos y orientar
al programador sobre los tipos de datos esperados. Serán sustituidos por los valores que se pasen a la función
al llamarla, en coherencia con los tipos de datos esperados según las anotaciones de tipo. Para ello,
utilizamos la palabra clave "def" seguida del nombre de la función, en este caso "sumar()", seguida del nombre
de los parámetros "a" y "b" entre paréntesis, separados por una coma y con su anotación de tipo
correspondiente. Esto se logra escribiendo dos puntos (:) después del nombre de cada parámetro con su anotación
de tipo correspondiente; en este caso, "int", para indicar que se espera que ambos parámetros sean de tipo
entero (int). Además, añadimos la anotación "-> int", lo que indica que la función devolverá un valor de tipo
entero (int) como resultado de la operación de suma, y terminamos con dos puntos (:) para indicar el inicio del
bloque de código asociado a la función. 

A continuación, dentro de la función utilizamos la instrucción "return" para devolver el resultado de la suma
entre los dos parámetros "a" y "b". La expresión (a + b) realiza la suma de los valores de ambos parámetros y
genera el resultado que será devuelto cuando la función sea llamada. La instrucción "return" indica al
intérprete de Python que la función debe finalizar su ejecución y enviar el valor especificado de vuelta al
lugar donde fue llamada. Para ello, escribimos la palabra clave "return" seguida del valor que queremos
devolver, en este caso el resultado de la suma entre los parámetros "a" y "b" utilizando el operador de suma
(+). En este caso, estamos devolviendo el resultado de una operación aritmética en una sola instrucción en
forma de número entero (int) tal y como se espera. Colocamos esta línea de código con una indentación de cuatro
espacios desde el margen izquierdo para indicar que forma parte del bloque de código asociado a la función y
debe ejecutarse siempre que la función sea llamada.

Luego, llamamos a la función "sumar()" con los argumentos correspondientes, en este caso los valores 3 y 5,
para ejecutar el código asociado dentro de ella. Para llamar a la función, simplemente escribimos su nombre
seguido de paréntesis con los argumentos correspondientes en el orden en que queremos que se transfieran,
separados por una coma, en este caso "sumar(3, 5)". Escribimos los argumentos como números para indicar que se
trata de números enteros (int) y así hacer que los tipos de datos sean compatibles, tal y como se especifica en
las anotaciones de tipo. 

De esta forma, estos valores serán transferidos y asignados a los parámetros "a" y "b", respectivamente, ya que
la función los recibe en el mismo orden en que se transfieren al ser argumentos posicionales. Además, asignamos
la llamada de la función a una variable llamada "resultado" para almacenar el valor devuelto por la función en
la variable en forma de número entero (int) tal y como se espera según la anotación de tipo "-> int:".
Colocamos esta línea de código sin indentación, ya que se encuentra en el nivel principal del código y no forma
parte de ninguna otra estructura.

Por último, imprimimos el resultado de la suma. Para ello, utilizamos la función "print()" en formato
"f-string" incluyendo la variable "resultado", la cual contiene el valor almacenado y devuelto por la función.
Esto nos permite mostrar el resultado de manera clara y legible en la consola. Colocamos esta línea de código
sin indentación, ya que se encuentra en el nivel principal del código y no forma parte de ninguna otra
estructura."""

# Código:
def sumar(a: int, b: int) -> int:
    return (a + b)

resultado = sumar(3, 5)
print(f"El resultado de la suma es: {resultado}")

# Nota Importante:
"""En este caso, la función "sumar()" tiene anotaciones de tipo que indican que ambos parámetros "a" y "b" 
deben ser enteros (int) y que la función devuelve un entero "-> int". En este caso, los argumentos pasados a la
función son ambos enteros (3 y 5), por lo que no hay discrepancias entre los tipos esperados y los tipos
reales.

Es importante recordar que las anotaciones de tipo en Python son solo informativas y no imponen restricciones
en tiempo de ejecución. Esto significa que, aunque se especifique que un parámetro debe ser de tipo (int),
Python permitirá pasar valores de otros tipos sin generar errores en tiempo de ejecución. Sin embargo,
herramientas de análisis estático, como "linters" o "IDEs", pueden advertir sobre discrepancias entre los tipos
especificados y los tipos reales, ayudando a identificar posibles errores antes de ejecutar el programa.

Por esta razón, aunque las anotaciones de tipo no son obligatorias ni estrictas, es recomendable seguirlas como
una guía para mantener la coherencia y evitar errores. Además, si se espera que los parámetros cumplan con
ciertos requisitos específicos, es buena práctica incluir validaciones explícitas dentro de la función para
garantizar que los datos sean correctos antes de realizar cualquier operación con ellos.

Por último, es importante recordar que las anotaciones de tipo no sustituyen las pruebas exhaustivas ni las
validaciones en tiempo de ejecución. Aunque proporcionan una guía clara sobre los tipos esperados, deben
considerarse como una herramienta complementaria dentro de un enfoque más amplio de desarrollo de software
robusto y confiable."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
