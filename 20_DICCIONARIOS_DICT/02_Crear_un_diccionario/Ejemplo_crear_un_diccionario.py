# Enunciado:
"""La forma más común de crear un diccionario en Python es utilizando llaves { }.  Los  diccionarios
son estructuras de datos que permiten almacenar múltiples elementos en un solo  objeto,  organizados
en pares clave-valor. Las claves deben ser inmutables,  mientras  que  los  valores  pueden  ser  de
cualquier tipo de dato, como números, textos, listas, otros diccionarios, entre otros. Para crear un
diccionario, simplemente se colocan los pares clave-valor dentro de las llaves { } y se separan  por
comas (,).

Los diccionarios en Python son objetos mutables e iterables. Además, desde Python 3.7, mantienen  el
orden de inserción. Esto significa que los elementos de un diccionario pueden modificarse después de
su creación y que se pueden recorrer utilizando  bucles  o  funciones  de  iteración,  accediendo  a
claves, valores o pares clave-valor.

Además, los diccionarios pueden contener una combinación de diferentes tipos de datos tanto  en  las
claves (como  cadenas,  números  o  tuplas  inmutables)  como  en  los  valores,  lo  que  los  hace
extremadamente flexibles y útiles en una amplia gama de aplicaciones. Por  ejemplo,  un  diccionario
puede contener números enteros, cadenas de  texto,  valores  booleanos,  resultados  de  operaciones
matemáticas, listas, otros diccionarios o estructuras más complejas.

Por último, es importante ser consistente en el uso de diccionarios dentro de un  proyecto,  ya  que
esto hace que el código sea más legible y menos propenso a errores. La consistencia incluye no  solo
el estilo de definición de los diccionarios, sino también la forma en que se accede  a  ellos  y  se
manipulan sus elementos. Además, los diccionarios son muy versátiles y permiten realizar operaciones
como agregar, eliminar o modificar pares clave-valor,  lo  que  los  convierte  en  una  herramienta
esencial para cualquier programador que trabaje con Python."""

# Ejemplo_crear_un_diccionario.py

# Explicación:
"""Definimos una variable llamada "diccionario_1" y le asignamos un diccionario que contiene  claves
y valores numéricos. Luego, definimos otra  variable  llamada  "diccionario_2"  y  le  asignamos  un
diccionario que contiene diferentes  tipos  de  datos  como  valores.  Para  ello,  en  ambos  casos
utilizamos llaves { } para crear los diccionarios y separamos cada par clave-valor  con  comas  (,).
Para cada clave y valor, respetamos  la  sintaxis  correspondiente  al  tipo  de  dato  que  estamos
utilizando y separamos la clave del valor con dos puntos (:).

Por último, utilizamos la función "print()" para mostrar los diccionarios en la consola, acompañados
de un mensaje en formato "f-string" que indica el contenido de cada diccionario.

De esta forma, hemos creado dos diccionarios en  Python:  uno  con  valores  numéricos  y  otro  con
diferentes tipos de datos, demostrando  la  flexibilidad  y  versatilidad  de  los  diccionarios  en
Python."""

# Código:
diccionario_1 = {"a": 1, "b": 2, "c": 3}
print(f"Este es un diccionario con valores numéricos: {diccionario_1}")

diccionario_2 = {"x": "texto", "y": 10, "z": True, "w": (3 + 4)}
print(f"Este es un diccionario con diferentes tipos de datos: {diccionario_2}")

# Nota Importante:
"""Es recomendable ser consistente en el uso de diccionarios dentro de un proyecto.  Esto  significa
elegir un estilo claro para definir y manipular diccionarios, y mantenerlo en  todo  el  código.  La
consistencia no solo mejora la legibilidad del código, sino que también reduce  la  probabilidad  de
errores, especialmente en proyectos colaborativos o de gran escala.

Además de este método para crear diccionarios, existen otras formas de  hacerlo,  como  utilizar  el
constructor "dict()" para convertir otros tipos de datos en diccionarios. De esta manera, se  pueden
crear diccionarios a partir de listas de tuplas, pares clave-valor,  otros  diccionarios  o  incluso
mediante comprensiones de diccionarios.

Los diccionarios pueden contener cualquier tipo de dato como valor, lo que los  hace  extremadamente
flexibles. Sin embargo, es importante tener cuidado al elegir las claves, ya  que  estas  deben  ser
inmutables y únicas dentro del diccionario.

Por ejemplo, al realizar operaciones sobre los elementos de  un  diccionario,  puede  ser  necesario
verificar el tipo de dato de cada valor para evitar errores en tiempo de ejecución.  Por  lo  tanto,
aunque los diccionarios permiten mezclar tipos de datos, es una buena práctica  mantener  coherencia
en los tipos de datos almacenados siempre que sea posible.

Por último, un objeto mutable es aquel que puede ser modificado después de su creación. En  el  caso
de los diccionarios, esto significa que podemos agregar, eliminar o modificar pares clave-valor  sin
necesidad de crear un nuevo diccionario cada vez que queramos hacer un cambio. Esta es  una  de  las
características más importantes de los diccionarios, ya que nos permite trabajar con datos de manera
eficiente y flexible, sin tener que preocuparnos por la necesidad de  crear  nuevas  estructuras  de
datos cada vez que queramos realizar una modificación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────