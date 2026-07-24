# Enunciado:
"""La inmutabilidad en Python se refiere a la propiedad de ciertos tipos de datos de no  cambiar  su
valor una vez que han sido creados. Una vez que un objeto inmutable ha  sido  creado,  su  valor  no
puede modificarse. Esto es útil para evitar errores de lógica en el código, ya que  los  valores  no
pueden cambiar sin que el programador lo sepa.

En el caso de las  tuplas,  esta  característica  asegura  que  los  datos  almacenados  permanezcan
constantes durante la ejecución del programa, lo que las hace ideales para  representar  colecciones
de datos que no deben alterarse. La inmutabilidad también contribuye a la optimización  del  uso  de
memoria y a la seguridad del código, ya que evita modificaciones accidentales o no deseadas.

Además, al ser inmutables, las tuplas pueden utilizarse como claves en los diccionarios, ya que  los
objetos inmutables son "hashables", lo que significa que su valor no cambiará durante  su  ciclo  de
vida.

Por último, la inmutabilidad es una característica fundamental de las tuplas en Python que garantiza
que los datos almacenados en ellas permanezcan constantes. Esto las  hace  útiles  para  representar
colecciones de datos que no deben ser modificadas, proporcionando mayor seguridad y  estabilidad  en
el manejo de datos dentro de un programa."""

# Ejemplo_inmutabilidad_de_las_tuplas.py

# Explicación:
"""Definimos una variable llamada "tupla" y le asignamos una tupla con los elementos (1, 2,  3),  la
cual será utilizada para demostrar la inmutabilidad de las tuplas en Python.

A continuación, intentamos modificar el tercer elemento  de  la  tupla  utilizando  el  operador  de
indexación "[]", con el índice 2, y asignándole un nuevo valor, en este caso, 4. Sin  embargo,  esto
generará un error de tipo "TypeError" debido a la inmutabilidad de las tuplas, ya que no permiten la
modificación directa de sus elementos una vez creadas.

Por último, utilizamos la función "print()" para intentar imprimir el valor de la variable  "tupla".
Sin embargo, el programa no llegará a ejecutar esta línea, ya que la ejecución  se  detendrá  en  la
línea en la que se intenta modificar la tupla, generando el error mencionado.

De esta forma, intentamos modificar el tercer elemento de la tupla, pero esto generará un  error  de
tipo "TypeError" debido a la inmutabilidad de las tuplas, lo que  significa  que  sus  elementos  no
pueden modificarse una vez que han sido creadas."""

# Código:
tupla = (1, 2, 3)

tupla[2] = 4
print(tupla)

# Nota Importante:
"""En este caso, el código generará un error de tipo "TypeError", ya que las tuplas son inmutables y
no se pueden modificar. Esto significa que, una vez que se crea una tupla, sus elementos  no  pueden
ser alterados directamente. La inmutabilidad de las tuplas es una característica que  garantiza  que
los datos almacenados en ellas permanezcan constantes, lo que  las  hace  ideales  para  representar
datos que no deben cambiar a lo largo de la ejecución del programa.

Si es necesario modificar los datos de una tupla, se debe crear una  nueva  tupla  con  los  valores
deseados o utilizar un tipo de dato mutable, como las listas, que permiten cambios en sus elementos.
Por ejemplo, se puede convertir una tupla en una lista con el  constructor  "list()",  realizar  las
modificaciones necesarias y luego volver a convertirla en una tupla con  el  constructor  "tuple()".
Sin embargo, es importante tener en cuenta que esto implica  la  creación  de  un  nuevo  objeto  en
memoria, ya que las tuplas originales no pueden modificarse directamente.

Por último, esta característica también contribuye a la eficiencia del programa, ya que los  objetos
inmutables pueden ser optimizados por el intérprete de Python para  ahorrar  memoria  y  mejorar  el
rendimiento. Además, las tuplas, al ser  inmutables,  son  "hashables".  La  palabra  "hashable"  se
refiere a la capacidad de un objeto de ser utilizado como clave en un diccionario o como elemento de
un conjunto, lo que no es posible con tipos de datos mutables, como las listas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────