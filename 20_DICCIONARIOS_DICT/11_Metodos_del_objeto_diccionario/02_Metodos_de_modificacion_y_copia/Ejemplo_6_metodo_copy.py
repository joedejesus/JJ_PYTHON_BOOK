# Enunciado:
"""El método ".copy()" en Python se utiliza para crear una copia superficial de un diccionario. Este
método devuelve un nuevo diccionario que contiene los mismos pares clave-valor  que  el  diccionario
original, pero como un objeto independiente en memoria. Es decir, la copia es un objeto distinto del
original, aunque ambos objetos contengan las mismas claves y los mismos valores.

Este método puede aplicarse a cualquier objeto de tipo  diccionario  en  Python,  como  diccionarios
literales, variables que contienen diccionarios  o  incluso  resultados  de  otras  operaciones  que
generan diccionarios.  Este  método  no  modifica  el  diccionario  original  y  devuelve  un  nuevo
diccionario que representa una copia superficial del diccionario original, la cual se almacena en la
variable asignada al resultado de la aplicación del método.

El método ".copy()" no toma argumentos adicionales, ya que su propósito  es  simplemente  crear  una
copia superficial del diccionario. Esto lo convierte en una herramienta sencilla  y  eficiente  para
duplicar diccionarios sin necesidad de  realizar  operaciones  adicionales  para  obtener  el  mismo
resultado.

Es importante destacar que el método ".copy()" crea una copia superficial del  diccionario,  lo  que
significa que los valores mutables del diccionario original y los valores mutables de la  copia  son
referencias al mismo objeto en memoria. Esto implica que, si los valores  del  diccionario  original
son objetos mutables, los cambios  realizados  en  esos  valores  dentro  de  la  copia  también  se
reflejarán en el diccionario original, ya que existe una referencia compartida a los mismos  objetos
mutables en memoria en ambos diccionarios.

Sin embargo, si los valores del diccionario original son  objetos  inmutables,  estos  no  se  verán
afectados por los cambios en la copia o en el diccionario original, ya que los objetos inmutables no
pueden modificarse después de su creación. Cada instancia de un objeto  inmutable  tiene  su  propia
referencia en memoria.

Por ello, es importante comprender la diferencia entre una copia superficial y una copia profunda al
trabajar con diccionarios en Python.

Una copia superficial, como la que se obtiene con el método ".copy()", crea un nuevo diccionario que
contiene referencias a los mismos objetos mutables que el diccionario original. Esto significa  que,
si los valores del diccionario original son  objetos  mutables,  los  cambios  realizados  en  estos
valores dentro de la copia también se reflejarán en el diccionario original.

Una copia profunda, por otro lado, crea un nuevo diccionario que contiene copias  independientes  de
los objetos mutables dentro del diccionario original. Esto significa que los cambios  realizados  en
los valores mutables de la copia no afectarán a los valores mutables del diccionario  original.  Una
copia profunda se puede obtener importando y utilizando el módulo "copy" de la  biblioteca  estándar
de Python y su función "deepcopy()".

Por último, el  método  ".copy()"  es  una  herramienta  sencilla,  pero  útil,  para  crear  copias
superficiales de diccionarios en Python, permitiendo trabajar con datos duplicados  sin  alterar  el
diccionario original."""

# Ejemplo_6_metodo_copy.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con  varias  claves  y
valores. Este diccionario se utilizará para demostrar el funcionamiento del método ".copy()".

A continuación, definimos una nueva variable llamada "copia_superficial" y le asignamos el resultado
de aplicar el método ".copy()" a la variable "diccionario". Para ello, escribimos el  nombre  de  la
variable seguido del nombre del método ".copy()" con los paréntesis vacíos, ya que  este  método  no
requiere ningún argumento para funcionar.

Por último, utilizamos la función "print()" para mostrar el contenido del diccionario original y  de
la copia en la consola, acompañados de un mensaje descriptivo en formato "f-string" para indicar que
se trata del diccionario original y de la copia, respectivamente.

De esta forma, hemos creado una copia superficial del diccionario original sin modificarlo y podemos
trabajar con ella de forma independiente sin afectar al diccionario original.

Adicionalmente, imprimimos los identificadores de ambos diccionarios para mostrar explícitamente que
el diccionario original y la copia son objetos diferentes en memoria. Esto nos permite verificar que
la copia es un objeto independiente en memoria, aunque los pares clave-valor sean los  mismos.  Para
ello, utilizamos la función incorporada "id()", que toma como argumento el nombre de la variable que
contiene el diccionario original y el nombre de la variable que contiene la copia,  respectivamente,
e imprime el identificador de cada objeto."""

# Código:
diccionario = {"a": 1, "b": 2, "c": 3}

copia_superficial = diccionario.copy()
print(f"Diccionario original: {diccionario}")
print(f"Copia del diccionario: {copia_superficial}")

print(id(diccionario))
print(id(copia_superficial))

# Nota Muy Importante:
"""Es fundamental  tener  en  cuenta  que  el  método  ".copy()"  crea  una  copia  superficial  del
diccionario, lo que significa que los valores  mutables  del  diccionario  original  y  los  valores
mutables de la copia son referencias  al  mismo  objeto  en  memoria.  Por  lo  tanto,  los  cambios
realizados en los valores mutables de la copia también se reflejarán en  los  valores  mutables  del
diccionario original.

Sin embargo, si los valores del diccionario original son  objetos  inmutables,  estos  no  se  verán
afectados por los cambios en la copia o en el diccionario original, ya que los objetos inmutables no
pueden modificarse después de su creación.

Cuando decimos que los valores del diccionario original y los valores de la copia son referencias al
mismo objeto en memoria, si estos son mutables,  significa  que  ambos  objetos  mutables  en  ambos
diccionarios apuntan al mismo lugar de la memoria del sistema. Por ello,  pueden  modificarse  desde
ambos diccionarios, ya que ambos objetos mutables son el mismo objeto en memoria.

Sin embargo, esto no significa que ambos diccionarios,  "original"  y  "copia",  sean  idénticos  en
términos  de  identidad,  ya  que  cada  diccionario  es  un  objeto  independiente  con  su  propio
identificador. Es por ello que los identificadores de ambos diccionarios son diferentes, a pesar  de
que los elementos sean los mismos y uno sea una copia superficial del otro.

Por último, si se desea realizar una copia profunda de un  diccionario,  es  necesario  utilizar  el
módulo "copy" y su función "deepcopy()" de la biblioteca estándar de Python. Esto  es  especialmente
útil cuando se trabaja con diccionarios que contienen objetos mutables y se desea  evitar  cualquier
interacción entre el diccionario original y su copia."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────