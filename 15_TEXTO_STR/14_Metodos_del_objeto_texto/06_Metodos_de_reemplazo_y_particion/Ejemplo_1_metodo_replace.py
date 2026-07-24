# Enunciado:
"""El método ".replace()" en Python  se  utiliza  para  reemplazar  todas  las  apariciones  de  una
subcadena por otra dentro de  una  cadena  principal.  Además,  es  posible  limitar  el  número  de
reemplazos que se van a realizar, lo que permite un control más preciso sobre la  transformación  de
la cadena. Este método es útil para realizar modificaciones en cadenas de texto de manera  eficiente
y sencilla.

Este método toma una cadena de texto y reemplaza todas las apariciones de una subcadena especificada
como primer argumento por otra subcadena especificada también como  segundo  argumento,  devolviendo
una nueva cadena con los cambios realizados. Si se desea limitar el número de reemplazos,  se  puede
proporcionar un tercer argumento que indique el número máximo de reemplazos que se van a realizar.

Además, este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de
cadena literal, de variable que contenga texto  o  incluso  como  resultado  de  una  expresión  que
devuelva un texto. El método ".replace()" distingue entre mayúsculas y minúsculas, lo que  significa
que solo reemplazará las apariciones exactas de la subcadena especificada.

El método toma tres argumentos: la subcadena que se desea reemplazar,  la  nueva  subcadena  que  la
reemplazará y, opcionalmente, un número entero que indica el número máximo de reemplazos que se  van
a realizar. Si no se especifica el tercer argumento, el método reemplazará todas las apariciones  de
la subcadena en la cadena original. Tanto el primer como el segundo argumento son  obligatorios,  ya
que el método necesita saber qué subcadena se desea reemplazar y cuál es la nueva subcadena  que  se
utilizará para el reemplazo.

Es importante destacar que el método ".replace()" no modifica la cadena original, ya que las cadenas
en Python son inmutables. En su lugar, devuelve una nueva cadena con los reemplazos realizados. Esto
significa que, si se desea conservar el resultado, es necesario asignarlo a  una  nueva  variable  o
usarlo directamente en una operación posterior.

El método ".replace()" es útil para tareas como la limpieza de datos, la normalización de texto o la
corrección de errores tipográficos en cadenas de texto. Además, es  una  herramienta  poderosa  para
realizar transformaciones en cadenas de texto de manera rápida y eficiente.

Por último, el método ".replace()" permite reemplazar subcadenas dentro de una cadena  de  texto  de
manera flexible y eficiente, devolviendo una nueva cadena con los cambios realizados."""

# Ejemplo_1_metodo_replace.py

# Explicación:
"""Definimos una variable  llamada  "texto"  y  le  asignamos  una  cadena  de  texto  que  contiene
información sobre un individuo. Esta cadena de texto se utilizará para demostrar  el  funcionamiento
del método ".replace()".

A continuación, definimos una nueva variable llamada "texto_reemplazado" y le asignamos el resultado
de aplicar el método ".replace()" a la variable "texto"  con  tres  argumentos:  el  primero  es  la
subcadena que queremos reemplazar, en este caso "nombre". El  segundo  es  la  nueva  subcadena  que
queremos usar para reemplazar la subcadena original, en este caso "Joe", y el tercero es  el  número
máximo de reemplazos que se van a realizar, en este caso "1", lo que indica que solo se  reemplazará
la primera aparición de la subcadena "nombre" en la cadena original.

Para ello, escribimos el nombre de la variable seguido del nombre del método ".replace()" y,  dentro
de los paréntesis, pasamos los tres argumentos. Primero, la subcadena que  queremos  reemplazar,  la
cual especificamos exactamente como aparece en la cadena original; luego,  la  nueva  subcadena  que
queremos usar para el reemplazo, ambas entre comillas para indicar que  son  cadenas  de  texto;  y,
finalmente, el número 1 en forma de número entero para indicar que solo se  realizará  un  reemplazo,  
todo ello separado por comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" para indicar cómo se ha transformado el texto original.

De esta forma, hemos reemplazado la primera aparición de la subcadena "nombre"  por  "Joe",  dejando
intacta la segunda aparición de "nombre" en la cadena original y obteniendo una nueva cadena con los
cambios realizados."""

# Código:
texto = "Hola me llamo nombre y mi nombre solo tiene 3 letras."
texto_reemplazado = texto.replace("nombre", "Joe", 1)
print(f"El texto: {texto} Se ha transformado en: {texto_reemplazado}")

# Nota Importante:
"""Es fundamental tener en cuenta que el  método  ".replace()"  no  realiza  cambios  en  la  cadena
original, ya que las cadenas en Python son inmutables. Esto significa  que  siempre  se  genera  una
nueva cadena como resultado de su aplicación, dejando intacta la cadena original.

Si se desea almacenar el resultado del método ".replace()",  es  necesario  asignarlo  a  una  nueva
variable o usar directamente el resultado en una operación posterior. De lo contrario, el  resultado
de la transformación se perderá.

En este caso, el primer y el segundo argumento del método se suelen  pasar  como  cadenas  de  texto
literales, pero también se pueden pasar como una  variable  que  contenga  la  subcadena  deseada  o
incluso como el resultado de una función que devuelva un texto.  Esto  proporciona  flexibilidad  al
método, permitiendo su uso en una amplia variedad de situaciones y contextos.

Es importante destacar que, si no se especifica el tercer argumento, el método reemplazará todas las
apariciones de la subcadena en la cadena original. Sin embargo, si se desea  limitar  el  número  de
reemplazos, se puede proporcionar un valor entero como tercer argumento. Si este valor es mayor  que
el número de apariciones de la subcadena en la cadena original,  el  método  reemplazará  todas  las
apariciones disponibles; si es menor, reemplazará solo las primeras apariciones  hasta  alcanzar  el
número especificado, dejando el resto sin modificar.

Por último, en cuanto al número de reemplazos, es  importante  mencionar  que  este  se  contará  de
izquierda a derecha; es decir, si se especifica un número de reemplazos, el método  reemplazará  las
primeras apariciones de la subcadena en ese orden hasta alcanzar el  número  especificado,  y  luego
dejará el resto de las apariciones restantes a la derecha sin modificar. Esto es especialmente  útil
cuando se desea realizar un reemplazo específico o cuando  se  trabaja  con  cadenas  que  contienen
múltiples apariciones de la subcadena que se desea reemplazar."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
