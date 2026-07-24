# Enunciado:
"""La forma más común de crear una tupla en Python es  utilizando  paréntesis  ().  Las  tuplas  son
estructuras de datos que permiten almacenar múltiples elementos en un solo objeto.  Estos  elementos
pueden ser de cualquier tipo de dato, como números, textos, otras tuplas, entre  otros.  Para  crear
una tupla, simplemente se colocan los elementos dentro de los paréntesis () y se separan  con  comas
(,).

Las tuplas en Python son objetos ordenados e iterables, pero  inmutables.  Esto  significa  que  los
elementos de una tupla mantienen un orden específico, no pueden modificarse después de su creación y
pueden recorrerse utilizando bucles o funciones de iteración.

Además, las tuplas pueden contener una combinación de diferentes tipos de datos,  lo  que  las  hace
flexibles y útiles en una amplia gama de aplicaciones. Por ejemplo, una tupla puede contener números
enteros, cadenas de texto, valores booleanos, expresiones  matemáticas  evaluadas  e  incluso  otras
tuplas o estructuras más complejas.

Por último, es importante mantener la consistencia en el uso de las tuplas dentro de un proyecto, ya
que esto hace que el código sea más legible y menos propenso a errores. La consistencia  incluye  no
solo el estilo de definición de las tuplas, sino también la forma en que se accede a sus elementos y
se utilizan. Aunque las tuplas no permiten modificaciones, su inmutabilidad las  hace  ideales  para
representar datos que no deben cambiar, lo  que  puede  mejorar  la  seguridad  y  la  claridad  del
código."""

# Ejemplo_crear_una_tupla.py

# Explicación:
"""Definimos una variable llamada "tupla_1" y le asignamos una tupla que contiene  números  enteros.
Luego, definimos otra variable llamada "tupla_2" y le asignamos una tupla  que  contiene  diferentes
tipos de datos. Para ello, en ambos casos utilizamos paréntesis () para crear las tuplas y separamos
cada elemento de estas con comas (,). Para  cada  elemento  dentro  de  las  tuplas,  respetamos  la
sintaxis correspondiente al tipo de dato que estamos utilizando.

Por último, utilizamos la función "print()" para mostrar las tuplas en la consola, acompañadas de un
mensaje descriptivo en formato "f-string" que indica el contenido de cada tupla.

De esta forma, hemos creado dos tuplas en Python: una con números  enteros  y  otra  con  diferentes
tipos de datos, demostrando la flexibilidad y versatilidad de las tuplas en Python."""

# Código:
tupla_1 = (1, 2, 3)
print(f"Esta es una tupla de números enteros: {tupla_1}")

tupla_2 = ("a", 1, True, (3 + 4))
print(f"Esta es una tupla de diferentes tipos de datos: {tupla_2}")

# Nota Importante:
"""Es recomendable mantener la consistencia en  el  uso  de  tuplas  dentro  de  un  proyecto.  Esto
significa elegir un estilo claro para definirlas y utilizarlas, y mantenerlo en todo el  código.  La
consistencia no solo mejora la legibilidad del código, sino que también reduce  la  probabilidad  de
errores, especialmente en proyectos colaborativos o de gran escala.

Además de este método para  crear  tuplas,  existen  otras  formas  de  hacerlo,  como  utilizar  el
constructor "tuple()" para convertir otros tipos de datos iterables en tuplas.  De  esta  forma,  se
pueden crear tuplas a partir de listas, conjuntos, diccionarios o incluso cadenas de texto.

Las tuplas pueden contener cualquier tipo de dato, lo que las  hace  extremadamente  flexibles.  Sin
embargo, es importante tener cuidado al mezclar tipos de datos en  una  tupla,  ya  que  esto  puede
provocar errores si no se manejan adecuadamente.

Por ejemplo, al realizar operaciones sobre los elementos de una tupla, puede ser necesario verificar
el tipo de dato de cada elemento para evitar errores en tiempo de ejecución. Por  lo  tanto,  aunque
las tuplas permiten mezclar tipos de datos, es una buena práctica mantener cierta coherencia en  los
tipos de datos almacenados siempre que sea posible.

Por último, un objeto inmutable es aquel que no puede modificarse después de su creación. En el caso
de las tuplas, esto significa que no podemos agregar, eliminar ni modificar sus  elementos  una  vez
creada la tupla. Esta es una de las características más  importantes  de  las  tuplas,  ya  que  nos
permite  trabajar  con  datos  de  manera  segura  y  confiable,  sin  tener  que  preocuparnos  por
modificaciones accidentales."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
