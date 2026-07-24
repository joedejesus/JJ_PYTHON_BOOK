# Enunciado:
"""Para modificar valores de un diccionario en Python, se utiliza la clave del diccionario junto con
el operador de asignación (=). Una clave es  un  identificador  único  dentro  del  diccionario  que
permite acceder y modificar directamente el valor asociado a ella.

A diferencia de las listas, los diccionarios no utilizan índices numéricos, sino  claves  inmutables
como cadenas, números o tuplas. Esto significa que, en lugar de modificar un  elemento  mediante  su
posición, se modifica utilizando la clave correspondiente. Este sistema  de  acceso  es  fundamental
para trabajar con diccionarios en Python, ya que permite actualizar  valores  de  manera  directa  y
eficiente.

Los diccionarios en Python son colecciones mutables de  pares  clave-valor,  lo  que  significa  que
podemos modificar sus valores directamente utilizando  sus  claves.  Además,  los  diccionarios  son
iterables, lo que permite recorrer sus pares clave-valor utilizando distintos métodos de iteración.

Además, Python permite utilizar métodos como ".update()" para modificar varios valores a la vez,  lo
que proporciona una forma flexible y poderosa de actualizar información dentro  de  un  diccionario.
Esta versatilidad hace que el manejo de diccionarios en Python  sea  muy  eficiente  y  adaptable  a
diferentes necesidades.

Por último, es importante tener en cuenta que al modificar valores de un diccionario, los cambios se
realizan directamente sobre el diccionario original, ya que  los  diccionarios  son  mutables.  Esto
puede afectar otras partes del programa que dependan del diccionario,  por  lo  que  es  fundamental
asegurarse de que los cambios sean intencionales y no generen efectos secundarios no deseados."""

# Ejemplo_modificar_valores_de_un_diccionario

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos  un  diccionario  con  los  elementos
{"a": 10, "b": 20, "c": 30, "d": 40}, el cual será utilizado para  modificar  sus  valores  mediante
claves.

A continuación, modificamos el valor asociado a la clave "c" asignándole el nuevo  valor  300.  Para
ello, utilizamos el operador de indexación [] con la clave "c" en su interior "["c"]", precedido  de
la variable "diccionario", donde la clave dentro de los corchetes representa la entrada que queremos
modificar. De esta forma, actualizamos el valor asociado a la clave "c", que originalmente era 30, y
ahora se ha actualizado a 300.

De manera similar, asignamos el valor 500 a la  clave  "e",  lo  que  añade  una  nueva  entrada  al
diccionario, y modificamos el valor asociado a la clave "d" asignándole el valor 600. Para ello,  en
cada caso nos referimos a la variable  "diccionario"  seguida  de  la  clave  correspondiente  entre
corchetes, y luego utilizamos el operador de asignación para asignar el nuevo  valor  a  cada  clave
específica.

Estas operaciones se realizan directamente sobre el diccionario original, sin asignar el resultado a
una nueva variable, ya que los diccionarios en Python son mutables.

Por último, utilizamos la función "print()" para mostrar el diccionario modificado  en  la  consola,
acompañada de un mensaje descriptivo en formato "f-string" para indicar los cambios realizados."""

# Código:
diccionario = {"a": 10, "b": 20, "c": 30, "d": 40}

diccionario["c"] = 300
diccionario["e"] = 500
diccionario["d"] = 600

print(f"Este es el diccionario modificado: {diccionario}")

# Nota Importante:
"""Es importante tener en cuenta que al modificar valores de un diccionario, los cambios se realizan
directamente sobre el diccionario original.  Esto  puede  afectar  otras  partes  del  programa  que
dependan del diccionario, por lo que es fundamental asegurarse de que los cambios sean intencionales
y no generen efectos secundarios no deseados.

Los diccionarios en Python pueden contener valores de  diferentes  tipos,  por  lo  que  es  posible
modificar valores numéricos, cadenas de texto, listas  u  otros  diccionarios  dentro  de  la  misma
estructura sin ningún problema. Esto se debe a que los diccionarios en Python son  heterogéneos,  lo
que permite almacenar y modificar valores de diferentes tipos  dentro  de  la  misma  estructura  de
datos.

Es posible modificar más de un valor a la vez utilizando el método ".update()", que permite  asignar
nuevos valores a varias claves de manera simultánea. Por ejemplo, si queremos modificar los  valores
asociados  a  las  claves  "a",   "b"   y   "c",   podemos   hacerlo   de   la   siguiente   manera:
diccionario.update({"a": 100, "b": 200, "c": 300}). Esto asignará los nuevos valores  a  las  claves
correspondientes de manera eficiente.

En el caso de los diccionarios, no es necesario almacenar el resultado de  la  modificación  en  una
nueva variable, ya que la modificación se realiza directamente sobre el diccionario original  debido
a su naturaleza mutable. Esto significa que cualquier cambio realizado en  el  diccionario  afectará
directamente al diccionario original y no se requiere asignar el resultado a una nueva variable.

Además, intentar modificar una clave inexistente utilizando el operador de indexación  "[]"  añadirá
una nueva clave al diccionario, lo que puede ser útil o problemático dependiendo del  contexto.  Por
lo tanto, es recomendable verificar si la clave existe utilizando  el  operador  "in"  o  el  método
".get()" antes de realizar modificaciones cuando se desee evitar la creación  accidental  de  nuevas
claves.

Por último, es importante tener en cuenta estas características, ya que hacen que  los  diccionarios
en Python sean una  herramienta  poderosa  y  flexible  para  trabajar  con  colecciones  de  datos,
permitiendo tanto el acceso como la modificación de sus valores de manera eficiente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────