# Enunciado:
"""El método ".clear()" en Python se utiliza para eliminar todos los elementos de un conjunto (set).
Este método modifica el conjunto original directamente, eliminando todos los elementos que  contiene
y dejándolo vacío, pero mantiene el conjunto como un objeto de tipo (set) válido y mutable.

El método ".clear()" puede aplicarse a cualquier objeto de tipo  (set)  en  Python,  como  conjuntos
literales, variables que contienen conjuntos o incluso resultados de otras operaciones  que  generan
conjuntos. Este método modifica el conjunto original  directamente,  lo  que  significa  que  no  es
necesario asignar el resultado de su aplicación a una nueva variable, ya que no  devuelve  un  nuevo
objeto, sino que altera el objeto existente. Este comportamiento  es  coherente  con  la  naturaleza
mutable de los conjuntos en Python.

El método ".clear()" no toma argumentos adicionales, ya que su propósito es  simplemente  vaciar  el
conjunto. Esto lo convierte en una  herramienta  sencilla  y  eficiente  para  reiniciar  conjuntos.
Además, los elementos eliminados pueden ser liberados por el recolector  de  basura  si  no  existen
otras referencias a ellos en el programa, lo que ayuda a gestionar la memoria de manera eficiente.

Por último, el método ".clear()" es una herramienta sencilla pero  útil  para  vaciar  conjuntos  en
Python, permitiendo una manipulación eficiente de los datos en estructuras de tipo (set)."""

# Ejemplo_5_metodo_clear.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un  conjunto  con  diferentes  tipos  de
datos inmutables, incluyendo valores booleanos, números enteros, cadenas de texto  y  una  expresión
matemática. Este conjunto se utilizará para demostrar el funcionamiento del método ".clear()".

A continuación, aplicamos el método ".clear()" a la variable "conjunto". Para  ello,  escribimos  el
nombre de la variable "conjunto" seguido del nombre del método ".clear()" con los paréntesis vacíos,
ya que este método no requiere ningún argumento para funcionar.

Por último, utilizamos la función "print()" para mostrar el contenido del conjunto  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método al conjunto.

De esta forma, hemos vaciado completamente el conjunto, modificándolo  directamente  con  el  método
".clear()"."""

# Código:
conjunto = {True, 3, "Hola", 5, False, "Adiós", (7 + 5)}

conjunto.clear()
print(f"Este es el resultado de aplicar el método al conjunto: {conjunto}")

# Nota Importante:
"""Es  fundamental  tener  en  cuenta  que  el  método  ".clear()"  modifica  el  conjunto  original
directamente, ya que los conjuntos en Python son  mutables.  Esto  significa  que  cualquier  cambio
realizado en el conjunto afecta al objeto original, lo que puede ser  útil  en  muchos  casos,  pero
también puede dar lugar a errores si no se maneja con cuidado.

Es importante recordar que este método elimina todos los elementos del conjunto, dejándolo vacío. Si
se desea conservar los elementos del conjunto antes de vaciarlo, se  debe  realizar  una  copia  del
conjunto antes de aplicar el método ".clear()". Esto se puede lograr utilizando el método ".copy()",
el cual crea un nuevo conjunto con los mismos elementos, permitiendo así mantener una referencia  al
conjunto original antes de vaciarlo.

Además, el método ".clear()" es útil en situaciones en las que se  necesita  reiniciar  un  conjunto
para reutilizarlo en un contexto diferente. Los elementos eliminados podrán  ser  liberados  por  el
recolector de basura si no existen otras referencias a ellos en el programa.

Por último, el método ".clear()" es una herramienta útil para trabajar con conjuntos en Python, pero
su uso debe ir acompañado de una comprensión clara de sus características y  limitaciones.  De  esta
forma, se podrán aprovechar al máximo  sus  capacidades  y  evitar  posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────