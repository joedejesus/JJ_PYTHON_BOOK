# Enunciado:
"""Define dos variables y asígnales, respectivamente, una estructura iterable. Los  nombres  de  las
variables deben describir el tipo de estructura contenida en ellas.

Luego, realiza dos verificaciones compuestas utilizando, en un caso, el operador de pertenencia "in"
y, en el otro caso, el operador de pertenencia "not in". En  ambos  casos,  usa  las  dos  variables
definidas anteriormente y combínalas con al menos dos valores o estructuras literales, empleando los
operadores lógicos "and" y "or" según corresponda.

En una de las verificaciones, el elemento debe estar presente en todas las estructuras, y  en  otra,
el elemento solo debe estar presente en dos de las estructuras. Este elemento  debe  ser  el  número
"7". Además, un resultado debe ser (True) y  el  otro  (False).  Usa  paréntesis  para  obtener  los
resultados esperados e imprime el resultado en la consola concatenado con un mensaje descriptivo."""

# Ejercicio_operadores_de_pertenencia.py

# Explicación:
"""Definimos dos variables con  nombres  descriptivos  y  les  asignamos  una  lista  y  una  tupla,
respectivamente.  Luego,  realizamos  dos  verificaciones  compuestas   siguiendo   los   parámetros
establecidos en el enunciado y respetando la sintaxis de Python para cada tipo de dato.

En el primer caso, usamos el operador de pertenencia "in" junto  con  las  dos  variables  definidas
anteriormente y con una lista y un diccionario literales, utilizando los operadores lógicos "and"  y
"or" para enlazar las verificaciones de pertenencia, además de paréntesis para separarlas entre sí.

Primero verificamos si "7" está entre los elementos de la lista y  la  tupla,  lo  cual  es  (True).
Después verificamos si "7" está entre los elementos  de  la  lista  literal  o  en  las  claves  del
diccionario literal, lo cual es (True). Por lo tanto, la verificación 1 es (True), ya que (True) and
(True) = True.

En el segundo caso, usamos el operador de pertenencia "not in" junto con las dos variables definidas
anteriormente y con una tupla y un conjunto literales, utilizando los  operadores  lógicos  "and"  y
"or" para enlazar las verificaciones de pertenencia, además de paréntesis para separarlas entre sí.

Primero verificamos si "7" no está entre los elementos de la lista y la tupla literal,  lo  cual  es
(False). Después verificamos si "7" no está entre los elementos de la tupla y el  conjunto  literal,
lo cual es (False). Por lo tanto, la verificación 2 es (False), ya que (False) or (False) = False.

En ambos casos,  utilizamos  la  función  "print()"  para  mostrar  los  resultados  en  la  consola
acompañados de un mensaje descriptivo."""

# Código:
lista_numeros = [1, 3, 5, 7, 9]
tupla_numeros = (2, 4, 6, 7, 8)

verificacion_1 = (7 in lista_numeros and 7 in tupla_numeros) and (7 in [7, 8, 9, 10, 11, 12] or 7 in {7: 7, 8: 8, 9: 9})
print("El número 7 está presente en todas las estructuras:", verificacion_1)

verificacion_2 = (7 not in lista_numeros and 7 not in (10, 11, 12)) or (7 not in tupla_numeros and 7 not in {1, 2, 3, 4, 5})
print("El número 7 está presente en dos estructuras pero no en todas:", verificacion_2)

# Nota Importante:
"""Este ejemplo muestra cómo, al combinar operadores de pertenencia con operadores lógicos,  primero
se evalúan las  verificaciones  de  pertenencia  y  luego  las  expresiones  lógicas,  siguiendo  la
precedencia de los operadores lógicos: "not", "and", "or". Dado que los  operadores  lógicos  tienen
menor precedencia, el uso de paréntesis permite controlar el orden de evaluación. De esta forma,  es
posible evaluar la pertenencia en diferentes contextos y estructuras de datos al mismo tiempo.

Es recomendable referenciar explícitamente el elemento a verificar en cada una  de  las  condiciones
para evitar errores de lógica. Cuando enlazamos dos verificaciones  de  pertenencia  con  operadores
lógicos, es importante usar paréntesis para agrupar las condiciones de manera adecuada, ya  que  los
paréntesis determinan el orden de evaluación.

Cabe aclarar que cada verificación consta de  dos  partes.  En  la  primera  obtenemos  dos  valores
booleanos, los cuales se evalúan para obtener uno solo. En la  segunda  parte  obtenemos  otros  dos
valores, los cuales se evalúan para obtener uno solo, y finalmente esos dos valores se  evalúan  con
el operador  que  se  sitúa  fuera  de  los  paréntesis  para  obtener  el  resultado  final  de  la
verificación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────