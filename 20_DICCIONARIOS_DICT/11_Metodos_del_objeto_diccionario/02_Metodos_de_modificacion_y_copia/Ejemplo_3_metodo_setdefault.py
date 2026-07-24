# Enunciado:
"""El método ".setdefault()" en Python se utiliza para obtener el valor asociado a una clave  dentro
de un diccionario y, si la clave no existe,  insertarla  con  un  valor  por  defecto.  Este  método
modifica el diccionario original únicamente cuando la clave no está presente, añadiendo un nuevo par
clave-valor y devolviendo el valor asignado. Si la clave ya existe, simplemente  devuelve  su  valor
sin realizar ninguna modificación.

El método ".setdefault()" puede aplicarse a cualquier objeto de tipo  diccionario  en  Python,  como
diccionarios  literales,  variables  que  contienen  diccionarios  o  incluso  resultados  de  otras
operaciones que generan diccionarios.

Este método puede modificar el diccionario original, pero solo en el caso de que la clave no exista.
Esto significa que no es necesario asignar el resultado de la aplicación  del  método  a  una  nueva
variable, ya que altera el objeto existente únicamente cuando es necesario. Sin embargo, si se desea
almacenar el valor devuelto, puede asignarse el resultado de la aplicación del método  a  una  nueva
variable para su uso posterior. Este comportamiento es consistente con la naturaleza mutable de  los
diccionarios en Python.

El método ".setdefault()" toma dos argumentos: el primero es la  clave  que  se  desea  consultar  o
insertar, y el segundo es el valor por defecto que se asignará si la  clave  no  existe.  Si  no  se
proporciona un valor por defecto, se utilizará "None" como valor predeterminado.

Además, la clave puede pasarse al método como un valor literal, como una cadena o un número, o  como
una variable que contenga la clave que se desea insertar o consultar. El valor por defecto puede ser
cualquier tipo de dato válido en Python, como  números,  cadenas,  listas,  diccionarios  u  objetos
personalizados.

Por último, el método ".setdefault()" es una herramienta útil para  acceder  a  los  valores  de  un
diccionario y, al mismo tiempo, garantizar  que  una  clave  exista,  permitiendo  una  manipulación
eficiente y segura de los datos en estructuras de tipo diccionario."""

# Ejemplo_3_metodo_setdefault.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con  varias  claves  y
valores. Este diccionario se utilizará para demostrar el funcionamiento del método ".setdefault()".

A continuación, definimos una variable llamada "valor_obtenido"  y  le  asignamos  el  resultado  de
aplicar el método ".setdefault()" a la variable "diccionario". Para ello, escribimos el nombre de la
variable "diccionario" seguido del nombre del método ".setdefault()", y dentro  de  los  paréntesis,
pasamos como primer argumento la clave que deseamos consultar o insertar, en este caso "c",  y  como
segundo argumento el valor por defecto "No definido".

Por último, utilizamos la función "print()" para mostrar el contenido del diccionario en la consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método al diccionario. Además, también mostramos el valor obtenido utilizando de nuevo
la función "print()", acompañado de un mensaje descriptivo en formato "f-string",  para  indicar  el
valor devuelto por el método.

De esta forma, hemos accedido al valor asociado a la clave "c" o, si no existía, la hemos  insertado
con un valor por defecto, modificando el diccionario original solo cuando ha sido necesario."""

# Código:
diccionario = {"a": 1, "b": 2}

valor_obtenido = diccionario.setdefault("c", "No definido")
print(f"Este es el resultado de aplicar el método al diccionario: {diccionario}")
print(f"Este es el valor obtenido del diccionario: {valor_obtenido}")

# Nota Importante:
"""Es fundamental tener en cuenta que el  método  ".setdefault()"  puede  modificar  el  diccionario
original, pero solo cuando la clave especificada no  existe.  Si  la  clave  ya  está  presente,  el
diccionario no se modifica, y el método devuelve el valor existente.

Este método es especialmente útil cuando se desea garantizar que una clave exista en el  diccionario
antes de realizar operaciones adicionales, evitando  errores  y  simplificando  el  código.  También
resulta útil en estructuras más complejas, como diccionarios que  almacenan  listas  o  diccionarios
internos, ya que permite inicializar valores predeterminados de manera segura.

Además, si se desea insertar o actualizar valores de manera  explícita,  se  pueden  utilizar  otros
métodos como ".update()" o la asignación directa mediante corchetes. Sin embargo, ".setdefault()" es
ideal cuando se necesita acceder a un valor y, al mismo tiempo, asegurarse de que  la  clave  exista
sin sobrescribir valores previos.

Por último, es importante recordar que este método devuelve  siempre  un  valor:  ya  sea  el  valor
existente o el valor por defecto insertado. Esto permite  utilizarlo  directamente  en  expresiones,
asignaciones o estructuras de control sin necesidad de realizar comprobaciones adicionales."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────