# Enunciado:
"""El método ".insert()" en Python se utiliza para insertar un elemento en una  posición  específica
de una lista. Este método modifica la lista original directamente, al añadir el nuevo elemento en el
índice especificado y desplazar los elementos existentes una posición hacia la  derecha  para  hacer
espacio para el nuevo elemento.

El método ".insert()" puede aplicarse a cualquier objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método modifica la lista original directamente, lo que significa que  no  es  necesario
asignar el resultado de su aplicación a una nueva variable, ya que no devuelve un nuevo objeto, sino
que altera el objeto existente. Este comportamiento es consistente con la naturaleza mutable de  las
listas en Python.

El método ".insert()" toma dos argumentos: el primero es el índice en el que se  desea  insertar  el
nuevo elemento, y el segundo es el elemento que se desea insertar.

El primer argumento debe ser un número entero que representa la posición en la que se desea insertar
el nuevo elemento en la lista. Si el índice especificado es mayor o igual  que  la  longitud  de  la
lista, el elemento se agrega al final de la lista. Si el índice es negativo, el elemento se  inserta
contando desde el final de la lista, donde el índice "-1" representa el último elemento de la lista.

Además, si el índice especificado no se encuentra dentro del rango de la lista, no  se  generará  un
error, ya que Python ajustará el índice automáticamente para que el elemento se inserte al principio
o al final, según corresponda, teniendo en cuenta la distancia del índice proporcionado con respecto
al inicio o al final de la lista.

El segundo argumento puede ser de cualquier tipo de dato, ya sea de forma literal  o  almacenado  en
una variable, lo que permite una gran flexibilidad al agregar elementos a la lista.  Esto  significa
que se pueden insertar números, cadenas de texto, listas, diccionarios, tuplas u  otros  objetos  de
cualquier tipo de dato en la lista. Sin embargo, si  el  elemento  contiene  más  de  un  valor,  se
insertará como un solo elemento en la posición  especificada,  manteniendo  su  estructura  original
dentro de la lista.

Por último, el método ".insert()" es una herramienta  útil  para  agregar  elementos  en  posiciones
específicas de una lista en Python, permitiendo una manipulación precisa y flexible de los datos  en
estructuras de lista."""

# Ejemplo_3_metodo_insert.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de números  enteros.  Esta  lista
será utilizada para demostrar el funcionamiento del método ".insert()".

A continuación, aplicamos el método ".insert()" a la variable  "lista".  Para  ello,  escribimos  el
nombre de la variable "lista", seguido del nombre del método ".insert()", y dentro de los paréntesis
pasamos el índice donde deseamos insertar el nuevo elemento como primer argumento y el elemento  que
deseamos insertar como segundo argumento, separados por una coma.

En este caso, utilizamos el índice "0" como primer argumento para indicar que queremos  insertar  el
nuevo elemento al principio de la lista, y la lista literal  ["Uno",  "Dos",  "Tres"]  como  segundo
argumento, es decir, como el nuevo elemento que deseamos agregar a la lista.

Por último, utilizamos la función "print()" para mostrar el contenido de la  lista  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string", para indicar que se trata del  resultado
de aplicar el método a la lista.

De esta forma, hemos agregado un elemento en una posición específica de la lista original y la hemos
modificado directamente con el método ".insert()" para obtener una lista con el nuevo elemento en la
posición deseada."""

# Código:
lista = [1, 2, 3]

lista.insert(0, ["Uno", "Dos", "Tres"])
print(f"Este es el resultado de aplicar el método a la lista: {lista}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".insert()" modifica la lista original directamente,
ya que las listas en Python son mutables. Esto significa que cualquier cambio realizado en la  lista
afecta al objeto original, lo que puede ser útil en  muchos  casos,  pero  también  puede  llevar  a
errores si no se maneja con cuidado.

Si se desea agregar un único elemento al final de la lista, se debe utilizar el  método  ".append()"
en lugar de ".insert()", ya que ".append()" agrega un único elemento al final de la lista,  mientras
que ".insert()" permite especificar la posición exacta en la que  se  desea  insertar  el  elemento.
Además, el método ".extend()" es otra alternativa para agregar múltiples elementos contenidos en  un
iterable proporcionado como argumento al final de la lista.

Es importante recordar que el método ".insert()" desplaza los elementos existentes hacia la  derecha
para hacer espacio para el nuevo elemento, manteniendo el orden de los elementos existentes.

Esto significa que el elemento que se encuentra en la posición especificada  para  la  inserción  se
moverá a la siguiente posición sin perder su valor ni su orden relativo con  respecto  a  los  demás
elementos de la lista, y que los índices de los elementos desplazados a  la  derecha  se  actualizan
automáticamente para reflejar su nueva posición, adquiriendo el índice correspondiente  a  su  nueva
ubicación en la lista después de la inserción del nuevo elemento.

Por último, el método ".insert()" es una herramienta esencial para trabajar con  listas  en  Python,
pero su uso debe ir acompañado de una comprensión clara de sus características  y  limitaciones.  De
esta forma, se podrán aprovechar al máximo sus capacidades y evitar posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
