# Enunciado:
"""En Python, la palabra clave "global" se utiliza para hacer referencia a una variable global desde
el ámbito actual de una función o bloque de código. Cuando se declara una  variable  dentro  de  una
función o bloque, esta variable se considera local, lo que significa que solo está disponible dentro
de esa función y no afecta el valor de ninguna variable con el mismo nombre en el ámbito global.  Si
se necesita acceder o modificar una variable global  desde  dentro  de  una  función  o  bloque,  es
necesario declararla explícitamente como global usando la palabra clave "global". De  lo  contrario,
Python tratará la variable como una nueva variable local.

El uso de "global" permite modificar el valor de una variable global desde dentro de una  función  o
bloque, lo que puede ser útil en ciertos casos, como cuando se trabaja con contadores,  acumuladores
o configuraciones globales que necesitan ser compartidas y actualizadas  en  diferentes  partes  del
programa. Sin embargo, el uso indiscriminado de variables globales puede hacer que el código sea más
difícil de depurar y  mantener,  ya  que  los  cambios  en  estas  variables  pueden  tener  efectos
colaterales inesperados en otras partes del programa. Por esta razón, se recomienda  usar  variables
globales con moderación y, siempre que sea posible, considerar alternativas como pasar parámetros  a
las funciones o devolver valores desde ellas.

Por último, aunque la palabra clave "global" permite modificar variables globales, su  uso  excesivo
puede llevar a un diseño de programa menos estructurado y  más  propenso  a  errores.  En  lugar  de
depender de variables globales, es preferible adoptar un enfoque modular, donde las  funciones  sean
independientes y se comuniquen mediante parámetros y valores de retorno. Esto mejora la claridad del
código, facilita su mantenimiento y reduce el riesgo de efectos  colaterales  no  deseados.  Por  lo
tanto, el uso de "global" debe ser una decisión consciente y justificada, basada en las  necesidades
específicas del programa."""

# Ejemplo_palabra_clave_global.py

# Explicación:
"""Definimos una variable global llamada "x" y le asignamos el valor entero "10". Esta  variable  es
accesible desde cualquier parte del programa, ya que está definida  fuera  de  cualquier  función  o
bloque de código. Además, utilizamos la instrucción "print()" para imprimir el valor inicial  de  la
variable global "x" en la consola, acompañado de un mensaje descriptivo en formato "f-string".  Esto
nos permite verificar el valor de "x" antes de que sea modificado por la función.

Definimos una función llamada "ambito()" que no recibe parámetros. Para ello, utilizamos la  palabra
clave "def" seguida del nombre de la función, en este caso "ambito", seguido  de  paréntesis  vacíos
(), ya que no recibe parámetros, y terminamos con dos puntos (:) para indicar el inicio  del  bloque
de código asociado a la función.

Dentro de la función, hacemos referencia a la variable global "x", la cual tiene  el  valor  inicial
"10". Para ello, utilizamos la palabra clave "global" seguida del nombre de  la  variable,  en  este
caso "x". Esta variable ahora es accesible dentro del ámbito de la función "ambito()" ya  que  hemos
utilizado la palabra clave "global" para indicar que queremos trabajar con  la  variable  global  en
lugar de crear una nueva variable local con el mismo nombre. Colocamos esta línea de código con  una
indentación de cuatro espacios desde el margen izquierdo para indicar que forma parte del cuerpo  de
la función y debe ejecutarse siempre que la función sea llamada.

A continuación, modificamos el valor de la variable global "x" dentro de la función, asignándole  el
valor entero "20". Para ello, utilizamos el operador de asignación (=) para asignar el  nuevo  valor
"20" a la variable "x". Al haber declarado "x" como global previamente, esta  modificación  afectará
el valor de "x" en el ámbito global. De esta forma, la variable global "x" ahora tiene el valor "20"
tanto dentro como fuera de la función, es decir, en todos  los  ámbitos.  Colocamos  esta  línea  de
código con una indentación de cuatro espacios desde el margen izquierdo para indicar que forma parte
del cuerpo de la función y debe ejecutarse siempre que la función sea llamada.

A continuación, dentro de la función, utilizamos la instrucción "print()"  para  imprimir  el  valor
modificado de la variable  global  "x"  desde  dentro  de  la  función,  acompañado  de  un  mensaje
descriptivo en formato "f-string". De esta forma, al llamar a la función "ambito()", se mostrará  el
valor actualizado de la variable global "x" en  la  consola.  Colocamos  esta  instrucción  con  una
indentación de cuatro espacios desde el margen izquierdo para indicar que forma parte del cuerpo  de
la función y debe ejecutarse siempre que la función sea llamada.

Luego, llamamos a la función "ambito()" para ejecutar el código asociado dentro de ella. Para llamar
a la función, simplemente escribimos su nombre seguido de paréntesis  vacíos,  ya  que  no  requiere
argumentos, en este caso "ambito()". Esto indica al intérprete que debe ejecutar el bloque de código
asociado a la función, modificando así el valor de la variable global "x"  e  imprimiendo  su  nuevo
valor. Colocamos la llamada a la función sin indentación, ya que se encuentra en el nivel  principal
del código y no forma parte de ninguna otra estructura.

Por último, utilizamos de nuevo la instrucción "print()" para  imprimir  el  valor  de  la  variable
global "x" desde fuera de la función, acompañado de un mensaje descriptivo en formato "f-string". Al
referirnos a la variable global "x" fuera de la función, estamos accediendo a la  variable  definida
al principio del código, cuyo valor es "20"  ya  que  la  hemos  modificado  dentro  de  la  función
"ambito()".

Esto significa que la instrucción "print()" mostrará el valor de la variable global y no el valor de
la variable local definida dentro de la función, la cual solo es accesible dentro de esa  función  y
ya ha sido impresa al llamar a la función. Colocamos esta instrucción sin  indentación,  ya  que  se
encuentra en el nivel principal del código y no forma parte de ninguna otra estructura. Al  ejecutar
esta línea después de llamar a la función, se mostraráel valor de  la  variable  global  "x"  en  la
consola, confirmando que ha sido modificado por la función."""

# Código:           
x = 10
print(f"Valor inicial de x: {x}") 

def ambito(): 
    global x
    x = 20   
    print(f"Impresión del valor modificado de 'x' desde dentro de la función: {x}")

ambito()
print(f"Impresión del valor modificado de 'x' desde fuera de la función: {x}")

# Nota Importante:
"""En este ejemplo, la variable "x" se  declara  como  global  en  la  función  "ambito()",  lo  que
significa que la función puede acceder y modificar el valor de "x" en el ámbito global. Esto permite
que el valor de "x" cambie tanto dentro como fuera de la función después de que esta sea llamada.

Es importante destacar que el valor de "x" se modifica dentro de la función cuando esta se  ejecuta,
y no simplemente al asignarle un nuevo valor dentro de  la  función.  Siempre  que  se  llame  a  la
función, el valor global de "x" será modificado. De esta forma, al imprimir el valor de "x" fuera de
la función, se reflejará el cambio realizado dentro de la función.

Además, es crucial entender que, al declarar  una  variable  como  global  dentro  de  una  función,
cualquier cambio que se realice en esa variable afectará directamente su valor en el ámbito  global.
Esto puede ser útil en situaciones donde se necesita compartir y actualizar el estado global de  una
variable entre diferentes partes  del  programa.  Sin  embargo,  también  puede  introducir  errores
difíciles de rastrear si no se tiene cuidado.

Por esta razón, es  una  buena  práctica  minimizar  el  uso  de  variables  globales  y  considerar
alternativas más seguras, como pasar parámetros a las funciones  o  devolver  valores  desde  ellas.
Estas estrategias no solo hacen que el código sea más fácil de entender y mantener, sino que también
reducen el riesgo de errores relacionados con el estado global del programa.

Por último, aunque el uso de "global" puede ser una herramienta poderosa en  ciertos  contextos,  su
uso excesivo puede llevar a problemas de diseño y mantenimiento en  el  código.  Por  lo  tanto,  es
fundamental evaluar cuidadosamente cuándo y cómo utilizar esta palabra clave, priorizando siempre la
claridad, la modularidad y la robustez del programa."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
