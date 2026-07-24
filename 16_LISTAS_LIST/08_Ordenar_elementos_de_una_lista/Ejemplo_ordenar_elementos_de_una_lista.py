# Enunciado:
"""Para ordenar los elementos de una lista en Python, se utilizan el método ".sort()" y  la  función
"sorted()". Estos métodos y funciones permiten  organizar  los  elementos  de  una  lista  en  orden
ascendente o descendente, así como realizar un ordenamiento personalizado.

El método ".sort()" modifica la lista original y no  devuelve  una  nueva  lista,  mientras  que  la
función "sorted()" devuelve una nueva lista ordenada sin modificar  la  lista  original.  Ambos  son
útiles dependiendo de si se desea conservar la lista original o no.

La función "sorted()" toma como argumento la lista que se desea ordenar y devuelve una  nueva  lista
ordenada. Además, puede aceptar parámetros opcionales como "reverse" y "key".

El parámetro "reverse" se utiliza para ordenar los elementos en orden  descendente.  Este  parámetro
debe tomar un valor booleano como "True" para ordenar en orden descendente o "False" para ordenar en
orden ascendente.  La  sintaxis  para  utilizar  este  parámetro  es  la  siguiente:  "sorted(lista,
reverse=True)" para ordenar en orden descendente o "sorted(lista, reverse=False)"  para  ordenar  en
orden ascendente.

Además, para ordenar en orden ascendente no es necesario  utilizar  el  parámetro  "reverse"  en  la
función "sorted()", ya que el ordenamiento por defecto es ascendente y se puede simplemente llamar a
la función "sorted(lista)" para obtener una nueva lista ordenada en orden ascendente.

El parámetro "key" se utiliza para especificar una función que se aplicará a  cada  elemento  de  la
lista antes de realizar la comparación para el ordenamiento de forma personalizada.  Este  parámetro
debe tomar un valor de tipo función, ya sea una función incorporada de  Python,  como  "len()"  para
ordenar por longitud, o una función  personalizada  definida  por  el  usuario  para  ordenar  según
criterios específicos. La sintaxis para utilizar este  parámetro  es  la  siguiente:  "sorted(lista,
key=funcion)" donde "funcion" es la función que se aplicará a cada elemento de  la  lista  antes  de
realizar la comparación para el ordenamiento.

Un valor de tipo función es una función que se puede pasar como argumento a un parámetro  dentro  de
otra función. En el caso del parámetro "key", recibe un valor que es una función que se  aplicará  a
cada elemento de la lista antes de realizar la comparación para el ordenamiento.

Es importante tener en cuenta que, al ordenar listas, los elementos deben ser comparables entre  sí.
Por ejemplo, no se puede ordenar una lista que contenga tanto cadenas de texto como números, ya  que
Python no puede comparar estos tipos de datos directamente.

Por último, es fundamental comprender que el  ordenamiento  de  listas  en  Python  se  basa  en  la
comparación de elementos, y que el resultado del  ordenamiento  dependerá  de  los  valores  de  los
elementos y de los parámetros utilizados en los métodos y funciones de ordenamiento. Es por ello que
es importante entender cómo funcionan estos métodos y funciones  para  manipular  listas  de  manera
efectiva."""

# Ejemplo_ordenar_elementos_de_una_lista.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de elementos [60, 10, 40, 20, 50,
30], la cual será utilizada para ordenar sus elementos utilizando la función "sorted()".

A continuación, definimos una variable llamada "lista_ordenada"  y  le  asignamos  el  resultado  de
llamar a la función "sorted()" con la variable "lista" como argumento y el parámetro  "reverse=True"
para indicar que deseamos ordenar los elementos en  orden  descendente.  Para  ello,  utilizamos  la
función "sorted()" con el argumento lista y el parámetro "reverse=True" para ordenar  los  elementos
en orden descendente de esta forma "sorted(lista, reverse=True)".

Utilizamos la función "print()" para mostrar la lista ordenada  en  la  consola,  acompañada  de  un
mensaje descriptivo en formato "f-string" para indicar el criterio utilizado para el ordenamiento.

Además, ordenamos los elementos de una lista de cadenas de texto por longitud utilizando la  función
"sorted()" con el parámetro "key=len". Para ello, definimos una  variable  llamada  "cadenas"  y  le
asignamos una lista de cadenas de texto. Luego, definimos una variable llamada "cadenas_ordenadas" y
le asignamos el resultado de llamar a la función "sorted()" con la variable "cadenas" como argumento
y el parámetro "key=len" para indicar que deseamos ordenar los elementos  por  la  longitud  de  las
cadenas mediante el uso, como valor del parámetro "key", de  la  función  incorporada  "len()",  que
devuelve la longitud de cada cadena, de esta forma: "sorted(cadenas, key=len)".

Por último, utilizamos la función "print()" para mostrar la  lista  ordenada  por  longitud  de  las
cadenas en la consola, acompañada de un mensaje descriptivo en formato "f-string"  para  indicar  el
criterio utilizado para el ordenamiento."""

# Código:
lista = [60, 10, 40, 20, 50, 30]
lista_ordenada = sorted(lista, reverse=True)
print(f"Lista ordenada en orden descendente: {lista_ordenada}")

cadenas = ["manzana", "kiwi", "sandía", "uva"]
cadenas_ordenadas = sorted(cadenas, key=len)
print(f"Lista ordenada por longitud de las cadenas: {cadenas_ordenadas}")

# Nota Muy Importante:
"""En este caso, solo utilizamos la función "sorted()" para ordenar los elementos  de  la  lista  en
orden descendente, pero es posible ordenar listas utilizando el método ".sort()". Este método no  se
ha incluido en este ejemplo ya que se explica con detalle en la sección  correspondiente  a  métodos
del objeto lista.

Es importante tener en cuenta que, al ordenar listas, los cambios realizados con el método ".sort()"
se aplican directamente sobre la lista original. Esto puede afectar otras partes  del  programa  que
dependan de la lista, por lo que es fundamental asegurarse de que los cambios sean  intencionales  y
no generen efectos secundarios no deseados.

Sin embargo, al utilizar la función "sorted()", se crea una nueva lista ordenada  sin  modificar  la
lista original, lo que permite conservarla sin cambios. Esto es especialmente útil cuando  se  desea
mantener la integridad de los datos originales o cuando se necesita realizar múltiples ordenamientos
sin afectar la lista original.

En el caso de las listas, si se utiliza la función "sorted()", es necesario almacenar  el  resultado
de la ordenación en una nueva variable, ya que la función devuelve  una  nueva  lista  ordenada  sin
modificar la lista original.

Por último, estas características hacen que las listas en Python sean  una  herramienta  poderosa  y
flexible para trabajar  con  colecciones  de  datos,  ya  que  permiten  tanto  el  acceso  como  el
ordenamiento de sus elementos de manera eficiente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
