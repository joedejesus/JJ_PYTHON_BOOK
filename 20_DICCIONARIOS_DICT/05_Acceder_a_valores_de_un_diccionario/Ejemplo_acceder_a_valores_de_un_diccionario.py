# Enunciado:
"""Para acceder a los valores de un diccionario en Python, se  utiliza  la  clave  asociada  a  cada
valor. Una clave es un identificador único dentro del diccionario que permite  acceder  directamente
al valor correspondiente.  A  diferencia  de  las  listas,  los  diccionarios  no  utilizan  índices
numéricos, sino claves inmutables, como cadenas,  números  o  tuplas.  Este  sistema  de  acceso  es
fundamental para trabajar con diccionarios en Python, ya  que  permite  obtener  valores  de  manera
directa mediante su clave asociada.

Los diccionarios en Python son colecciones de pares clave-valor, y cada valor está  asociado  a  una
clave única. Los diccionarios son mutables, lo que  significa  que  podemos  modificar  sus  valores
directamente utilizando sus claves. Además, los diccionarios son iterables, lo que permite  recorrer
cada par clave-valor mediante sus claves u otros métodos de iteración.

Esto es útil para manipular o inspeccionar partes específicas de un diccionario, ya que  cada  clave
permite acceder a un valor concreto sin depender de una posición.

Por último, es importante destacar que  Python  ofrece  métodos  adicionales,  como  ".get()",  para
acceder a valores de forma segura y evitar errores cuando una clave  no  existe.  Esta  flexibilidad
hace que el manejo de diccionarios en Python sea muy potente y versátil."""

# Ejemplo_acceder_a_valores_de_un_diccionario.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con varios  elementos,
{"a": 10, "b": 20, "c": 30, "d": 40, "e": 50, "f": 60}, el cual se  utilizará  para  acceder  a  sus
valores mediante claves.

A continuación, definimos una variable llamada "valor" y le asignamos el  resultado  de  aplicar  el
operador de indexación "[]" a la variable "diccionario" con la clave "c". Para ello,  utilizamos  el
operador de indexación con la clave "c"  en  su  interior,  "[\"c\"]",  precedido  por  la  variable
"diccionario". De esta forma, obtenemos el valor asociado a la clave "c", que es "30".

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica que se trata del valor asociado a la clave "c".

Por último, accedemos a otros dos valores del diccionario de forma  directa  utilizando  la  función
"print()" en formato "f-string" y el operador de indexación "[]" con  las  claves  correspondientes.
Para ello, utilizamos el operador de  indexación  con  la  clave  "e"  en  su  interior,  "[\"e\"]",
precedido por la variable "diccionario" para acceder al valor "50", y  el  método  ".get()"  con  la
clave "d" para acceder al valor "40" de forma segura.

En ambos casos, las operaciones se realizan dentro de las llaves {} de las expresiones de la  cadena
"f-string" para mostrar  el  resultado  sin  necesidad  de  asignarlo  a  una  variable  intermedia,
acompañadas de un mensaje descriptivo que indica que se trata del valor asociado a cada clave."""

# Código:
diccionario = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50, "f": 60}

valor = diccionario["c"]
print(f"Este es el valor asociado a la clave 'c': {valor}")

print(f"Este es el valor asociado a la clave 'e': {diccionario['e']}")
print(f"Este es el valor asociado a la clave 'd' utilizando .get(): {diccionario.get('d')}")

# Nota Importante:
"""Es fundamental tener en cuenta que los diccionarios no utilizan índices  numéricos,  sino  claves
únicas para acceder a sus valores. Esto significa que no podemos acceder a los valores por posición,
sino utilizando directamente la clave asociada a cada valor.

Además, Python también permite utilizar el método ".get()" para  acceder  a  los  valores  de  forma
segura. Este método devuelve "None" si la clave no existe, evitando que se produzca un error de tipo
"KeyError". Esto es especialmente útil cuando se necesita acceder a valores sin estar  completamente
seguro de que la clave esté presente en el diccionario.

Aunque los diccionarios en Python son objetos mutables, en este ejemplo solo  estamos  accediendo  a
los valores sin modificarlos, lo que proporciona una forma segura de trabajar con ellos sin  alterar
su contenido. Sin embargo, es importante tener cuidado al modificar valores  utilizando  claves,  ya
que esto puede afectar el comportamiento de otras partes del programa que dependan de esos valores.

Por último, intentar acceder a una clave inexistente  utilizando  el  operador  de  indexación  "[]"
generará un error de tipo "KeyError", por lo que es recomendable utilizar el método ".get()"  cuando
se desee evitar este tipo de errores. Estas características hacen que el manejo de claves en  Python
sea una herramienta muy útil para trabajar con diccionarios de manera eficiente y segura."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────