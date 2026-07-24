# Enunciado:
"""El retorno de valores en Python es una forma de devolver un resultado  desde  una  función.  Esto
significa que una función devuelve un valor específico después de completar su tarea o cálculo a  la
parte del programa desde donde fue  llamada.  Esto  se  logra  utilizando  la  instrucción  "return"
asociada a un valor o a una expresión dentro de  la  función.  Cuando  se  ejecuta  una  instrucción
"return", la función finaliza su ejecución y el valor especificado después de "return" se  envía  de
vuelta al lugar desde donde fue llamada.

Este mecanismo es fundamental para estructurar programas modulares y reutilizables, ya  que  permite
que las funciones realicen cálculos o procesamientos y luego envíen los resultados  a  otras  partes
del programa. Esto fomenta la separación de responsabilidades, ya que cada función  puede  enfocarse
en una tarea específica y devolver un resultado que puede ser utilizado por otras funciones o partes
del programa. Además, el uso de valores de retorno permite que las funciones sean  más  flexibles  y
adaptables, ya que pueden reutilizarse en diferentes contextos con distintas entradas.

El valor retornado puede almacenarse en una  variable,  utilizarse  directamente  en  expresiones  o
incluso pasarse como argumento a otras funciones. Python también permite  que  una  función  retorne
múltiples valores utilizando tuplas. Esto es especialmente útil cuando se necesita  devolver  varios
resultados relacionados en una sola llamada. Por ejemplo, se puede devolver el cociente y el residuo
de una división en una sola instrucción.

Además, el retorno de valores no se limita únicamente a  tipos  de  datos  simples  como  números  o
cadenas. Python permite devolver estructuras de datos  más  complejas,  como  listas,  diccionarios,
conjuntos  o  incluso  objetos  personalizados.  Esto  hace  que  las  funciones  sean  herramientas
extremadamente versátiles para encapsular lógica y manejar datos de manera eficiente.

Por último, es importante saber que, una vez que se ejecuta una  instrucción  "return",  la  función
finaliza su ejecución y no se ejecuta ningún código adicional dentro de ella. Si no se especifica un
valor de retorno, Python devuelve el valor nulo "None" de forma predeterminada. Esto significa  que,
incluso si una función no tiene un "return" explícito, siempre devolverá un valor, lo que  garantiza
consistencia en el comportamiento de las funciones. Este comportamiento predeterminado es útil  para
funciones que realizan acciones, pero no necesitan devolver un resultado  explícito,  como  las  que
imprimen mensajes en pantalla o modifican datos directamente."""

# Ejemplo_retorno_de_valores.py

# Explicación:
"""Definimos una función llamada "operacion()" que recibe tres parámetros: "a",  "b"  y  "c".  Estos
parámetros se utilizarán para realizar una operación aritmética y serán sustituidos por los  valores
que se pasen a la función al llamarla. Para ello, utilizamos la palabra  clave  "def",  seguida  del
nombre de la función, en este caso "operacion()", y de los parámetros "a", "b" y "c", separados  por
comas entre paréntesis (). Terminamos con dos puntos (:) para indicar el inicio del bloque de código
asociado a la función.

Dentro de la función definimos dos variables locales: "suma" y "resta".  A  la  variable  "suma"  le
asignamos el resultado de la suma de los tres parámetros (a + b + c), utilizando el operador de suma
(+) y encerrando la operación entre paréntesis. A la variable "resta" le asignamos el  resultado  de
la resta de los tres parámetros (a - b - c), utilizando el operador de resta  (-)  y  encerrando  la
operación  entre  paréntesis.  Estas  variables  solo  existen  dentro  del  ámbito  de  la  función
"operacion()" y no pueden ser accedidas desde fuera de ella. Colocamos ambas líneas  de  código  con
una indentación de cuatro espacios desde el margen izquierdo  para  indicar  que  forman  parte  del
bloque de código asociado a la función y deben ejecutarse siempre que la función sea llamada.

A continuación, utilizamos la instrucción "return" para devolver  los  valores  de  las  operaciones
almacenados en las variables "suma" y "resta" en forma de tupla. La instrucción "return"  indica  al
intérprete que la función debe finalizar su ejecución y enviar los valores especificados  de  vuelta
al lugar desde donde fue llamada. Para ello, escribimos la palabra clave  "return"  seguida  de  los
nombres de las variables "suma" y "resta", separados por una coma y encerrados entre paréntesis.  En
este caso, estamos devolviendo ambos resultados en una sola instrucción en forma de tupla.  De  esta
forma, retornamos múltiples valores relacionados en una sola llamada. Colocamos esta línea de código
con la misma indentación que las anteriores para indicar  que  forma  parte  del  bloque  de  código
asociado a la función y debe ejecutarse siempre que la función sea llamada.

Luego, llamamos a la función "operacion()" con los argumentos correspondientes,  en  este  caso  los
valores 10, 5 y 2, para ejecutar el código asociado dentro  de  ella.  Para  llamar  a  la  función,
simplemente escribimos su nombre seguido de paréntesis con los  argumentos  correspondientes  en  el
orden en que deben transferirse, separados por comas, en este caso "operacion(10, 5, 2)". Escribimos
los argumentos como números para indicar que se trata de números enteros (int)  y,  de  esta  forma,
trabajar con tipos de datos compatibles.

Así, estos valores serán transferidos y asignados a los parámetros "a", "b" y  "c"  respectivamente,
ya que la función los recibe en el mismo orden en que son pasados. Además, asignamos la  llamada  de
la función a una variable llamada "resultado" para almacenar los valores devueltos por la función en
forma de tupla. Colocamos esta línea de código sin indentación, ya que  se  encuentra  en  el  nivel
principal del código y no forma parte de ninguna otra estructura.

Por último, utilizamos la función "print()" para mostrar en consola los resultados de la suma  y  la
resta. Dentro  de  la  función  "print()",  pasamos  un  mensaje  explicativo  junto  con  el  valor
correspondiente de la tupla devuelta por la función "operacion()". Para  acceder  a  estos  valores,
usamos el operador de indexación ([]) precedido por el nombre de la variable "resultado".  Dado  que
estamos trabajando con una tupla de dos  elementos,  utilizamos  los  índices  para  acceder  a  las
posiciones correspondientes: "resultado[0]" para obtener el resultado de la  suma  y  "resultado[1]"
para obtener el resultado de la resta.

De esta forma, mostramos en consola los mensajes seguidos del valor correspondiente, lo que  permite
ver claramente los resultados de las operaciones realizadas dentro de la  función.  Colocamos  estas
líneas de código sin indentación, ya que se encuentran en el nivel principal del código y no  forman
parte de ninguna otra estructura."""

# Código:
def operacion(a, b, c):
    suma = (a + b + c)
    resta = (a - b - c)
    return (suma, resta)

resultado = operacion(10, 5, 2)

print("El resultado de la suma es:", resultado[0])
print("El resultado de la resta es:", resultado[1])

# Nota Muy Importante:
"""Es posible usar "return" para devolver cualquier tipo de valor, no  solo  números  o  cadenas  de
texto, sino también listas, diccionarios, objetos personalizados, entre otros.  Esto  significa  que
las funciones en Python  son  extremadamente  versátiles,  ya  que  pueden  adaptarse  a  diferentes
necesidades y escenarios. Además, una función puede devolver múltiples valores utilizando tuplas, lo
que resulta útil para retornar varios resultados relacionados en una sola llamada. Por  ejemplo,  se
puede devolver tanto el resultado  de  una  operación  como  un  mensaje  explicativo  en  una  sola
instrucción.

Cuando  utilizamos  la  instrucción  "return"  con  más  de  un  valor,  el   intérprete   empaqueta
automáticamente esos valores en una tupla, independientemente de  si  usamos  o  no  paréntesis.  Es
importante tener esto en cuenta al momento de recibir esos valores en la parte del código  donde  se
llama a la función, ya que las tuplas son inmutables y deben ser manejadas como tal.  Para  un  solo
valor devuelto, el tipo de dato será el del valor retornado. Para múltiples valores, el tipo de dato
será "tuple" ya que Python devuelve una tupla automáticamente cuando se retornan múltiples  valores.
Sin embargo, si se necesita modificar los valores devueltos, se pueden convertir a  otros  tipos  de
datos mutables utilizando el constructor correspondiente.

Además, en los valores devueltos, podemos realizar cualquier tipo de operación o  cálculo  antes  de
retornarlos usando cualquier  tipo  de  operador  o  función  disponible  en  Python.  Esto  permite
encapsular la lógica dentro de las funciones, haciendo que el código sea más limpio, legible y fácil
de mantener. Además, los valores devueltos pueden  ser  utilizados  directamente  en  expresiones  o
almacenados en variables para su uso posterior, lo que fomenta la modularidad y la reutilización del
código.

Para almacenar el resultado devuelto por "return", simplemente llamamos a la función y asignamos  la
llamada a  una  variable.  Si  la  función  devuelve  múltiples  valores,  podemos  desempaquetarlos
directamente en varias variables utilizando la sintaxis de desempaquetado. Esto facilita el acceso a
cada valor individualmente y mejora la legibilidad del código.  El  concepto  de  desempaquetado  de
tuplas se abordará en detalle en secciones posteriores.

En el caso de definir variables dentro de una función, estas se consideran locales a la función y no
pueden ser accedidas desde fuera de ella. Esto asegura que el estado  interno  de  la  función  esté
aislado del resto del programa, lo que reduce el riesgo de errores y  facilita  la  depuración.  Sin
embargo, si se necesita compartir datos entre funciones, se pueden  usar  valores  de  retorno  para
pasar información de una función a otra.

Por último, es importante destacar que una vez que se ejecuta una instrucción "return",  la  función
finaliza su ejecución y no se ejecuta ningún código adicional dentro de  ella.  Esto  significa  que
cualquier código después de "return" dentro de la función será ignorado. Además, si no se especifica
un valor de retorno, Python devuelve "None" de forma predeterminada, lo que puede  ser  útil  cuando
una  función  solo  necesita  realizar  una  acción  sin  devolver  un  resultado  específico.  Este
comportamiento permite que las funciones sean utilizadas de manera flexible en una  amplia  variedad
de contextos."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
