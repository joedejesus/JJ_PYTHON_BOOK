# Enunciado:
"""Los contenedores de tuplas en Python son variables que almacenan colecciones de elementos.  Estas
variables permiten  organizar  y  almacenar  datos  de  manera  eficiente.  Aunque  las  tuplas  son
inmutables, lo que significa que no se pueden modificar directamente  después  de  ser  creadas,  es
posible crear nuevas tuplas a partir de las existentes mediante operaciones como la concatenación de
tuplas.

Los contenedores de tuplas no pueden crecer dinámicamente como los contenedores de  listas,  ya  que
las tuplas son inmutables. Cada vez que se agrega un elemento a la tupla mediante concatenación,  se
crea una nueva tupla en memoria. Esto puede ser  menos  eficiente  en  comparación  con  estructuras
mutables como las listas, pero garantiza la inmutabilidad de los datos.

Además, al ser las tuplas objetos inmutables, la única forma de "agregar" elementos a un  contenedor
de tuplas es mediante la creación de una nueva tupla que combine los elementos  existentes  con  los
nuevos utilizando la concatenación de tuplas. Esto se logra mediante la sintaxis  "contenedor_tuplas
+= (i,)" para crear una tupla de un solo elemento y concatenarla a la tupla existente dentro  de  un
bucle. La coma después de "i" es necesaria para indicar que  se  trata  de  una  tupla  de  un  solo
elemento y no de un valor entre paréntesis; de otro modo, se  interpretaría  como  un  entero  entre
paréntesis, lo que generaría un error de tipo "TypeError".

El uso adecuado de las tuplas garantiza  que  las  operaciones  sobre  colecciones  sean  seguras  y
predecibles, lo que contribuye a la creación de  programas  robustos  y  fáciles  de  mantener.  Por
ejemplo, cuando se trabaja con datos que no deben modificarse, las tuplas son una excelente  opción.
Sin embargo, para operaciones que requieren modificaciones frecuentes, las  listas  suelen  ser  más
adecuadas.

Por último, es importante destacar que las tuplas son compatibles con una amplia gama de  métodos  y
funciones incorporadas en Python que facilitan tareas comunes como la búsqueda y la iteración.  Esto
las  convierte  en  una  herramienta  esencial  para  trabajar  con  datos  almacenados  de   manera
inmutable."""

# Ejemplo_contenedores_de_tuplas.py

# Explicación:
"""Definimos una variable llamada "contenedor_tuplas" y la inicializamos como una tupla vacía.  Esta
variable se utilizará para almacenar los datos procesados. Además, definimos otra  variable  llamada
"tupla" y le asignamos la tupla (1, 2, 3, 4, 5). Esta  variable  contiene  los  datos  que  queremos
procesar.

A continuación, utilizamos un bucle "for" para iterar sobre cada elemento de la  tupla.  Para  ello,
escribimos la palabra clave "for", seguida de la variable "i", que representa cada  elemento  de  la
secuencia y que definimos en este  momento,  seguida  del  operador  "in"  para  indicar  sobre  qué
secuencia queremos iterar y el nombre de la secuencia sobre la que queremos iterar, en este caso  la
variable "tupla". A continuación, escribimos dos puntos (:) para indicar el final de la expresión  y
el inicio del bloque de código asociado al bucle "for".

Dentro del bucle utilizamos la expresión de incremento "contenedor_tuplas += (i,)"  para  crear  una
nueva tupla que incluye el elemento actual "i"  en  cada  iteración  y  concatenarla  con  la  tupla
existente en "contenedor_tuplas". Esto se logra utilizando  el  operador  de  asignación  (+=)  para
concatenar la tupla actual "contenedor_tuplas" con una nueva tupla que contiene el elemento  "i"  en
cada iteración.

Colocamos esta línea de código con una indentación de cuatro espacios desde el margen izquierdo para
indicar que pertenece al bloque de código del bucle "for" y debe ejecutarse en cada iteración.

La sintaxis de la tupla que se va a concatenar, "(i,)", se utiliza para crear una tupla de  un  solo
elemento, donde "i" es el elemento que se va a agregar en cada iteración. La coma después de "i"  es
necesaria para indicar que se trata de una tupla de  un  solo  elemento  y  no  de  un  valor  entre
paréntesis. Los paréntesis son necesarios para denotar una tupla.

Por último, fuera del bucle, utilizamos la  función  "print()"  para  mostrar  el  contenido  de  la
variable "contenedor_tuplas" en  la  consola,  acompañado  de  un  mensaje  descriptivo  en  formato
"f-string". Esto nos permite verificar que el contenedor de tuplas se ha llenado  correctamente  con
los elementos de la tupla original contenida en la variable "tupla"."""

# Código:
contenedor_tuplas = ()

tupla = (1, 2, 3, 4, 5)

for i in tupla:
    contenedor_tuplas += (i,)

print(f"El contenedor de tuplas se ha llenado correctamente: {contenedor_tuplas}")

# Nota Importante:
"""Es importante inicializar el contenedor de tuplas como  una  tupla  vacía  antes  de  comenzar  a
agregar elementos. Esto asegura que el contenedor  esté  preparado  para  almacenar  los  datos  sin
errores.

Inicializar correctamente las variables mejora la claridad del código, ya  que  otros  programadores
pueden entender fácilmente la intención de esa inicialización.

Es crucial mantener la sintaxis "contenedor_tuplas += (i,)" al trabajar con tuplas de esta forma, ya
que, si intentáramos concatenar un elemento a una tupla sin la coma, como en  "contenedor_tuplas  +=
(i)", estaríamos intentando concatenar un número entero entre  paréntesis  con  una  tupla,  lo  que
generaría un error de tipo "TypeError", ya que la concatenación consiste en unir  dos  tuplas  y  un
número entero no es una tupla. Por lo tanto, es crucial utilizar la sintaxis  correcta  para  evitar
errores y garantizar que el programa funcione como se espera.

Por último, aunque las tuplas  son  inmutables,  su  uso  es  ideal  para  datos  que  no  necesitan
modificarse. Para los casos en los que se requiera modificar los datos con  frecuencia,  las  listas
son una mejor opción debido a su mutabilidad."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
