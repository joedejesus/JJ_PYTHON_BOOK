# Enunciado:
"""La función "len()" es una función incorporada en  Python  que  permite  conocer  la  cantidad  de
elementos que contiene un rango, es decir, su longitud. Esta función  es  ampliamente  utilizada  en
programación debido a su simplicidad y eficiencia.

La función "len()" toma un rango u otra estructura iterable como  argumento  y  devuelve  un  número
entero que representa la cantidad de elementos que contiene. En el caso de los  rangos,  la  función
"len()" calcula la cantidad de elementos generados por el rango, teniendo en cuenta  el  inicio,  el
final y el paso.

La función "len()" permite realizar operaciones como validar la longitud de  rangos  en  algoritmos,
analizar datos en estructuras más complejas y controlar el flujo de programas  que  dependen  de  la
cantidad de elementos en un rango.

Es importante destacar que, si se utilizan rangos con pasos, la función  "len()"  cuenta  únicamente
los elementos generados por el rango, lo que puede resultar en una longitud diferente de la esperada
si no se considera el paso. Esto significa que los valores omitidos por el paso no serán tenidos  en
cuenta ni contados en la longitud del rango. Además, el último valor especificado en el rango no  se
incluye, ya que los rangos son excluyentes en su límite superior.

La implementación de la función "len()" en  Python  está  optimizada  para  ofrecer  un  rendimiento
rápido, confiable y eficiente, independientemente del tamaño del rango o de la  estructura  iterable
que se esté evaluando. Esto la convierte en una herramienta fundamental para tareas  que  involucran
la manipulación y el análisis de datos en rangos, así como para el manejo de  estructuras  iterables
como listas y diccionarios.

Por último, su versatilidad y facilidad de uso hacen que la función "len()" sea una de las funciones
más utilizadas, lo que permite resolver problemas comunes de manera eficiente y con  un  código  más
legible."""

# Ejemplo_medir_la_longitud_de_un_rango.py

# Explicación:
"""Definimos una variable llamada "rango" y le asignamos  un  rango  que  genera  una  secuencia  de
números desde el 1 hasta el 10. Este rango será utilizado para medir su longitud mediante la función
"len()".

A continuación, definimos una variable llamada "longitud" y le asignamos el resultado de llamar a la
función "len()" con la variable "rango" como argumento.  Para  ello,  escribimos  el  nombre  de  la
función "len()" y, dentro de los paréntesis, colocamos la variable "rango" como argumento.

La función "len()" toma como argumento el rango y  devuelve  un  número  entero  que  representa  la
cantidad de elementos que contiene, el cual se almacena en la variable "longitud".

Además, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica que se trata de la longitud del rango. De  esta
forma, obtenemos la longitud del rango "range(1, 11)", que es 10, ya que la función  "len()"  cuenta
cada elemento generado por el rango.

Por último, utilizamos la función "len()" directamente con un rango literal para medir su  longitud.
Para ello, utilizamos la función "print()" y, dentro de esta, colocamos la función "len()", que toma
como argumento el rango literal "range(5, 15, 2)", lo que nos permite obtener la  longitud  de  este
rango directamente, sin necesidad de almacenarlo en una variable.

En este caso, al ser un rango con un paso de 2,  la  función  "len()"  contará  solo  los  elementos
generados por el rango, lo que resulta en una longitud de 5, ya que el rango genera los  números  5,
7, 9, 11 y 13, excluyendo el valor final 15.

De igual manera, también podríamos pasar como argumento a la función "len()", dentro de  la  función
"print()", una variable que almacene un rango,  de  esta  forma:  "print(len(rango))",  lo  que  nos
permitiría medir la longitud de cualquier  rango  almacenado  en  la  variable  de  forma  rápida  y
directa."""

# Código:
rango = range(1, 11)

longitud = len(rango)
print(f"La longitud del rango es: {longitud}")

print(len(range(5, 15, 2)))

# Nota Importante:
"""La función "len()" también se utiliza para obtener la  longitud  o  el  número  de  elementos  de
estructuras como listas, diccionarios, cadenas de texto, conjuntos y otros objetos iterables. Lo que
hace que esta función sea tan versátil es su capacidad para trabajar con diferentes tipos de  datos,
realizar validaciones o implementar algoritmos que dependan de la longitud  de  las  estructuras  de
datos.

La función "len()" no mide el tamaño en memoria, en  bytes,  de  un  objeto,  sino  la  cantidad  de
elementos que contiene. Esto significa que, en el caso de los rangos,  la  longitud  corresponde  al
número de elementos generados, mientras que, en las cadenas  de  texto,  se  refiere  al  número  de
caracteres; en las listas, al número de elementos; y  en  los  diccionarios,  al  número  de  claves
almacenadas, y no a la cantidad de memoria que ocupan.

Es importante tener en cuenta que, si se utilizan  rangos  con  pasos,  la  función  "len()"  cuenta
únicamente los elementos generados por el rango, lo que puede resultar en una longitud diferente  de
la esperada si no se considera el paso. Esto significa que los elementos omitidos  por  el  paso  no
serán contados en la longitud del rango, ya que la función "len()" solo  cuenta  los  elementos  que
realmente se generan en el rango. Además, el último valor especificado en el rango no se incluye, ya
que los rangos son excluyentes en su límite superior.

Por último, la función "len()" es una  herramienta  clave  para  optimizar  procesos  que  requieren
conocer la cantidad de elementos en una estructura, como en algoritmos de búsqueda, clasificación  o
análisis de datos. Su capacidad para trabajar con diferentes tipos de datos  y  su  integración  con
otras funciones y estructuras  de  Python  la  convierten  en  una  herramienta  indispensable  para
cualquier programador que busque escribir código eficiente, robusto y fácil de mantener."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────