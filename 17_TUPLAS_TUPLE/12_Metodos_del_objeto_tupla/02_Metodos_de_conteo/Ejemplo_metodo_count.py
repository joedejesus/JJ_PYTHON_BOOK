# Enunciado:
"""El método ".count()" en Python se utiliza para contar cuántas veces aparece un  elemento  en  una
tupla. Este método devuelve un número entero que representa la cantidad de ocurrencias del  elemento
especificado en ella.

El método ".count()" evalúa toda la tupla y devuelve  el  número  total  de  veces  que  aparece  el
elemento en ella. Si el  elemento  no  se  encuentra  en  la  tupla,  el  método  devuelve  0.  Este
comportamiento es útil para verificar la frecuencia de un elemento en una  tupla  sin  necesidad  de
recorrerla manualmente.

El método ".count()" puede aplicarse a cualquier  objeto  de  tipo  tupla  en  Python,  como  tuplas
literales, variables que contienen tuplas o incluso resultados  de  otras  operaciones  que  generan
tuplas. Este método no modifica la tupla original, ya que las tuplas son inmutables, y  devuelve  un
valor que representa la cantidad de ocurrencias del elemento buscado  el  cual  se  almacena  en  la
variable asignada al resultado de la aplicación del método.

El método ".count()" toma un único argumento obligatorio: el elemento  que  se  desea  contar.  Este
argumento puede ser un valor literal, una variable o incluso el resultado de una función. Este valor
debe coincidir exactamente con el tipo de dato presente en la tupla, respetando  la  sintaxis  y  el
formato, ya que, de lo contrario, el método no contará ninguna coincidencia y devolverá 0.

Por último, el método ".count()" es una  herramienta  útil  para  determinar  la  frecuencia  de  un
elemento dentro de una tupla en Python, y su simplicidad lo hace ideal para realizar esta  tarea  de
manera eficiente."""

# Ejemplo_metodo_count.py

# Explicación:
"""Definimos una variable llamada "tupla" y le asignamos una tupla que  contiene  varios  elementos.
Esta tupla se utilizará para demostrar el funcionamiento del método ".count()".

A continuación, definimos una nueva variable llamada "frecuencia" y le  asignamos  el  resultado  de
aplicar el método ".count()" a la variable "tupla" con un argumento: el elemento "texto". Para ello,
escribimos el nombre de la variable seguido del  método  ".count()",  y  dentro  de  los  paréntesis
pasamos el elemento como argumento.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" que indica la cantidad de veces que el elemento "texto"
aparece en la tupla.

De esta forma, determinamos la frecuencia del elemento "texto" en la tupla y obtenemos un número que
indica la cantidad de ocurrencias encontradas. En este caso, el resultado será 2, ya que el elemento
"texto" aparece dos veces en la tupla."""

# Código:
tupla = (1, 2, 3, "texto", 5, 6, "texto", 8, 9)

frecuencia = tupla.count("texto")
print(f"El elemento 'texto' aparece {frecuencia} veces en la tupla.")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".count()" es sensible a mayúsculas y minúsculas  en
el caso de las cadenas dentro de la tupla, por lo que "Texto" y "texto"  se  consideran  diferentes.
Además, el elemento que se busca debe coincidir exactamente con el  tipo  de  dato  presente  en  la
tupla, respetando la sintaxis y el formato, ya que, de lo contrario, el método  no  contará  ninguna
coincidencia y devolverá 0.

Este método no modifica la tupla original, ya que las tuplas son inmutables, y devuelve un valor que
representa la cantidad de ocurrencias del elemento buscado. Dicho valor se almacena en  la  variable
asignada al resultado de la aplicación del método. Esto  significa  que  siempre  genera  un  número
entero como resultado de su aplicación, dejando intacta la tupla original.

Además, si el elemento no se encuentra en la tupla, el método  devuelve  0.  Por  lo  tanto,  no  es
necesario manejar excepciones al utilizar este método, ya que no genera errores si  el  elemento  no
está presente en la tupla.

Por último, es importante destacar que este método cuenta todas las apariciones de un elemento en la
tupla, por lo que es ideal para determinar la  frecuencia  de  un  elemento  de  manera  sencilla  y
eficiente. Sin embargo, si se desea realizar operaciones más complejas, como  contar  elementos  que
cumplan una condición específica, se deben considerar otros métodos  o  estructuras  de  datos  para
lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
