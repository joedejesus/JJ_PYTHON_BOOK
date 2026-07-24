# Enunciado:
"""El método ".extend()" en Python se utiliza para agregar  múltiples  elementos  al  final  de  una
lista. Este método modifica la lista original directamente, añadiendo al final de la lista  original
los nuevos elementos contenidos en el iterable pasado como argumento al método. Es  una  herramienta
útil para trabajar con listas dinámicas, ya que permite construir listas de  forma  incremental  con
varios elementos a la vez.

El método ".extend()" puede aplicarse a cualquier objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método modifica la lista original directamente, lo que significa que  no  es  necesario
asignar el resultado de su aplicación a una nueva variable, ya que no devuelve un nuevo objeto, sino
que altera el objeto existente. Este comportamiento es consistente con la naturaleza mutable de  las
listas en Python.

El método ".extend()" toma un único argumento, el  cual  debe  ser  un  iterable  que  contenga  los
elementos que se desean agregar al final de la lista. Este argumento puede  ser  de  cualquier  tipo
iterable, como una lista, una tupla, una cadena, entre otros, ya sea de forma literal  o  almacenado
en una variable.

Además, solo los elementos del iterable pasado como argumento al método ".extend()" serán  agregados
al final de la lista original y no el iterable completo como un solo elemento. Esto significa que si
se pasa una lista como argumento, cada elemento de esa lista se agregará individualmente al final de
la lista original, modificándola y obteniendo como resultado  una  lista  con  todos  los  elementos
combinados.

Por último, el método ".extend()" es una herramienta sencilla pero poderosa para  agregar  múltiples
elementos al final de listas en Python, permitiendo una manipulación eficiente y flexible  de  datos
en estructuras de lista."""

# Ejemplo_2_metodo_extend.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de números  enteros.  Esta  lista
será utilizada para demostrar el funcionamiento del método ".extend()".

A continuación, aplicamos el método ".extend()" a la variable  "lista".  Para  ello,  escribimos  el
nombre de la variable "lista" seguido del nombre del método ".extend()", y dentro de los paréntesis,
pasamos como argumento un iterable cuyos elementos deseamos agregar, en este caso, una lista literal
que contiene los números enteros 4, 5 y 6.

Por último, utilizamos la función "print()" para mostrar el contenido de  la  lista  en  la  consola
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método a la lista.

De esta forma, hemos agregado múltiples  elementos  al  final  de  la  lista  original  y  la  hemos
modificado directamente con el método ".extend()" para obtener una lista  combinada  con  todos  los
elementos de ambas listas."""

# Código:
lista = [1, 2, 3]

lista.extend([4, 5, 6])
print(f"Este es el resultado de aplicar el método a la lista: {lista}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".extend()" modifica la lista original directamente,
ya que las listas en Python son mutables. Esto significa que cualquier cambio realizado en la  lista
afecta al objeto original, lo que puede ser útil en  muchos  casos,  pero  también  puede  llevar  a
errores si no se maneja con cuidado.

Si se desea agregar solo un elemento a la lista, es recomendable utilizar el método  ".append()"  en
lugar de ".extend()", ya que ".append()" agrega un único elemento al final de la lista, mientras que
".extend()" agrega cada elemento del iterable como un nuevo elemento de la lista.

Además, es importante recordar que el método ".extend()" siempre  agrega  los  nuevos  elementos  al
final de la lista, manteniendo el orden de los elementos existentes.

Por último, el método ".extend()" es una herramienta esencial para trabajar con  listas  en  Python,
pero su uso debe ir acompañado de una comprensión clara de sus características  y  limitaciones.  De
esta forma, se podrá aprovechar al máximo sus capacidades y evitar  posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────