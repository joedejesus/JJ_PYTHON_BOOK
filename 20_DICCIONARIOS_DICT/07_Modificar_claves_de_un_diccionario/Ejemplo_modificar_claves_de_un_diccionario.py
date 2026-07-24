# Enunciado:
"""Para modificar las claves de un diccionario en Python, es importante  comprender  que  no  pueden
modificarse directamente.  A  diferencia  de  los  valores,  que  sí  pueden  actualizarse  mediante
asignación, las claves son inmutables dentro de la estructura del diccionario. Esto significa que no
es posible cambiar una clave existente de forma directa utilizando el operador de indexación.

Sin embargo, Python permite modificar claves de manera indirecta mediante un proceso de  dos  pasos:
crear una nueva clave con el valor asociado a la clave antigua y, posteriormente, eliminar la  clave
original. Este procedimiento es fundamental  para  trabajar  con  diccionarios  cuando  se  necesita
actualizar la estructura de las claves sin perder la información almacenada en los valores.

Los diccionarios en Python son colecciones mutables de  pares  clave-valor,  lo  que  significa  que
podemos agregar nuevas claves, eliminar claves existentes y modificar los valores asociados. Además,
los diccionarios son iterables, lo  que  permite  recorrerlos  o  acceder  a  cada  par  clave-valor
utilizando sus claves u otros métodos de iteración.

Por último, es importante destacar que esta técnica de "modificar" claves  resulta  útil  cuando  se
requiere actualizar identificadores, normalizar los nombres de las claves o  adaptar  la  estructura
del diccionario a nuevas necesidades del programa. También es importante tener en  cuenta  que  este
proceso afecta directamente al diccionario original, por lo que es fundamental asegurarse de que los
cambios sean intencionales y de que no generen efectos secundarios no deseados."""

# Ejemplo_modificar_claves_de_un_diccionario.py

# Explicación:
"""Definimos una variable llamada "aeropuertos" y le asignamos un diccionario que  contiene  códigos
de aeropuertos como claves y nombres de aeropuertos como valores. Este diccionario se utilizará para
modificar una de sus claves mediante un proceso de reasignación y eliminación.

A continuación, creamos una nueva clave llamada "NEW_UIO" y le asignamos  el  valor  asociado  a  la
clave existente "UIO". Para ello, utilizamos el operador de indexación [] con la clave "UIO"  en  su
interior,  precedido  por  la  variable  "aeropuertos",  lo  que  nos  permite  obtener   el   valor
correspondiente. Luego, asignamos ese valor a la nueva clave "NEW_UIO"  utilizando  el  operador  de
asignación (=).

Una vez creada la nueva clave con el valor deseado, eliminamos la clave antigua "UIO" utilizando  la
instrucción "del". De esta forma, simulamos la modificación de  la  clave  al  reemplazar  la  clave
antigua por una nueva, sin perder el valor asociado.

Estas operaciones se realizan directamente sobre el diccionario original, ya que los diccionarios en
Python son mutables.

Por último, utilizamos la función "print()" para mostrar el diccionario actualizado en  la  consola,
acompañada de un mensaje descriptivo en formato "f-string" para indicar los cambios realizados."""

# Código:
aeropuertos = {
    "UIO": "Aeropuerto Internacional Mariscal Sucre",
    "JFK": "John F. Kennedy",
    "LAX": "Los Angeles Internacional"
}

aeropuertos["NEW_UIO"] = aeropuertos["UIO"]  # Creamos la nueva clave con el valor existente.
del aeropuertos["UIO"]                       # Eliminamos la clave original.

print(f"Este es el diccionario actualizado: {aeropuertos}")

# Nota Importante:
"""Es importante tener en cuenta que las claves de un diccionario no pueden modificarse directamente
debido a su naturaleza inmutable dentro de  la  estructura  del  diccionario.  Por  lo  tanto,  para
"modificar" una clave, es necesario crear una nueva clave con el valor deseado y eliminar  la  clave
anterior.

Los diccionarios en Python pueden contener valores de  diferentes  tipos,  por  lo  que  es  posible
modificar claves que apuntan a valores numéricos, cadenas de texto, listas u otros diccionarios  sin
ningún problema. Esto se debe a que los diccionarios son heterogéneos, lo que  permite  almacenar  y
manipular valores de diferentes tipos dentro de la misma estructura de datos.

Es posible modificar  más  de  una  clave  a  la  vez  utilizando  técnicas  como  comprensiones  de
diccionarios o iteraciones sobre las claves existentes. Por ejemplo, si se  desea  normalizar  todas
las claves a mayúsculas, se puede crear un nuevo diccionario con las claves  transformadas  y  luego
reemplazar el diccionario original.

En el caso de los diccionarios, no es necesario almacenar el resultado de  la  modificación  en  una
nueva variable, ya que el cambio se realiza directamente sobre el diccionario original debido  a  su
naturaleza mutable. Esto significa  que  cualquier  cambio  realizado  en  el  diccionario  afectará
directamente al contenido original.

Además, intentar acceder a una clave inexistente utilizando el operador de indexación "[]"  generará
un error de tipo "KeyError". Por lo tanto, es recomendable verificar si la clave  existe  utilizando
el operador "in" o el método ".get()" antes de  realizar  modificaciones,  cuando  se  desee  evitar
errores o la creación accidental de nuevas claves.

Por último, es importante destacar que estas características hacen que los  diccionarios  en  Python
sean una herramienta poderosa y flexible para trabajar con colecciones de  datos,  ya  que  permiten
tanto la modificación de valores como la actualización de sus claves de manera eficiente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────