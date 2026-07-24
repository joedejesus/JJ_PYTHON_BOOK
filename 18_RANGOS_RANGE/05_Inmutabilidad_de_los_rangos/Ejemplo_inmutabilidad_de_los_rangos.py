# Enunciado:
"""La inmutabilidad en Python se refiere a la propiedad de ciertos tipos de datos de no  cambiar  su
valor una vez que han sido creados. Una vez que un objeto inmutable ha  sido  creado,  su  valor  no
puede modificarse. Esto es útil para evitar errores de lógica en el código, ya que  los  valores  no
pueden cambiar sin que el programador lo sepa.

En el caso de los rangos, esta  característica  asegura  que  los  elementos  generados  permanezcan
constantes durante la ejecución del programa, lo que los hace ideales para representar secuencias de
números que no deben alterarse. La inmutabilidad también contribuye a la  optimización  del  uso  de
memoria y a la seguridad del código, ya que evita modificaciones accidentales o no deseadas.

Además, al ser inmutables, los rangos pueden ser utilizados en estructuras de control  y  bucles  de
manera segura, ya que su valor no cambiará durante su ciclo de vida.

Por último, la inmutabilidad es una característica fundamental de los rangos en Python que garantiza
que los elementos generados por estos permanezcan constantes. Esto los hace útiles para  representar
secuencias que no deben modificarse, proporcionando mayor seguridad y estabilidad en  el  manejo  de
datos dentro de un programa."""

# Ejemplo_inmutabilidad_de_los_rangos.py

# Explicación:
"""Definimos una variable llamada "rango" y le asignamos un rango que genera números enteros desde 1
hasta 3. Este rango se utilizará para demostrar la inmutabilidad de los rangos en Python.

A continuación, intentamos modificar  el  tercer  elemento  del  rango  utilizando  el  operador  de
indexación "[]" con el índice 2 y asignándole un nuevo valor, en este caso,  4.  Sin  embargo,  esto
generará un error de tipo "TypeError" debido a la inmutabilidad de los rangos, ya que no permiten la
modificación de sus elementos una vez creados.

Por último, utilizamos la función "print()" para intentar imprimir el valor de la variable  "rango".
Sin embargo, el programa no llegará a ejecutar esta línea, ya que la ejecución  se  detendrá  en  la
línea donde se intenta modificar el rango, generando el error mencionado.

De esta forma, hemos intentado modificar el tercer elemento del rango, pero esto generará  un  error
de tipo "TypeError" debido a la inmutabilidad  de  los  rangos,  lo  que  significa  que  no  pueden
modificarse sus elementos una vez que han sido creados."""

# Código:
rango = range(1, 4)

rango[2] = 4
print(rango)

# Nota Muy Importante:
"""En este caso, el código generará un error de tipo "TypeError", ya que los rangos son inmutables y
no pueden modificarse. Esto significa que, una vez que se crea un rango,  sus  elementos  no  pueden
alterarse. La inmutabilidad de los rangos es una característica  que  garantiza  que  los  elementos
generados permanezcan constantes, lo que los hace ideales para representar secuencias que  no  deben
cambiar a lo largo de la ejecución del programa.

Si se necesita modificar los elementos de un rango, es  necesario  crear  un  nuevo  rango  con  los
valores deseados o utilizar un tipo de dato mutable, como las listas, que permiten realizar  cambios
en sus elementos. Por ejemplo, se puede convertir un rango en una lista  utilizando  el  constructor
"list()", realizar las modificaciones necesarias y luego trabajar con la lista resultante.

Sin embargo, si se desea convertir la lista en un rango nuevamente  con  el  constructor  "range()",
este requiere valores que definan el inicio, el fin  y,  opcionalmente,  el  paso,  por  lo  que  se
obtendría un nuevo rango y los cambios realizados en la lista no necesariamente se reflejarían en el
nuevo rango creado.

Por último, esta característica inmutable contribuye a  la  eficiencia  del  programa,  ya  que  los
objetos inmutables pueden ser optimizados por el intérprete de Python para ahorrar memoria y mejorar
el rendimiento. Además, los rangos, al ser inmutables, ofrecen seguridad y estabilidad  al  trabajar
con secuencias que no deben cambiar, algo que no  ocurre  con  tipos  de  datos  mutables  como  las
listas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────