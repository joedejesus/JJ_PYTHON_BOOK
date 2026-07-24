# Enunciado:
"""La comprensión de listas es una característica poderosa y elegante de Python  que  permite  crear
nuevas listas de manera concisa y eficiente. Consiste en aplicar una expresión a cada elemento de un
iterable y, opcionalmente, filtrar los elementos que cumplan una condición, todo ello  en  una  sola
línea de código para generar una nueva lista con el resultado.

Esto hace que las comprensiones de  listas  sean  especialmente  útiles  para  escribir  código  más
compacto y legible, eliminando la necesidad de bucles for tradicionales y estructuras  condicionales
adicionales en ciertos casos. Sin  embargo,  no  siempre  reemplazan  a  los  bucles  tradicionales,
especialmente cuando se requieren múltiples pasos o una lógica compleja que  podría  comprometer  la
claridad del código.

La sintaxis básica de una comprensión de listas es: x = [(expresión) for  elemento  in  iterable  if
(condición)] Donde "expresión" es la operación que se desea aplicar a cada elemento,  "elemento"  es
la variable que representa cada elemento del iterable, "iterable" es la colección de datos sobre  la
cual se itera, y "condición" es una expresión opcional que filtra los elementos  en  función  de  la
condición que se imponga, determinando si se incluirán en la nueva lista o no.

La "expresión" puede ser tan simple  o  compleja  como  sea  necesario,  lo  que  permite  una  gran
flexibilidad en la manipulación de datos. Pero debe ser una expresión válida que pueda ser  evaluada
para cada elemento del iterable. Esta expresión se aplica a cada elemento del  iterable  que  cumple
con la condición si se impone, y este se incluye en la  nueva  lista  resultante.  Si  se  omite  la
condición, la expresión se aplicará a todos los elementos del iterable, generando  una  nueva  lista
con el resultado de la expresión aplicada a cada elemento sin ningún filtro adicional.

El "elemento" es la variable que representa cada elemento del iterable durante la  iteración,  y  se
puede nombrar de cualquier manera, siempre y cuando siga las reglas de nomenclatura de Python.

El "iterable" es la colección de datos sobre la cual se itera, y puede ser cualquier objeto que  sea
iterable en Python, como listas, tuplas, conjuntos, diccionarios, cadenas de texto, entre otros.

La "condición" es opcional, pero su inclusión permite  filtrar  los  elementos  del  iterable  según
criterios específicos. Esta debe ser una expresión que  evalúe  a  "True"  o  "False",  y  solo  los
elementos que cumplan con la condición serán incluidos en la nueva lista. La condición evalúa si  el
elemento del iterable cumple o no con el criterio establecido después de la palabra clave "if" y, si
es así, se aplica la expresión a ese elemento para incluirlo en la nueva lista; de lo contrario,  se
omite.

Por último, las comprensiones de listas son más rápidas  que  los  bucles  tradicionales  en  muchos
casos, debido a que están optimizadas a nivel interno en Python. Sin embargo, es importante  usarlas
con moderación y asegurarse de que su uso no comprometa la claridad  del  código,  especialmente  en
casos donde las operaciones dentro de la comprensión sean complejas o difíciles de entender.

Además, son una herramienta versátil que combina eficiencia y legibilidad, siempre que  se  utilicen
de manera apropiada y en contextos donde su propósito sea claro."""

# Ejemplo_comprension_de_listas.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista de cadenas de texto.  Esta  lista
será utilizada como base para crear una nueva lista  utilizando  comprensión  de  listas,  aplicando
diferentes operaciones y filtros según sea necesario.

Definimos una nueva variable llamada "nueva_lista" y le asignamos una nueva lista generada a  partir
de la variable "lista" usando una comprensión de listas. Utilizamos corchetes  []  para  definir  la
nueva lista, y dentro de ellos añadiremos las partes que componen la comprensión de listas.

Para ello, en primer lugar, añadimos la expresión "(i.upper())" que se aplicará a cada elemento  "i"
de la lista original que cumpla la condición; en este caso, el elemento se  convierte  a  mayúsculas
antes de ser incluido en "nueva_lista" gracias al método ".upper()". Encerramos la  expresión  entre
paréntesis para asegurarnos de que se evalúe correctamente.

En segundo lugar, añadimos el bucle "for i in lista" que itera  sobre  cada  elemento  de  la  lista
original, asignando cada elemento a la variable "i" en cada iteración.

En tercer lugar, añadimos la condición "if (len(i) >= 5)" que verifica si la longitud  del  elemento
"i" es mayor o igual a 5 gracias a la función  "len()";  si  es  así,  se  le  aplica  la  expresión
"(i.upper())" a ese elemento para incluirlo en "nueva_lista"; de lo contrario, se omite.  Encerramos
la condición entre paréntesis para asegurarnos de que se evalúe correctamente.

En este caso, la condición permite filtrar solo los elementos de la lista original  que  tienen  una
longitud mayor o igual a 5, ya que (len(i) >= 5) evalúa como "True" para los elementos  que  cumplen
con la condición y como "False" para los que no, por lo que solo los elementos que  cumplen  con  la
condición serán incluidos en "nueva_lista" después de ser convertidos a mayúsculas por la  expresión
"(i.upper())".

Por último, utilizamos la  función  "print()"  acompañada  de  un  mensaje  descriptivo  en  formato
"f-string" que indica que se trata de la  nueva  lista  generada  a  partir  de  la  comprensión  de
listas."""

# Código:
lista = ["Hola", "Mundo", "Python", "Programación"]

nueva_lista = [(i.upper()) for i in lista if (len(i) >= 5)]
print(f"Esta es la nueva lista generada a partir de la comprensión de listas: {nueva_lista}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que las comprensiones de listas están diseñadas para ser una forma
declarativa de construir nuevas listas basadas en iterables  existentes,  sin  modificar  los  datos
originales. Esto significa que las comprensiones de listas no alteran el iterable original, sino que
generan una nueva lista con los resultados de la expresión aplicada a cada elemento que  cumple  con
la condición, si se especifica alguna.

Es por ello que los métodos o funciones utilizados en una expresión dentro  de  una  comprensión  de
listas deben ser aquellos que no modifiquen el iterable original, ya que las  comprensiones  generan
una nueva lista independiente.

La comprensión de listas funciona de la siguiente manera: primero  itera  sobre  cada  elemento  del
iterable original, luego evalúa la condición (si se proporciona)  para  determinar  si  el  elemento
iterado cumple o no con esa condición. Si cumple, se aplica la expresión a ese elemento para generar
el valor que se incluirá en la nueva lista. Si la condición no se cumple, el elemento se omite y  no
se incluye en la nueva lista. Además, si la condición no se proporciona, la expresión se aplicará  a
todos los elementos del iterable original,  generando  una  nueva  lista  con  el  resultado  de  la
expresión aplicada a cada elemento sin ningún filtro adicional.

En cuanto a la expresión y la condición dentro de la comprensión de listas, es importante asegurarse
de que sean claras y legibles. Además, deben encerrarse entre paréntesis () para garantizar  que  se
evalúen correctamente dentro de la comprensión, y los operadores utilizados dentro  de  ellas  deben
ser apropiados para el tipo de datos que se  está  manipulando,  ya  que  el  uso  de  operadores  o
funciones inadecuados puede generar errores o resultados inesperados. De igual modo, las funciones o
métodos dentro de la expresión o condición deben definirse de forma adecuada y respetar  las  reglas
de sintaxis de Python para evitar errores de ejecución.

Por último, aunque las comprensiones de listas son una herramienta poderosa para crear nuevas listas
de manera concisa y eficiente, se deben mantener simples y  enfocadas  en  su  propósito  principal:
transformar o filtrar datos de manera eficiente y legible.  En  casos  donde  las  operaciones  sean
complejas o impliquen  múltiples  pasos,  puede  ser  preferible  utilizar  bucles  tradicionales  o
funciones auxiliares para garantizar la claridad y mantenibilidad del código."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
