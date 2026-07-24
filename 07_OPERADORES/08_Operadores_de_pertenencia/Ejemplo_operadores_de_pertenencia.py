# Enunciado:
"""Los operadores de pertenencia en Python son herramientas que permiten comprobar  si  un  elemento
forma parte de una estructura iterable o  de  un  contenedor  personalizado,  devolviendo  un  valor
booleano (True o False) como respuesta.

Estos operadores son: "in" y "not in". El operador "in" verifica si el  elemento  referenciado  está
presente en la estructura, mientras que el operador "not in" verifica su ausencia.  La  equivalencia
semántica de los operadores de pertenencia al español es: (in = está en) y (not in = no está en).

Además, es posible utilizar estos operadores en estructuras de datos como cadenas de texto,  listas,
tuplas, rangos, conjuntos,  conjuntos  congelados,  diccionarios  e  incluso  secuencias  de  bytes,
bytearray y memoryview, tanto en forma de variable como de forma literal, y en cualquier objeto  que
implemente el método mágico "__contains__", el cual se verá en la sección de programación  orientada
a objetos.

Sin embargo, para los diccionarios, estos operadores solo  permiten  verificar  si  una  clave  está
presente y no su valor asociado. Para el resto de estructuras, solo es posible saber si el  elemento
está presente o no, pero no cuántas veces lo está.

Los operadores de pertenencia son sensibles al tipo de dato.  En  la  verificación  de  pertenencia,
Python compara el elemento con los contenidos  de  la  estructura.  Si  no  encuentra  coincidencia,
devuelve (False).

Por esta razón, es muy importante referenciar el elemento a verificar dentro de  la  estructura  tal
como se define por norma cada elemento dentro de esa estructura; de lo contrario,  Python  devolverá
(False) o, en ciertos casos específicos, lanzará un error de tipo. Un "TypeError" solo se  producirá
si el contenedor no admite este tipo  de  operación.  Por  lo  tanto,  es  recomendable  usar  tipos
compatibles para que la comparación tenga sentido. También es importante encerrar las expresiones de
pertenencia entre paréntesis, especialmente si se combinan con otras expresiones.

Por último, los operadores de pertenencia son esenciales en la programación porque permiten que  las
estructuras de control, como los condicionales "if", "elif" y "else", así como los  bucles  "for"  y
"while", determinen el flujo del programa basándose en las respuestas booleanas devueltas por  estos
operadores. Por todo ello, dominar los operadores de pertenencia permite escribir código más legible
y lógico, facilitando el control del flujo según las necesidades."""

# Ejemplo_operadores_de_pertenencia.py

# Explicación:
"""Definimos varias variables, cada una con un  nombre  que  describe  el  tipo  de  estructura  que
almacenan. En cada caso, les asignamos la  estructura  correspondiente,  siguiendo  la  sintaxis  de
Python para cada tipo de dato.

A continuación, en cada caso definimos dos variables con nombres descriptivos para cada verificación
y les asignamos, respectivamente, el resultado de dos verificaciones.

En el primer caso, verificamos si el dato referenciado está presente en la  estructura.  Para  ello,
primero hacemos referencia al dato respetando la  sintaxis  correspondiente,  seguido  del  operador
"in", seguido de la estructura en la  que  queremos  verificar  su  presencia,  y  encerrando  entre
paréntesis la expresión completa.

En el segundo caso, verificamos si el dato referenciado no está  presente  en  la  estructura.  Para
ello, primero hacemos referencia  al  dato  respetando  la  sintaxis  correspondiente,  seguido  del
operador "not in", seguido de la estructura en la que queremos verificar su ausencia,  y  encerrando
entre paréntesis la expresión completa.

Por último, en cada caso  imprimimos  el  resultado  de  cada  verificación  utilizando  la  función
"print()", concatenada con un mensaje que describe el propósito de  la  verificación.  El  resultado
será un valor booleano (True o False), indicando si el dato está presente o no en la estructura."""

# Código:
texto = "Hola amigo"
v_1_texto = ("Hola" in texto)
v_2_texto = ("Python" not in texto)
print("El texto contiene la palabra \"Hola\":", v_1_texto)
print("El texto no contiene la palabra \"Python\":", v_2_texto)

lista = [1, 2, 3, 4, 5]
v_1_lista = (3 in lista)
v_2_lista = (6 not in lista)
print("La lista contiene el número 3:", v_1_lista)
print("La lista no contiene el número 6:", v_2_lista)

tupla = (10, 20, 30)
v_1_tupla = (20 in tupla)
v_2_tupla = (40 not in tupla)
print("La tupla contiene el número 20:", v_1_tupla)
print("La tupla no contiene el número 40:", v_2_tupla)

rango = range(1, 11)
v_1_rango = (5 in rango)
v_2_rango = (11 not in rango)
print("El rango contiene el número 5:", v_1_rango)
print("El rango no contiene el número 11:", v_2_rango)

conjunto = {1, 2, 3, 4, 5}
v_1_conjunto = (3 in conjunto)
v_2_conjunto = (6 not in conjunto)
print("El conjunto contiene el número 3:", v_1_conjunto)
print("El conjunto no contiene el número 6:", v_2_conjunto)

conjunto_congelado = frozenset({1, 2, 3, 4, 5})
v_1_conjunto_congelado = (3 in conjunto_congelado)
v_2_conjunto_congelado = (6 not in conjunto_congelado)
print("El conjunto congelado contiene el número 3:", v_1_conjunto_congelado)
print("El conjunto congelado no contiene el número 6:", v_2_conjunto_congelado)

diccionario = {"a": 1, "b": 2, "c": 3}
v_1_diccionario = ("b" in diccionario)
v_2_diccionario = ("d" not in diccionario)
print("El diccionario contiene la clave \"b\":", v_1_diccionario)
print("El diccionario no contiene la clave \"d\":", v_2_diccionario)

# Nota Muy Importante:
"""Es posible combinar las evaluaciones de pertenencia con otras expresiones, estructuras o  valores
para crear expresiones más complejas y potentes, enlazándolas mediante operadores  lógicos,  siempre
que la combinación tenga sentido lógico.

Cada expresión o estructura debe seguir la sintaxis correcta y estar encerrada entre paréntesis o en
su signo de cierre correspondiente, y los valores deben estar correctamente definidos  siguiendo  la
sintaxis de  Python.  Además,  las  estructuras,  valores  o  literales  contenidos  dentro  de  una
subexpresión se deben separar con los operadores lógicos "or" o "and" para su correcta evaluación.

De esta forma, el resultado  final  dependerá  de  cómo  se  combinen  las  subexpresiones  con  los
operadores lógicos. En consecuencia,  podrá  ser  (True)  o  (False)  según  se  cumplan  o  no  las
condiciones evaluadas.

Es muy importante no usar comas para separar subexpresiones ni estructuras o valores dentro  de  las
subexpresiones, porque Python las interpreta como una tupla y no las evaluará de manera correcta.

Los operadores de pertenencia siguen la jerarquía de  operadores.  Dentro  de  su  categoría,  todos
tienen la misma precedencia, lo que significa que se evaluarán en el mismo nivel  de  prioridad.  El
orden de evaluación estará determinado por la jerarquía de operadores en el caso de  operadores  con
diferente precedencia, la asociatividad en el caso de los operadores de igual precedencia y  el  uso
de paréntesis con el que podemos forzar el orden de precedencia  y  evaluación.  En  este  caso,  la
asociatividad no se aplica ya que no es posible encadenar operadores de  pertenencia  en  una  misma
expresión.

Cabe destacar que los operadores de pertenencia comparten categoría con los operadores de identidad.
Esto significa que, en presencia de ambos, se evaluarán en el mismo nivel de prioridad y se aplicará
la misma lógica de evaluación.

Además, en ausencia de paréntesis, primero se resuelven las pruebas  de  pertenencia,  luego  "not",
"and" y por último "or". Para forzar un orden distinto o aclarar la intención, debemos encerrar cada
subexpresión entre paréntesis. Esto  es  importante  tenerlo  en  cuenta  al  construir  expresiones
complejas que involucren múltiples operadores.

Por último, en este ejemplo no se muestran las verificaciones con los operadores de  pertenencia  en
las secuencias de bytes, bytearray y memoryview porque estas estructuras son más complejas y aún  no
se han explorado. Sin embargo, los operadores de pertenencia también son aplicables a  ellas  de  la
misma manera que a las otras estructuras de datos mencionadas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────