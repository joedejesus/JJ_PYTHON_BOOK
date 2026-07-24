# Enunciado:
"""Los cambios indirectos en tuplas se refieren a la posibilidad de modificar los elementos  de  una
tupla de forma indirecta al convertirla en una  lista,  ya  que  las  tuplas  son  inmutables.  Esto
significa que no pueden modificarse  directamente,  pero  podemos  convertirlas  en  una  estructura
mutable, como una lista, realizar las modificaciones necesarias y luego convertirlas de nuevo en una
tupla.

Este enfoque es muy útil cuando se necesita realizar cambios en los datos almacenados en una  tupla.
Sin embargo, la tupla original permanece intacta y  se  genera  una  nueva  tupla  con  los  cambios
aplicados, además de una lista intermedia que se utiliza para efectuar las modificaciones.

Por último, este proceso es una solución práctica para trabajar con la inmutabilidad de  las  tuplas
en Python, pero debe utilizarse con precaución en situaciones en las que el rendimiento sea crítico,
ya que implica operaciones adicionales de conversión."""

# Ejemplo_cambios_indirectos_en_tuplas.py

# Explicación:
"""Definimos una variable llamada "tupla" y le asignamos una tupla de números enteros (1, 2,  3,  4,
5). Esta tupla se utilizará para demostrar el proceso de cambios indirectos.

A continuación, definimos una variable llamada "lista" y le asignamos el resultado de la  conversión
de la tupla a una lista utilizando el constructor "list()". Para  ello,  utilizamos  el  constructor
"list()" que toma la tupla como argumento y devuelve una nueva lista con los mismos elementos.  Esto
nos permite trabajar con una estructura mutable, ya que las listas pueden ser modificadas.

Modificamos el tercer elemento de la lista situado en el índice 2 asignándole  el  nuevo  valor  10.
Para ello, utilizamos el operador de indexación [] con el número dos en su interior "[2]", precedido
de la variable "lista", donde el número dentro de los corchetes representa el  índice  del  elemento
que queremos modificar y le asignamos el nuevo valor 10 utilizando el operador de asignación (=). De
esta forma, hemos modificado el tercer elemento de la lista, que originalmente era 3, y ahora se  ha
actualizado a 10.

Luego, definimos una variable llamada "nueva_tupla" y le asignamos  el  resultado  de  convertir  la
lista de nuevo  en  una  tupla  utilizando  el  constructor  "tuple()".  Para  ello,  utilizamos  el
constructor "tuple()" que toma la lista como argumento y devuelve una nueva  tupla  con  los  mismos
elementos. Esto nos permite trabajar con una estructura inmutable, ya que las tuplas no  pueden  ser
modificadas directamente.

Por último, utilizamos la función "print()" para mostrar el resultado en  la  consola  de  la  nueva
tupla que corresponde a la tupla  original  modificada  indirectamente,  acompañada  de  un  mensaje
descriptivo en formato "f-string" que indica que se trata de la tupla modificada indirectamente.  El
resultado mostrará la nueva tupla con el tercer elemento actualizado a 10,  mientras  que  la  tupla
original permanecerá sin cambios."""

# Código:
tupla = (1, 2, 3, 4, 5)

lista = list(tupla)
lista[2] = 10

nueva_tupla = tuple(lista)
print(f"Esta es la tupla modificada indirectamente: {nueva_tupla}")

# Nota Importante:
"""Es importante destacar que este proceso no modifica la tupla original, sino que  crea  una  nueva
tupla con los cambios deseados. Esto significa que la tupla original permanece  inalterada,  lo  que
garantiza la integridad de los datos originales. Sin embargo, este método puede ser ineficiente para
tuplas grandes, ya que implica la creación de una lista intermedia y la conversión de vuelta  a  una
tupla, lo que puede aumentar el uso de memoria y el tiempo de ejecución.

El término "cambios indirectos" se refiere a la idea de que estamos  modificando  los  datos  de  la
tupla a través de una estructura mutable, en este caso, la lista, en lugar  de  modificar  la  tupla
directamente debido a su naturaleza inmutable.

Técnicamente no estamos realizando cambios indirectos en la tupla,  sino  que  estamos  creando  una
nueva tupla a partir de la lista que se creó a partir de la tupla original, lo que  implica  que  se
están utilizando recursos adicionales para almacenar tanto la lista como  la  nueva  tupla,  lo  que
puede resultar problemático en términos de rendimiento, especialmente si la tupla original es grande
o si se realizan múltiples modificaciones.

Por lo tanto, se recomienda usar este enfoque solo cuando  sea  realmente  necesario  y  no  existan
alternativas más eficientes. En general, es mejor diseñar  el  código  de  manera  que  no  requiera
modificaciones indirectas en tuplas, ya que esto puede llevar a un código más limpio,  mantenible  y
eficiente.

Por último, comprender las limitaciones y ventajas de este enfoque es clave  para  tomar  decisiones
informadas al trabajar con tuplas en Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
