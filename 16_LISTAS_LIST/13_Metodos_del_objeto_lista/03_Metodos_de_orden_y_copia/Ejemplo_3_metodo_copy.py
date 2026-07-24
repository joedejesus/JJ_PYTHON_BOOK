# Enunciado:
"""El método ".copy()" en Python se utiliza para crear una copia  superficial  de  una  lista.  Este
método devuelve una nueva lista que contiene los mismos elementos que la lista original,  pero  como
un objeto independiente en memoria. Es decir, la copia es un objeto diferente del  original,  aunque
ambos objetos contengan los mismos elementos.

El método ".copy()" puede aplicarse a  cualquier  objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método no modifica la lista original y devuelve una  nueva  lista  que  representa  una
copia superficial de la lista original, que se almacena en la variable asignada al resultado  de  la
aplicación del método.

El método ".copy()" no toma argumentos adicionales, ya que su propósito es, simplemente,  crear  una
copia superficial de la lista. Esto lo convierte  en  una  herramienta  sencilla  y  eficiente  para
duplicar listas sin necesidad de realizar operaciones adicionales para lograr el mismo resultado.

Además, es importante destacar que el método ".copy()" crea una copia superficial de  la  lista,  lo
que significa que los elementos mutables de la lista original y los elementos mutables de  la  copia
son referencias al mismo objeto en memoria. Esto implica que, si los elementos de la lista  original
son objetos mutables, los cambios realizados en esos elementos de la copia también se reflejarán  en
la lista original, ya que existe una referencia compartida a los mismos objetos  mutables  en  ambas
listas.

Sin embargo, si los elementos de la lista  original  son  objetos  inmutables,  estos  no  se  verán
afectados por los cambios en la copia o en la lista original,  ya  que  los  objetos  inmutables  no
pueden modificarse después de su creación. Cada instancia de un objeto  inmutable  tiene  su  propia
referencia en memoria.

Por ello, es importante comprender la diferencia entre una copia superficial y una copia profunda al
trabajar con listas en Python.

Una copia superficial, como la que se obtiene con el método ".copy()",  crea  una  nueva  lista  que
contiene referencias a los mismos objetos mutables que la lista original. Esto significa que, si los
elementos de la lista original son objetos mutables,  los  cambios  realizados  en  estos  elementos
dentro de la copia también se reflejarán en la lista original.

Una copia profunda, por otro lado, crea una nueva lista que contiene copias  independientes  de  los
objetos mutables dentro de la lista original. Esto significa  que  los  cambios  realizados  en  los
elementos mutables de la copia no afectarán a los elementos mutables de la lista original. Una copia
profunda puede obtenerse importando y utilizando el módulo  "copy"  de  la  biblioteca  estándar  de
Python y su función "deepcopy()".

Por  último,  el  método  ".copy()"  es  una  herramienta  sencilla  pero  útil  para  crear  copias
superficiales de listas en Python, permitiendo trabajar con datos duplicados sin  alterar  la  lista
original."""

# Ejemplo_3_metodo_copy.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de números enteros. Esta lista se
utilizará para demostrar el funcionamiento del método ".copy()".

A continuación, definimos una nueva variable llamada "copia_superficial" y le asignamos el resultado
de aplicar el método ".copy()" a la variable "lista". Para ello, escribimos el nombre de la variable
seguido del método ".copy()" con los paréntesis vacíos,  ya  que  este  método  no  requiere  ningún
argumento para funcionar.

Por último, utilizamos la función "print()" para mostrar el contenido de la lista original y  de  la
copia en la consola, acompañado de un mensaje descriptivo en formato "f-string", para indicar que se
trata de la lista original y de la copia, respectivamente.

De esta forma, hemos creado una copia superficial de la lista original, sin modificarla,  y  podemos
trabajar con ella de forma independiente sin afectar a la lista original.

Adicionalmente, imprimimos las direcciones de memoria de ambas listas  para  mostrar  explícitamente
que la lista original y la copia son objetos diferentes en memoria. Esto nos permite  verificar  que
la copia es un objeto independiente en memoria, aunque los elementos sean los mismos. Para ello,  en
cada caso utilizamos la función "print()", acompañada de la función  incorporada  "id()",  que  toma
como argumento el nombre de la variable que contiene la lista original y el nombre  de  la  variable
que contiene la copia, respectivamente, e imprime el valor  de  la  dirección  de  memoria  de  cada
objeto."""

# Código:
lista = [1, 2, 3, 4, 5]

copia_superficial = lista.copy()
print(f"Lista original: {lista}")
print(f"Copia de la lista: {copia_superficial}")

print(id(lista))
print(id(copia_superficial))

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".copy()" crea una copia superficial de la lista, lo
que significa que los elementos mutables de la lista original y los elementos mutables de  la  copia
son referencias al mismo objeto en memoria. Por lo tanto, los cambios realizados  en  los  elementos
mutables de la copia también se reflejarán en los elementos mutables de la lista original.

Sin embargo, si los elementos de la lista  original  son  objetos  inmutables,  estos  no  se  verán
afectados por los cambios en la copia o en la lista original,  ya  que  los  objetos  inmutables  no
pueden ser modificados después de su creación.

Cuando decimos que los elementos de la lista original y los elementos de la copia son referencias al
mismo objeto en memoria, si estos son mutables, significa  que  dichos  elementos  en  ambas  listas
apuntan al mismo lugar en la memoria del sistema. Por ello, pueden modificarse desde  ambas  listas,
ya que ambos objetos mutables son, en realidad, el mismo objeto en memoria.

Sin embargo, esto no significa que ambas listas, "original" y "copia", sean idénticas en términos de
contenido o comportamiento, ya que cada lista puede tener  su  propia  identidad  y  características
únicas. Por ello, las direcciones de memoria de ambas listas son diferentes,  a  pesar  de  que  los
elementos de ambas listas sean los mismos y de que una sea una copia superficial de la otra.

Por último, si se desea realizar una copia profunda de una lista, es necesario  utilizar  el  módulo
"copy" y su función "deepcopy()" de la biblioteca estándar de Python.  Esto  es  especialmente  útil
cuando se trabaja con listas que contienen objetos mutables y se desea evitar cualquier  interacción
entre la lista original y su copia."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
