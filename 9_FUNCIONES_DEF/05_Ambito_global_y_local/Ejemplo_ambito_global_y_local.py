# Enunciado:
"""En Python, el ámbito "global" y "local" se refieren a  la  visibilidad  y  accesibilidad  de  las
variables y funciones dentro de un programa.  El  ámbito  "global"  incluye  variables  y  funciones
definidas fuera de cualquier función o bloque, lo que las hace accesibles desde cualquier parte  del
programa, siempre que no sean redefinidas en un ámbito más restringido.

Esto quiere decir que lasvariables globales  pueden  ser  utilizadas  y  modificadas  por  cualquier
función o bloque de código en el programa, siempre que se haga referencia a ellas correctamente. Por
otro lado, el ámbito "local" se refiere a variables y funciones definidas dentro de  una  función  o
bloque específico, lo que limita su visibilidad únicamente a ese  contexto.  Esto  permite  que  las
variables locales puedan tener el mismo nombre que las globales sin  interferir  entre  sí,  ya  que
operan en espacios de memoria diferentes.

El ámbito global es útil para almacenar información que debe ser compartida entre diferentes  partes
del programa, pero su uso excesivo  puede  dificultar  el  mantenimiento  del  código,  ya  que  las
variables globales pueden ser modificadas desde  cualquier  lugar,  lo  que  aumenta  el  riesgo  de
errores. Por el contrario, las variables locales son ideales para  encapsular  datos  que  solo  son
relevantes dentro de una función, lo que mejora la modularidad y reduce la probabilidad  de  efectos
secundarios no deseados.

Python permite modificar  variables  globales  dentro  de  funciones  utilizando  la  palabra  clave
"global", lo que indica que la variable referenciada pertenece al ámbito global y  que  no  se  debe
crear una nueva variable local. Asimismo, en el caso de  funciones  anidadas,  se  puede  acceder  y
modificar variables locales de funciones externas (pero no globales)  utilizando  la  palabra  clave
"nonlocal". Esto es especialmente útil para mantener el estado entre llamadas a  funciones  internas
sin necesidad de recurrir a variables globales.  Es  importante  saber  que  con  la  palabra  clave
"nonlocal" podemos modificar variables de un ámbito  superior,  pero  no  del  ámbito  global.  Esto
significa que "nonlocal" solo afecta variables definidas en una función externa cercana, y no  puede
modificar variables globales ni variables de ámbitos más alejados en la jerarquía.

Por último, comprender cómo Python maneja los ámbitos es fundamental para  escribir  código  limpio,
predecible y fácil de depurar. Al minimizar el uso de variables globales y aprovechar las  variables
locales y las funciones anidadas, se puede garantizar que cada parte del programa  opere  de  manera
independiente, reduciendo conflictos y mejorando la claridad del código. Además, el uso adecuado  de
los ámbitos permite evitar errores relacionados con  la  sobrescritura  accidental  de  variables  y
facilita la implementación de estructuras más complejas, como cierres (closures) y decoradores,  que
dependen del manejo correcto de los ámbitos en Python."""

# Ejemplo_ambito_global_y_local.py

# Explicación:
"""Definimos una variable global llamada "x" y le asignamos el  valor  "global".  Esta  variable  es
accesible desde cualquier parte del programa ya que está  definida  fuera  de  cualquier  función  o
bloque de código.

Definimos una función llamada "ambito()" que no recibe parámetros. Para ello, utilizamos la  palabra
clave "def" seguida del nombre de la función, en este caso "ambito()", seguido de paréntesis  vacíos
() ya que no recibe parámetros, y terminamos con dos puntos (:) para indicar el inicio del bloque de
código asociado a la función.

Dentro de la función, definimos una variable local llamada "x" con el valor "local".  Esta  variable
solo es accesible dentro del ámbito de la función "ambito()", ya que  está  definida  dentro  de  la
función. Además, la variable local "x" tiene el mismo  nombre  que  la  variable  global,  pero  son
independientes entre sí ya que están en diferentes  ámbitos  y  además  tienen  diferentes  valores.
Colocamos esta instrucción con una indentación de cuatro espacios desde  el  margen  izquierdo  para
indicar que forma parte del cuerpo de la función y  debe  ejecutarse  siempre  que  la  función  sea
llamada.

A continuación, dentro de la función, utilizamos la instrucción "print()" para mostrar el  valor  de
la variable local "x" en la consola  cuando  la  función  sea  llamada,  acompañado  de  un  mensaje
descriptivo en formato "f-string". Colocamos esta instrucción con una indentación de cuatro espacios
desde el margen izquierdo para indicar que forma parte del cuerpo de la función  y  debe  ejecutarse
siempre que la función sea llamada.

Luego, llamamos a la función "ambito()" para ejecutar el código asociado dentro de ella. Para llamar
a la función, simplemente escribimos su nombre seguido de  paréntesis  vacíos  ya  que  no  requiere
argumentos, en este caso "ambito()". Esto indica al intérprete que debe ejecutar el bloque de código
asociado a la función, mostrando así el mensaje en la consola gracias  a  la  instrucción  "print()"
dentro de ella. Colocamos la llamada a la función sin indentación, ya que se encuentra en  el  nivel
principal del código y no forma parte de ninguna otra estructura.

Por último, utilizamos de nuevo la instrucción "print()" para mostrar el valor de la variable global
"x" en la consola, acompañado de un mensaje descriptivo en formato "f-string". Al  referirnos  a  la
variable global "x" fuera de la función, estamos accediendo a la variable definida al principio  del
código, cuyo valor es "global" y no a la variable local "x" definida dentro de la función,  la  cual
solo es accesible dentro de esa función. Colocamos esta  instrucción  sin  indentación,  ya  que  se
encuentra en el nivel principal del código y no forma parte de ninguna otra estructura. Al  ejecutar
esta línea después de llamar a la función, se mostrará el valor de la  variable  global  "x"  en  la
consola, además del valor de la variable local "x" impreso dentro de la función."""

# Código:
x = "global"

def ambito():
    x = "local"
    print(f"Esta es la variable x {x}")

ambito()
print(f"Esta es la variable x {x}")

# Nota Importante:
"""En este ejemplo, la variable "x" se  define  como  "global"  al  principio  del  código,  lo  que
significa que está disponible en todo el programa fuera de cualquier función. Dentro de  la  función
"ambito()", se define una nueva variable local "x" con el mismo  nombre,  pero  esta  variable  solo
existe dentro del ámbito de la función. Cuando se llama a la función "ambito()", se imprime el valor
de la variable local "x", ya que esta es "local". Sin embargo, al salir de la función,  la  variable
local deja de existir y el programa vuelve a referirse a la  variable  global  "x",  cuyo  valor  es
"global". Esto demuestra cómo Python maneja los diferentes ámbitos y cómo las  variables  locales  y
globales pueden coexistir sin interferir entre sí.

Es importante destacar que las variables locales tienen prioridad sobre las globales  dentro  de  su
ámbito. Esto significa que, si una variable local y  una  global  tienen  el  mismo  nombre,  Python
utilizará la variable local dentro de la función o bloque donde está definida. Por otro lado, si  se
necesita  modificar  una  variable  global  dentro  de  una  función,  debemos  referirnos  a   ella
explícitamente con la palabra clave "global". Sin  esta  referencia,  Python  asumirá  que  se  está
creando una nueva variable local con el mismo nombre, lo que puede llevar a  resultados  inesperados
si se intenta modificar el valor de la variable global.

Además, las dos variables definidas en este ejemplo son independientes entre sí, ya que pertenecen a
diferentes ámbitos. La variable local "x" solo existe dentro de la función "ambito()", mientras  que
la variable global "x" está disponible en todo el programa. Esto permite que ambas variables  tengan
el mismo nombre sin causar conflictos, lo que es una característica útil  en  la  programación  para
evitar colisiones de nombres y mantener el código  organizado.  Sin  embargo,  es  importante  tener
cuidado al utilizar nombres de variables similares en diferentes ámbitos para evitar  confusiones  y
errores involuntarios. Si es posible,  es  recomendable  utilizar  nombres  de  variables  únicos  y
distintos para mejorar la legibilidad del código.

En el caso de funciones anidadas, Python permite modificar variables locales de  funciones  externas
utilizando la palabra clave "nonlocal". Esto es útil cuando se  necesita  que  una  función  interna
acceda y modifique una variable definida en una función externa, pero sin afectar el ámbito  global.
Sin embargo, tanto el uso de "global" como "nonlocal" debe ser limitado y bien justificado,  ya  que
puede introducir efectos secundarios difíciles de rastrear.  Es  preferible  diseñar  el  código  de
manera que minimice la dependencia de variables globales y maximice el uso de parámetros  y  valores
de retorno para compartir información entre funciones.

Por último, el manejo adecuado de los ámbitos en Python es esencial  para  evitar  conflictos  entre
variables, garantizar la independencia de las funciones y mantener el código más limpio y  fácil  de
depurar. Al comprender cómo  funcionan  los  ámbitos  y  utilizar  las  palabras  clave  "global"  y
"nonlocal" de manera responsable, se puede escribir código más robusto y  mantenible.  Además,  este
conocimiento es clave para implementar patrones de diseño  avanzados  y  aprovechar  al  máximo  las
capacidades del lenguaje, como el uso de cierres (closures) y decoradores, que dependen de un manejo
preciso de los ámbitos."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
