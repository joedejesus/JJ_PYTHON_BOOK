# Enunciado:
"""El método ".count()" en Python se utiliza para contar el número de veces que un elemento  aparece
en una lista. Este método devuelve un número entero que representa la cantidad  de  ocurrencias  del
elemento especificado en la lista.

El método ".count()" recorre la lista completa y devuelve el número total de veces que  el  elemento
aparece en ella. Si  el  elemento  no  se  encuentra  en  la  lista,  el  método  devuelve  0.  Este
comportamiento es útil para verificar la frecuencia de un elemento en una  lista  sin  necesidad  de
recorrerla manualmente.

El método ".count()" puede aplicarse a cualquier  objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método no modifica la lista original y devuelve un valor que representa la cantidad  de
ocurrencias del elemento buscado, el cual se almacena en la variable asignada  al  resultado  de  la
aplicación del método.

El método ".count()" toma un único argumento obligatorio: el elemento  que  se  desea  contar.  Este
argumento puede ser un valor literal, una variable o incluso el resultado de una función. Este valor
debe coincidir exactamente con el tipo de dato presente en la lista, respetando  la  sintaxis  y  el
formato, ya que, de lo contrario, el método no contará ninguna coincidencia y devolverá 0.

Por último, el método ".count()" es una  herramienta  útil  para  determinar  la  frecuencia  de  un
elemento dentro de una lista en Python, y su simplicidad lo hace ideal para realizar esta  tarea  de
manera eficiente."""

# Ejemplo_2_metodo_count.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista que  contiene  varios  elementos.
Esta lista se utilizará para demostrar el funcionamiento del método ".count()".

A continuación, definimos una nueva variable llamada "frecuencia" y le  asignamos  el  resultado  de
aplicar el método ".count()" a la variable "lista" con un argumento: el elemento "texto". Para ello,
escribimos el nombre de la variable, seguido del nombre del  método  ".count()",  y  dentro  de  los
paréntesis, pasamos el elemento como argumento.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar la cantidad  de  veces  que  el  elemento
"texto" aparece en la lista.

De esta forma, hemos contado la frecuencia  del  elemento  "texto"  en  la  lista  sin  modificarla,
obteniendo un número que indica la cantidad de ocurrencias encontradas. En este caso,  el  resultado
será 2, ya que el elemento "texto" aparece dos veces en la lista."""

# Código:
lista = [1, 2, 3, "texto", 5, 6, "texto", 8, 9]

frecuencia = lista.count("texto")
print(f"El elemento 'texto' aparece {frecuencia} veces en la lista.")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".count()" es sensible a mayúsculas y minúsculas  en
el caso de las cadenas dentro de la lista, por lo que "Texto" y "texto"  se  consideran  diferentes.
Además, el elemento que se busca debe coincidir exactamente con el  tipo  de  dato  presente  en  la
lista, respetando la sintaxis y el formato, ya que, de lo contrario, el método  no  contará  ninguna
coincidencia y devolverá 0.

Este método no modifica la lista original  y  devuelve  un  valor  que  representa  la  cantidad  de
ocurrencias del elemento buscado, el cual se almacena en la variable asignada  al  resultado  de  la
aplicación del método. Esto significa que siempre genera un  número  entero  como  resultado  de  su
aplicación, dejando intacta la lista original.

Si el elemento no se encuentra en la lista, el método devuelve 0. Por  lo  tanto,  no  es  necesario
manejar excepciones al utilizar este método, ya que  no  genera  errores  si  el  elemento  no  está
presente en la lista.

Por último, es importante destacar que este método cuenta todas las apariciones de un elemento en la
lista, por lo que es ideal para determinar la  frecuencia  de  un  elemento  de  manera  sencilla  y
eficiente. Sin embargo, si se desea realizar operaciones más complejas, como  contar  elementos  que
cumplan una condición específica, se deben considerar otros métodos  o  estructuras  de  datos  para
lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
