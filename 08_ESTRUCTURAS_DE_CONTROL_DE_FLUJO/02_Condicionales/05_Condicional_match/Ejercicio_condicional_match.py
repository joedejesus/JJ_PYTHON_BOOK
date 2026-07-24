# Enunciado:
"""Escribe un programa que solicite al usuario ingresar un número del 1 al  11.  Utiliza  un  bloque
"match" para verificar la entrada y proporcionar una respuesta adecuada dependiendo  de  la  entrada
del usuario. Si el número ingresado está en el rango principal (1-5) definido internamente como  una
variable, informa al usuario del número que ingresó.

Si el número ingresado no está en el rango principal, verifica si pertenece a  un  rango  secundario
(7-11) definido internamente como una variable e informa al usuario en consecuencia con la ayuda  de
un condicional "if" asociado al caso comodín utilizando el operador de pertenencia "in".

Si el usuario ingresa un número que no pertenece a ninguno de los rangos, informa al usuario que  el
número no está en ninguno de los rangos con la ayuda de  un  condicional  "else"  asociado  al  caso
comodín; este actuará como un "default". Los rangos deben estar definidos internamente en  forma  de
listas con elementos numéricos literales y separados por comas.

Por último, no se debe mostrar al usuario ninguno de los rangos  ya  que  la  información  debe  ser
transmitida mediante la función "input()". Por último, el programa debe finalizar con un mensaje que
indique "Fin del programa"."""

# Ejercicio_condicional_match.py

# Explicación:
"""Definimos una variable llamada "rango_principal" y le  asignamos  una  lista  con  una  serie  de
números del 1 al 5. Esta lista es meramente orientativa y no se utiliza en  el  código  ya  que  los
casos literales coinciden con los números del 1 al 5, los cuales se  encuentran  en  la  lista.  Sin
embargo, es necesario definirla para cumplir con el enunciado del ejercicio.

Además, definimos una segunda variable llamada "rango_secundario" y le asignamos otra lista con  una
serie de números del 7 al 11. Esta última lista se utilizará posteriormente  en  el  bloque  "match"
como una lista secundaria para verificar si el número ingresado se encuentra en un conjunto definido
internamente. Esta lista es necesaria para verificar si el número  ingresado  por  el  usuario  está
fuera del rango principal pero pertenece al rango secundario.

Utilizamos la función "input()" para solicitar al usuario que elija un número  del  1  al  11.  Para
ello, definimos una variable llamada "opcion_usuario", escribimos la palabra clave  "input"  seguida
de paréntesis (), y dentro de estos incluimos un mensaje o "prompt" que se mostrará  en  la  consola
indicando qué tipo de información se espera.

Como la función "input()" devuelve un valor de tipo string (str), usamos el constructor "int()" para
convertir esa entrada en un número entero, encerrando la función "input()" dentro de los  paréntesis
del constructor "int()", el cual colocamos justo antes de  la  función  "input()".  De  esta  forma,
obtenemos un valor de tipo entero (int) que podremos utilizar en  el  bloque  "match",  cuyos  casos
están definidos con números enteros.

Luego, utilizamos un bloque "match" para comparar si el valor ingresado por el usuario coincide  con
alguno de los casos para así ejecutar el bloque de código asociado al caso coincidente.  Para  ello,
escribimos la palabra clave "match" seguida de la variable  "opcion_usuario"  y  terminada  con  dos
puntos (:). Esto indica que el bloque "match" se asociará a la variable  "opcion_usuario",  la  cual
contiene el valor ingresado por el usuario.

A continuación, utilizamos la palabra clave "case" para definir la lista de  casos  posibles  dentro
del bloque "match". Para ello, escribimos la palabra clave "case" con una indentación de 4  espacios
desde el margen izquierdo, seguida del valor que queremos comparar y dos puntos (:). El  valor  debe
estar escrito tal y como  esperamos  que  sea  ingresado  por  el  usuario  y  coincidiendo  con  la
información proporcionada a través de la función "input()".

Añadimos un caso para cada número del 1 al 5. A cada uno de estos casos le asociamos  un  bloque  de
código que se ejecutará si la opción del usuario  coincide.  En  cada  caso,  el  bloque  de  código
asociado es una instrucción "print()" que muestra un mensaje en la consola indicando qué  número  se
ha ingresado. Este bloque de código se coloca en cada caso justo debajo de la palabra clave "case" y
con una indentación de 4 espacios desde la propia palabra clave "case".

Por último, añadimos un caso comodín, el cual se ejecutará  solo  si  no  hay  ninguna  coincidencia
previa,  para  manejar  todas  las  demás  entradas  que  no  coincidan  con  los  casos   definidos
anteriormente. Para ello, escribimos la palabra clave "case" seguida de un  guion  bajo  (_)  y  dos
puntos (:). Colocamos el caso comodín al final de la lista de casos posibles, con una indentación de
4 espacios desde el margen izquierdo.

A este caso se le asocia un bloque condicional "if...else" para verificar si el número ingresado por
el usuario pertenece al "rango_secundario" o no, con ayuda del operador "in", y se asocia un  bloque
de código a cada condicional que se ejecutará si la condición se cumple (si el  número  está  en  la
segunda lista), correspondiente al condicional "if" y otro bloque de código que se ejecutará  si  la
condición no se cumple (si el número no  está  en  la  segunda  lista  ni  en  los  casos  definidos
anteriormente), correspondiente al condicional "else".

En ambos casos, el bloque de código asociado es una instrucción "print()" que muestra un mensaje  en
la consola. Ambos bloques de código se colocan justo debajo de la palabra clave "if" o "else" y  con
una indentación de 4 espacios desde la propia palabra clave "if" o "else". En  este  caso,  como  la
variable "rango_secundario" contiene una lista de números enteros,  no  es  necesario  convertir  su
contenido a datos de tipo entero (int).

Finalmente, fuera del bloque "match", utilizamos la función "print()" que muestra  el  mensaje  "Fin
del programa" en la consola. Esta instrucción se coloca sin indentación, es decir,  al  mismo  nivel
que la palabra clave "match", para que se ejecute siempre al final del programa."""

# Código:
rango_principal = [1, 2, 3, 4, 5]

rango_secundario = [7, 8, 9, 10, 11]

opcion_usuario = int(input("Ingrese un número del 1 al 11: "))

match opcion_usuario:
    case 1:
        print("El número ingresado es 1")
    case 2:
        print("El número ingresado es 2")
    case 3:
        print("El número ingresado es 3")
    case 4:
        print("El número ingresado es 4")
    case 5:
        print("El número ingresado es 5")
    case _:
        if (opcion_usuario in rango_secundario):
            print(
                "El número está fuera del rango principal pero pertenece al rango secundario")
        else:
            print("El número no está en ninguno de los rangos")

print("Fin del programa")

# Nota Muy Importante:
"""El uso de la función "input()" siempre devuelve un valor de tipo string (str). Por lo  tanto,  si
se requiere comparar la entrada del usuario con valores de tipo entero (int), es necesario convertir
explícitamente la entrada utilizando el constructor "int()". Esto asegura que  los  tipos  de  datos
sean compatibles para la comparación en el bloque "match".

No es posible utilizar un único "input()" para manejar casos  que  involucren  diferentes  tipos  de
datos (por ejemplo, enteros y cadenas) sin realizar conversiones adicionales. Si se intenta comparar
directamente un string (str) con un entero (int), se generará un error de tipo.  Por  lo  tanto,  es
recomendable manejar cada tipo de dato por separado o realizar  conversiones  explícitas  según  sea
necesario.

Además, es importante destacar que la colocación del código afecta su ejecución. Si una  instrucción
depende de la entrada del usuario, debe  ubicarse  después  de  la  llamada  a  "input()"  y  de  la
conversión correspondiente. Por lo tanto, es fundamental estructurar el código de  manera  que  cada
entrada del usuario sea procesada antes de continuar con el siguiente bloque de lógica.

En el caso de querer manejar múltiples entradas en un solo bloque  "match",  se  puede  utilizar  el
operador de patrón "|" (or) para combinar varios casos en una sola línea. Por ejemplo, "case 1 | 2 |
3:" manejaría los casos 1, 2 y 3 en conjunto. Sin embargo, esto  puede  reducir  la  claridad  y  la
legibilidad del código, especialmente si se manejan muchos casos. Es preferible mantener  los  casos
separados para facilitar la comprensión y el mantenimiento del código.

Por último, el uso de patrones en el bloque "match"  debe  ser  claro  y  explícito.  Se  recomienda
utilizar patrones simples y legibles para evitar confusiones. Además, el caso comodín "case _:" debe
utilizarse como último recurso para manejar entradas que  no  coincidan  con  ningún  caso  definido
previamente. Esto asegura que el código sea  robusto  y  maneje  adecuadamente  todas  las  posibles
entradas del usuario."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
