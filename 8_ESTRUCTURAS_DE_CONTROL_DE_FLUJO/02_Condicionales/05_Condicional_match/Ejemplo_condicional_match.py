# Enunciado:
"""El condicional "match" en Python es una estructura de control de flujo basada en la  coincidencia
de patrones ("pattern matching"). Permite realizar comparaciones estructurales  de  manera  clara  y
concisa.

Evalúa una expresión y ejecuta el bloque de código del primer patrón  que  coincide.  Los  casos  se
evalúan en el orden en que aparecen, y solo se ejecuta el bloque de código asociado al  primer  caso
coincidente. El caso comodín "case _:" actúa como un "default" para manejar situaciones en  las  que
no hay coincidencias.

El condicional "match" admite patrones avanzados como la desestructuración de datos, la  captura  de
valores y el uso de comodines. La desestructuración de datos permite separar  estructuras  complejas
en sus componentes, la captura de valores extrae partes de estas para usarlas más  adelante,  y  los
comodines como el guion bajo "case _:" coinciden con cualquier  valor  no  contemplado,  permitiendo
manejar casos por defecto.

Además, resulta ideal para trabajar con estructuras de datos como listas, tuplas y diccionarios. Sin
embargo, los patrones deben ser valores literales, variables o estructuras válidas según las  reglas
de coincidencia de patrones.

En este ejemplo, usamos por primera vez la  función  "input()",  que  permite  al  usuario  ingresar
información a través del teclado durante la ejecución del programa. La función "input()" muestra  un
mensaje o "prompt" en la consola para indicar al usuario qué  tipo  de  información  se  espera  que
ingrese. Una vez que el usuario ingresa la  información  y  presiona  la  tecla  "Enter",  el  valor
ingresado se guarda en una variable para su posterior uso en el código.

Por último, es importante saber que la función "input()" devuelve el valor ingresado como una cadena
de texto (str). Si se necesita otro tipo de dato (como un número entero o  un  número  decimal),  se
debe convertir explícitamente utilizando constructores como "int()" o "float()". De lo contrario, el
valor se tratará como una cadena de texto en el resto del código."""

# Ejemplo_condicional_match.py

# Explicación:
"""Definimos una variable llamada "lista_lenguajes" y le  asignamos  una  lista  con  una  serie  de
lenguajes de programación como elementos en forma de texto  (str)  y  separados  por  comas.  Luego,
usamos la función "print()" para imprimir el valor de la variable "lista_lenguajes"  en  la  consola
junto con un mensaje descriptivo. Esto permite que el usuario vea las opciones disponibles  y  elija
una de ellas.

Utilizamos la función "input()" para solicitar  al  usuario  que  elija  uno  de  los  lenguajes  de
programación de la lista. Para ello, definimos una variable llamada "opcion_usuario", escribimos  la
función "input()" seguida de paréntesis y dentro de estos incluimos un mensaje o "prompt", el  cual,
al ejecutar el código, se mostrará en la consola indicando al usuario qué  tipo  de  información  se
espera  que  ingrese.  De  esta  forma,  lo  que  el  usuario  ingrese  se  guarda  en  la  variable
"opcion_usuario" como una cadena de texto (str) y podremos usarlo en el resto del código.

Luego, utilizamos un bloque "match" para comparar si el valor ingresado por el usuario coincide  con
alguno de los casos para así ejecutar el bloque de código asociado al caso coincidente.  Para  ello,
escribimos la palabra clave "match" seguida de la variable  "opcion_usuario"  y  terminada  con  dos
puntos (:). Esto indica que el bloque "match" se asociará a la variable  "opcion_usuario",  la  cual
contiene el valor ingresado por el usuario.

Por último, utilizamos la palabra clave "case" para definir la lista de casos  posibles  dentro  del
bloque "match". Para ello, escribimos la palabra clave "case" con  una  indentación  de  4  espacios
desde el margen izquierdo, seguida del valor que queremos comparar y dos puntos (:). El  valor  debe
estar escrito tal y como  esperamos  que  sea  ingresado  por  el  usuario  y  coincidiendo  con  la
información proporcionada al usuario en la lista de lenguajes. Añadimos un caso para  cada  lenguaje
de programación en la lista y para el caso comodín, escribimos la palabra clave "case" seguida de un
guion bajo (_) y dos puntos (:) y lo colocamos al final de la lista de casos posibles.

Cada caso representa un lenguaje de programación específico de la lista proporcionada al usuario. Si
la opción del usuario coincide con uno de estos casos, se ejecuta el bloque de código asociado a ese
caso, el cual colocamos justo debajo de la palabra clave "case" y con una indentación de 4  espacios
desde la propia palabra clave "case".

El bloque de código asociado a cada caso es una acción o conjunto de acciones  que  se  ejecutan  en
respuesta a la opción seleccionada por el usuario, que en este ejemplo es una instrucción  "print()"
que proporciona una breve descripción sobre el lenguaje seleccionado.

Además, si la opción ingresada por el usuario no coincide con ninguno de  los  casos  definidos,  se
ejecuta el bloque de código asociado al caso comodín "case  _:",  que  actúa  como  un  "default"  y
muestra un mensaje indicando que el lenguaje no es reconocido."""

# Código:
lista_lenguajes = ["python", "javascript","java", "c++", "ruby", "go", "swift"]
print("Lista de lenguajes de programación disponibles:", lista_lenguajes)

opcion_usuario = input("Elige uno de los lenguajes de programación de la lista: ")

match opcion_usuario:
    case "python":
        print("Python es un lenguaje de programación interpretado, de alto nivel y con una sintaxis sencilla y legible.")
    case "javascript":
        print("JavaScript es un lenguaje de programación interpretado, orientado a objetos y basado en prototipos.")
    case "java":
        print("Java es un lenguaje de programación compilado, orientado a objetos y basado en clases.")
    case "c++":
        print("C++ es un lenguaje de programación compilado, de alto rendimiento y orientado a objetos.")
    case "ruby":
        print("Ruby es un lenguaje de programación interpretado, de alto nivel y con una sintaxis sencilla y legible.")
    case "go":
        print("Go es un lenguaje de programación compilado, de alto rendimiento y con soporte para concurrencia.")
    case "swift":
        print("Swift es un lenguaje de programación compilado, de alto rendimiento y con una sintaxis sencilla y legible.")
    case _:
        print("El lenguaje no es reconocido.")

# Nota Muy Importante:
"""El condicional "match" evalúa una expresión y compara su resultado con los patrones definidos  en
los casos. Si el usuario elige una opción que no está en la lista de casos, se ejecutará  el  bloque
de código asociado al comodín "case _:".

En cuanto a la expresión asociada al bloque "match", esta debe ser una variable o una expresión  que
devuelva un valor. No es posible asociar un valor literal directamente al bloque "match",  como  por
ejemplo: match "python". Esto se debe a que el condicional "match" evalúa  una  expresión  y  no  un
valor fijo. Para evaluar un valor fijo, se debe usar una variable que contenga dicho  valor,  aunque
esta opción no es práctica ni común.

En cuanto a los casos dentro del bloque "match", cada caso representa un patrón que se  compara  con
el valor de la expresión asociada al bloque "match", que comúnmente es una variable que almacena una
entrada del usuario.

Los patrones en los casos deben ser valores literales, variables o  estructuras  válidas  según  las
reglas de coincidencia de patrones, aunque se recomienda que estos sean siempre  valores  literales,
ya que los casos están diseñados para comparar con valores específicos o patrones simples. Cuando se
intenta asociar una variable que contiene varios elementos a un caso, como una lista, una tupla o un
diccionario, Python no lo interpreta como una comparación con cada elemento presente, sino como  una
comparación con la estructura completa en cuestión.

Sin embargo, si se desea evaluar si un valor introducido por el  usuario  pertenece  a  un  conjunto
definido internamente, se debe usar un condicional "if" dentro del caso comodín "case _:". Dentro de
este caso, se pueden usar estructuras condicionales como "if...elif...else" para manejar situaciones
más específicas y complejas, como verificar si el valor ingresado por el usuario  está  presente  en
una lista, tupla o diccionario, cosa que veremos en el ejercicio correspondiente a esta sección.

Además, solo puede haber un caso comodín por bloque "match". Este debe  colocarse  al  final  de  la
lista de casos posibles, y los condicionales "if...elif...else" se deben asociar a este caso y no  a
otros casos específicos dentro del bloque "match". Es posible incluir todos los casos que se  deseen
dentro de un bloque "match" y tener múltiples bloques "match" en un mismo programa, pero cada bloque
debe tener su propio caso comodín "case _:" si se desea  manejar  situaciones  en  las  que  no  hay
coincidencias.

Por último, en cuanto a la conversión de tipos de datos, es fundamental asegurarse de que el tipo de
dato del valor ingresado por el usuario o los valores contenidos en el conjunto, ya sea lista, tupla
o diccionario, coincida con el tipo de dato esperado  en  el  bloque  "match",  ya  que  la  función
"input()" devuelve siempre una cadena de texto (str) y los datos contenidos tienen su propio tipo de
dato.

Esto es especialmente importante cuando se trabaja con números. Si se necesita trabajar con números,
es necesario convertir explícitamente la entrada o cada valor del conjunto usando los  constructores
"int()"  o  "float()".  Esto  asegura  que  las  comparaciones  en  el  bloque   "match"   funcionen
correctamente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
