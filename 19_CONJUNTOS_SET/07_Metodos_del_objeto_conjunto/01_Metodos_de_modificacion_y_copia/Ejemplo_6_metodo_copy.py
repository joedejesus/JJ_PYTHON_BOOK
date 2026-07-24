# Enunciado:
"""El método ".copy()" en Python se utiliza para crear una copia superficial de un  conjunto  (set).
Este método devuelve un nuevo conjunto que contiene los mismos elementos que el  conjunto  original,
pero como un objeto independiente en memoria.  Es  decir,  la  copia  es  un  objeto  diferente  del
original, aunque ambos objetos contengan los mismos elementos.

El método ".copy()" puede aplicarse a cualquier objeto de  tipo  (set)  en  Python,  como  conjuntos
literales, variables que contienen conjuntos o incluso resultados de otras operaciones  que  generan
conjuntos. Este método no modifica el conjunto original y devuelve un nuevo conjunto que  representa
una copia superficial de este, la cual se almacena en  la  variable  asignada  al  resultado  de  la
aplicación del método.

El método ".copy()" no toma argumentos adicionales, ya que su propósito  es  simplemente  crear  una
copia superficial del conjunto. Esto lo convierte en  una  herramienta  sencilla  y  eficiente  para
duplicar conjuntos  sin  necesidad  de  realizar  operaciones  adicionales  para  obtener  el  mismo
resultado.

Por último, el  método  ".copy()"  es  una  herramienta  sencilla,  pero  útil,  para  crear  copias
superficiales de conjuntos en Python, lo que permite trabajar con datos duplicados  sin  alterar  el
conjunto original."""

# Ejemplo_6_metodo_copy.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".copy()".

A continuación, definimos una nueva variable llamada "copia_superficial" y le asignamos el resultado
de aplicar el método ".copy()" a la variable "conjunto". Para  ello,  escribimos  el  nombre  de  la
variable seguido del nombre del método ".copy()" con los paréntesis vacíos, ya que  este  método  no
requiere ningún argumento para funcionar.

Por último, utilizamos la función "print()" para mostrar el contenido del conjunto original y de  la
copia en la consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que  se
trata del conjunto original y de la copia, respectivamente.

De esta forma, hemos creado una copia superficial del conjunto original sin  modificarlo  y  podemos
trabajar con ella de forma independiente sin afectar al conjunto original.

Adicionalmente, imprimimos las direcciones de memoria de ambos conjuntos para mostrar explícitamente
que el conjunto original y la copia son objetos diferentes en memoria. Esto  nos  permite  verificar
que la copia es un objeto independiente en memoria, aunque los elementos sean los mismos.

Para ello, en cada caso utilizamos la función "print()" acompañada de la función incorporada "id()",
que toma como argumento el nombre de la variable que contiene el conjunto original y el nombre de la
variable que contiene la copia, respectivamente, e imprime el valor de la dirección  de  memoria  de
cada objeto."""

# Código:
conjunto = {1, 2, 3, 4, 5}

copia_superficial = conjunto.copy()
print(f"Conjunto original: {conjunto}")
print(f"Copia del conjunto: {copia_superficial}")

print(id(conjunto))
print(id(copia_superficial))

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".copy()" crea una copia superficial de un conjunto,
es decir, un nuevo conjunto con los mismos elementos que el original, pero independiente en memoria.
Por eso, las direcciones de memoria de ambos conjuntos son diferentes, a pesar de que los  elementos
sean los mismos.

Además, es  importante  destacar  que  los  conjuntos  en  Python  solo  pueden  contener  elementos
inmutables, como números, cadenas o tuplas inmutables. Por lo tanto, no pueden  contener  listas  ni
diccionarios, ya que estos pueden modificarse y no se admiten como elementos de un conjunto.

Debido a esta restricción, normalmente no existen problemas de referencias  compartidas  ni  efectos
colaterales por modificaciones, como ocurre en otros tipos  de  colecciones  que  admiten  elementos
mutables, como listas o diccionarios. Sin embargo, si se agregaran objetos personalizados que puedan
modificarse (caso poco común y no  recomendado),  podrían  presentarse  efectos  colaterales  si  se
modificara alguno de esos objetos desde cualquiera de los conjuntos.

Por último, en este caso, crear una copia superficial  del  conjunto  original  es  suficiente  para
trabajar con los mismos elementos sin afectar al conjunto original. Si se trabajara con otro tipo de
colección que admitiera elementos  mutables,  como  listas  o  diccionarios,  podría  ser  necesario
considerar una copia profunda, "deep copy", para evitar cualquier interacción no  deseada  entre  la
colección original y su copia."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────