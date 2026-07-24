# Enunciado:
"""El método ".values()" en Python se utiliza para obtener una vista iterable que contiene todos los
valores presentes en un diccionario. Este método devuelve  un  objeto  especial  llamado  "vista  de
valores" que refleja los cambios realizados en el diccionario en tiempo real, lo que lo convierte en
una herramienta útil para acceder, analizar o recorrer los valores almacenados en un diccionario  de
manera eficiente.

El método ".values()" actúa sobre el diccionario completo y  devuelve  una  colección  dinámica  que
contiene únicamente los valores, sin incluir las claves asociadas. Esta vista no es una lista,  pero
puede convertirse en una utilizando el constructor "list()" si se necesita trabajar con los  valores
como una secuencia indexada. El método no genera errores,  ya  que  siempre  devuelve  la  vista  de
valores, incluso si el diccionario está vacío.

Este método puede aplicarse a cualquier objeto de tipo  diccionario  en  Python,  como  diccionarios
literales, variables que contienen diccionarios  o  incluso  resultados  de  otras  operaciones  que
generan diccionarios. Este método no modifica el diccionario  original  y  devuelve  una  vista  que
representa todos los valores almacenados en él, la cual se  almacena  en  la  variable  asignada  al
resultado de la aplicación del método.

El método ".values()" no recibe argumentos, ya que su función es simplemente devolver  la  colección
de valores del diccionario. Esta vista puede utilizarse  directamente  en  bucles,  comparaciones  o
conversiones, lo que la convierte en una herramienta versátil para trabajar con estructuras de datos
basadas en pares clave-valor.

Por último, el método ".values()" es una herramienta fundamental para acceder a los  valores  de  un
diccionario en Python, permitiendo  analizarlos,  recorrerlos  o  transformarlos  sin  modificar  el
diccionario original."""

# Ejemplo_3_metodo_values.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario  que  contiene  varios
pares clave-valor. Este diccionario  se  utilizará  para  demostrar  el  funcionamiento  del  método
".values()".

A continuación, definimos una nueva variable llamada  "valores"  y  le  asignamos  el  resultado  de
aplicar el método ".values()" a la variable "diccionario". Para ello, escribimos  el  nombre  de  la
variable seguido del nombre del método ".values()", con los paréntesis vacíos, ya que este método no
requiere argumentos para funcionar.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola acompañado de un
mensaje descriptivo en formato "f-string" para indicar la  colección  de  valores  presentes  en  el
diccionario.

De esta forma, hemos accedido a todos los valores del diccionario sin  modificarlo,  obteniendo  una
vista dinámica que refleja el contenido actual del diccionario."""

# Código:
diccionario = {"a": 1, "b": 2, "c": "texto", "d": 4}

valores = diccionario.values()
print(f"Los valores del diccionario son: {valores}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".values()"  devuelve  una  vista  dinámica  de  los
valores del diccionario, lo que significa que si el diccionario se modifica después  de  obtener  la
vista, esta se actualizará automáticamente para reflejar los  cambios.  Esto  lo  convierte  en  una
herramienta muy útil para trabajar con diccionarios que cambian durante la ejecución del programa.

Este método no modifica el diccionario original y  devuelve  una  vista  que  representa  todos  los
valores almacenados en él, la cual se almacena en la variable asignada al resultado de la aplicación
del método. Si se necesita trabajar con los valores como una lista tradicional, se  puede  convertir
la vista utilizando el constructor "list()", lo que permite acceder a los valores mediante índices o
aplicar métodos propios de las listas.

El método ".values()" es ideal para recorrer los valores  de  un  diccionario  utilizando  un  bucle
"for", ya que permite acceder a cada valor de manera  ordenada  según  el  orden  de  inserción  del
diccionario. Además, es útil para realizar análisis, filtrados o transformaciones  sobre  los  datos
almacenados.

Por último, este método es adecuado para obtener únicamente los valores del diccionario. Si se desea
acceder a las claves o a los pares clave-valor completos, se deben utilizar los métodos ".keys()"  o
".items()", respectivamente, los cuales se explican en sus secciones correspondientes."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────