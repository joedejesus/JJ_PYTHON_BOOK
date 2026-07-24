# Enunciado:
"""La función "len()" es una función incorporada de  Python  que  permite  conocer  la  cantidad  de
caracteres que contiene una cadena de texto, es decir, su  longitud.  Esta  función  es  ampliamente
utilizada en la programación debido a su simplicidad y eficiencia.

Esta función toma un objeto como argumento y devuelve un número entero que representa la cantidad de
elementos que contiene dicho objeto. En el caso de las cadenas de texto, la función  "len()"  cuenta
cada carácter, incluidos espacios y caracteres especiales, para proporcionar una medida  precisa  de
la longitud del texto.

La función "len()" permite realizar operaciones como contar la cantidad de caracteres en una  frase,
validar la longitud de entradas de usuario en formularios o incluso analizar  datos  en  estructuras
más complejas.

Además, su implementación en Python está optimizada para ofrecer un rendimiento rápido y  confiable,
independientemente del tamaño del texto o la estructura iterable que  se  esté  evaluando.  Esto  la
convierte en una herramienta fundamental para tareas que involucran la manipulación  y  análisis  de
datos  textuales,  así  como  para  el  manejo  de  estructuras  iterables  como  listas,  tuplas  y
diccionarios.

En resumen, su versatilidad y facilidad de uso hacen que sea una de las funciones más utilizadas por
los programadores, permitiendo resolver problemas comunes de manera eficiente y con  un  código  más
legible."""

# Ejemplo_medir_la_longitud_de_un_texto.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos la cadena de texto  "Elefante  azul".  Esta
cadena será utilizada para medir su longitud utilizando la función "len()".

A continuación, definimos una variable llamada "longitud" y le asignamos el resultado de llamar a la
función "len()" con la variable "texto" como argumento.  Para  ello,  escribimos  el  nombre  de  la
función seguido de un paréntesis dentro del cual colocamos el nombre de  la  variable  "texto"  como
argumento.

La función "len()" toma como argumento la cadena de texto y devuelve un número entero que representa
la cantidad de caracteres que contiene, el cual se almacena en la variable "longitud".

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" que indica que se trata de la longitud  del  texto.  De
esta forma, obtenemos la longitud del texto "Elefante azul", que es 13, ya que  la  función  "len()"
cuenta cada carácter, incluido el espacio entre las palabras.

Además, utilizamos la función "len()" directamente con una cadena de texto  literal  para  medir  su
longitud. Para ello, utilizamos la función "print()" y dentro de esta colocamos la  función  "len()"
que toma como argumento la cadena de texto literal "Hola, ¿cómo estás?", lo que nos permite  obtener
la longitud de esta cadena de texto directamente sin necesidad de almacenarla en una variable.

En este caso, también podríamos pasar como argumento a la función "len()" una variable que  almacene
una cadena de texto, lo que nos permitiría medir la longitud de cualquier  texto  almacenado  en  la
variable de forma rápida y directa."""

# Código:
texto = "Elefante azul"
longitud = len(texto)
print(f"La longitud del texto es: {longitud}")

print(len("Hola, ¿cómo estás?"))

# Nota Importante:
"""La función "len()" también se utiliza para obtener la  longitud  o  el  número  de  elementos  de
estructuras como listas, tuplas, diccionarios, entre otras. Por ejemplo, en una  lista,  la  función
"len()" devuelve la cantidad de elementos que contiene, lo que resulta útil para iterar sobre  ellos
o realizar validaciones.

Es importante destacar que la función "len()" no mide el tamaño en  bytes  de  un  objeto,  sino  la
cantidad de elementos que contiene, lo que puede variar dependiendo del tipo de dato. Esto significa
que, en el caso de cadenas de texto, la longitud corresponde al número de caracteres,  mientras  que
en estructuras como listas o diccionarios, se refiere al número de elementos que contienen.

La función "len()" no solo se limita a medir la longitud de objetos almacenados en  variables,  sino
que también puede ser utilizada directamente con cadenas de texto literales. Además,  es  importante
notar que las comillas utilizadas para definir la cadena de texto no se cuentan  como  parte  de  la
longitud, ya que son simplemente delimitadores que indican el inicio y el final de la cadena.

Por último, la función "len()" no solo es útil para  validar  datos,  sino  también  para  optimizar
procesos que requieren conocer la cantidad de elementos en una estructura,  como  en  algoritmos  de
búsqueda o clasificación. Su capacidad para trabajar con diferentes tipos de datos la  convierte  en
una herramienta indispensable para cualquier programador que  busque  escribir  código  eficiente  y
robusto."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
