# Enunciado:
"""El método ".issubset()" en Python se utiliza para comprobar si todos los elementos de un conjunto
(set) están contenidos dentro de otro conjunto o iterable. Este método devuelve un  valor  booleano:
"True" si el conjunto original es un subconjunto del iterable proporcionado y "False"  si  al  menos
uno de sus elementos no se encuentra en él. Es una herramienta útil para trabajar con relaciones  de
inclusión entre conjuntos, especialmente cuando se necesita verificar si un conjunto cumple  ciertos
requisitos o pertenece a una categoría más amplia.

Este método puede aplicarse a cualquier objeto de tipo set en  Python,  así  como  a  otros  objetos
iterables, como listas, tuplas, diccionarios (tomando sus claves) o cadenas de texto. Este método no
modifica el conjunto original, ya que únicamente realiza una comprobación lógica y devuelve un valor
booleano, el cual se almacena en la variable asignada al resultado de la aplicación del método.

El método ".issubset()" toma un único argumento, que es el iterable con el que se desea comprobar si
el conjunto original está completamente contenido.  Este  argumento  puede  pasarse  como  un  valor
literal o como una variable que contenga el iterable. El método evaluará si todos los elementos  del
conjunto original están presentes en el iterable proporcionado.

Por último, el método ".issubset()" es una herramienta sencilla pero poderosa para comprobar  si  un
conjunto está contenido dentro de otro, lo que permite realizar verificaciones rápidas y seguras sin
modificar los datos originales."""

# Ejemplo_2_metodo_issubset.py

# Explicación:
"""Definimos una variable llamada "conjunto"  y  le  asignamos  un  conjunto  que  contiene  números
enteros. Este conjunto se utilizará para demostrar el funcionamiento del método ".issubset()".

A continuación, aplicamos el método ".issubset()" a la variable "conjunto". Para ello, escribimos el
nombre de la variable "conjunto" seguido del nombre  del  método  ".issubset()"  y,  dentro  de  los
paréntesis, pasamos como argumento un conjunto de referencia que contiene los elementos {1, 2, 3, 4,
5}.

Por último, utilizamos la función "print()" para mostrar el  resultado  de  la  comprobación  en  la
consola, acompañado de un mensaje descriptivo en formato "f-string"  para  indicar  si  el  conjunto
original está o no contenido dentro del otro conjunto.

De esta forma,  comprobamos  si  un  conjunto  es  un  subconjunto  de  otro  utilizando  el  método
".issubset()", sin modificar el conjunto original."""

# Código:
conjunto = {1, 2, 3}

resultado = conjunto.issubset({1, 2, 3, 4, 5})
print(f"¿El conjunto es un subconjunto del otro? {resultado}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".issubset()" no modifica el conjunto original, sino
que realiza una comprobación lógica para determinar si un conjunto está contenido  dentro  de  otro.
Esto significa que el conjunto original permanece sin cambios, lo  que  puede  ser  útil  en  muchos
casos, aunque también puede provocar confusiones si no se interpreta correctamente el resultado.

Además, este método devuelve un valor booleano, lo que lo convierte en una  herramienta  ideal  para
realizar validaciones previas antes de ejecutar operaciones entre conjuntos, especialmente cuando se
necesita comprobar si un conjunto cumple con ciertos requisitos o  pertenece  a  una  categoría  más
amplia.

Por último, el método ".issubset()" es una herramienta  esencial  para  trabajar  con  conjuntos  en
Python, permitiendo comprobar de forma segura y sencilla si un conjunto está completamente contenido
dentro de otro. De esta forma, se podrán aprovechar al máximo  sus  capacidades  y  evitar  posibles
inconvenientes en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────