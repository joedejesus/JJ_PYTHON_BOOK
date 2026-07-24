# Enunciado:
"""En Python, la palabra clave "nonlocal" se utiliza para referirse a una variable  definida  en  un
ámbito que envuelve a la función actual, pero que  no  es  el  ámbito  global.  Esto  significa  que
"nonlocal" permite modificar una variable que pertenece a  un  nivel  intermedio  de  anidación,  es
decir, una variable que no es ni local a la función interna ni  global  en  el  programa.  Sin  esta
palabra clave, no podríamos trabajar con una variable en el ámbito intermedio ni modificar su  valor
desde una función interna; en ese caso, crearíamos una nueva variable local en el ámbito interno con
el mismo nombre, dejando intacta la variable en el ámbito externo.

El uso de "nonlocal" es especialmente útil en casos donde se trabaja con  funciones  anidadas  y  se
necesita modificar el estado de una variable definida  en  una  función  externa.  Esto  permite  un
control más preciso sobre el flujo de datos entre los diferentes niveles de anidación,  evitando  el
uso de variables globales, que pueden introducir efectos  secundarios  no  deseados.  Es  importante
destacar que "nonlocal" no puede usarse para referirse a variables globales, ya que su propósito  es
exclusivamente trabajar con variables en ámbitos intermedios, es decir, entre el ámbito local  y  el
ámbito global. Además, "nonlocal" solo puede ser utilizada en  funciones  anidadas;  fuera  de  este
contexto, su uso generará un error de sintaxis de tipo "SyntaxError".

Por último, la palabra clave "nonlocal" es una herramienta poderosa  para  gestionar  el  estado  de
variables en funciones anidadas, permitiendo modificar variables en ámbitos  intermedios  de  manera
explícita y controlada, sin recurrir a  prácticas  menos  recomendadas  como  el  uso  de  variables
globales."""

# Ejemplo_palabra_clave_nonlocal.py

# Explicación:
"""Definimos una función llamada "funcion_externa()" que no recibe parámetros. Para ello, utilizamos
la palabra clave "def" seguida del nombre de la función, en este caso "funcion_externa", seguido  de
paréntesis vacíos () ya que no recibe parámetros, y terminamos con dos puntos (:)  para  indicar  el
inicio del bloque de código asociado a la función externa.

Dentro de la función externa, definimos una variable local llamada  "x"  y  le  asignamos  el  valor
entero 10. Esta variable es accesible dentro del ámbito de la  función  externa  y  desde  cualquier
función interna anidada dentro de ella, pero no es accesible desde el ámbito  global  del  programa.
Además, solo podríamos modificar su valor desde la  función  externa  en  condiciones  normales;  es
decir, si no utilizamos la palabra clave "nonlocal" y realizamos los cambios  dentro  de  esta.  Sin
embargo, gracias a la palabra clave "nonlocal", es posible  modificar  su  valor  desde  la  función
interna anidada. Colocamos esta línea de código con una indentación  de  cuatro  espacios  desde  el
margen izquierdo para indicar que forma parte del cuerpo de la función  externa  y  debe  ejecutarse
siempre que la función externa sea llamada.

A  continuación,  dentro  de  la  función   externa,   definimos   una   función   anidada   llamada
"funcion_interna()" que tampoco recibe parámetros. Para ello,  utilizamos  la  palabra  clave  "def"
seguida del nombre de la función, en este caso "funcion_interna", seguido de paréntesis vacíos () ya
que no recibe parámetros, y terminamos con dos puntos (:) para  indicar  el  inicio  del  bloque  de
código asociado a la función interna. Colocamos esta función con una indentación de cuatro  espacios
desde el margen izquierdo para indicar que forma parte del cuerpo  de  la  función  externa  y  debe
ejecutarse solo cuando la función externa sea llamada.

Dentro de la función interna, hacemos referencia a la variable "x", la cual tiene el  valor  inicial
"10". Para ello, utilizamos la palabra clave "nonlocal" seguida del nombre de la variable,  en  este
caso "x". Esta variable ahora es accesible dentro del ámbito de la  función  interna  ya  que  hemos
utilizado la palabra clave "nonlocal" para indicar que queremos trabajar con ella en lugar de  crear
una nueva variable local con el mismo nombre. Colocamos esta línea de código con una indentación  de
cuatro espacios desde la propia función interna para indicar que forma parte del  bloque  de  código
asociado a dicha función y debe ejecutarse siempre que la función interna sea llamada.

A continuación, modificamos el valor de la variable "x" dentro de la función interna, asignándole el
valor entero "13". Para ello, utilizamos el operador de asignación (=) para asignar el  nuevo  valor
"13" a la variable "x". Al haber  declarado  "x"  como  "nonlocal"  previamente,  esta  modificación
afectará el valor de "x" en los ámbitos interno y externo de la función. De esta forma, la  variable
"x" ahora tiene el valor "13" dentro de la función interna, y este cambio se reflejará en el  ámbito
de la función externa, siempre y cuando se llame a la función interna; de otra forma,  el  valor  de
"x" permanecerá siendo "10"  ya  que  si  no  llamamos  a  la  función  interna  no  se  realiza  la
modificación. Colocamos esta línea de código con una indentación de cuatro espacios desde la  propia
función interna para indicar que forma parte del bloque de código asociado a dicha  función  y  debe
ejecutarse siempre que la función interna sea llamada.

Además, utilizamos la instrucción "return" para devolver el valor actualizado de "x" cada vez que se
llame a la función interna. La instrucción  "return"  indica  al  intérprete  que  la  función  debe
finalizar su ejecución y enviar los valores especificados de vuelta al lugar donde fue  llamada.  En
este caso, el valor será retornado al ámbito de la función externa ya que la  función  interna  será
llamada desde el ámbito externo. Para ello, escribimos la palabra clave "return" seguida del  nombre
de la variable "x". En este caso, estamos devolviendo el resultado en una sola instrucción en  forma
de número entero (int), que representa el valor actual de "x"  después  de  haber  sido  modificado.
Colocamos esta línea de código con una indentación  de  cuatro  espacios  desde  la  propia  función
interna para indicar que forma parte del bloque de código asociado a dicha función y debe ejecutarse
siempre que la función interna sea llamada.

Luego, fuera de la función interna pero aún dentro de la función  externa,  llamamos  a  la  función
interna y retornamos su resultado utilizando la  instrucción  "return".  Para  ello,  escribimos  la
palabra clave "return" seguida del nombre de la función interna "funcion_interna()". De esta  forma,
cuando se llame a la función externa, se ejecutará la  función  interna  y  se  devolverá  el  valor
actualizado de "x" (que ahora es 13) al ámbito externo. Colocamos  esta  línea  de  código  con  una
indentación de cuatro espacios desde el margen izquierdo para indicar que forma parte del bloque  de
código asociado a la función externa y debe ejecutarse siempre que se llame a la función externa.

Además, fuera del ámbito de las funciones, llamamos a la función externa y almacenamos el  resultado
de la llamada en una variable llamada "resultado". Para ello, escribimos el  nombre  de  la  función
externa "funcion_ externa()" y asignamos el resultado  de  la  llamada  a  la  variable  "resultado"
utilizando el operador de asignación (=). De esta forma, cuando se ejecute esta línea de código,  se
llamará a la función externa, que a su vez llamará a la función interna, modificará el valor de  "x"
a 13 y devolverá ese valor al ámbito externo,  donde  se  almacenará  en  la  variable  "resultado".
Colocamos esta línea de código sin indentación para indicar que forma parte del  ámbito  global  del
programa y debe ejecutarse al momento de ejecutar el código.

Por último, imprimimos el valor de la variable "resultado" con ayuda de la  función  "print()"  para
mostrar el valor retornado por la función externa, que es "13" después de la modificación  realizada
en la función interna. Colocamos esta línea de código sin indentación para indicar que  forma  parte
del ámbito global del programa y debe ejecutarse al momento de ejecutar el código."""

# Código:
def funcion_externa():
    x = 10

    def funcion_interna():
        nonlocal x
        x = 13
        return x

    return funcion_interna()

resultado = funcion_externa()
print(resultado)

# Nota Muy Importante:
"""Si no asignamos la llamada a la función externa a una variable, no  podríamos  acceder  al  valor
modificado de "x" fuera de la función externa. Esto se debe a que  "x"  sigue  siendo  una  variable
local dentro de la función externa y no es accesible desde el ámbito global ya que  no  hay  ninguna
instrucción que permita retornar o mostrar  su  valor  al  ámbito  global.  Por  lo  tanto,  sin  la
asignación a la variable "resultado", el valor modificado de "x" no estaría disponible en el  ámbito
global.

Por otro lado, el retorno de la función interna es necesario para que el  valor  modificado  de  "x"
pueda ser utilizado fuera de la función  interna,  ya  que  sin  el  "return  funcion_interna()"  no
podríamos acceder a ese valor desde el ámbito externo, lo que limitaría la utilidad  de  la  función
interna y su capacidad para modificar el estado de "x" de manera efectiva. Además, la función no  se
ejecutaría ya que no está siendo llamada. Del mismo modo, el uso de "return" asociado a la  variable
"x" es fundamental para que el valor modificado de "x" pueda ser devuelto a la  función  externa  y,
posteriormente, a cualquier ámbito que llame a la función externa. Esto nos permite obtener el valor
modificado de "x" y utilizarlo en el ámbito externo.

Además, es importante saber que, en principio, la variable "x" tiene un valor inicial de  10  dentro
de la función externa. Sin embargo, este valor solo se modifica a 13 cuando se llama  a  la  función
interna. Si no se llama a esta función, el valor de "x" permanecerá siendo 10 dentro de  la  función
externa. Por lo tanto, el valor de "x" en el ámbito externo depende de si se ha ejecutado la función
interna o no, ya que es posible ejecutar la función externa sin llamar a la función interna, lo  que
haría que "x" mantuviera su valor inicial de 10.

En este caso utilizamos la instrucción "return" para retornar la función interna y cambiar el  valor
de "x" una sola vez. Hacemos esto porque no necesitamos mantener un estado persistente a lo largo de
múltiples  ejecuciones,  sino  que  solo  queremos  modificar  "x"  en  un  momento  específico.  Si
necesitáramos mantener un estado persistente entre múltiples llamadas, podríamos usar un  "closure",
que encapsula el estado sin necesidad de usar "nonlocal". Los closures son útiles cuando se requiere
que una función interna recuerde el estado de las variables de su función externa,  incluso  después
de que esta última haya terminado su ejecución.

Para modificar una variable de una función externa, se puede usar "nonlocal" junto con "return" para
realizar cambios puntuales, o un closure prescindiendo de "nonlocal"  si  se  necesita  mantener  un
estado persistente. La elección entre "nonlocal" y closures depende del caso  de  uso  y  de  si  se
requiere modificar el estado de forma temporal o persistente. Ambas herramientas  son  fundamentales
para gestionar el flujo de datos y el estado en programas que hacen uso de funciones anidadas.  Esta
diferencia se explicará con detalle en la  sección  correspondiente  a  cierres  "closures"  en  los
códigos siguientes.

Por último, en cuanto al uso de parámetros y argumentos,  el  funcionamiento  es  el  mismo  que  en
cualquier otra función. En este caso, tanto la función externa como la función  interna  no  reciben
parámetros, pero podrían ser modificadas para aceptar argumentos si se necesitara pasar  información
entre ellas. El uso de parámetros y argumentos no afecta el funcionamiento  de  "nonlocal",  ya  que
esta palabra clave se refiere específicamente a la modificación de variables en ámbitos intermedios,
independientemente de si las funciones reciben o no parámetros."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
