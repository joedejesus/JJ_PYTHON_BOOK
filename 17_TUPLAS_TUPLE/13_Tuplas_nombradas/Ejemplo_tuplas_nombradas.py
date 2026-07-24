# Enunciado:
"""Las tuplas nombradas son una característica avanzada de Python que  permite  crear  tuplas  cuyos
elementos pueden ser accedidos mediante nombres en lugar de índices. Esto  mejora  la  claridad,  la
legibilidad y la organización del código, ya que cada elemento  recibe  un  nombre  descriptivo  que
facilita su uso en estructuras de datos complejas.

En  Python,  las  tuplas  nombradas  se  crean  utilizando  la  función  "namedtuple"   del   módulo
"collections". Esta función  permite  definir  una  nueva  clase  de  tupla  con  campos  nombrados,
proporcionando una forma más estructurada y expresiva de representar datos. Al igual que las  tuplas
comunes, las tuplas nombradas son inmutables, lo que garantiza la integridad de los  datos  y  evita
modificaciones accidentales.

Para crear una tupla nombrada, se debe importar la función  "namedtuple"  del  módulo  "collections"
utilizando la siguiente sintaxis: "from collections import namedtuple".

Una vez  importada,  la  sintaxis  para  definir  una  tupla  nombrada  es  la  siguiente:  tupla  =
namedtuple("NombreDeLaTupla", ["campo1", "campo2", "campo3"])

Después de definir la clase, se pueden crear instancias de la tupla nombrada utilizando la  sintaxis
de llamada a la clase y pasando  los  valores  correspondientes  para  cada  campo  como  argumentos
nombrados. Por ejemplo: opcion = tupla(nombre="Joe", edad=34, ocupacion="Desarrollador de Software")

Además, también es posible acceder a los valores de forma independiente utilizando  la  sintaxis  de
acceso por nombre: opcion.ocupacion

Las tuplas nombradas ofrecen una sintaxis clara y concisa para definir y acceder a  los  campos,  lo
que mejora la legibilidad del código y reduce la posibilidad de errores. Esto es especialmente  útil
en proyectos grandes, donde la claridad y la organización del código son fundamentales.

Por último, las tuplas nombradas son una herramienta poderosa para representar  datos  estructurados
de forma legible, segura e inmutable."""

# Ejemplo_tuplas_nombradas.py

# Explicación:
"""Importamos la  función  "namedtuple"  del  módulo  "collections"  utilizando  la  sintaxis:  from
collections import namedtuple

A continuación, definimos una variable llamada "tupla" y le asignamos el resultado de  llamar  a  la
función "namedtuple()" con los argumentos necesarios  para  crear  una  tupla  nombrada.  El  primer
argumento es el nombre de la clase, en este caso "Persona". El segundo argumento es  una  lista  con
los nombres de los campos: ["nombre", "edad", "ocupacion"].

De esta forma, hemos creado una clase de tupla nombrada llamada "Persona" con los  campos  "nombre",
"edad" y "ocupacion".

Luego, creamos  una  instancia  de  esta  tupla  nombrada  llamada  "opcion",  pasando  los  valores
correspondientes para cada campo mediante argumentos nombrados.

Por último, imprimimos la instancia completa y uno de sus campos utilizando  la  función  "print()",
acompañada de mensajes descriptivos en formato "f-string"."""

# Código:
from collections import namedtuple

tupla = namedtuple("Persona", ["nombre", "edad", "ocupacion"])

opcion = tupla(nombre="Joe", edad=34, ocupacion="Desarrollador de Software")

print(f"Esta es la opción: {opcion}")
print(f"Ocupación: {opcion.ocupacion}")

# Nota Importante:
"""Las tuplas nombradas son inmutables, lo que significa  que  sus  valores  no  pueden  modificarse
después de su creación. Esto garantiza la consistencia de los datos y evita efectos  secundarios  no
deseados.

Los nombres de los campos también pueden definirse  como  una  cadena  separada  por  espacios,  por
ejemplo: "nombre edad ocupacion" lo que ofrece una sintaxis más compacta.

Además, las tuplas nombradas son ideales para  representar  datos  estructurados,  ya  que  permiten
acceder a los elementos por nombre en lugar de por índice, lo que mejora  la  legibilidad  y  reduce
errores.

Sin embargo, debido a su inmutabilidad, no son adecuadas para datos que  necesiten  modificarse  con
frecuencia. En esos casos, puede ser más apropiado utilizar diccionarios o clases personalizadas.

Por último, el uso de "namedtuple"  es  una  forma  eficiente  y  flexible  de  trabajar  con  datos
estructurados en Python, especialmente cuando se requiere claridad, seguridad e inmutabilidad."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
