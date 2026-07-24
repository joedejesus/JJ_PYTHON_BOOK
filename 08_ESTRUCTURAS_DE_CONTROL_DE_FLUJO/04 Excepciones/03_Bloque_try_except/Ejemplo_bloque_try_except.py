# Enunciado:
"""El bloque "try-except" en Python es una estructura de control de flujo que  permite  ejecutar  un
bloque de código y manejar los errores que puedan ocurrir durante su ejecución. El bloque de  código
se encierra entre las palabras clave "try" y "except".

El bloque "try" se utiliza para encapsular el código que puede generar una excepción,  mientras  que
el bloque "except" se encarga de capturar y manejar dichas  excepciones.  Si  no  se  genera  ningún
error, el bloque "except" no se ejecuta.

En caso de que se genere un error, el bloque "except"  se  ejecuta  para  manejarlo,  ejecutando  el
bloque de código asociado  al  error  específico.  Esto  asegura  que  el  programa  no  se  detenga
abruptamente y pueda continuar su ejecución o finalizar de manera controlada.  En  ambos  casos,  el
bloque de código asociado podrá ser cualquier código válido en Python, siempre y cuando  respete  la
indentación, la lógica y la  sintaxis  correspondientes,  con  el  objetivo  de  manejar  errores  y
excepciones.

Además, Python permite manejar diferentes tipos de excepciones de manera específica, lo  que  brinda
flexibilidad para tratar cada error de forma adecuada. También es posible incluir múltiples  bloques
"except" para manejar distintos tipos de errores o incluso un bloque "except" genérico para capturar
cualquier excepción no prevista.

Esto es especialmente útil en programas que necesitan ser  robustos  y  no  detenerse  ante  errores
inesperados, como en aplicaciones críticas o sistemas que interactúan con el  usuario.  Al  capturar
errores específicos, el desarrollador puede proporcionar mensajes claros y acciones correctivas,  lo
que mejora la experiencia del usuario. Además, el uso adecuado  de  "try-except"  ayuda  a  prevenir
comportamientos inesperados y asegura que los recursos,  como  archivos  o  conexiones,  se  liberen
correctamente incluso en caso de error.

El bloque "try-except" actúa, en cierta manera, como un bloque  condicional  "if...elif...else",  ya
que permite ejecutar diferentes bloques de código dependiendo de si se produce una excepción o no se
produce. Así como en un bloque "if...elif...else" se evalúa una condición para decidir qué bloque de
código ejecutar, en un bloque "try-except" se intenta ejecutar un bloque de código y, si ocurre  una
excepción, se ejecuta el bloque de código correspondiente al manejo de esa excepción.  Esto  permite
que el programa  maneje  errores  de  manera  controlada  y  continúe  su  ejecución  sin  detenerse
abruptamente.

Es posible añadir condicionales dentro de un bloque "try-except" para generar  intencionalmente  una
excepción, manejarla y tomar una decisión basada en ella. Sin embargo, es importante destacar que la
principal función de este bloque es manejar excepciones y  errores  que  puedan  surgir  durante  la
ejecución  del  código,  en  lugar  de  evaluar   condiciones   lógicas,   como   en   los   bloques
"if...elif...else". Por ello, este mecanismo está enfocado en las entradas  del  usuario  y  en  los
errores inesperados que puedan surgir en tiempo de ejecución.  El  manejo  de  excepciones  no  solo
mejora la robustez del programa, sino que también facilita la  depuración  y  el  mantenimiento  del
código.

Por último, es importante destacar que la terminación "as x" en un bloque "except" permite  capturar
la excepción generada y asignarla a una variable (en este caso, "x"). Esto es útil para  acceder  al
mensaje de error o a otros atributos de la  excepción,  lo  que  facilita  proporcionar  información
detallada al usuario o realizar acciones específicas basadas en el error capturado."""

# Ejemplo_bloque_try_except.py

# Explicación:
"""Utilizamos un bloque "try-except" para manejar posibles  errores  al  solicitar  al  usuario  que
ingrese un número entero (int) y dividir el valor "100" entre el valor  ingresado  por  el  usuario.
Para ello, utilizamos la palabra clave "try" seguida de dos puntos (:) para  iniciar  el  bloque  de
código que intentaremos ejecutar.

Dentro del bloque "try", utilizamos la función "input()" para solicitar al usuario  que  ingrese  un
número entero (int) para dividir el valor "100" entre el valor ingresado. Para ello,  definimos  una
variable llamada "opcion_usuario", escribimos la palabra clave "input" seguida de paréntesis  ()  y,
dentro de estos, incluimos un mensaje o "prompt", el cual, al ejecutar el código, se mostrará en  la
consola indicando al usuario qué tipo de información se espera que ingrese. De esta forma, lo que el
usuario ingrese se guarda en la variable "opcion_usuario" como una cadena de texto (str) y  podremos
usarlo en el resto del código.

A continuación, definimos una variable llamada "resultado", a la cual asignamos el resultado  de  la
operación de división entre el valor  "100"  y  el  valor  ingresado  por  el  usuario.  Para  ello,
escribimos el valor "100", el cual será el dividendo, seguido del  operador  aritmético  (/)  y  del
divisor "int(opcion_usuario)", que en este caso es el  valor  ingresado  por  el  usuario,  el  cual
convertimos a un número entero  utilizando  el  constructor  "int()".  Además,  encerramos  toda  la
operación entre paréntesis (). El constructor toma como argumento la variable  "opcion_usuario",  la
cual contendrá el valor introducido por el usuario convertido a  entero  (int).  Esto  es  necesario
porque la función "input()" devuelve una cadena  de  texto  (str)  y,  para  realizar  la  división,
necesitamos un número; en este caso, un entero (int).

Además, utilizamos la función "print()" para mostrar el resultado de  la  división  en  la  consola,
acompañado de un mensaje en formato de "f-string"  para  dar  formato  a  la  salida.  Colocamos  el
contenido del bloque "try" con una indentación de cuatro espacios desde  el  margen  izquierdo  para
indicar que pertenece a este bloque y debe ejecutarse siempre que no se genere ninguna excepción.

Después del bloque "try", utilizamos dos bloques "except"  para  manejar  posibles  excepciones  que
puedan ocurrir durante la ejecución del código dentro del bloque "try".

En el primer bloque "except", capturamos la excepción "ValueError", que puede ocurrir si el  usuario
ingresa un valor no numérico, como letras o símbolos, o un valor  numérico  distinto  de  un  entero
(int). Esta excepción es una subclase de <class 'Exception'> y es una excepción específica para este
error. Para ello, escribimos la palabra clave "except" seguida del nombre de la excepción,  en  este
caso "ValueError", seguida de la terminación "as e" y dos puntos (:). De esta forma,  capturamos  la
excepción y la asignamos a la variable "e", la cual definimos en este momento, lo  que  nos  permite
acceder al mensaje de error asociado a la excepción.

Si se genera esta excepción, se ejecuta el bloque de código asociado a este bloque "except", el cual
es una instrucción "print()" que muestra un mensaje de error en formato "f-string", acompañado de la
variable "e", la cual contendrá el error, indicando así al  usuario  que  debe  ingresar  un  número
válido. Colocamos esta instrucción con una indentación de cuatro espacios desde el margen  izquierdo
para indicar que pertenece a  este  bloque  y  debe  ejecutarse  solo  si  se  genera  la  excepción
"ValueError".

Por último, en el segundo bloque "except", capturamos la excepción  "ZeroDivisionError",  que  puede
ocurrir si el usuario ingresa el valor "cero". Esta excepción es una subclase de <class 'Exception'>
y es una excepción específica para este error. Para  ello,  escribimos  la  palabra  clave  "except"
seguida del nombre de la excepción, en este caso "ZeroDivisionError", seguida de la terminación  "as
f" y dos puntos (:). De esta forma, capturamos la excepción y la asignamos a  la  variable  "f",  la
cual definimos en este momento, lo que nos permite  acceder  al  mensaje  de  error  asociado  a  la
excepción.

Si se genera esta excepción, se ejecuta el bloque de código asociado a este bloque "except", el cual
es una instrucción "print()" que muestra un mensaje de error en formato "f-string", acompañado de la
variable "f", la cual contendrá el error, indicando así al usuario que no se puede dividir por cero.
Colocamos esta instrucción con una indentación de cuatro espacios desde  el  margen  izquierdo  para
indicar  que  pertenece  a  este  bloque  y  debe  ejecutarse  solo  si  se  genera   la   excepción
"ZeroDivisionError"."""

# Codigo:
try:
    opcion_usuario = input("Ingrese un número entero (int) para dividir 100 entre ese número: ")
    resultado = (100 / int(opcion_usuario))
    print(f"El resultado de la división es: {resultado}")

except ValueError as e:
    print(f"Error: {e}. Debe ingresar un número válido.")

except ZeroDivisionError as f:
    print(f"Error: {f}. No se puede dividir por cero.")

# Nota Muy Importante:
"""El bloque "try" contiene instrucciones  que  pueden  generar  errores,  mientras  que  el  bloque
"except" maneja las excepciones que puedan ocurrir. Si no se genera ningún error, el bloque "except"
no se ejecuta. En caso de que se genere un error, el bloque  "except"  se  ejecuta  para  manejarlo,
ejecutando el bloque de código asociado al error específico. Esto asegura  que  el  programa  no  se
detenga abruptamente y pueda continuar su ejecución o finalizar de manera controlada.

Es importante destacar que el manejo de excepciones no solo mejora la robustez  del  programa,  sino
que también facilita la depuración y el mantenimiento del código. Al capturar  errores  específicos,
el desarrollador puede proporcionar mensajes  claros  y  acciones  correctivas,  lo  que  mejora  la
experiencia del usuario. Además, el uso adecuado de "try-except" ayuda  a  prevenir  comportamientos
inesperados y asegura que los recursos, como archivos o conexiones, se liberen correctamente incluso
en caso de error.

Además, cada clase de excepción tiene un propósito específico y se utiliza para  manejar  diferentes
tipos de errores que pueden ocurrir durante la ejecución de un programa. Por  ejemplo,  "ValueError"
se utiliza para manejar  casos  en  los  que  un  valor  no  es  del  tipo  esperado,  mientras  que
"ZeroDivisionError" se utiliza para manejar casos en  los  que  se  intenta  dividir  por  cero.  Al
capturar y manejar estas excepciones, es posible  crear  programas  más  robustos  y  resistentes  a
fallos, mejorando la experiencia del usuario y reduciendo el riesgo de errores críticos.  Por  ello,
es importante estudiar qué excepción usar en cada caso determinado.

Dentro del bloque "try" intentamos ejecutar un bloque de código que puede generar una excepción,  en
este caso la división entre "100" y el valor ingresado por el usuario.  Si  el  usuario  ingresa  un
valor no numérico, no entero o el valor "cero", se generará una excepción que será capturada por los
bloques "except" correspondientes, evitando que el programa se detenga abruptamente. Nos referimos a
"intentar" porque la palabra "try" en español significa "intentar" o "probar" y, en  este  contexto,
indica que estamos intentando ejecutar un bloque de código que puede generar una excepción.

Por último, es importante darse cuenta de que, en este ejemplo, estamos condicionando al  usuario  a
introducir un número válido, en este caso un entero (int), sin utilizar  estructuras  condicionales,
para evitar errores durante la ejecución del programa."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
