# Enunciado:
"""La función "len()" es una función incorporada de  Python  que  permite  conocer  la  cantidad  de
elementos que contiene una lista, es decir, su longitud. Esta función es  ampliamente  utilizada  en
programación debido a su simplicidad y eficiencia.

La función "len()" toma una lista u otra estructura iterable como argumento  y  devuelve  un  número
entero que representa la cantidad de elementos que contiene. En el caso de las  listas,  la  función
"len()" cuenta cada elemento para proporcionar una medida  precisa  de  su  longitud.  Esto  incluye
cualquier tipo de dato almacenado dentro de la lista, ya sean números, cadenas de texto,  objetos  o
incluso otras listas.

La función "len()" permite realizar operaciones como validar la longitud de  listas  en  algoritmos,
analizar datos en estructuras más complejas y controlar el flujo de programas  que  dependen  de  la
cantidad de elementos de una lista.

Además, su implementación en Python está optimizada para ofrecer un rendimiento rápido, confiable  y
eficiente, independientemente del tamaño de la lista  o  de  la  estructura  iterable  que  se  esté
evaluando. Esto  la  convierte  en  una  herramienta  fundamental  para  tareas  que  involucran  la
manipulación y el análisis de datos en listas, así como para el manejo de estructuras iterables como
tuplas y diccionarios.

Por último, su versatilidad y facilidad de uso hacen que la función "len()" sea una de las funciones
más utilizadas, ya que permite resolver problemas comunes de manera eficiente y con  un  código  más
legible."""

# Ejemplo_medir_la_longitud_de_una_lista.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de números enteros [1, 2,  3,  4,
5]. Esta lista se utilizará para medir su longitud mediante la función "len()".

A continuación, definimos una variable llamada "longitud" y le asignamos el resultado de llamar a la
función "len()" con la variable "lista" como argumento.  Para  ello,  escribimos  el  nombre  de  la
función "len()" y, dentro de los paréntesis, colocamos la variable "lista" como argumento.

La función "len()" toma como argumento la lista y  devuelve  un  número  entero  que  representa  la
cantidad de elementos que contiene, el cual se almacena en la variable "longitud".

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica que se trata de la longitud  de  la  lista.  De
esta forma, obtenemos la longitud de la lista [1, 2, 3, 4, 5], que es 5, ya que la  función  "len()"
cuenta cada elemento de la lista.

Por último, utilizamos la función "len()" directamente con una lista literal para medir su longitud.
Para ello, utilizamos la función "print()" y, dentro de esta, colocamos la función "len()", que toma
como argumento la lista literal ["a", "b", "c", "d"], lo que nos permite obtener la longitud de esta
lista directamente, sin necesidad de almacenarla en una variable.

En este caso, también podríamos pasar como argumento a la función  "len()",  dentro  de  la  función
"print()", una variable que almacene una lista, de  esta  forma:  "print(len(lista))",  lo  que  nos
permitiría medir la longitud de cualquier  lista  almacenada  en  la  variable  de  forma  rápida  y
directa."""

# Código:
lista = [1, 2, 3, 4, 5]

longitud = len(lista)
print(f"La longitud de la lista es: {longitud}")

print(len(["a", "b", "c", "d"]))

# Nota Importante:
"""La función "len()" también se utiliza para obtener la  longitud  o  el  número  de  elementos  de
estructuras como tuplas, diccionarios, cadenas de texto, conjuntos y otros objetos iterables. Lo que
hace que esta función sea tan versátil es su capacidad para trabajar con diferentes tipos de  datos,
realizar validaciones o implementar algoritmos que dependan de la longitud de estas  estructuras  de
datos.

Es importante destacar que la función "len()" no mide el tamaño en memoria, en bytes, de un  objeto,
sino la cantidad de elementos que contiene. Esto significa  que,  en  el  caso  de  las  listas,  la
longitud corresponde al número de elementos almacenados; en las cadenas  de  texto,  se  refiere  al
número de caracteres; y en los diccionarios, al número de claves almacenadas, y no a la cantidad  de
memoria que ocupan.

Por último, la función "len()" es una  herramienta  clave  para  optimizar  procesos  que  requieren
conocer la cantidad de elementos de una estructura, como en algoritmos de búsqueda, clasificación  o
análisis de datos. Su capacidad para trabajar con diferentes tipos de datos  y  su  integración  con
otras funciones y estructuras  de  Python  la  convierten  en  una  herramienta  indispensable  para
cualquier programador que busque escribir código eficiente, robusto y fácil de mantener."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
