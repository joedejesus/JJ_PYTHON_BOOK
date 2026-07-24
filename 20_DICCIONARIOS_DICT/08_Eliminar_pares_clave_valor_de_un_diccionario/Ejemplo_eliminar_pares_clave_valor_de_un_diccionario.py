# Enunciado:
"""Para eliminar pares clave-valor de un diccionario en Python, se utiliza la palabra  clave  "del".
Esta instrucción permite eliminar una clave específica junto con su valor asociado. A diferencia  de
las listas, los diccionarios no utilizan índices numéricos, sino  claves  inmutables  como  cadenas,
números o tuplas, por lo que la eliminación se realiza indicando directamente la clave que se  desea
eliminar.

Los diccionarios en Python son colecciones mutables de  pares  clave-valor,  lo  que  significa  que
podemos agregar, modificar y eliminar claves directamente utilizando  sus  identificadores.  Además,
los diccionarios son iterables, lo que permite recorrer o acceder a cada par clave-valor  utilizando
sus claves u otros métodos de iteración.

La palabra clave  "del"  elimina  un  par  clave-valor  específico  del  diccionario.  Si  la  clave
especificada no existe, se genera un error de tipo "KeyError".  Esta  palabra  clave  es  útil  para
eliminar elementos sin devolverlos, ya que su función principal consiste en  modificar  directamente
la estructura del diccionario.

Es importante tener en cuenta que, al eliminar pares clave-valor de un diccionario, los  cambios  se
realizan directamente sobre el diccionario original, ya que  los  diccionarios  son  mutables.  Esto
puede afectar a otras partes del programa que dependan del diccionario, por lo  que  es  fundamental
asegurarse de que los cambios sean intencionales y no generen efectos secundarios no deseados.

Por último, es importante conocer las necesidades específicas  de  cada  situación  para  elegir  la
técnica de eliminación adecuada. En este caso, solo utilizamos la palabra clave "del", mientras  que
otros  métodos  de  eliminación,  como  ".pop()"  y  ".popitem()",  se  explican   en   la   sección
correspondiente a métodos del objeto diccionario."""

# Ejemplo_eliminar_pares_clave_valor_de_un_diccionario.py

# Explicación:
"""Definimos una variable llamada "aeropuertos" y le asignamos un diccionario que  contiene  códigos
de aeropuertos como claves y nombres de aeropuertos como valores. Este diccionario se utilizará para
eliminar uno de sus pares clave-valor mediante la palabra clave "del".

Utilizamos la función "print()" para mostrar el diccionario original en la consola, acompañado de un
mensaje descriptivo en formato "f-string" para indicar que este es el diccionario antes de  realizar
cualquier eliminación.

A continuación, eliminamos el par clave-valor asociado a la clave "UIO" utilizando la palabra  clave
"del". Para ello, escribimos la palabra clave "del" seguida del nombre de la variable  "aeropuertos"
y luego utilizamos el operador de indexación "[]" con la clave "UIO" en su interior, "[\"UIO\"]". De
esta forma, eliminamos el par clave-valor correspondiente a la clave "UIO".

Esta operación se realiza directamente sobre el diccionario original, sin asignar el resultado a una
nueva variable, ya que los diccionarios en Python son mutables y la palabra clave "del" no  devuelve
ningún valor que se pueda almacenar en una variable.

Por último, utilizamos la función "print()" para mostrar el diccionario modificado  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar el cambio realizado."""

# Código:
aeropuertos = {
    "UIO": "Aeropuerto Internacional Mariscal Sucre",
    "JFK": "John F. Kennedy",
    "LAX": "Los Angeles Internacional"
}

print(f"Este es el diccionario antes de realizar cualquier eliminación: {aeropuertos}")

del aeropuertos["UIO"]
print(f"Este es el diccionario después de eliminar la clave 'UIO': {aeropuertos}")

# Nota Muy Importante:
"""En este caso, solo utilizamos la palabra clave "del" para eliminar un par clave-valor  específico
del diccionario, pero también es posible  eliminar  elementos  utilizando  los  métodos  ".pop()"  y
".popitem()". El método ".pop()" elimina y devuelve  el  valor  asociado  a  una  clave  específica,
mientras que ".popitem()" elimina y devuelve el último par clave-valor insertado. Estos  métodos  no
se han incluido en este ejemplo, ya que se explican con detalle  en  la  sección  correspondiente  a
métodos del objeto diccionario.

Es importante tener en cuenta que, al eliminar pares clave-valor de un diccionario, los  cambios  se
realizan directamente sobre el diccionario original. Esto puede afectar a otras partes del  programa
que dependan del diccionario, por  lo  que  es  fundamental  asegurarse  de  que  los  cambios  sean
intencionales y no generen efectos secundarios no deseados.

En el caso de los diccionarios, no es necesario almacenar el resultado  de  la  eliminación  en  una
nueva variable, ya que la eliminación se realiza directamente sobre el diccionario original debido a
su naturaleza mutable. Además, la palabra clave "del" no devuelve ningún valor y, por lo  tanto,  no
es necesario asignar su resultado a una variable, ya que su  función  principal  es  eliminar  pares
clave-valor sin devolverlos.

Intentar eliminar una clave inexistente utilizando el operador de indexación "[]" generará un  error
de tipo "KeyError". Por lo tanto, es recomendable verificar que la  clave  utilizada  exista  en  el
diccionario antes de realizar eliminaciones. Esto se puede lograr utilizando el operador  "in"  para
comprobar la existencia de la clave.

Por último, es importante destacar que estas características hacen que los  diccionarios  en  Python
sean una herramienta poderosa y flexible para trabajar con colecciones de datos,  permitiendo  tanto
el acceso como la eliminación de sus pares clave-valor de manera eficiente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────