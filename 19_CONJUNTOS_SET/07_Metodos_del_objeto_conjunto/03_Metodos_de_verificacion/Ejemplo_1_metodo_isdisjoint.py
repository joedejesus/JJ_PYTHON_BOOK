# Enunciado:
"""El método ".isdisjoint()" en Python se utiliza para comprobar si dos conjuntos (set) no comparten
ningún elemento en común. Este método devuelve  un  valor  booleano:  "True"  si  no  existe  ningún
elemento compartido entre el conjunto original y el iterable proporcionado como argumento, y "False"
si al menos un elemento coincide. Es una herramienta útil para  trabajar  con  conjuntos  cuando  se
necesita verificar si dos colecciones son completamente independientes entre sí.

Este método puede aplicarse a cualquier objeto de tipo set en  Python,  así  como  a  otros  objetos
iterables cuyos elementos sean comparables, como listas, tuplas, diccionarios (tomando sus claves) o
cadenas de texto. Este método no modifica el  conjunto  original,  ya  que  únicamente  realiza  una
comprobación lógica y devuelve un valor booleano, el cual se almacena en  la  variable  asignada  al
resultado de la aplicación del método.

El método ".isdisjoint()" toma un único argumento, que es el iterable con el que se desea  comprobar
si existe algún elemento en común. Este argumento puede pasarse como un valor  literal  o  como  una
variable que contenga el iterable. El método evaluará  si  alguno  de  los  elementos  del  iterable
coincide con alguno de los del conjunto original.

Por último, el método ".isdisjoint()" es una herramienta sencilla, pero poderosa, para comprobar  si
dos conjuntos o colecciones no comparten elementos, lo que permite realizar verificaciones rápidas y
seguras sin modificar los datos originales."""

# Ejemplo_1_metodo_isdisjoint.py

# Explicación:
"""Definimos una variable llamada "conjunto"  y  le  asignamos  un  conjunto  que  contiene  números
enteros. Este conjunto se utilizará para demostrar el funcionamiento del método ".isdisjoint()".

A continuación, aplicamos el método ".isdisjoint()" a la variable "conjunto". Para ello,  escribimos
el nombre de la variable "conjunto", seguido del nombre del método ".isdisjoint()" y, dentro de  los
paréntesis, pasamos como argumento un conjunto cuyos elementos deseamos comparar; en este caso,  {6,
7, 8}.

Por último, utilizamos la función "print()" para mostrar el  resultado  de  la  comprobación  en  la
consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar  si  los  conjuntos
comparten o no elementos.

De  esta  forma,  comprobamos  si  dos  conjuntos  no  comparten  elementos  utilizando  el   método
".isdisjoint()", sin modificar el conjunto original."""

# Código:
conjunto = {1, 2, 3, 4, 5}

resultado = conjunto.isdisjoint({6, 7, 8})
print(f"¿Los conjuntos no comparten elementos? {resultado}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".isdisjoint()" no modifica  el  conjunto  original,
sino que realiza una comprobación lógica para determinar si los conjuntos  no  comparten  elementos.
Esto significa que el conjunto original permanece sin cambios, lo  que  puede  ser  útil  en  muchos
casos, aunque también puede provocar errores si no se maneja con cuidado.

Además, este método devuelve un valor booleano, lo que lo convierte en una  herramienta  ideal  para
realizar validaciones previas antes de ejecutar operaciones  entre  conjuntos,  evitando  errores  o
comportamientos inesperados cuando se requiere que los conjuntos no compartan elementos.

Por último, el método ".isdisjoint()" es una herramienta esencial para  trabajar  con  conjuntos  en
Python, ya que permite comprobar de forma segura y sencilla si dos colecciones no  tienen  elementos
en común. De esta  forma,  se  podrán  aprovechar  al  máximo  sus  capacidades  y  evitar  posibles
inconvenientes en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────