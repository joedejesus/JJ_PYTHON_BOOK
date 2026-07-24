# Enunciado:
"""El método ".items()" en Python se utiliza para obtener una vista iterable que contiene todos  los
pares clave-valor presentes en un diccionario. Este  método  devuelve  un  objeto  especial  llamado
"vista de ítems" que refleja los cambios realizados en el diccionario en  tiempo  real,  lo  que  lo
convierte en una herramienta muy útil para acceder, analizar o recorrer la estructura completa de un
diccionario de manera eficiente.

El método ".items()" evalúa el diccionario completo y devuelve una  colección  dinámica  donde  cada
elemento es una tupla formada por dos valores: la clave y el valor asociado. Esta vista  no  es  una
lista, pero puede convertirse en una utilizando el constructor "list()" si se necesita trabajar  con
los pares clave-valor como una secuencia indexada. El método  no  genera  errores,  ya  que  siempre
devuelve la vista de ítems, incluso si el diccionario está vacío.

Este método puede aplicarse a cualquier objeto de tipo  diccionario  en  Python,  como  diccionarios
literales, variables que contienen diccionarios  o  incluso  resultados  de  otras  operaciones  que
generan diccionarios. Este método no modifica el diccionario  original  y  devuelve  una  vista  que
representa todos los pares clave-valor almacenados en  él,  la  cual  se  almacena  en  la  variable
asignada al resultado de la aplicación del método.

El método ".items()" no recibe argumentos, ya que su función es simplemente  devolver  la  colección
completa de pares clave-valor del diccionario. Esta vista puede utilizarse directamente  en  bucles,
comparaciones o conversiones, lo que la convierte en una  herramienta  versátil  para  trabajar  con
estructuras de datos organizadas mediante claves.

Por último, el método ".items()" es una herramienta fundamental para acceder simultáneamente  a  las
claves y valores de un diccionario en Python, permitiendo analizarlos, recorrerlos o  transformarlos
sin modificar el diccionario original."""

# Ejemplo_4_metodo_items.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario  que  contiene  varios
pares clave-valor. Este diccionario  se  utilizará  para  demostrar  el  funcionamiento  del  método
".items()".

A continuación, definimos una nueva variable llamada "items_diccionario" y le asignamos el resultado
de aplicar el método ".items()" a la variable "diccionario". Para ello, escribimos el nombre  de  la
variable seguido del nombre del método ".items()", con los paréntesis vacíos, ya que este método  no
requiere argumentos para funcionar.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola acompañado de un
mensaje descriptivo en formato "f-string" para indicar la colección de pares  clave-valor  presentes
en el diccionario.

De esta forma, hemos accedido a  todos  los  pares  clave-valor  del  diccionario  sin  modificarlo,
obteniendo una vista dinámica que refleja el contenido actual del diccionario."""

# Código:
diccionario = {"a": 1, "b": 2, "c": "texto", "d": 4}

items_diccionario = diccionario.items()
print(f"Los pares clave-valor del diccionario son: {items_diccionario}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".items()" devuelve una vista dinámica de los  pares
clave-valor del diccionario, lo que significa que si el diccionario se modifica después  de  obtener
la vista, esta se actualizará automáticamente para reflejar los cambios. Esto lo  convierte  en  una
herramienta muy útil para trabajar con diccionarios que cambian durante la ejecución del programa.

Este método no modifica el diccionario original y devuelve una vista que representa todos los  pares
clave-valor almacenados en él, la cual se almacena en  la  variable  asignada  al  resultado  de  la
aplicación del método. Si se necesita trabajar con los pares como una lista  tradicional,  se  puede
convertir la vista utilizando el constructor "list()",  lo  que  permite  acceder  a  los  elementos
mediante índices o aplicar métodos propios de las listas.

El método ".items()" es ideal para recorrer un diccionario utilizando un bucle "for", ya que permite
acceder a cada clave y su valor  asociado  de  manera  simultánea.  Esto  facilita  tareas  como  la
impresión estructurada, la validación de datos o la transformación de información.

Por último, este método es adecuado para obtener tanto las claves como los valores  del  diccionario
en una sola operación. Si se desea acceder únicamente a las claves o únicamente a  los  valores,  se
deben utilizar los métodos ".keys()" o ".values()", respectivamente, los cuales se explican  en  sus
secciones correspondientes."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ───────────────────────────────────────────────────────────