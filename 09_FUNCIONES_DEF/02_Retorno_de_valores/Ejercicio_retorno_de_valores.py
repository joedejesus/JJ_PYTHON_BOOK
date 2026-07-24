# Enunciado:
"""Crea una función llamada "saludar()" que tome un parámetro llamado "persona" y devuelva un saludo
personalizado usando la instrucción "return". El saludo debe ser un mensaje  en  formato  "f-string"
que contenga el nombre del parámetro, el cual será sustituido por el valor  que  se  le  pase  a  la
función al llamarla.

Luego, define una lista llamada "lista_nombres" que contenga varios nombres como cadenas  de  texto.
Usa un bucle "for" para iterar sobre la lista de nombres y, dentro del bucle,  llama  a  la  función
"saludar()" con cada uno de los nombres de la lista  como  argumento  para  ejecutar  la  función  e
imprimir un mensaje para cada uno de los nombres de la lista."""

# Ejercicio_retorno_de_valores.py

# Explicación:
"""Definimos una función llamada  "saludar()"  que  recibe  un  parámetro  llamado  "persona".  Este
parámetro se utilizará para personalizar el mensaje de saludo que será devuelto desde la  función  y
sustituido por el valor que se le pase a la función al llamarla. Para ello,  utilizamos  la  palabra
clave "def" seguida del nombre de la función, en este  caso  "saludar()",  seguida  del  nombre  del
parámetro "persona" entre paréntesis (), y terminamos con dos puntos (:) para indicar el inicio  del
bloque de código asociado a la función.

A continuación, dentro de la función utilizamos la instrucción "return" para devolver un mensaje  en
formato "f-string". La instrucción "return" indica al intérprete  de  Python  que  la  función  debe
finalizar su ejecución y enviar el valor especificado de vuelta al lugar donde fue llamada.

Para ello, escribimos la palabra clave "return" seguida del mensaje que queremos devolver,  en  este
caso un saludo personalizado en formato "f-string" que incluye el nombre del parámetro "persona", el
cual será sustituido por el valor que se le pase a la función al llamarla.  En  este  caso,  estamos
devolviendo un resultado en una sola instrucción en forma de cadena de texto. Colocamos  esta  línea
de código con una indentación de cuatro espacios desde el margen izquierdo para  indicar  que  forma
parte del bloque de código asociado a la función y  debe  ejecutarse  siempre  que  la  función  sea
llamada.

Luego, definimos una lista llamada "lista_nombres" que  contiene  varios  nombres  como  cadenas  de
texto. Esta lista será utilizada como objeto iterable en el bucle "for" y, de esta forma, se llamará
a la función "saludar()" con cada uno de los nombres de la lista.

Utilizamos un bucle "for" para iterar sobre cada elemento de la  lista.  Para  ello,  escribimos  la
palabra clave "for", seguida de la variable "i", que representa cada  iteración  o  elemento  de  la
secuencia y la cual definimos en este momento, seguida del operador "in" para indicar dónde queremos
que se realice la iteración y el nombre de la secuencia sobre la que queremos iterar, en  este  caso
"lista_nombres". A continuación, escribimos dos puntos (:) para indicar el final de la  expresión  y
el inicio del bloque de código asociado al bucle "for".

Dentro del bucle "for", definimos una variable llamada "saludo" y  le  asignamos  la  llamada  a  la
función "saludar()" pasando como argumento a la función el valor actual  de  la  variable  "i",  que
representa cada elemento de la lista en cada iteración del bucle y corresponde a  un  nombre  de  la
lista. Para llamar a la función, simplemente escribimos su  nombre  seguido  de  paréntesis  con  el
argumento correspondiente, en este caso "saludar(i)". De esta forma, el valor "i" será transferido y
asignado al parámetro "persona" dentro de la función, la cual se ejecutará  y  devolverá  el  saludo
personalizado incluyendo el valor "i" que corresponde a un nombre de persona de la lista.

La llamada a la función y su ejecución se realizarán tantas veces como elementos haya en la lista  e
indica al intérprete de Python que debe ejecutar el bloque de código asociado a la función, el  cual
es una instrucción "return" que  devuelve  un  mensaje  en  formato  "f-string"  tantas  veces  como
elementos haya en la lista. Colocamos esta línea de código con una indentación  de  cuatro  espacios
desde el margen izquierdo para indicar que forma parte del bloque de código asociado al bucle  "for"
y debe ejecutarse en cada iteración del bucle.

Por último, dentro del bucle "for" utilizamos la función "print()" para imprimir en consola el valor
de la variable  "saludo",  la  cual  contiene  el  saludo  personalizado  devuelto  por  la  función
"saludar()" en cada iteración del bucle. Para ello, dentro de  la  función  "print()"  colocamos  la
variable "saludo", la cual contiene el valor devuelto por la función "saludar()" tantas  veces  como
elementos haya en la lista ya que se ha igualado a la llamada de la función en  cada  iteración  del
bucle.

De esta forma se imprime en consola el saludo personalizado para cada nombre de la lista.  Colocamos
esta línea de código con una indentación de cuatro espacios desde el margen izquierdo  para  indicar
que forma parte del bloque de código asociado al bucle "for" y debe ejecutarse en cada iteración del
bucle."""

# Código:
def saludar(persona):
    return (f"Hola, {persona} qué tal estás!")

lista_nombres = ["Ana", "Luis", "Carlos", "Marta"]

for i in lista_nombres:
    saludo = saludar(i)
    print(saludo)

# Nota Importante:
"""Es importante destacar que la función "saludar()" utiliza la instrucción "return"  para  devolver
el saludo personalizado. Esto significa que la función no  imprime  directamente  el  saludo  en  la
consola, sino que devuelve el mensaje al lugar donde fue llamada, en este caso el bucle "for".  Esto
permite que el valor devuelto por la función sea reutilizable en diferentes  contextos,  ya  que  no
está limitado a ser mostrado únicamente en la consola. Por ejemplo, el  valor  devuelto  podría  ser
almacenado en una variable, utilizado en cálculos o incluso pasado como argumento a otra función.

El uso de "return" en lugar de "print()" dentro  de  la  función  es  una  práctica  recomendada  en
programación, ya que separa la lógica de la función (en este caso, generar un saludo  personalizado)
de la presentación del resultado (mostrar el saludo en la consola). Esto mejora la  modularidad  del
código, haciéndolo más flexible y fácil de mantener. Si en el futuro se requiere cambiar la forma en
que se presenta el saludo (por ejemplo, guardarlo en un archivo, enviarlo por correo o mostrarlo  en
una interfaz gráfica), no será necesario modificar la función "saludar()", sino únicamente el código
que utiliza el valor devuelto por ella. Este enfoque promueve el principio de responsabilidad única,
que es fundamental en el diseño de software.

En el bucle "for", se utiliza una variable intermedia  llamada  "saludo"  para  almacenar  el  valor
devuelto por la función "saludar()". Esto no es estrictamente necesario,  ya  que  se  podría  haber
llamado a la función directamente dentro de la función "print()", como en  "print(saludar(i))".  Sin
embargo, el uso de una variable intermedia mejora la claridad del código, ya que permite separar  la
llamada a la función de la presentación del  resultado.  Además,  al  almacenar  el  saludo  en  una
variable, se facilita su reutilización en otros contextos dentro del mismo  bloque  de  código,  sin
necesidad de volver a llamar a la función. Esto también puede ser  útil  para  realizar  operaciones
adicionales con el valor devuelto antes  de  presentarlo,  como  concatenarlo  con  otros  textos  o
aplicarle transformaciones.

Es importante tener en cuenta que el argumento pasado a la función "saludar()" debe ser del tipo  de
dato esperado por la función, en este caso una cadena de texto, ya que  el  parámetro  "persona"  se
utiliza dentro de una "f-string". Si se pasa un argumento de otro tipo, como un número o un  objeto,
Python intentará convertirlo a cadena de texto automáticamente. Sin embargo, si el argumento  no  es
convertible a cadena, se generará un error. Por lo tanto, es una buena práctica  validar  los  datos
antes de pasarlos como argumentos a una función, especialmente en casos donde los datos provienen de
fuentes externas o del usuario. Esto puede lograrse mediante verificaciones explícitas o  utilizando
estructuras de control que aseguren que los datos cumplen con los requisitos esperados.

Además, el uso de "return" en la función "saludar()" no solo permite devolver un valor reutilizable,
sino que también mejora la flexibilidad, claridad y mantenibilidad del código. Separar la lógica  de
la función de la presentación del resultado es una práctica  fundamental  en  programación,  ya  que
facilita la reutilización del código en  diferentes  contextos  y  escenarios.  Además,  el  uso  de
variables intermedias como "saludo" puede mejorar la legibilidad del código, especialmente en  casos
donde se requiere realizar múltiples operaciones con el valor devuelto por una función. Este enfoque
también reduce la probabilidad de errores, ya que cada parte del código  tiene  una  responsabilidad
bien definida.

Por último, en este ejemplo hemos visto cómo es posible utilizar un bucle "for"  para  iterar  sobre
una lista de nombres y llamar a la función "saludar()" con cada nombre de la lista  como  argumento,
siendo dicho argumento cada elemento iterable de la lista. Es útil saber que es posible utilizar  un
bucle "for i in range(x)" para iterar un número determinado de veces  "x"  y  llamar  a  la  función
"saludar()" en cada iteración del bucle, pasando como argumento el valor de la variable  de  control
del bucle.

Esto permite ejecutar la función  un  número  específico  de  veces,  lo  cual  puede  ser  útil  en
situaciones donde se requiere repetir una acción un número determinado de veces, como en  pruebas  o
simulaciones. De esta forma llamaríamos a la función un número determinado  de  veces  en  una  sola
estructura de control de flujo, lo cual mejora la eficiencia y claridad  del  código.  Además,  este
enfoque puede  combinarse  con  estructuras  condicionales  o  listas  dinámicas  para  adaptarse  a
diferentes escenarios, haciendo que el código sea más robusto y versátil."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
