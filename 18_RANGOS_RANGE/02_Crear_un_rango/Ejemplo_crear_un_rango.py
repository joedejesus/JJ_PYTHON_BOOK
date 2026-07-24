# Enunciado:
"""La forma más común de crear un rango en Python es utilizando el constructor "range()". Los rangos
son estructuras de datos que permiten generar secuencias de números  enteros  de  manera  eficiente.
Estas secuencias pueden utilizarse en bucles, listas o en  cualquier  otra  operación  que  requiera
iterar sobre un conjunto de números enteros.

Los rangos en Python son objetos ordenados, iterables e inmutables. Esto significa que los elementos
de un rango mantienen un orden específico, no pueden modificarse después de  su  creación  y  pueden
recorrerse utilizando bucles o funciones de iteración. A diferencia de las  listas,  los  rangos  no
almacenan todos los números en memoria, lo que los  hace  más  eficientes  en  términos  de  uso  de
recursos. Además, los rangos solo pueden contener números enteros, ya sea  en  forma  literal  o  en
variables, lo que los convierte en una opción ideal para representar secuencias de índices.

El constructor "range()" puede aceptar uno, dos o tres argumentos, dependiendo de la  secuencia  que
se desee generar. Cuando se utiliza un solo argumento, este representa  el  límite  superior  de  la
secuencia (exclusivo), comenzando desde 0 de forma predeterminada. Si se utilizan dos argumentos, el
primero representa el inicio (inclusivo) y el segundo el límite superior (exclusivo). Finalmente, si
se utiliza un tercer argumento, este representa el  paso  o  incremento  entre  los  números  de  la
secuencia.

Además, todos los argumentos deben ser números enteros, positivos o negativos. En todos  los  casos,
el valor inicial está incluido en la secuencia, mientras que el valor final está excluido.

Es posible crear secuencias descendentes utilizando un paso negativo. Para ello, el índice de inicio
debe ser mayor que el índice final, y el paso debe ser un número negativo. En este caso, el paso  es
obligatorio, ya que,  sin  él,  el  constructor  "range()"  no  sabría  cómo  generar  la  secuencia
descendente. De igual forma que con los rangos ascendentes, el índice final  no  se  incluye  en  la
secuencia generada.

Es importante ser consistente en el uso de rangos dentro de un proyecto, ya que  esto  hace  que  el
código sea más legible y menos propenso a errores. La consistencia incluye  no  solo  el  estilo  de
definición de los rangos, sino también la forma  en  que  se  accede  a  ellos  y  se  utilizan  sus
elementos.

Por último, los rangos son una herramienta fundamental en Python para generar secuencias de  números
enteros de manera eficiente y segura. Aunque no permiten modificaciones, su inmutabilidad  los  hace
ideales para representar secuencias que no deben cambiar, lo  que  puede  mejorar  la  claridad  del
código."""

# Ejemplo_crear_un_rango.py

# Explicación:
"""Definimos una variable llamada "rango_1" y le asignamos un rango que genera números enteros desde
0 hasta 10, sin incluir 10. Para ello,  utilizamos  el  constructor  "range()"  con  los  argumentos
correspondientes separados por comas; en este caso, el índice de inicio "0"  y  el  límite  superior
"10".

A continuación, definimos otra variable llamada "rango_2" y le asignamos un rango que genera números
enteros desde 10 hasta 0, sin  incluir  0,  con  un  decremento  de  2.  Para  ello,  utilizamos  el
constructor "range()" con los argumentos correspondientes separados por  comas;  en  este  caso,  el
índice de inicio "10", el límite inferior "0" y el paso "-2".

En ambos casos, el valor que corresponde al límite final no se incluye en el rango, por  lo  que  el
primer rango genera números del 0 al 9 y el segundo  rango  genera  números  del  10  al  2  con  un
decremento de 2; es decir: 10, 8, 6, 4 y 2.

Por último, utilizamos la función "print()" para mostrar el contenido de  los  rangos  en  forma  de
lista en la consola, acompañados de un mensaje descriptivo  en  formato  "f-string"  que  indica  el
contenido de cada rango en forma de lista. Para ello, utilizamos el constructor "list()"  dentro  de
la expresión "f-string" para convertir los rangos en listas  y,  de  esta  forma,  poder  visualizar
claramente los números generados por cada rango en lugar de la representación del objeto rango.

De esta forma, hemos creado dos rangos en Python,  uno  con  valores  consecutivos  y  otro  con  un
decremento específico, demostrando la flexibilidad y la versatilidad de los rangos en Python."""

# Código:
rango_1 = range(0, 10)
print(f"Este es un rango de números consecutivos: {list(rango_1)}")

rango_2 = range(10, 0, -2)
print(f"Este es un rango con un decremento de 2: {list(rango_2)}")

# Nota Importante:
"""Es recomendable ser consistente en el uso de rangos dentro de un proyecto. Esto significa  elegir
un estilo claro para definir y utilizar rangos, y mantenerlo en todo el código. La  consistencia  no
solo mejora la legibilidad  del  código,  sino  que  también  reduce  la  probabilidad  de  errores,
especialmente en proyectos colaborativos o de gran escala.

Es importante tener en cuenta que el índice final  de  un  rango  no  se  incluye  en  la  secuencia
generada. Ya se trate de secuencias ascendentes o descendentes, el índice final siempre se  excluye,
lo que significa que el  rango  generado  no  incluirá  el  valor  de  dicho  índice.  Esta  es  una
característica fundamental de los rangos en Python, y es crucial tenerla en cuenta  al  definir  los
límites de un rango para evitar confusiones o errores en el código.

Además, el valor del paso permite generar secuencias con incrementos  específicos,  lo  que  resulta
útil para crear patrones numéricos o  para  iterar  sobre  elementos  de  una  lista  con  un  salto
determinado. Para secuencias ascendentes, el paso  debe  ser  un  número  positivo  y  es  opcional,
mientras que para secuencias descendentes, el paso debe ser un número negativo y es obligatorio.

El paso no debe ser cero en ningún caso, ya que esto generaría un error de ejecución. El constructor
"range()" no puede generar una secuencia de números enteros con un paso de cero, lo que  produce  un
error de tipo "ValueError".

Los rangos son ideales para trabajar con secuencias de números enteros, pero es importante tener  en
cuenta que son inmutables. Esto significa que no se pueden agregar, eliminar ni modificar  elementos
de un rango una vez creado.

Por último, los rangos se utilizan ampliamente en bucles  "for"  para  iterar  sobre  secuencias  de
números o para generar índices con los que acceder a  elementos  de  una  lista.  Su  eficiencia  en
términos de uso de memoria y su capacidad para generar  secuencias  de  números  enteros  de  manera
rápida y sencilla  los  convierten  en  una  herramienta  esencial  para  cualquier  programador  de
Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
