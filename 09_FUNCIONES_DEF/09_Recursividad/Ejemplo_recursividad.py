# Enunciado:
"""La recursividad en Python es una técnica de programación que se basa en la llamada de una función
desde dentro de sí misma. Esto permite que una función se ejecute repetidamente hasta que se  cumpla
una condición de parada. La recursividad es una herramienta poderosa que permite resolver  problemas
dividiéndolos en subproblemas más pequeños  y  manejables,  siguiendo  el  principio  de  "divide  y
vencerás". Cada llamada recursiva trabaja con una versión  reducida  del  problema  original,  y  el
proceso continúa hasta alcanzar un caso base, que es la condición que  detiene  la  recursión.  Esta
técnica  es  especialmente  útil  en  problemas  jerárquicos  o  repetitivos,  como  el  cálculo  de
factoriales, la generación de secuencias de Fibonacci y la búsqueda en  estructuras  de  datos  como
árboles. 

El caso base es fundamental para evitar que la recursión se convierta en un bucle infinito.  Sin  un
caso  base  definido,  la  función  seguirá  llamándose  indefinidamente,  lo   que   provocará   un
desbordamiento de la pila de llamadas (stack overflow). Por lo tanto, es crucial asegurarse  de  que
el caso base esté correctamente definido y de que las llamadas recursivas reduzcan el problema hacia
ese caso base. Además, cada llamada recursiva consume memoria en la pila de ejecución, por lo que la
recursividad debe usarse con precaución en  problemas  con  entradas  muy  grandes.  En  Python,  la
recursividad no cuenta con optimización de  "recursión  de  cola",  lo  que  aumenta  el  riesgo  de
desbordamiento si el número de llamadas es excesivo.

Un factorial es el producto de todos los números enteros positivos desde 1 hasta un número dado "n",
denotado como "n!". El factorial de 0 se define como 1  por  convención.  La  fórmula  general  para
calcular el factorial es: n! = n * (n-1) * (n-2) *... * 1. De forma recursiva, esta fórmula se puede
expresar como: n! = n * (n-1)!, donde "n" es un número dado y (n-1)!  es  el  factorial  del  número
anterior a "n", hasta llegar al caso base, en el que el factorial de 0 es igual a 1. Usamos "n-1" en
este ejemplo porque cada llamada recursiva reduce el problema, acercándolo al caso base y asegurando
que la recursión se detenga cuando "n" sea igual a 0. Esto permite que la  función  se  llame  a  sí
misma varias veces, resolviendo subproblemas más pequeños hasta alcanzar el resultado final.

Por último, el factorial se utiliza en áreas como la combinatoria, la probabilidad y el análisis  de
algoritmos. Su definición recursiva es una forma común de implementarlo en programación,  dividiendo
el problema en subproblemas más pequeños hasta alcanzar el caso base. Es  importante  recordar  que,
aunque elegante, la recursividad no  siempre  es  la  solución  más  eficiente,  especialmente  para
problemas con entradas muy grandes."""

# Ejemplo_recursividad.py

# Explicación:
"""Definimos una función llamada "factorial()" que recibe un parámetro llamado "n".  Este  parámetro
se utilizará para calcular el factorial de un número y será sustituido por el valor que se le pase a
la función al llamarla. Para ello, utilizamos la palabra  clave  "def"  seguida  del  nombre  de  la
función, en este caso "factorial()", seguido del  nombre  del  parámetro  "n"  entre  paréntesis,  y
terminamos con dos puntos (:) para indicar el inicio del bloque de código asociado a la función.

Dentro de la función utilizamos el condicional "if" para evaluar si la variable "n" es  igual  a  0.
Para ello, escribimos la palabra clave "if" seguida de la condición entre paréntesis y terminada con
dos puntos (:). La condición se compone de la variable "n", el operador de igualdad (==) y el  valor 0.

Si la condición se cumple, se ejecuta el bloque de código asociado al "if",  el  cual  contiene  una
instrucción "return" que devuelve el valor 1. Esto corresponde al caso base de la recursión, ya  que
el factorial de 0 se define como 1. Al retornar este valor,  la  función  finaliza  su  ejecución  y
devuelve el resultado al lugar desde donde fue llamada, deteniendo la ejecución  de  la  función  en
este punto.

Colocamos el condicional "if" con una indentación de cuatro espacios desde el margen izquierdo, para
indicar que forma parte del cuerpo de la función  y  debe  evaluarse  siempre  que  la  función  sea
llamada. Además, colocamos la instrucción "return"  con  una  indentación  de  cuatro  espacios  con
respecto al propio condicional "if", para indicar que esta instrucción forma  parte  del  bloque  de
código asociado al condicional "if" y debe ejecutarse cada vez que se llame a la función, pero  solo
si la condición del "if" se cumple.

A continuación, utilizamos el condicional "else" para manejar el caso en que la condición  del  "if"
no se cumpla. Para ello, escribimos la palabra clave  "else"  seguida  de  dos  puntos  (:).  Si  la
condición del "if" no se cumple, se ejecuta el bloque de código asociado al "else", el cual contiene
una instrucción "return" que devuelve la multiplicación de "n" por  el  resultado  de  llamar  a  la
función "factorial()" con el argumento "n-1" de esta forma:  "return  (n  *  factorial(n-1))".  Esto
corresponde al caso recursivo de la función, donde se llama a sí misma con un valor reducido de  "n"
para acercarse al caso base. Al retornar este valor,  la  función  genera  una  cadena  de  llamadas
recursivas que se resuelven en orden inverso, multiplicando los valores obtenidos para  calcular  el
resultado final.

De esta forma, llamamos a la función "factorial()" dentro de sí misma, lo que  crea  una  cadena  de
llamadas recursivas que se resuelven en orden inverso,  multiplicando  los  valores  obtenidos  para
calcular el resultado final. Esta llamada en cadena se repetirá hasta que se alcance el  caso  base,
donde "n" es igual a 0, momento en el cual se detendrá la recursión y se comenzarán a  resolver  las
llamadas pendientes, multiplicando los resultados obtenidos para calcular el factorial de "n".

Colocamos el condicional "else" con una indentación de cuatro espacios desde  el  margen  izquierdo,
para indicar que forma parte del cuerpo de la función "factorial()" y debe evaluarse siempre que  la
función sea llamada. Además, colocamos  la  instrucción  "return"  con  una  indentación  de  cuatro
espacios con respecto al propio condicional "else", para indicar que esta  instrucción  forma  parte
del bloque de código asociado al condicional "else" y debe ejecutarse cada vez que  se  llame  a  la
función, pero solo si la condición del "if" no se cumple.

Por último, llamamos a la función "factorial()" con el argumento 5 y almacenamos el resultado de  la
llamada en una variable llamada "resultado". Este argumento será transferido y asignado a la función
"factorial()" como el valor de "n" para calcular el factorial de 5.  Luego,  utilizamos  la  función
"print()" para mostrar el valor de la variable "resultado", acompañado de un mensaje descriptivo  en
formato "f-string". Colocamos las dos últimas líneas de código sin indentación, para indicar que  no
pertenecen a ninguna otra estructura y deben ejecutarse al momento de ejecutar el código."""

# Código:
def factorial(n):
    if (n == 0):
        return 1
    else:
        return (n * factorial(n-1))

resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}")

# Nota Importante:
"""La recursividad  es  una  técnica  poderosa  que  permite  resolver  problemas  dividiéndolos  en
subproblemas más pequeños. En este ejemplo, el caso base ocurre cuando "n" es igual a 0, devolviendo
1 directamente. Si "n" es mayor que 0, la función devuelve el resultado de multiplicar  "n"  por  el
factorial de "n-1". Esto crea una cadena de llamadas recursivas que se resuelven en  orden  inverso,
multiplicando los valores obtenidos para calcular el resultado final. Este orden recursivo no afecta
al resultado, ya que se obtendría el mismo valor si  se  resolviera  de  forma  iterativa,  pero  la
recursividad ofrece una forma más elegante y fácil de entender para problemas que se pueden  dividir
en subproblemas similares, como el cálculo de factoriales.

Además, es importante tener en cuenta que cada llamada recursiva  consume  memoria  en  la  pila  de
ejecución. Si el valor de "n" es muy grande, el número de llamadas recursivas también  lo  será,  lo
que podría llevar a un desbordamiento de la pila (stack overflow). Python no implementa optimización
de "recursión de cola", por lo que es crucial definir un caso base y asegurarse de que las  llamadas
recursivas reduzcan el problema hacia ese caso base.

En este ejemplo, la función "factorial()" calcula el factorial de 5 siguiendo este  flujo:  primero,
se evalúa si "n" es igual a 0. Como "n" es 5, se calcula "5 * factorial(4)".  Luego,  "factorial(4)"
calcula "4 * factorial(3)", y así sucesivamente, hasta alcanzar el caso base en "factorial(0)",  que
devuelve 1. La multiplicación quedaría de la siguiente forma: 5 * (4  *  (3  *  (2  *  (1  *  1)))).
Finalmente, los resultados de las llamadas se resuelven en orden inverso, obteniendo el factorial de
5, que es 120. Este ejemplo ilustra cómo la  recursividad  puede  ser  una  herramienta  elegante  y
eficiente para resolver problemas matemáticos, siempre que se utilice con precaución."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
