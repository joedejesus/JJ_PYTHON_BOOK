# Enunciado:
"""La forma más común de crear una lista en Python es utilizando  corchetes  [  ].  Las  listas  son
estructuras de datos que permiten almacenar múltiples elementos en un solo objeto.  Estos  elementos
pueden ser de cualquier tipo de dato, como números, textos, otras listas, entre  otros.  Para  crear
una lista, simplemente se colocan los elementos dentro de los corchetes [ ] y se separan  con  comas
(,).

Las listas en Python son objetos ordenados, mutables e iterables. Esto significa que  los  elementos
de una lista mantienen un orden específico, pueden modificarse después de su creación  y  se  pueden
recorrer utilizando bucles o funciones de iteración.

Además, pueden contener una combinación de diferentes tipos de datos, lo que las  hace  flexibles  y
útiles en una amplia gama de aplicaciones. Por ejemplo, una lista puede  contener  números  enteros,
cadenas de texto, valores booleanos, operaciones matemáticas e incluso otras  listas  o  estructuras
más complejas.

Es importante ser consistente en el uso de listas dentro de un proyecto, ya que esto asegura que  el
código sea más legible y menos propenso a errores. La consistencia incluye  no  solo  el  estilo  de
definición de las listas, sino también la forma en  que  se  accede  a  ellas  y  se  manipulan  sus
elementos.

Por último, las listas son muy versátiles y permiten realizar operaciones como agregar,  eliminar  o
modificar elementos, lo que las convierte en una herramienta esencial para cualquier programador que
trabaje con Python."""

# Ejemplo_crear_una_lista.py

# Explicación:
"""Definimos una variable llamada "lista_1" y le asignamos una lista que contiene  números  enteros.
Luego, definimos otra variable llamada "lista_2" y le asignamos una lista  que  contiene  diferentes
tipos de datos. Para ello, en ambos casos utilizamos corchetes [ ] para crear las listas y separamos
cada elemento dentro de ellas con comas (,). En cada elemento de las listas respetamos  la  sintaxis
correspondiente al tipo de dato que estamos utilizando.

Por último, utilizamos la función "print()" para mostrar las listas en la consola, acompañadas de un
mensaje en formato "f-string" que indica el contenido de cada lista.

De esta forma, hemos creado dos listas en Python: una con números  enteros  y  otra  con  diferentes
tipos de datos, demostrando la flexibilidad y versatilidad de las listas en Python."""

# Código:
lista_1 = [1, 2, 3]
print(f"Esta es una lista de números: {lista_1}")

lista_2 = ["a", 1, True, (3 + 4)]
print(f"Esta es una lista de diferentes tipos de datos: {lista_2}")

# Nota Importante:
"""Es recomendable ser consistente en el uso de listas dentro de un proyecto. Esto significa  elegir
un estilo claro para definir y manipular listas, y mantenerlo en todo el código. La consistencia  no
solo mejora la legibilidad  del  código,  sino  que  también  reduce  la  probabilidad  de  errores,
especialmente en proyectos colaborativos o de gran escala.

Además de este método para  crear  listas,  existen  otras  formas  de  hacerlo,  como  utilizar  el
constructor "list()" para convertir otros tipos de datos iterables en listas.  De  esta  manera,  se
pueden crear listas a partir de tuplas, conjuntos, diccionarios o incluso cadenas de texto.

Las listas pueden contener cualquier tipo de dato, lo que las  hace  extremadamente  flexibles.  Sin
embargo, es importante tener cuidado al mezclar tipos de datos en una lista, ya que esto  puede  dar
lugar a errores si no se manejan adecuadamente.

Por ejemplo, al realizar operaciones sobre los elementos de una lista, puede ser necesario verificar
el tipo de dato de cada elemento para evitar errores en tiempo de ejecución. Por  lo  tanto,  aunque
las listas permiten mezclar tipos de datos, es una buena práctica  mantener  la  coherencia  en  los
tipos de datos almacenados siempre que sea posible.

Por último, un objeto mutable es aquel que puede modificarse después de su creación. En el  caso  de
las listas, esto significa que podemos agregar, eliminar o  modificar  elementos  de  la  lista  sin
necesidad de crear  una  nueva  cada  vez  que  queramos  hacer  un  cambio.  Esta  es  una  de  las
características más importantes de las listas, ya que nos  permite  trabajar  con  datos  de  manera
eficiente y flexible, sin tener que preocuparnos por la necesidad de  crear  nuevas  estructuras  de
datos cada vez que queramos realizar una modificación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
