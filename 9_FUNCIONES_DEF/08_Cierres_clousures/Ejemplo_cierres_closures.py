# Enunciado:
"""Un cierre o "closure" en Python es una técnica de programación que permite a una función  interna
acceder a las variables locales de una función externa y recordar ese entorno incluso después de que
la función externa haya terminado su ejecución. Esto significa que la función interna puede  acceder
a las variables locales de la función externa y mantener  un  estado  persistente  a  lo  largo  del
tiempo. Los cierres permiten encapsular datos y comportamientos relacionados  de  manera  eficiente,
mejorando la modularidad y evitando efectos secundarios no deseados.

Además, los cierres permiten que las funciones internas actúen  como  "contenedores"  de  datos  que
realizan una tarea específica, manteniendo un estado privado y  controlado.  Esto  es  especialmente
útil para crear funciones que  necesitan  conservar  un  estado  entre  llamadas,  como  contadores,
acumuladores o cualquier otro tipo de dato que deba persistir a lo largo del tiempo.

Cuando se crea un cierre, la función interna captura y  mantiene  una  referencia  a  las  variables
locales de la función externa. Esto permite que dichas variables sean accesibles incluso después  de
que la función externa haya terminado su ejecución. A diferencia  de  las  variables  globales,  las
variables capturadas por un cierre están limitadas al contexto de la función interna.

La sintaxis para crear un cierre implica definir una función dentro de otra y  retornar  la  función
interna desde la función externa usando "return" seguido del  nombre  de  la  función  interna  "sin
paréntesis". Además, debemos asignar la llamada a la función externa a una variable, lo que  permite
que la función interna conserve una referencia y pueda ser llamada posteriormente. Esto convierte  a
la variable "resultado" en una función "resultado()" que recuerda el estado de las variables locales
de la función externa en el momento de su creación. Además, las  variables  de  la  función  externa
pasan a formar parte del entorno accesible para la función interna.

Si llamamos a la función externa sin asignarla a una variable después de haber creado el cierre,  se
ejecutará solamente la función externa y no se mantendrá ninguna referencia a la función interna  ni
a su entorno. Esto significa que no se podrá acceder a las variables locales de la  función  externa
ni a la función interna después de que la función externa haya terminado su ejecución. En este caso,
la función interna no se ejecutará automáticamente, ya que solo  se  define  dentro  de  la  función
externa, pero no se invoca explícitamente. Esto limita su utilidad y funcionalidad,  ya  que  no  se
crea un cierre ni se conserva el estado.

Por último, es importante saber cuándo y cómo  usar  los  cierres,  ya  que,  a  pesar  de  ser  una
herramienta poderosa, su uso inadecuado puede llevar a  problemas  de  rendimiento  o  a  un  código
difícil de entender. Es fundamental comprender el concepto de los cierres y su  funcionamiento  para
aprovechar al máximo sus beneficios en la programación funcional y modular."""

# Ejemplo_cierres_closures.py

# Explicación:
"""Definimos una función llamada "funcion_externa()" que no recibe parámetros. Para ello, utilizamos
la palabra clave "def" seguida del nombre de la función, en este caso "funcion_externa", seguido  de
paréntesis vacíos () ya que no recibe parámetros, y terminamos con dos puntos (:)  para  indicar  el
inicio del bloque de código asociado a la función externa.

Dentro de la función externa, definimos una variable local llamada  "contador"  y  le  asignamos  el
valor entero 1. Esta variable controla el estado del contador, que se incrementará cada vez  que  se
llame a la función interna, modificando su valor.  Además,  utilizamos  la  función  "print()"  para
mostrar el valor inicial del contador acompañado de un mensaje  descriptivo  en  formato  "f-string"
desde la función externa, lo que nos permite verificar que el contador se  inicializa  correctamente
antes de que la función interna lo  modifique  a  través  de  las  llamadas  a  la  función  interna
"resultado()". Colocamos el bloque de código asociado a la función externa con  una  indentación  de
cuatro espacios desde el margen izquierdo para indicar que forma parte  del  cuerpo  de  la  función
externa y debe ejecutarse una sola vez cuando la función externa sea llamada.

A  continuación,  dentro  de  la  función   externa,   definimos   una   función   interna   llamada
"funcion_interna()" que tampoco recibe parámetros. Para ello,  utilizamos  la  palabra  clave  "def"
seguida del nombre de la función, en este caso "funcion_interna", seguido de paréntesis vacíos () ya
que no recibe parámetros, y terminamos con dos puntos (:) para  indicar  el  inicio  del  bloque  de
código asociado a la función interna. Colocamos esta función con una indentación de cuatro  espacios
desde el margen izquierdo para indicar que forma parte del cuerpo  de  la  función  externa  y  debe
ejecutarse siempre que se llame a la función interna a través de la variable "resultado()",  ya  que
la llamada a la función externa no ejecuta la función interna, sino que la retorna  como  un  cierre
"closure" para ser llamada posteriormente.

Dentro de la función interna, hacemos referencia a la variable "contador", la cual  tiene  el  valor
inicial "1". Para ello, utilizamos la palabra clave "nonlocal" seguida del nombre de la variable, en
este caso "contador". Esto indica que queremos trabajar con la variable "contador"  definida  en  el
ámbito de la función externa, en lugar de crear una nueva variable local con el mismo nombre  dentro
de la función interna.

A continuación, incrementamos el valor de la variable  "contador"  dentro  de  la  función  interna,
utilizando la expresión de incremento "contador += 1". Al haber declarado "contador" como "nonlocal"
previamente, esta modificación afecta el valor de "contador" en el ámbito  de  la  función  externa.
Esto significa que el valor de "contador" se mantendrá y se actualizará cada vez que se llame  a  la
función interna a través de la variable  "resultado()",  permitiendo  que  el  estado  del  contador
persista a lo largo del tiempo.

Además, utilizamos la instrucción "return" para devolver el valor actualizado de "contador" cada vez
que se llame a la función interna a través de la variable  "resultado()".  La  instrucción  "return"
indica al intérprete que la función debe finalizar su ejecución y enviar el  valor  especificado  de
vuelta al lugar desde donde fue llamada. En este caso, el valor será retornado como un número entero
(int), que representa el valor actual de "contador" después de haber sido modificado.

Colocamos todo el bloque de código asociado a la función  interna  con  una  indentación  de  cuatro
espacios desde la propia función interna para indicar que forma parte del bloque de código  asociado
a la función interna y debe ejecutarse siempre que se llame a la función  interna  a  través  de  la
variable "resultado()".

Luego, fuera de la función interna pero  aún  dentro  de  la  función  externa,  creamos  un  cierre
"closure" con ayuda de la  instrucción  "return"  para  retornar  la  función  interna.  Para  ello,
escribimos la palabra clave "return" seguida del nombre de la función interna "funcion_interna"  sin
paréntesis. De esta forma, la función interna mantendrá una referencia  al  entorno  de  la  función
externa, lo que permite que el estado del contador se mantenga a lo largo del tiempo y sea accesible
desde el ámbito global del programa a través de la variable  "resultado".  Al  retornar  la  función
interna sin paréntesis, estamos  devolviendo  la  referencia  a  la  función  interna  en  lugar  de
ejecutarla inmediatamente, lo que permite que el cierre "closure" se cree y conserve  el  estado  de
las variables locales de la función externa. Colocamos esta línea de código con una  indentación  de
cuatro espacios desde el margen izquierdo para indicar que forma parte  del  cuerpo  de  la  función
externa y debe ejecutarse una sola vez cuando se llame a la función externa.

Además, fuera del ámbito de las funciones, llamamos a la función externa y almacenamos el  resultado
de la llamada en una variable llamada "resultado". De esta forma, estamos creando una  referencia  a
la función interna, llamada ahora "resultado()", que ha sido retornada por la  función  externa,  lo
que permite que el cierre "closure" mantenga el estado  de  las  variables  locales  de  la  función
externa y que la función interna acceda a ellas a través de la llamada incluso  después  de  que  la
función externa haya terminado su ejecución. Para ello, escribimos el nombre de la  función  externa
"funcion_externa()" y asignamos el resultado de la llamada a la variable "resultado"  utilizando  el
operador de asignación (=). De esta forma, ejecutamos la  función  externa,  lo  que  inicializa  el
contador y retorna la referencia a la función interna "closure", permitiendo que, cuando se llame  a
la variable "resultado()", se ejecute la función interna, que incrementará el contador  y  retornará
su valor actualizado. Colocamos esta línea de código sin indentación para indicar  que  forma  parte
del ámbito global del programa y debe ejecutarse al momento de ejecutar el código.

Por último, imprimimos el valor de la variable "resultado()" con ayuda de la función "print()"  tres
veces para mostrar el valor actualizado del contador cada vez que se llame a la  función  interna  a
través de la variable "resultado()", acompañado de un mensaje descriptivo en formato "f-string".  Al
llamar a la función "resultado()" varias veces dentro de la función "print()", podemos observar cómo
el contador se incrementa y mantiene su estado a lo largo del tiempo. Además, colocamos estas líneas
de código sin indentación para indicar que forman parte del  ámbito  global  del  programa  y  deben
ejecutarse al momento de ejecutar el código, permitiendo que se muestre  el  valor  actualizado  del
contador cada vez que se llame a la función interna a través de la variable "resultado()"."""

# Código:
def funcion_externa():
    contador = 1
    print(f"Valor inicial del contador desde la función externa: {contador} y única ejecución")

    def funcion_interna():
        nonlocal contador
        contador += 1
        return contador

    return funcion_interna

resultado = funcion_externa()

print(f"Valor de la variable contador en la segunda llamada: {resultado()}")
print(f"Valor de la variable contador en la tercera llamada: {resultado()}")
print(f"Valor de la variable contador en la cuarta llamada: {resultado()}")

# Nota Muy Importante:
"""En este caso, utilizamos la función "print()" para mostrar el valor inicial del contador desde la
función externa, lo que nos permite verificar que el contador se inicializa correctamente  antes  de
que la función interna lo modifique. Al llamar a la  función  "resultado()"  varias  veces,  podemos
observar cómo el contador se incrementa y mantiene su estado a lo largo del tiempo.  Esto  demuestra
cómo el estado entre llamadas se mantiene gracias al cierre "closure" creado por la función  interna
al capturar la variable "contador".

Una diferencia clave entre retornar una función y crear un cierre radica en cómo se maneja el estado
de las variables locales de la  función  externa.  Retornar  una  función  simplemente  devuelve  la
referencia a la función interna, permitiendo que esta sea ejecutada posteriormente. Sin embargo,  un
cierre se crea cuando la función interna captura y recuerda el estado de las variables locales de la
función externa en el momento de su creación. Esto permite que las funciones  internas  actúen  como
"contenedores" de datos, manteniendo un estado privado y controlado. Los cierres son una herramienta
poderosa para  encapsular  lógica  y  datos,  y  son  fundamentales  para  implementar  patrones  de
programación funcional y modular.

Además, en cuanto al uso de "nonlocal", es importante destacar que, aunque el cierre permite que  la
función interna mantenga acceso al entorno de la función externa, el uso de "nonlocal" es  necesario
para modificar las variables definidas en  dicho  entorno.  Sin  "nonlocal",  cualquier  intento  de
asignar un nuevo valor a la variable "contador" dentro de  la  función  interna  crearía  una  nueva
variable local en lugar de modificar la existente en el ámbito de la función externa. Esto significa
que "nonlocal" es esencial para  indicar  explícitamente  que  queremos  trabajar  con  la  variable
"contador" del cierre y no crear una nueva variable local dentro de la función interna.

El flujo sería el siguiente: primero, se llama a la  función  externa  "funcion_externa()",  lo  que
ejecuta su código, inicializa el contador y retorna la referencia a la función interna. Luego,  cada
vez que se llama a "resultado()", se ejecuta la función interna "funcion_interna()", que  incrementa
el contador y retorna su valor actualizado. Esto demuestra cómo  el  estado  del  contador  persiste
gracias al cierre creado por la función interna, que captura la variable "contador"  de  la  función
externa.

Debe quedar claro que el cierre permite que la función interna mantenga  acceso  al  entorno  de  la
función externa incluso después de que esta última haya terminado su ejecución. Esto es lo que  hace
que los  cierres  sean  una  herramienta  poderosa  para  encapsular  lógica  y  datos,  permitiendo
implementar patrones de programación funcional y modular de manera eficiente.

Por último, en el momento en que creamos el closure, la variable "contador" pasa a formar parte  del
entorno de la función interna, lo que significa que cada vez que se llama a  la  función  interna  a
través de la variable "resultado()", se accede a la variable  "contador"  que  se  encuentra  en  el
ámbito compartido por la función interna, y no a  una  variable  global  ni  a  una  variable  local
independiente de la función externa. Esto es lo que permite que el estado del contador se mantenga a
lo largo del tiempo, ya que cada llamada a la función interna modifica el valor de "contador" dentro
de ese entorno compartido, y este valor se mantiene entre llamadas gracias al cierre creado  por  la
función interna al capturar la variable "contador" de la función externa."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
