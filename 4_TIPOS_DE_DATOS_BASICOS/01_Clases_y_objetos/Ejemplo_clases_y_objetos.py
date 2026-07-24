# Enunciado:
"""Una clase en Python es una plantilla que define un tipo de dato predefinido o personalizado.  Los
números (int, float y complex), los booleanos (bool), las cadenas de  texto  (str),  las  secuencias
(list, tuple y range), los conjuntos (set y frozenset), los diccionarios (dict) y los bytes  (bytes,
bytearray y memoryview) son ejemplos de clases predefinidas en Python.

A partir de estas clases, podemos crear objetos predefinidos que son  instancias  de  ellas.  Python
maneja las clases de forma implícita para cada tipo de dato, lo que significa que  no  es  necesario
definirlas de forma explícita. Sin embargo, Python también  permite  definir  clases  explícitamente
mediante constructores  de  objetos.  Estos  constructores  permiten  crear  objetos  de  una  clase
predefinida.

Los objetos son instancias de clases y pueden contener  atributos  y  métodos.  Cuando  se  crea  un
objeto, se utiliza la estructura definida por su clase. Los objetos permiten trabajar  con  datos  y
funcionalidades de manera organizada y reutilizable. Para estos objetos existen métodos  específicos
aplicables, así como funciones incorporadas genéricas que pueden utilizarse con cualquier objeto."""

# Ejemplo_clases_y_objetos.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de números. En este  momento,  la
variable "lista" es un objeto o una instancia de  la  clase  (list).  Luego,  aplicamos  la  función
"type()" a la variable "lista" y encerramos la llamada a esta función dentro de la función "print()"
para mostrar el tipo de dato de la variable.  La  función  "type()"  devuelve  la  clase  a  la  que
pertenece el objeto "lista", que en este caso es la clase  (list).  Esto  nos  permite  ver  que  la
variable "lista" es un objeto o una instancia de la clase (list) y comprender cómo Python maneja las
clases de manera implícita."""

# Código:

lista = [1, 2, 3, 4]  # La variable "lista" contiene un objeto que es una instancia de la clase (list).
print(type(lista))    # La función "type()" devuelve la clase a la que pertenece el objeto.

# Nota Muy Importante:
"""Es importante destacar la diferencia entre las clases y los objetos predefinidos de Python y  las
clases y los objetos personalizados que podemos crear. Este código aborda las clases y  los  objetos
predefinidos, y en la sección de "Programación Orientada a Objetos" se explicará cómo crear nuestras
propias clases y objetos personalizados.

Por otra parte, aunque los términos "objeto" e "instancia" suelen usarse de  manera  intercambiable,
existe una distinción. Un "objeto" es una instancia específica de una clase  o  tipo,  mientras  que
"instancia" se refiere al acto de crear ese objeto  concreto.  Por  ejemplo,  cuando  definimos  una
lista, creamos un objeto de una clase específica, en este caso la clase (list), e instanciamos dicho
objeto."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────