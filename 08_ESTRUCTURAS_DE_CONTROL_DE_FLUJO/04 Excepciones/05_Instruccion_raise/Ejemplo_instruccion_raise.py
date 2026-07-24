# Enunciado:
"""En Python, la instrucción "raise" se utiliza para generar una excepción de manera  explícita.  La
palabra "raise" significa "elevar" en inglés y es una forma de generar una excepción intencional  en
el código. En programación, una excepción es un evento que interrumpe el flujo normal  de  ejecución
de un programa debido a un error o a un comportamiento inesperado.

Las excepciones nos permiten manejar situaciones que no se pueden prever durante el  desarrollo  del
software, como errores de entrada del usuario, problemas de  red  o  archivos  inexistentes.  Cuando
utilizamos "raise" en Python, estamos creando intencionalmente una excepción para señalar  que  algo
no está funcionando como se espera.

Esto es útil para validar condiciones específicas en el  programa  y  proporcionar  mensajes  claros
sobre el problema. Por ejemplo, en un juego, podríamos utilizar la instrucción "raise" para  generar
una excepción si el usuario selecciona una opción incorrecta, lo que permite  manejar  el  error  de
manera controlada y evitar que el programa falle inesperadamente.

El uso de "raise" también es fundamental para implementar validaciones personalizadas en el  código.
Por ejemplo, si una función recibe un argumento que no cumple con los requisitos esperados,  podemos
usar "raise" para generar una excepción con un mensaje descriptivo que indique el problema. Esto  no
solo mejora la claridad del código, sino que también facilita la depuración y el  mantenimiento,  ya
que los errores se detectan y manejan de manera explícita.

Además, "raise" puede utilizarse para propagar excepciones hacia niveles  superiores  del  programa,
permitiendo que otros bloques de código manejen el error según sea necesario. En resumen, "raise" es
una herramienta poderosa para garantizar que el programa se comporte de manera predecible y  robusta
incluso en situaciones inesperadas."""

# Ejemplo_instruccion_raise.py

# Explicación:
"""Utilizamos el bucle "while" para ejecutar un bloque de código mientras se cumpla  una  condición.
Para ello, escribimos la palabra clave "while", seguida de la condición entre paréntesis y terminada
con dos puntos (:). La condición en este caso es el valor booleano "True", lo que significa  que  el
bucle se ejecutará indefinidamente hasta que se encuentre una instrucción "break" dentro del  bloque
de código asociado al bucle. La instrucción "break" se  utiliza  para  salir  del  bucle  cuando  se
cumplen ciertas condiciones. En este caso, la condición se dará  cuando  el  usuario  introduzca  el
valor 2, el cual corresponde al número secreto.

Dentro del bucle "while", utilizamos la función "input()" para solicitar al usuario que  ingrese  un
número entre 1 y 3 para adivinar el número secreto y, además, convertir la entrada del usuario en un
número entero (int).

Para ello, definimos una variable llamada "opcion_usuario", escribimos la función "input()"  seguida
de paréntesis () y, dentro de estos, incluimos un mensaje  o  "prompt",  el  cual,  al  ejecutar  el
código, se mostrará en la consola indicando al  usuario  qué  tipo  de  información  se  espera  que
ingrese. Además, encerramos todo el contenido de la función "input()" dentro del constructor "int()"
para convertir la entrada del usuario a un número entero (int).

De esta forma, lo que el usuario ingrese se guarda en la variable "opcion_usuario"  como  un  número
entero (int) y podremos usarlo en el resto del código. Convertimos  la  entrada  del  usuario  a  un
número entero (int) porque la función "input()"  devuelve  siempre  una  cadena  de  texto  (str)  y
necesitamos un número para realizar comparaciones numéricas más adelante en el código.

Dentro del bucle "while", utilizamos  un  bloque  "try-except"  para  manejar  posibles  errores  al
comparar el valor ingresado por el usuario con el número secreto, que es 2. El  bloque  "try-except"
nos permite intentar ejecutar un bloque de código y capturar cualquier excepción que  pueda  ocurrir
durante la ejecución de  ese  bloque.  En  este  caso,  el  bloque  "try"  contiene  el  código  que
intentaremos ejecutar, el cual incluye la lógica de comparación del número ingresado por el  usuario
con el número secreto. Para ello, utilizamos la palabra clave "try" seguida de dos puntos  (:)  para
iniciar el bloque de código que intentaremos ejecutar. Colocamos la  palabra  clave  "try"  con  una
indentación de cuatro espacios desde el margen izquierdo para indicar que  pertenece  al  bloque  de
código asociado al bucle "while" y debe intentar ejecutarse en cada iteración del bucle.

Dentro del bloque "try", utilizamos el condicional "if" para evaluar si  el  valor  de  la  variable
"opcion_usuario" es igual a 1 o a 3. Para ello, escribimos la palabra  clave  "if"  seguida  de  las
condiciones entre paréntesis, separadas por el operador lógico "or", y  terminadas  con  dos  puntos
(:). La primera condición se compone de la variable "opcion_usuario", el operador de igualdad (==) y
el valor 1. La segunda condición se compone de la variable "opcion_usuario", el operador de igualdad
(==) y el valor 3.

Si alguna de las condiciones se cumple (si el valor de la variable "opcion_usuario" es igual a 1 o a
3), se lanza la excepción intencional "ValueError" utilizando la instrucción "raise" y mostrando  un
mensaje personalizado que indica que el usuario no ha adivinado el número secreto y debe  intentarlo
de nuevo.

Esta excepción será capturada por el bloque "except". Para ello, escribimos la palabra clave "raise"
seguida del nombre de la excepción, en este caso  "ValueError",  y  entre  paréntesis  incluimos  el
mensaje personalizado que queremos mostrar al usuario. Colocamos  la  instrucción  "raise"  con  una
indentación de cuatro espacios desde el propio condicional "if" para indicar que pertenece al bloque
de código asociado a este condicional y debe  ejecutarse  solo  si  se  cumple  alguna  de  las  dos
condiciones asociadas al condicional "if".

A continuación,  utilizamos  el  condicional  "elif"  para  evaluar  si  el  valor  de  la  variable
"opcion_usuario" es igual a 2. Para ello, escribimos la palabra clave "elif" seguida de la condición
entre paréntesis  y  terminada  con  dos  puntos  (:).  La  condición  se  compone  de  la  variable
"opcion_usuario", el operador de igualdad (==) y el valor 2. Si la condición se cumple (si el  valor
de la variable "opcion_usuario" es igual a 2), se imprime un mensaje en  la  consola  utilizando  la
función "print()", el cual corresponde al bloque de código  asociado  al  condicional  "elif".  Este
mensaje indica que el usuario ha acertado el número secreto y le felicita por ello.

Además, utilizamos la instrucción "break" asociada  al  condicional  "elif"  para  salir  del  bucle
"while" una vez que  el  usuario  ha  adivinado  correctamente  el  número  secreto.  Colocamos  las
instrucciones "print()" y "break" con una indentación de cuatro espacios desde el propio condicional
"elif" para indicar que pertenecen  al  bloque  de  código  asociado  a  este  condicional  y  deben
ejecutarse solo si se cumple la condición del condicional "elif".

Para completar el bloque "try", utilizamos el condicional "else" para manejar el caso en el  que  el
valor de la variable "opcion_usuario" sea cualquier  valor  diferente  de  1,  2  o  3.  Para  ello,
escribimos la palabra clave "else" seguida de dos puntos (:). Si la condición se cumple (si el valor
de la variable "opcion_usuario" es cualquier valor diferente de 1, 2 o 3),  se  lanza  la  excepción
intencional "ValueError" utilizando la instrucción "raise" y mostrando un mensaje personalizado  que
indica que el usuario ha ingresado una opción no válida.

Esta excepción será capturada por el bloque "except". Para ello, escribimos la palabra clave "raise"
seguida del nombre de la excepción, en este caso  "ValueError",  y  entre  paréntesis  incluimos  el
mensaje  personalizado  que  queremos  mostrar  al  usuario.  Colocamos  esta  instrucción  con  una
indentación de cuatro espacios desde el propio condicional "else"  para  indicar  que  pertenece  al
bloque de código asociado a este condicional y debe ejecutarse solo si se cumple  la  condición  del
condicional "else".

Colocamos el bloque de condicionales asociado al bloque "try" con una indentación de  ocho  espacios
desde el margen izquierdo para indicar que pertenece al bloque de código asociado al bloque "try"  y
debe intentar ejecutarse en cada iteración del bucle "while", siempre que no se genere una excepción
dentro de este bloque.

Luego, después  del  bloque  "try",  utilizamos  un  bloque  "except"  para  capturar  las  posibles
excepciones generadas intencionalmente con la instrucción "raise" dentro del bloque "try", ya sea la
excepción asociada al condicional "if" o al "else". El  bloque  "except"  nos  permite  manejar  las
excepciones que puedan ocurrir durante la ejecución del código dentro del bloque "try".

Para ello, escribimos la palabra clave "except" seguida del nombre  de  la  excepción  que  queremos
capturar, en este caso "ValueError", seguida de la terminación "as e" y  terminada  con  dos  puntos
(:). De esta forma, capturamos la excepción "ValueError" y la asignamos a la variable "e" para poder
acceder a los mensajes  personalizados  que  hemos  definido  al  generar  las  excepciones  con  la
instrucción "raise" dentro del bloque "try" en  ambos  condicionales.  Colocamos  la  palabra  clave
"except" con una indentación de cuatro espacios desde el margen izquierdo para indicar que pertenece
al bloque de código asociado al bucle "while" y debe ejecutarse en cada iteración del bucle, siempre
que se genere una excepción "ValueError" dentro del bloque "try".

Si se genera una excepción "ValueError" dentro del bloque "try", se  ejecuta  el  bloque  de  código
asociado a este bloque "except", el cual contiene una instrucción "print()" que muestra  el  mensaje
correspondiente a la excepción capturada y los detalles del error.  Además,  usamos  la  instrucción
"continue" para pasar a la siguiente iteración del bucle "while"  y  permitir  al  usuario  intentar
adivinar el número secreto nuevamente. Colocamos ambas instrucciones "print()" y "continue" con  una
indentación de cuatro espacios desde la palabra clave "except" para indicar que pertenecen al bloque
de código asociado a este bloque "except" y  deben  ejecutarse  solo  si  se  genera  una  excepción
"ValueError" dentro del bloque "try".

Por último, utilizamos la función "print()" para mostrar un mensaje que indica el fin del  programa.
Colocamos esta instrucción sin indentación, es decir, pegada al margen izquierdo  del  código,  para
indicar que debe ejecutarse una vez que se rompa el bucle "while" con la instrucción "break"."""

# Código:
while (True):

    opcion_usuario = int(
        input("Selecciona un número entre 1 y 3 para adivinar el número secreto: "))

    try:
        if (opcion_usuario == 1) or (opcion_usuario == 3):
            raise ValueError("No has adivinado el número secreto. Inténtalo de nuevo.")
        elif (opcion_usuario == 2):
            print("Has acertado el número secreto. ¡Felicidades!")
            break
        else:
            raise ValueError("Opción inválida. Por favor, selecciona un número entre 1 y 3.")

    except ValueError as e:
        print(f"Error: {e}.")
        continue

print("Fin del programa.")

# Nota Importante:
"""Con el uso de "raise" generamos una excepción incluso cuando no hay un  error  específico  en  el
código, pero queremos manejar una situación particular que  consideramos  incorrecta  o  inesperada.
Esto nos permite personalizar el comportamiento  del  programa  y  proporcionar  mensajes  claros  y
específicos al usuario. En este caso, si el usuario ingresa una opción que no  es  la  correcta,  en
este caso diferente de 2, se genera una excepción "ValueError"  con  un  mensaje  personalizado  que
indica que la opción es inválida. Esto ayuda a que el usuario entienda mejor  el  problema  y  pueda
corregir su entrada.

"ValueError" es una excepción predefinida en Python que se utiliza para indicar que una  función  ha
recibido un argumento con el tipo correcto pero con un valor inapropiado. En  este  ejemplo,  usamos
"raise" para generar un "ValueError" cuando la opción seleccionada por el usuario no está dentro del
rango esperado (1, 2 o 3).

Esto es útil porque no existe una excepción predefinida específica para este  caso,  y  "raise"  nos
permite crear una excepción personalizada que se ajuste a  nuestras  necesidades.  De  esta  manera,
podemos manejar errores de entrada de forma más precisa y controlada, mejorando la  experiencia  del
usuario y la robustez del programa.

Además, el uso de "raise" en combinación con bloques "try-except" permite  capturar  y  manejar  las
excepciones de manera estructurada. Esto asegura que el programa no se detenga abruptamente ante  un
error, sino que pueda continuar ejecutándose de manera controlada. Por ejemplo,  en  este  caso,  el
bloque "except" captura las excepciones generadas por "raise" y muestra mensajes claros al  usuario,
permitiéndole corregir su entrada y volver a intentarlo. Esto es  especialmente  útil  en  programas
interactivos, donde la experiencia del usuario es una prioridad.

Es importante destacar que "raise" no solo se limita a excepciones predefinidas  como  "ValueError".
También esposible definir nuestras propias excepciones personalizadas creando clases que hereden  de
la clase base "Exception". Esto nos permite adaptar las excepciones a las necesidades específicas de
nuestro programa, proporcionando aún más flexibilidad y control sobre cómo se manejan  los  errores.
En resumen, "raise" es una herramienta esencial para escribir  código  robusto,  claro  y  fácil  de
mantener, ya que nos permite manejar errores de manera explícita y controlada.

Por último, cabe aclarar que en este ejemplo usamos la excepción "ValueError" simplemente  como  una
muestra de cómo utilizar la instrucción "raise" para generar excepciones intencionales en el código,
ya que esta excepción es la que mejor se adapta a este caso. En situaciones reales, es  posible  que
se utilicen diferentes tipos de excepciones según el  contexto  y  los  requisitos  específicos  del
programa. Utilizar excepciones específicas es una buena práctica  que  puede  ayudar  a  mejorar  la
claridad del código y facilitar la depuración y el mantenimiento del mismo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
