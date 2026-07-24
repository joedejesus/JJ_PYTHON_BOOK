# Enunciado:
"""Una función anidada en Python es una función definida dentro de otra función. Esto significa  que
la función "interna" está disponible en el ámbito local  de  la  función  "externa",  pero  no  está
disponible en el ámbito global. Este tipo de estructura es útil  para  encapsular  lógica  que  solo
tiene sentido dentro del contexto de la función externa, mejorando la modularidad y  la  legibilidad
del código. Además, las funciones anidadas pueden acceder a las  variables  locales  de  la  función
externa, lo que permite crear cierres (closures) que  capturan  y  recuerdan  el  estado  de  dichas
variables incluso  después  de  que  la  función  externa  haya  terminado  su  ejecución.  Esto  es
especialmente útil en situaciones donde se necesita mantener un estado  o  configuración  específica
sin recurrir a variables globales, lo que promueve un diseño más limpio y seguro.

Los conceptos de "externa" e "interna" se refieren a la relación jerárquica entre las funciones.  La
función externa es la que contiene a la función interna. La función interna solo puede  ser  llamada
desde dentro de la función externa, lo que limita su ámbito de visibilidad y  evita  conflictos  con
otras funciones o variables en el ámbito global o en otros ámbitos.  Esto  asegura  que  la  función
interna esté protegida de accesos no deseados,  reforzando  el  principio  de  encapsulación  en  la
programación.

Los conceptos de "global" y "local" se refieren a los ámbitos de  visibilidad  de  las  variables  y
funciones en Python. Las variables y funciones definidas en el ámbito global  son  accesibles  desde
cualquier parte del código, mientras que las variables y funciones  definidas  en  el  ámbito  local
(dentro de una función) solo son accesibles desde esa función. En el caso de las funciones anidadas,
la función interna tiene acceso a las variables y funciones definidas en su ámbito local, así como a
las variables y funciones definidas en el ámbito de la función externa. Además, la  función  interna
también puede acceder a las variables y funciones definidas en el ámbito global. Las palabras  clave
"global" y "nonlocal" se utilizan cuando se necesita modificar variables de esos  ámbitos  desde  la
función interna. Los conceptos de ámbito global y local se abordarán en  detalle  en  las  secciones
posteriores de este tema.

Además, los parámetros de la función externa también pueden ser  utilizados  dentro  de  la  función
interna. Esto significa que la función interna tiene acceso no solo a las variables  locales  de  la
función externa, sino también a los valores que se pasaron como argumentos a la función  externa  al
llamarla. Esto permite que la función  interna  utilice  estos  valores  para  realizar  cálculos  o
personalizar su comportamiento según sea necesario. Por otro  lado,  se  pueden  definir  parámetros
específicos para la función interna, que  solo  serán  accesibles  dentro  de  esa  función,  y  los
argumentos deben ser pasados cuando se llame a la función interna desde  la  función  externa.  Este
diseño permite una mayor flexibilidad y control sobre el flujo de datos entre las funciones.

El uso  de  funciones  anidadas  es  común  en  situaciones  donde  se  desea  ocultar  detalles  de
implementación o evitar que ciertas funciones sean accesibles fuera de un contexto específico.  Esto
promueve el principio de encapsulación, que es fundamental en la programación modular.  Además,  los
cierres permiten que las funciones internas "recuerden" el entorno en el que fueron creadas, lo  que
resulta útil para construir funciones dinámicas o mantener estados entre llamadas sin  necesidad  de
usar variables globales. Esta característica hace que las funciones anidadas  sean  una  herramienta
poderosa para diseñar código más limpio,  reutilizable  y  seguro.  Por  ejemplo,  los  cierres  son
ampliamente utilizados en patrones de  diseño  como  funciones  de  fábrica  (factory  functions)  o
decoradores.

Por último, las funciones anidadas también son útiles para reducir  la  complejidad  del  código  al
dividir tareas grandes en subtareas más pequeñas y manejables. Esto no solo mejora  la  organización
del código, sino que también facilita su depuración y mantenimiento. Sin embargo, no es recomendable
abusar de ellas para evitar complicaciones innecesarias en la lectura y el mantenimiento del código.
Un uso excesivo o mal diseñado de funciones anidadas puede dificultar la comprensión del  flujo  del
programa,  por  lo  que  es  importante  encontrar  un  equilibrio  adecuado  entre  modularidad   y
simplicidad."""

# Ejemplo_funciones_anidadas.py

# Explicación:
"""Definimos una función llamada "funcion_externa()" que no recibe parámetros. Para ello, utilizamos
la palabra clave "def" seguida del nombre de la función, en este caso "funcion_externa", seguido  de
paréntesis vacíos () ya que no recibe parámetros, y terminamos con dos puntos (:)  para  indicar  el
inicio del bloque de código asociado a la función externa.

Dentro de la función externa, utilizamos la instrucción "print()" para  mostrar  un  mensaje  en  la
consola. Colocamos esta instrucción con una indentación de cuatro espacios desde el margen izquierdo
para indicar que forma parte del cuerpo de la función externa  y  debe  ejecutarse  siempre  que  la
función sea llamada.

A  continuación,  dentro  de  la  función   externa,   definimos   una   función   anidada   llamada
"funcion_interna()" que tampoco recibe parámetros. Para ello,  utilizamos  la  palabra  clave  "def"
seguida del nombre de la función, en este caso "funcion_interna", seguido de paréntesis vacíos () ya
que no recibe parámetros, y terminamos con dos puntos (:) para  indicar  el  inicio  del  bloque  de
código asociado a la función interna. Colocamos esta función con una indentación de cuatro  espacios
desde el margen izquierdo para indicar que forma parte del cuerpo de la función externa.  Su  código
solo estará disponible cuando la función externa sea llamada.

Dentro de la función interna, utilizamos nuevamente la instrucción "print()" para mostrar un mensaje
en la consola. Colocamos esta instrucción con una indentación de cuatro  espacios  desde  la  propia
función interna para indicar que forma parte del cuerpo de la función interna y se ejecutará siempre
que la función interna sea llamada.

Luego, llamamos a la función interna dentro de la función externa para ejecutar su código  asociado.
Para llamar a la función, simplemente escribimos su nombre seguido de paréntesis vacíos, ya  que  no
recibe parámetros, en este caso "funcion_interna()". Esto  asegura  que  el  código  de  la  función
interna se ejecute cada vez que se llame a la función  externa  desde  fuera  de  su  definición  en
cualquier parte del código. Colocamos esta llamada con una indentación de cuatro espacios  desde  el
margen izquierdo para indicar que forma parte del cuerpo  de  la  función  externa  y  se  ejecutará
siempre que la función externa sea llamada.

Por último, fuera de la definición de las funciones, llamamos a la función externa para ejecutar  su
código. Para llamar a la función, simplemente escribimos su nombre seguido de paréntesis vacíos,  ya
que no recibe parámetros, en este caso "funcion_externa()". Esto inicia la ejecución de  la  función
externa, que a su vez llama a la función interna, ejecutándola y  mostrando  ambos  mensajes  en  la
consola gracias a las instrucciones "print()" dentro de cada función.

Además, añadimos una supuesta llamada a la función interna de la misma forma y  con  la  indentación
correspondiente, pero la comentamos con una almohadilla (#) para evitar  errores  de  ejecución.  De
esta forma, si borramos el comentario y ejecutamos el código, obtendremos un error  de  "NameError",
ya que la función interna no está definida en el ámbito global.

De esta forma demostramos que la función interna no puede ser llamada  desde  fuera  de  la  función
externa, ya que su ámbito está limitado al cuerpo de la función externa. Además, la función  interna
en este caso forma parte de la lógica asociada a la función externa y  se  ejecuta  solo  cuando  se
llama a la función externa. Esto asegura que la lógica  interna  esté  encapsulada  y  protegida  de
accesos externos, reforzando el principio de encapsulación en la programación. Debemos fijarnos  muy
bien en la indentación  para  entender  claramente  los  ámbitos  de  cada  función  y  su  relación
jerárquica."""

# Código:
def funcion_externa():
    print("Esta es la función externa.")

    def funcion_interna():
        print("Esta es la función interna.")

    funcion_interna()

funcion_externa()
# funcion_interna()  # Esto generaría un error de "NameError" si se descomenta y se ejecuta.

# Nota Importante:
"""La función interna no puede llamarse desde fuera de la función externa, ya  que  su  ámbito  está
limitado a la función externa. Esto significa que la función interna  es  privada  para  la  función
externa y no puede ser accedida directamente desde el ámbito global o desde  otras  funciones.  Esto
asegura que la lógica interna de  la  función  externa  esté  protegida  y  no  pueda  ser  alterada
accidentalmente desde otros contextos. Este comportamiento es útil para mantener la integridad y  la
seguridad del código, especialmente en aplicaciones grandes o críticas.

En este ejemplo conseguimos que la función interna se ejecute cuando se llama a la  función  externa
porque llamamos a la función interna dentro del cuerpo de la función externa  y,  de  ese  modo,  se
ejecuta cuando se llama a la función externa. Sin embargo, si intentamos llamar a la función interna
desde fuera de la función externa, obtendremos un error de  tipo  "NameError",  ya  que  la  función
interna no está definida en el ámbito global. Del mismo modo, si no llamamos a  la  función  interna
dentro de la función externa, esta no se ejecutará cuando llamemos a la función externa.

Además, existe un concepto relacionado llamado "cierre" (closure), que  ocurre  cuando  una  función
interna recuerda el entorno en el que fue creada, incluso después de que  la  función  externa  haya
terminado su ejecución. Esto permite que la función interna siga teniendo  acceso  a  las  variables
locales de la función externa, incluso cuando se invoca desde fuera de su ámbito original  a  través
del valor devuelto por la función  externa.  Los  cierres  son  particularmente  útiles  para  crear
funciones dinámicas que mantienen un estado interno o  para  implementar  patrones  de  diseño  como
decoradores y funciones de fábrica. Por ejemplo, un cierre puede ser usado  para  generar  funciones
personalizadas basadas en parámetros específicos, lo que mejora la reutilización del código.

Por último, es importante destacar que el uso  de  cierres  también  puede  ayudar  a  optimizar  el
rendimiento del programa al evitar la creación de variables globales innecesarias. Sin  embargo,  su
uso debe ser cuidadoso, ya que un diseño inadecuado puede llevar a un código difícil de  entender  o
mantener. Por lo tanto, es fundamental comprender bien el funcionamiento de las funciones anidadas y
los cierres antes de aplicarlos en proyectos complejos. Una buena práctica es documentar  claramente
el propósito y el  comportamiento  de  las  funciones  anidadas  para  facilitar  su  comprensión  y
mantenimiento a largo plazo. El concepto de cierres (closures) se abordará en las próximas secciones
de este tema."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
