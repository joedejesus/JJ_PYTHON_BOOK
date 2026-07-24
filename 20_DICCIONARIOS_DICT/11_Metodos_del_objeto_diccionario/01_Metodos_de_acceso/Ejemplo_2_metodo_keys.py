# Enunciado:
"""El método ".keys()" en Python se utiliza para obtener una vista iterable que contiene  todas  las
claves presentes en un diccionario. Este método  devuelve  un  objeto  especial  llamado  "vista  de
claves", que refleja los cambios realizados en el diccionario en tiempo real, lo que lo convierte en
una herramienta útil para acceder, analizar o recorrer  las  claves  de  un  diccionario  de  manera
eficiente.

El método ".keys()" accede al diccionario y devuelve una colección dinámica que contiene  únicamente
las claves, sin incluir los valores asociados. Esta vista no es una lista, pero puede convertirse en
una lista utilizando el constructor "list()" si  se  necesita  trabajar  con  las  claves  como  una
secuencia indexada. El método no genera errores, ya que siempre devuelve la vista de claves, incluso
si el diccionario está vacío.

Este método puede aplicarse a cualquier objeto de tipo  diccionario  en  Python,  como  diccionarios
literales, variables que contienen diccionarios  o  incluso  resultados  de  otras  operaciones  que
generan diccionarios. Este método no modifica el diccionario  original  y  devuelve  una  vista  que
representa todas las claves almacenadas en él, la cual  se  almacena  en  la  variable  asignada  al
resultado de la aplicación del método.

El método ".keys()" no recibe argumentos, ya que su función es simplemente devolver la colección  de
claves del diccionario.  Esta  vista  puede  utilizarse  directamente  en  bucles,  comparaciones  o
conversiones, lo que la convierte en una herramienta versátil para trabajar con estructuras de datos
basadas en pares clave-valor.

Por último, el método ".keys()" es una herramienta fundamental para  acceder  a  las  claves  de  un
diccionario en Python, ya que permite analizarlas, recorrerlas o  transformarlas  sin  modificar  el
diccionario original."""

# Ejemplo_2_metodo_keys.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario  que  contiene  varios
pares clave-valor. Este diccionario  se  utilizará  para  demostrar  el  funcionamiento  del  método
".keys()".

A continuación, definimos una nueva variable llamada "claves" y le asignamos el resultado de aplicar
el método ".keys()" a la variable "diccionario". Para ello, escribimos  el  nombre  de  la  variable
seguido del nombre del método ".keys()", con los paréntesis vacíos, ya que este método  no  requiere
argumentos para funcionar.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" para indicar cuáles son  las  claves  presentes  en  el
diccionario.

De esta forma, accedemos a todas las claves del diccionario sin modificarlo,  obteniendo  una  vista
dinámica que refleja el contenido actual del diccionario."""

# Código:
diccionario = {"a": 1, "b": 2, "c": "texto", "d": 4}

claves = diccionario.keys()
print(f"Las claves del diccionario son: {claves}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".keys()" devuelve una vista dinámica de las  claves
del diccionario, lo que significa que, si el diccionario se modifica después de  obtener  la  vista,
esta se actualizará automáticamente para reflejar los cambios. Esto lo convierte en una  herramienta
muy útil para trabajar con diccionarios que cambian durante la ejecución del programa.

Este método no modifica el diccionario original y devuelve una vista que representa todas las claves
almacenadas en él, la cual se almacena en la variable  asignada  al  resultado  del  método.  Si  se
necesita trabajar con las claves como una lista tradicional, se puede convertir la vista  utilizando
el constructor "list()", lo que permite acceder a las claves  mediante  índices  o  aplicar  métodos
propios de las listas.

El método ".keys()" es ideal para recorrer las claves de un diccionario utilizando un  bucle  "for",
ya que permite acceder a cada clave de manera ordenada, según el orden de inserción del diccionario.
Además, es útil para realizar comprobaciones, como verificar si una clave existe en  el  diccionario
utilizando el operador "in".

Por último, este método es adecuado para obtener únicamente las claves del diccionario. Si se  desea
acceder a los valores o a los pares clave-valor completos, se deben utilizar los métodos ".values()"
o ".items()", respectivamente, los cuales se explican en sus secciones correspondientes."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────