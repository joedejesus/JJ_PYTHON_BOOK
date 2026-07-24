# Enunciado:
"""Una función anónima o lambda en Python es una función que no  tiene  un  nombre  explícito  y  se
define en una sola línea utilizando la palabra clave "lambda". Estas funciones son útiles cuando  se
necesita una función simple y pequeña para una tarea específica, especialmente  en  casos  donde  la
función será utilizada como argumento de otra función o en operaciones con  las  funciones  "map()",
"filter()" o "reduce()", esta última importando el módulo "functools". A diferencia de las funciones
definidas con "def", las funciones lambda no requieren un nombre ni un bloque de código, lo que  las
hace ideales para operaciones rápidas y de corta duración. Sin embargo, tienen limitaciones, como la
imposibilidad de incluir múltiples expresiones o instrucciones complejas dentro de su cuerpo.

La sintaxis básica de una función lambda es: "variable  =  lambda  parámetros:  (expresión)",  donde
"variable" es el nombre que se le asigna a la función lambda para poder reutilizarla posteriormente,
"lambda" es la palabra clave que indica que se está definiendo una función anónima, "parámetros" son
uno o varios parámetros separados por comas y "(expresión)" es la operación que  se  desea  realizar
con esos parámetros. Los paréntesis son opcionales y solo se usan  aquí  para  dejar  más  clara  la
expresión, que se evalúa y se devuelve como resultado de la función lambda.

El número de parámetros que puede recibir una función lambda es ilimitado, siempre y  cuando  en  la
expresión se utilicen de forma correcta y en  la  llamada  se  le  pasen  el  número  de  argumentos
correspondiente a los parámetros definidos. En cuanto a la expresión, esta puede  incluir  cualquier
operación que combine los parámetros,  como  operaciones  matemáticas,  manipulación  de  cadenas  o
cualquier tarea que requiera una función simple y rápida. Por ejemplo, se puede definir una  función
lambda que reciba dos parámetros y devuelva su  suma,  o  una  que  combine  un  parámetro  con  una
operación aritmética en forma literal, o incluso una función lambda que manipule  cadenas  de  texto
para formatearlas de una manera específica.

Además, es preciso definir una variable  para  almacenar  la  función  lambda,  lo  que  permite  su
reutilización en diferentes partes del código, además de poder  llamarla  posteriormente  o  pasarla
como argumento a otras funciones de orden superior, ya sea  de  forma  literal  con  los  argumentos
correspondientes o utilizando la variable que la almacena.  Las  funciones  de  orden  superior  son
aquellas que pueden recibir otras funciones como argumentos o devolver funciones como  resultado  de
su ejecución. Las funciones lambda son especialmente  útiles  en  este  contexto,  ya  que  permiten
definir funciones de manera concisa y pasarlas como argumentos a otras funciones.

Por último,  las  funciones  lambda  se  pueden  utilizar  para  realizar  operaciones  matemáticas,
manipulación de datos o cualquier tarea que  requiera  una  función  simple  y  rápida.  Aunque  son
poderosas, es importante recordar que su uso debe ser  limitado  a  casos  donde  la  simplicidad  y
brevedad sean esenciales, ya que para tareas  más  complejas,  las  funciones  definidas  con  "def"
ofrecen mayor claridad y flexibilidad.

Estas funciones son herramientas prácticas para resolver problemas específicos de manera  eficiente,
siempre que se comprendan sus limitaciones y se utilicen en el contexto adecuado.  Su  uso  adecuado
puede mejorar significativamente la legibilidad  y  eficiencia  del  código,  pero  su  abuso  puede
resultar en un código menos mantenible y más propenso a errores."""

# Ejemplo_funciones_anonimas_o_lambda.py

# Explicación:
"""Definimos una variable llamada "area_circulo" y le asignamos una función lambda  que  recibe  dos
parámetros, "pi" y "radio", y devuelve el área del círculo utilizando la fórmula "area = pi *  radio
** 2". Estos parámetros serán sustituidos por los argumentos que se le pasen  a  la  función  lambda
cuando sea llamada. Para ello utilizamos  la  palabra  clave  "lambda"  seguida  de  los  parámetros
separados por comas "pi, radio", seguida de dos puntos (:) para indicar el inicio de la expresión y,
por último, la expresión entre  paréntesis  que  define  la  operación  a  realizar.  En  este  caso
utilizamos paréntesis para hacer más claro el orden de las operaciones.

En este caso, la expresión es: (pi * (radio ** 2)). Utilizamos el valor "2"  en  la  expresión  para
elevar el radio al cuadrado, lo que indica que se realizará una operación de potencia para  calcular
el área del círculo. Esto demuestra cómo podemos combinar los parámetros con operaciones  o  valores
en la expresión de la  función  lambda  para  realizar  cálculos  específicos  de  manera  rápida  y
eficiente.

Luego definimos una variable llamada "resultado" que almacena el resultado de llamar  a  la  función
lambda "area_ circulo()" con los argumentos 3.14 y 5. Para ello, simplemente llamamos a  la  función
"area_circulo()" con los argumentos 3.14 y 5 entre paréntesis en el orden correspondiente, ya que el
orden de los argumentos debe coincidir con el orden de los parámetros definidos en la función lambda
"area_circulo". En este caso, el primer argumento "3.14" se asigna al parámetro "pi"  y  el  segundo
argumento "5" se asigna al parámetro "radio". Estos corresponden a la constante pi y  al  radio  del
círculo, respectivamente, lo que ejecuta la función lambda y devuelve el resultado del  cálculo  del
área, que se almacena en la variable "resultado". Por último, mostramos el resultado  utilizando  la
función "print()", acompañada de un mensaje descriptivo en formato "f-string"  junto  con  el  valor
calculado.

En este caso utilizamos el valor de pi como 3.14, pero es importante destacar que en Python  también
se puede utilizar la constante "math.pi" del módulo "math" para obtener un valor más preciso de  pi,
lo que puede ser especialmente útil en cálculos científicos o  matemáticos  donde  se  requiere  una
mayor precisión. Además, utilizamos el valor del radio como 5, pero  este  valor  puede  modificarse
para calcular el área  de  círculos  con  diferentes  radios,  simplemente  cambiando  el  argumento
correspondiente al llamar a la función lambda.

Además, la operación de potencia se realiza antes que la multiplicación, de acuerdo con  las  reglas
de precedencia de las operaciones matemáticas. Esto es crucial para obtener  el  resultado  correcto
del área del círculo, ya que la fórmula requiere  que  el  radio  se  eleve  al  cuadrado  antes  de
multiplicarlo por "pi"."""

# Código:
area_circulo = lambda pi, radio: (pi * (radio ** 2))
resultado = area_circulo(3.14, 5)
print(f"El área del círculo es: {resultado}")

# Nota Importante:
"""Las funciones lambda son una herramienta poderosa  en  Python,  pero  su  uso  debe  considerarse
cuidadosamente. Aunque son ideales para tareas simples y rápidas, su abuso puede llevar a un  código
menos legible y más difícil de  mantener.  Es  recomendable  utilizarlas  en  situaciones  donde  su
brevedad y simplicidad aporten claridad al código, como en operaciones con listas, diccionarios o al
trabajar con funciones de orden superior. Sin  embargo,  para  tareas  más  complejas  o  cuando  se
requiere documentación detallada, es preferible optar por funciones definidas con "def".

Además, es importante tener en  cuenta  que  las  funciones  lambda  no  pueden  contener  múltiples
expresiones ni definiciones, lo que limita su capacidad  para  manejar  lógica  compleja.  Por  esta
razón, su uso debe estar siempre alineado con las mejores prácticas de programación, priorizando  la
legibilidad y mantenibilidad del código. En proyectos colaborativos, el uso  excesivo  de  funciones
lambda puede generar confusión, especialmente si no se documentan adecuadamente o si su propósito no
es evidente a simple vista.

Por último, aunque las funciones lambda son una excelente herramienta para escribir código  compacto
y eficiente, es fundamental recordar que la claridad del código siempre debe ser una  prioridad.  En
situaciones donde la función lambda pueda ser reemplazada por una función definida con "def" que sea
más descriptiva y fácil de seguir, es preferible optar por esta última. De esta manera, se garantiza
que el código sea comprensible y mantenible a largo plazo incluso para  otras  personas  que  puedan
trabajar en el proyecto en el futuro."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
