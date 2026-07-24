# Enunciado:
"""La función "len()" es una función incorporada de  Python  que  permite  conocer  la  cantidad  de
elementos que contiene un conjunto (set),  es  decir,  su  longitud.  Esta  función  es  ampliamente
utilizada en programación debido a su simplicidad y eficiencia.

La función "len()" toma un conjunto u otra estructura iterable como argumento y devuelve  un  número
entero que representa la cantidad de elementos que contiene. En el caso de los conjuntos, la función
"len()" cuenta cada elemento único para proporcionar una medida precisa de su longitud. Esto incluye
cualquier tipo de dato almacenado dentro del conjunto, como números,  cadenas  de  texto  u  objetos
inmutables.

Es importante destacar que, si se crea un conjunto a partir de un iterable  que  contiene  elementos
duplicados, la función "len()" contará solo los elementos únicos, ya que los conjuntos  no  permiten
duplicados.

La función "len()" permite realizar operaciones como validar la longitud de conjuntos en algoritmos,
analizar datos en estructuras más complejas y controlar el flujo de programas  que  dependen  de  la
cantidad de elementos en un conjunto.

Además, su implementación en Python está optimizada para ofrecer un rendimiento rápido, confiable  y
eficiente, independientemente del tamaño del conjunto o  de  la  estructura  iterable  que  se  esté
evaluando. Esto  la  convierte  en  una  herramienta  fundamental  para  tareas  que  involucran  la
manipulación y el análisis de datos en conjuntos, así como para el manejo de  estructuras  iterables
como listas, tuplas y diccionarios.

Por último, su versatilidad y facilidad de uso hacen que la función "len()" sea una de las funciones
más utilizadas, lo que permite resolver problemas comunes de manera eficiente y con  un  código  más
legible."""

# Ejemplo_medir_la_longitud_de_un_conjunto.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto que contiene números enteros
del 1 al 5. Para ello, utilizamos llaves {} y separamos sus elementos con comas (,).

A continuación, definimos una variable llamada "longitud" y le asignamos el resultado de llamar a la
función "len()" con la variable "conjunto" como argumento. Para ello, escribimos  el  nombre  de  la
función "len()" y, dentro de los paréntesis, colocamos la variable "conjunto" como argumento.

La función "len()" toma como argumento el conjunto y devuelve un número  entero  que  representa  la
cantidad de elementos únicos que contiene, el cual se almacena en la variable "longitud".

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica que se trata de la longitud  del  conjunto.  De
esta forma, obtenemos la longitud del conjunto {1, 2, 3, 4, 5}, que es 5, ya que la función  "len()"
cuenta cada elemento único del conjunto.

Por último, utilizamos la función "len()"  directamente  con  un  conjunto  literal  para  medir  su
longitud. Para ello, utilizamos la función  "print()"  y,  dentro  de  esta,  colocamos  la  función
"len()", que toma como argumento el conjunto literal {"a",  "b",  "c",  "d"},  lo  que  nos  permite
obtener la longitud de este conjunto directamente, sin necesidad de almacenarla en una variable.

En este caso, también podríamos pasar como argumento a la función  "len()",  dentro  de  la  función
"print()", una variable que almacene un conjunto, de esta forma: "print(len(conjunto))", lo que  nos
permitiría medir la longitud de cualquier conjunto almacenado en  la  variable  de  forma  rápida  y
directa."""

# Código:
conjunto = {1, 2, 3, 4, 5}

longitud = len(conjunto)
print(f"La longitud del conjunto es: {longitud}")

print(len({"a", "b", "c", "d"}))

# Nota Importante:
"""La función "len()" también se utiliza para obtener la  longitud  o  el  número  de  elementos  de
estructuras como las tuplas, los diccionarios, las cadenas de texto,  las  listas  y  otros  objetos
iterables. Lo que hace que esta  función  sea  tan  versátil  es  su  capacidad  para  trabajar  con
diferentes tipos de datos, realizar  validaciones  o  implementar  algoritmos  que  dependan  de  la
longitud de las estructuras de datos.

Es importante destacar que la función "len()" no mide el tamaño de un objeto en memoria,  en  bytes,
sino la cantidad de elementos que contiene. Esto significa que, en el  caso  de  los  conjuntos,  la
longitud corresponde al número de elementos únicos almacenados, mientras  que,  en  las  cadenas  de
texto, se refiere al número de caracteres y, en los diccionarios, al número de claves almacenadas  y
no a la cantidad de memoria que ocupan.

Por último, la función "len()" es una  herramienta  clave  para  optimizar  procesos  que  requieren
conocer la cantidad de elementos en una estructura, como en algoritmos de búsqueda, clasificación  o
análisis de datos. Su capacidad para trabajar con diferentes tipos de datos  y  su  integración  con
otras funciones y estructuras  de  Python  la  convierten  en  una  herramienta  indispensable  para
cualquier programador que busque escribir código eficiente, robusto y fácil de mantener."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────