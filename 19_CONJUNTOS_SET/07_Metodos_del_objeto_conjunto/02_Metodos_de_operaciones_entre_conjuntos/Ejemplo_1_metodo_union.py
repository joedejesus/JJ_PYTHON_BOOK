# Enunciado:
"""El método ".union()" en Python se utiliza para obtener un nuevo conjunto que contiene  todos  los
elementos presentes en el conjunto original y en  los  conjuntos  o  iterables  proporcionados  como
argumentos. Los conjuntos no mantienen un orden específico de sus elementos, por lo que el resultado
de la unión será un nuevo conjunto con los elementos combinados, sin  una  posición  determinada  ni
predecible.

El método ".union()" puede aplicarse a cualquier objeto de tipo  (set)  en  Python,  como  conjuntos
literales, variables que contienen conjuntos o incluso resultados de otras operaciones  que  generan
conjuntos. Este método no modifica el conjunto original y devuelve un nuevo  conjunto  que  contiene
todos los elementos presentes en el conjunto original y en los conjuntos o iterables  proporcionados
como argumentos, el cual se almacena en la variable asignada a la aplicación del método.

El método ".union()" toma uno o varios argumentos: los conjuntos  o  iterables  cuyos  elementos  se
desean combinar con el conjunto original. Si no se proporcionan argumentos, el método  devuelve  una
copia del conjunto original, ya que no hay elementos adicionales que unir.

Estos argumentos deben ser objetos iterables, lo que significa que  pueden  ser  cualquier  tipo  de
objeto que se pueda recorrer, como listas, tuplas, conjuntos,  diccionarios  o  incluso  cadenas  de
texto, siempre y cuando sus elementos sean inmutables. En el caso de  los  diccionarios,  el  método
toma sus claves como referencia, no sus valores; y, en el caso de las cadenas  de  texto,  toma  sus
caracteres como elementos individuales para calcular la unión.

Sin embargo, estos argumentos no pueden ser valores individuales que  no  sean  iterables,  como  un
número entero o decimal, ya que el método ".union()" espera recibir uno o varios iterables.

Además, si algún elemento aparece repetido en cualquiera de los conjuntos o  iterables  involucrados
en la operación de unión, este no se duplicará en el  resultado  final,  ya  que  los  conjuntos  no
permiten elementos duplicados. Esto significa que el resultado de la  unión  será  un  conjunto  con
elementos únicos.

Por último, el método ".union()" es una  herramienta  eficiente  para  combinar  conjuntos,  ya  que
permite una manipulación directa y flexible de datos en estructuras de tipo  (set)  sin  alterar  el
conjunto original."""

# Ejemplo_1_metodo_union.py

# Explicación:
"""Definimos una variable llamada "conjunto" y le asignamos un conjunto  de  números  enteros.  Este
conjunto se utilizará para demostrar el funcionamiento del método ".union()".

A continuación, definimos una nueva variable llamada "nuevo_conjunto" y le asignamos el resultado de
aplicar el método ".union()" a la variable  "conjunto".  Para  ello,  escribimos  el  nombre  de  la
variable "conjunto", seguido del nombre del método ".union()" y, dentro de los  paréntesis,  pasamos
como argumentos los iterables cuyos elementos deseamos combinar con el conjunto original,  separados
por comas; en este caso, un conjunto literal de  números  enteros,  una  lista  literal  de  números
enteros y una tupla literal de números enteros.

Por último, utilizamos la función "print()" para mostrar el contenido del nuevo conjunto  resultante
en la consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar que se  trata
del resultado de aplicar el método al conjunto original.

De esta forma, obtenemos un nuevo conjunto que contiene todos los elementos presentes en el conjunto
original y en los iterables proporcionados como argumentos, sin modificar el conjunto original."""

# Código:
conjunto = {1, 2, 3, 4, 5}

nuevo_conjunto = conjunto.union({6, 7}, [8, 9], (10, 11))
print(f"Este es el resultado de aplicar el método al conjunto original: {nuevo_conjunto}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".union()" no modifica el  conjunto  original,  sino
que devuelve un nuevo conjunto con todos los elementos presentes en el conjunto original  y  en  los
conjuntos o iterables proporcionados como  argumentos.  Esto  significa  que  el  conjunto  original
permanece sin cambios, lo que puede ser útil en muchos casos, pero también puede provocar errores si
no se maneja con cuidado.

Además, es importante aclarar que este  método  toma  uno  o  varios  argumentos:  los  conjuntos  o
iterables cuyos elementos se desean combinar con el conjunto original, y devuelve un nuevo  conjunto
con todos los  elementos  presentes  en  el  conjunto  original  y  en  los  conjuntos  o  iterables
proporcionados como argumentos.

La diferencia entre el método ".union()" y el método ".update()" radica en que el  primero  devuelve
un nuevo conjunto con la unión, sin alterar el conjunto original, mientras que el  segundo  modifica
el conjunto original directamente.

En este caso, hablamos de combinar y no de añadir, porque el método ".union()" no añade elementos al
conjunto original, sino que devuelve un nuevo conjunto que contiene la unión de todos los  elementos
proporcionados, sin afectar al conjunto original.

El método ".union()" es una opción eficiente si se desea combinar conjuntos sin alterar el  conjunto
original. Además, es importante recordar que el método ".union()" opera sobre elementos  únicos,  ya
que los conjuntos no admiten elementos duplicados.

Por último, el método ".union()" es una herramienta esencial para trabajar con conjuntos en  Python,
pero su uso debe ir acompañado de una comprensión clara de sus características y limitaciones.  Esto
permitirá  aprovechar  al  máximo  sus  capacidades  y  evitar   posibles   inconvenientes   en   su
implementación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────