# Enunciado:
"""El método ".fromkeys()" en Python se utiliza para crear un  diccionario  nuevo  a  partir  de  un
conjunto de claves. Este método  devuelve  un  diccionario  completamente  nuevo,  independiente  en
memoria, en el que cada clave proporcionada se asocia al mismo valor por defecto. Es  decir,  genera
una estructura nueva basada en una colección de claves,  inicializando  todas  ellas  con  el  mismo
valor.

El diccionario devuelto se almacena en la variable asignada al resultado de la aplicación del método
y no afecta a ningún diccionario existente. Esto permite  crear  diccionarios  de  manera  rápida  y
eficiente, especialmente cuando se necesita inicializar un diccionario con  un  conjunto  de  claves
conocidas y un valor común. Además, la variable que almacena la colección de claves no se  modifica,
ya que el método ".fromkeys()" no altera la estructura de datos original, sino que genera  un  nuevo
diccionario a partir de ella.

Este método puede aplicarse utilizando cualquier iterable que contenga claves válidas, como  listas,
tuplas, cadenas o incluso resultados de otras operaciones que generen colecciones  de  claves.  Este
método no modifica ningún diccionario existente, ya que su propósito es crear un  diccionario  nuevo
desde cero.

El método ".fromkeys()" toma dos argumentos: el primero es un iterable que contiene las  claves  que
formarán el nuevo diccionario, y el segundo es el valor por defecto que  se  asignará  a  todas  las
claves. Si no se proporciona un valor por defecto, se utilizará "None" como valor predeterminado.

Es importante destacar que el método ".fromkeys()" crea un diccionario nuevo, pero si el  valor  por
defecto es un objeto mutable, dicho objeto será compartido entre todas las claves  del  diccionario.
Esto significa que, si se modifica ese valor mutable desde una clave,  el  cambio  se  reflejará  en
todas las demás claves que comparten ese mismo objeto en memoria.

Sin embargo, si el valor por defecto es un objeto inmutable, no habrá interacción entre las  claves,
ya que los objetos inmutables no pueden modificarse después de su creación.

Por  último,  el  método  ".fromkeys()"  es  una  herramienta  sencilla  pero  poderosa  para  crear
diccionarios nuevos a partir de un conjunto de claves, ya que  permite  inicializar  estructuras  de
datos de manera rápida, clara y controlada."""

# Ejemplo_metodo_fromkeys.py

# Explicación:
"""Definimos una variable llamada "claves" y le asignamos una lista  que  contiene  varias  cadenas.
Esta lista se utilizará como  conjunto  de  claves  para  demostrar  el  funcionamiento  del  método
".fromkeys()".

A continuación, definimos  una  nueva  variable  llamada  "diccionario_creado"  y  le  asignamos  el
resultado de aplicar el método ".fromkeys()" utilizando  la  clase  "dict".  Para  ello,  escribimos
"dict.fromkeys()" y, dentro de los paréntesis, pasamos como primer  argumento  la  lista  de  claves
contenidas en la variable "claves" y como segundo  argumento  el  valor  por  defecto  que  deseamos
asignar, en este caso el valor 0.

Por último, utilizamos la función "print()" para mostrar el contenido del diccionario creado  en  la
consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que  se  trata  del
diccionario generado a partir de esas claves con el método ".fromkeys()".

De esta forma, hemos  creado  un  diccionario  completamente  nuevo,  inicializado  con  las  claves
proporcionadas y con un valor por defecto asignado a cada una de ellas."""

# Código:
claves = ["a", "b", "c", "d"]

diccionario_creado = dict.fromkeys(claves, 0)
print(f"Diccionario creado con el método fromkeys: {diccionario_creado}")

# Nota Muy Importante:
"""Es  fundamental  tener  en  cuenta  que  el  método  ".fromkeys()"  crea  un  diccionario  nuevo,
independiente en memoria, lo que significa que no modifica ningún  diccionario  existente.  Esto  es
especialmente útil cuando se desea inicializar estructuras de datos de manera rápida y controlada.

Sin embargo, es importante recordar que, si el valor por defecto es  un  objeto  mutable,  como  una
lista o un diccionario, dicho objeto será compartido entre todas las claves  del  diccionario.  Esto
implica que cualquier modificación realizada en ese objeto desde una clave se reflejará en todas las
demás claves que compartan el mismo valor mutable.

Por otro lado, si el valor por defecto es un objeto inmutable, como un número entero, una  cadena  o
una tupla, no habrá  interacción  entre  las  claves,  ya  que  los  objetos  inmutables  no  pueden
modificarse.

Además, cuando decimos que el valor por defecto puede ser compartido entre las claves si es mutable,
significa que todas las claves apuntan al mismo objeto en memoria. Por ello, se recomienda  utilizar
valores inmutables como valores predeterminados o, si se necesita  un  valor  mutable  independiente
para cada clave, inicializar el diccionario manualmente o mediante una comprensión de diccionario.

Por último, es importante recordar que este método devuelve siempre un diccionario nuevo, por lo que
es necesario asignar el resultado a una variable si se desea utilizar la  estructura  creada  en  el
programa."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────