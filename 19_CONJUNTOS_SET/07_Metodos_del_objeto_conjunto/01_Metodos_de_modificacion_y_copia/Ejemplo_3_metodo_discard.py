# Enunciado:
"""El método ".discard()" en Python se utiliza para eliminar un elemento específico de  un  conjunto
(set). Este método modifica el conjunto original directamente, eliminando el elemento indicado si se
encuentra en el conjunto. Es una herramienta útil para trabajar  con  conjuntos  dinámicos,  ya  que
permite eliminar elementos de manera selectiva.

El método ".discard()" puede aplicarse a cualquier objeto de tipo  set  en  Python,  como  conjuntos
literales, variables que contienen conjuntos o incluso resultados de otras operaciones  que  generan
conjuntos. Este método modifica el conjunto original  directamente,  lo  que  significa  que  no  es
necesario asignar el resultado de su aplicación a una nueva variable, ya que no  devuelve  un  nuevo
objeto, sino que altera el objeto existente. Este comportamiento es consistente  con  la  naturaleza
mutable de los conjuntos en Python.

El método ".discard()" toma un único argumento, que  es  el  elemento  que  se  desea  eliminar  del
conjunto. Si el elemento no se encuentra en el conjunto, no se genera ningún error. Por lo tanto, es
seguro utilizarlo incluso si no se está seguro de que el elemento esté presente en el conjunto.

Este argumento puede pasarse al método como un valor literal o como una  variable  que  contenga  el
valor a eliminar. Además, el argumento debe coincidir exactamente  con  el  elemento  que  se  desea
eliminar, incluido el tipo de dato.

Por último, el método ".discard()"  es  una  herramienta  sencilla,  pero  poderosa,  para  eliminar
elementos de conjuntos en Python, permitiendo una manipulación eficiente y flexible de los conjuntos
según las necesidades del programa, sin riesgo de errores si el elemento no existe."""

# Ejemplo_3_metodo_discard.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto que contiene números enteros
y una cadena de texto. Este conjunto se  utilizará  para  demostrar  el  funcionamiento  del  método
".discard()".

A continuación, aplicamos el método ".discard()" a la variable "conjunto". Para ello, escribimos  el
nombre de la variable "conjunto" seguido del  nombre  del  método  ".discard()",  y  dentro  de  los
paréntesis, pasamos como argumento el elemento que deseamos eliminar, en este caso, el número entero
2.

Por último, utilizamos la función "print()" para mostrar el contenido del conjunto  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método al conjunto.

De esta forma, hemos eliminado un elemento específico del conjunto, en este caso el número entero 2,
y modificado el conjunto original directamente con el método ".discard()"."""

# Código:
conjunto = {1, 2, 3, "2", 4, 5}

conjunto.discard(2)
print(f"Este es el resultado de aplicar el método al conjunto: {conjunto}")

# Nota Importante:
"""Es fundamental tener  en  cuenta  que  el  método  ".discard()"  modifica  el  conjunto  original
directamente, ya que los conjuntos en Python son  mutables.  Esto  significa  que  cualquier  cambio
realizado en el conjunto afecta al objeto original, lo que puede ser  útil  en  muchos  casos,  pero
también puede llevar a errores si no se maneja con cuidado.

Además, en el caso de los conjuntos, cada elemento es único, por lo que no existen duplicados. Si el
elemento especificado no se encuentra en el conjunto, el método ".discard()" no genera ningún error;
simplemente no realiza ninguna acción.

Esto hace que ".discard()" sea especialmente útil cuando no se está seguro de que el  elemento  esté
presente en el conjunto, ya que  evita  la  necesidad  de  comprobar  su  existencia  o  de  manejar
excepciones.

Por último, el método ".discard()" es una  herramienta  esencial  para  trabajar  con  conjuntos  en
Python, permitiendo eliminar elementos de forma segura y sencilla,  sin  riesgo  de  errores  si  el
elemento no existe. De esta forma, se podrán aprovechar al máximo sus capacidades y evitar  posibles
inconvenientes en su implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────