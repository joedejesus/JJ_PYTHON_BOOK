# Enunciado:
"""Los parámetros con valores predeterminados en Python son aquellos que se definen con un valor inicial en la 
definición de la función. Esto significa que, si no se proporciona un argumento correspondiente al parámetro al
llamar a la función, se utilizará el valor predeterminado especificado en su definición. Esto es útil para
proporcionar flexibilidad en las funciones, permitiendo que sean llamadas con menos argumentos de los que
normalmente requerirían, especialmente cuando ciertos parámetros tienen valores comunes o esperados que no
necesitan ser especificados explícitamente en cada llamada.

Es importante tener en cuenta que, si se combinan parámetros con valores predeterminados con parámetros
obligatorios, los parámetros con valores predeterminados deben declararse después de los parámetros
obligatorios en la definición de la función. Esto se debe a que Python evalúa los argumentos en el orden en que
se definen al llamar a la función, asignándolos respectivamente a los parámetros definidos en la función de
izquierda a derecha. Los parámetros obligatorios no pueden seguir a los opcionales, ya que esto generaría un
error de sintaxis. Los parámetros obligatorios son aquellos que no tienen un valor predeterminado y requieren
un argumento al llamar a la función, mientras que los parámetros opcionales tienen un valor predeterminado que
puede ser omitido o sobrescrito al llamar a la función.

Los parámetros con valores predeterminados son posicionales en cuanto al orden en que se definen en la función,
y los argumentos que se les asignan deben coincidir con ese orden si se utilizan argumentos posicionales al
llamar a la función. Sin embargo, si se utilizan argumentos nombrados al llamar a la función, se puede
especificar explícitamente a qué parámetro corresponde cada valor, sin necesidad de respetar el orden de los
parámetros en la definición. Esto proporciona una mayor flexibilidad y claridad en las llamadas a funciones,
especialmente cuando se trabaja con funciones que tienen muchos parámetros o cuando se desea sobrescribir solo
algunos de los valores predeterminados. Es importante tener en cuenta que, al usar argumentos nombrados, se
debe especificar el nombre exacto del parámetro tal como está definido en la función.

Además, el orden de los parámetros en la definición de una función es crucial para evitar errores y garantizar
que los valores predeterminados se utilicen de manera adecuada. Respetar esta regla no solo evita problemas de
sintaxis, sino que también mejora la legibilidad y la consistencia del código. Además, el tipo de dato de los
argumentos pasados debe ser compatible con el valor predeterminado de los parámetros con valores
predeterminados y con el uso que se les da dentro de la función. Por ejemplo, si un parámetro tiene un valor
predeterminado de tipo (str), como "Hola", pero dentro de la función se intenta realizar una operación
matemática con él, se producirá un error si se pasa un argumento incompatible. Sin embargo, Python no impone
restricciones estrictas sobre los tipos de datos de los argumentos, por lo que es responsabilidad del
programador asegurarse de que los tipos de datos sean compatibles para evitar errores en tiempo de ejecución.

Si se llama a la función sin argumentos, se usarán los valores predeterminados. Además, cualquier argumento
omitido en la llamada a la función será reemplazado por su valor predeterminado, respetando la posición de los
parámetros. Esto permite una gran flexibilidad al usar funciones, ya que se pueden manejar tanto casos simples
como complejos sin necesidad de definir múltiples versiones de la misma función. Si se desea evitar el
requisito de respetar el orden de los parámetros, se pueden usar argumentos nombrados al llamar a la función,
lo que permite especificar explícitamente a qué parámetro corresponde cada valor. Esto hace que las llamadas
sean más claras y menos propensas a errores, especialmente en funciones con muchos parámetros.

Por último, los parámetros con valores predeterminados son una herramienta poderosa para simplificar las
llamadas a funciones y hacer que el código sea más legible y flexible. Su uso adecuado puede reducir la
cantidad de código necesario, mejorar la claridad al proporcionar valores por defecto para los casos más
comunes y facilitar la escritura de funciones más versátiles y robustas. Además, permiten que las funciones
sean más intuitivas y fáciles de usar, ya que los valores predeterminados actúan como una guía para los
usuarios sobre los casos de uso más frecuentes."""

# Ejemplo_parametros_con_valores_predeterminados.py

# Explicación:
"""Definimos una función llamada "saludar()" que recibe tres parámetros con valores predeterminados, los cuales 
son: "saludo", "nombre" y "vives_en". A cada uno de estos parámetros se le asigna un valor predeterminado que
se utilizará si no se proporciona un argumento correspondiente al llamar a la función, o bien podrá ser
sobrescrito por los valores que se le pasen a la función al llamarla. Para ello, utilizamos la palabra clave
"def" seguida del nombre de la función, en este caso "saludar()", seguida del nombre de los parámetros entre
paréntesis, separados por una coma, y terminamos con dos puntos (:) para indicar el inicio del bloque de código
asociado a la función. A cada uno de los parámetros le asignamos un valor predeterminado en su formato
correspondiente usando el operador de asignación (=), en este caso cadenas de texto (str) entre comillas
dobles. En este caso, el parámetro "saludo" tiene el valor predeterminado "hola", el parámetro "nombre" tiene
el valor predeterminado "usuario" y el parámetro "vives_en" tiene el valor predeterminado "desconocido".

A continuación, dentro de la función, utilizamos la instrucción "print()" para mostrar un mensaje en la consola
en formato "f-string", el cual incluye los nombres de los parámetros "saludo", "nombre" y "vives_en" dentro del
mensaje de saludo. Estos parámetros serán sustituidos por los argumentos pasados al llamar a la función, los
cuales serán de nuestra elección, a no ser que no se pasen argumentos, en cuyo caso se usarán los valores
predeterminados definidos en la función para personalizar el mensaje. Colocamos esta instrucción con una
indentación de cuatro espacios desde el margen izquierdo para indicar que forma parte del cuerpo de la función
y debe ejecutarse siempre que la función sea llamada.

Realizamos varias llamadas a la función "saludar()" para ilustrar cómo funcionan los parámetros con valores
predeterminados y cómo se pueden sobrescribir al pasar argumentos al llamar a la función. De esta forma,
ejecutamos el código asociado a la función con diferentes combinaciones de argumentos y observamos los
resultados en la consola.

En la primera llamada a la función "saludar()", no se pasan argumentos, por lo que se utilizan los valores
predeterminados de los parámetros definidos en la función. Esto significa que el mensaje que se mostrará será
"hola, usuario que vives en desconocido.", ya que "saludo" toma el valor "hola", "nombre" toma el valor
"usuario" y "vives_en" toma el valor "desconocido". Esta llamada demuestra cómo los valores predeterminados
permiten que la función sea ejecutada sin necesidad de proporcionar argumentos explícitos. La llamada a la
función se realiza simplemente escribiendo su nombre seguido de paréntesis vacíos, lo que indica que no se
están pasando argumentos.

En la segunda llamada, se pasa un único argumento, "buenos días", que corresponde al primer parámetro "saludo".
Los otros dos parámetros, "nombre" y "vives_en", mantienen sus valores predeterminados, por lo que el mensaje
que se mostrará será "buenos días, usuario que vives en desconocido.". Esto ilustra cómo se pueden sobrescribir
los valores predeterminados de los parámetros de izquierda a derecha, respetando el orden en que están
definidos. La llamada a la función se realiza escribiendo su nombre seguido del argumento en forma de cadena de
texto (str) entre paréntesis.

En la tercera llamada, se pasan dos argumentos: "buenos días" y "Ana". El primer argumento sobrescribe el valor
predeterminado de "saludo", mientras que el segundo sobrescribe el valor predeterminado de "nombre". El
parámetro "vives_en" conserva su valor predeterminado, "desconocido". Por lo tanto, el mensaje que se mostrará
será "buenos días, Ana que vives en desconocido." Esto muestra cómo se pueden sobrescribir múltiples valores
predeterminados al proporcionar argumentos adicionales de izquierda a derecha, respetando el orden en que están
definidos. La llamada a la función se realiza escribiendo su nombre seguido de los dos argumentos en forma de
cadenas de texto (str) separados por una coma y entre paréntesis.

En la cuarta y última llamada, se proporcionan tres argumentos: "buenos días", "Ana" y "Asturias". Cada uno de
estos argumentos sobrescribe el valor predeterminado correspondiente a su posición de izquierda a derecha:
"saludo" toma el valor "buenos días", "nombre" toma el valor "Ana" y "vives_en" toma el valor "Asturias". El
mensaje que se mostrará será "buenos días, Ana que vives en Asturias.". Esta llamada demuestra cómo se pueden
sobrescribir todos los valores predeterminados al proporcionar argumentos para cada parámetro de la función. La
llamada a la función se realiza escribiendo su nombre seguido de los tres argumentos en forma de cadenas de
texto (str) separados por comas y entre paréntesis.

Colocamos todas las llamadas a la función sin indentación para indicar que no forman parte de ninguna otra
estructura y se ejecutan de forma independiente.

Por último, cabe añadir que la sustitución de los valores predeterminados de los parámetros por los argumentos
pasados se realiza en el orden en que se definen los parámetros en la función y, a su vez, en el orden en que
se definen los argumentos al llamar a la función, de izquierda a derecha. Si no se proporciona un argumento
para un parámetro con valor predeterminado, se utiliza el valor predeterminado definido en la función. Si se
proporciona un argumento, este sobrescribe el valor predeterminado del parámetro correspondiente. Con el uso de
estos argumentos "posicionales" es imposible sustituir solo el valor del segundo parámetro sin sustituir el
primero, o el tercero sin sustituir el primero y el segundo, y asimismo para los demás parámetros, a no ser que
se usen argumentos nombrados al llamar a la función."""

# Código:
def saludar(saludo="hola", nombre="usuario", vives_en="desconocido"):
    print(f"{saludo}, {nombre} que vives en {vives_en}.")

saludar()
saludar("buenos días")
saludar("buenos días", "Ana")
saludar("buenos días", "Ana", "Asturias")

# Nota Muy Importante:
"""Si se combinan parámetros con valores predeterminados "opcionales" y parámetros sin valores predeterminados 
"obligatorios" en la definición de una función, los argumentos correspondientes a los parámetros sin valores
predeterminados deben ser proporcionados obligatoriamente y primero que los argumentos correspondientes a los
parámetros con valores predeterminados. Esto se debe a que Python evalúa los argumentos en el orden en que se
definen, y los parámetros obligatorios (aquellos sin valores predeterminados) deben ser asignados antes de los
opcionales. Si se colocaran parámetros obligatorios después de los opcionales, el intérprete no podría
determinar qué valores corresponden a cada parámetro, lo que generaría un error de sintaxis.        

Cuando hablamos de "obligatorios" u "opcionales", nos referimos a si un parámetro tiene o no un valor
predeterminado. Si no tiene un valor predeterminado, es obligatorio pasarle un argumento como valor; por eso lo
llamamos "obligatorio". Y si lo tiene, es opcional pasarle un argumento como valor, ya que, si no se le pasa un
argumento se usará el valor predeterminado, por eso lo llamamos "opcional".

Adicionalmente, una vez que los argumentos son transferidos a los parámetros de la función, no hay diferencia
entre parámetros con valores predeterminados y sin valores predeterminados. Ambos tipos de parámetros se
comportan de la misma manera dentro de la función, y se pueden usar indistintamente. La única diferencia radica
en cómo se definen y cómo se asignan los argumentos al llamar a la función. Lo importante es saber el valor
almacenado en el parámetro en un momento dado, independientemente de si ese valor proviene de un argumento
pasado o del valor predeterminado definido en la función.

Por último, es importante saber que este método tiene sus limitaciones, ya que los parámetros con valores
predeterminados siguen siendo posicionales en cuanto a su orden y cómo reciben los argumentos. Por ejemplo, si
se desea omitir el segundo parámetro no se podría, ya que el tercer parámetro pasaría a ser el segundo y se
perdería el valor predeterminado del segundo parámetro. Es por ello muy importante saber cuándo usar parámetros
con valores predeterminados y cuándo usar argumentos nombrados para evitar estos problemas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
