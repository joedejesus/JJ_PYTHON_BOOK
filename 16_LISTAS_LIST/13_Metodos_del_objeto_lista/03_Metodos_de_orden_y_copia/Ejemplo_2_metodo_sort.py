# Enunciado:
"""El método ".sort()" en Python se utiliza para ordenar los elementos de  una  lista.  Este  método
organiza los elementos en orden ascendente de forma predeterminada, pero también permite especificar
un criterio de orden personalizado mediante los parámetros opcionales "reverse" y "key".

El método ".sort()" puede aplicarse a  cualquier  objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método modifica la lista original directamente, lo que significa que  no  es  necesario
asignar el resultado de su aplicación a una nueva variable, ya que no devuelve un nuevo objeto, sino
que modifica el objeto existente. Este comportamiento es consistente con la  naturaleza  mutable  de
las listas en Python.

El método ".sort()" no toma argumentos obligatorios, pero sí puede tomar dos parámetros  opcionales:
"reverse" y "key".

El parámetro "reverse" se utiliza para ordenar los elementos en orden  descendente.  Este  parámetro
debe tomar un valor booleano, como "True" para ordenar en orden descendente o "False"  para  ordenar
en   orden   ascendente.   La   sintaxis   para   utilizar   este   parámetro   es   la   siguiente:
"lista.sort(reverse=True)" para ordenar en  orden  descendente  o  "lista.sort(reverse=False)"  para
ordenar en orden ascendente.

Para ordenar en orden ascendente no es necesario  utilizar  el  parámetro  "reverse"  en  el  método
".sort()", ya que el ordenamiento por defecto es ascendente  y  se  puede  simplemente  utilizar  el
método sin parámetros, es decir, "lista.sort()" para ordenar la lista en orden ascendente.

El parámetro "key" se utiliza para especificar una función que se aplicará a  cada  elemento  de  la
lista antes de realizar la comparación, con el fin de personalizar el ordenamiento.  Este  parámetro
debe tomar un valor de tipo función, ya sea una función  incorporada  de  Python,  como  "len"  para
ordenar por longitud, o una función  personalizada  definida  por  el  usuario  para  ordenar  según
criterios   específicos.   La   sintaxis   para   utilizar   este   parámetro   es   la   siguiente:
"lista.sort(key=funcion)" donde "funcion" es la función que se aplicará a cada elemento de la  lista
antes de realizar la comparación para el ordenamiento.

Además, un valor de tipo función es una función que puede pasarse  como  argumento  a  un  parámetro
dentro de un método. En el caso del parámetro "key", este recibe como argumento una función, en este
caso "len", que se aplicará a cada elemento de la lista antes de realizar  la  comparación  para  el
ordenamiento.

Por último, el método ".sort()" es una herramienta útil para ordenar listas en  Python,  permitiendo
una manipulación precisa y flexible de datos en estructuras de lista."""

# Ejemplo_2_metodo_sort.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista  de  sublistas  sin  ordenar  por
longitud. Esta lista será utilizada para demostrar el funcionamiento del método ".sort()".

A continuación, aplicamos el método ".sort()" a la variable "lista". Para ello, escribimos el nombre
de la variable "lista" seguido del nombre del método ".sort()", y dentro de los paréntesis,  pasamos
los parámetros opcionales "reverse=True" y "key=len" para ordenar  la  lista  en  orden  descendente
según la longitud de las sublistas.

El parámetro "reverse" toma el valor "True" para indicar que queremos ordenar en orden  descendente,
mientras que el parámetro "key" toma el valor de la función incorporada  "len()"  para  ordenar  las
sublistas según su longitud. El parámetro "key" se utiliza  para  especificar  una  función  que  se
aplicará a cada elemento de la lista antes de realizar la comparación para el ordenamiento.

Por último, utilizamos la función "print()" para mostrar el contenido de  la  lista  en  la  consola
acompañado de un mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado
de aplicar el método a la lista.

De esta forma, hemos modificado la lista, ordenando los elementos en orden descendente  y  según  la
longitud de las sublistas dentro de la lista utilizando  el  método  ".sort()"  con  los  parámetros
"reverse" y "key"."""

# Código:
lista = [[], [1, 2], [1, 2, 3], [1], [1, 2, 3, 4]]

lista.sort(reverse=True, key=len)
print(f"Este es el resultado de aplicar el método a la lista: {lista}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".sort()" modifica la lista  original  directamente,
ya que las listas en Python son mutables. Esto significa que cualquier cambio realizado en la  lista
afecta al objeto original, lo que puede ser útil en  muchos  casos,  pero  también  puede  llevar  a
errores si no se maneja con cuidado.

Si se desea obtener una nueva lista ordenada sin modificar la lista original, se  debe  utilizar  la
función incorporada "sorted()" en lugar del método ".sort()", ya que la función "sorted()"  devuelve
una nueva lista con los elementos ordenados, dejando intacta la lista original.

Además, es importante recordar que el método ".sort()"  suele  ser  más  eficiente  que  la  función
"sorted()" cuando no se necesita conservar la lista original, ya que evita la creación de  un  nuevo
objeto y realiza la ordenación directamente en la lista existente.

Normalmente, los métodos reciben valores como argumentos que se pasan a un método para  proporcionar
información adicional o instrucciones sobre cómo debe ejecutarse. En el caso del  método  ".sort()",
"key" y "reverse" son parámetros que reciben argumentos específicos para determinar el orden de  los
elementos. Es importante entender cómo funcionan estos parámetros para evitar confusiones y  conocer
la diferencia entre argumentos y parámetros.

Por último, el método ".sort()" es una herramienta esencial para trabajar con listas en Python, pero
su uso debería estar acompañado de una comprensión clara de sus características y  limitaciones.  De
esta forma, se podrá aprovechar al máximo sus capacidades y evitar  posibles  inconvenientes  en  su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
