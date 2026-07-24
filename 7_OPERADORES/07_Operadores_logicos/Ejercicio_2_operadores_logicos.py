# Enunciado:
"""Define  todas  las  variables  del  ejercicio  anterior  y  asígnales   sus   valores   booleanos
correspondientes. Representa estos valores booleanos en una tabla de  resultados,  donde  cada  fila
contenga el nombre de la variable y, a su derecha, el valor correspondiente. Para  crear  la  tabla,
usa el mismo formato que se utiliza para la tabla de verdad.

Usa la tabla de resultados para realizar una evaluación lógica compleja  utilizando  los  operadores
"and", "or" y "not", combinados con las variables de la tabla de resultados. Asegúrate de no repetir
ninguna de las variables y utilízalas todas. Usa el operador "not" para invertir  el  valor  de  dos
subexpresiones situadas a su derecha, sin negar toda la evaluación.

Además, incluye los valores literales (True) y (False) para enriquecer la evaluación. En  todos  los
casos, usa paréntesis para agrupar las subexpresiones de manera clara, así como para  encerrar  cada
valor que  lo  requiera.  Guarda  el  resultado  en  una  variable  llamada  "evaluacion_final"  sin
imprimirlo. Este debe ser (False).

Por último, utilizando la tabla de verdad que se muestra a  continuación,  descompón  y  analiza  la
evaluación lógica compleja como comentario en formato de tabla para predecir la salida esperada.  La
tabla debe contener el orden de evaluación, la subexpresión evaluada y, en cada  caso,  el  operador
usado y los operadores que aún no se han utilizado. Para crear la tabla, usa el mismo formato que se
utiliza para la tabla de verdad.

La tabla de verdad es la siguiente:

|---------|---------|---------|---------|--------|
| Valor X | Valor Y | X and Y | X or Y  | not X  |
|---------|---------|---------|---------|--------|
| True    | True    | True    | True    | False  |
| True    | False   | False   | True    | False  |
| False   | True    | False   | True    | True   |
| False   | False   | False   | False   | True   |
|---------|---------|---------|---------|--------|"""

# Ejercicio_2_operadores_logicos.py

# Explicación:
"""Definimos todas las variables del ejercicio  anterior  y  les  asignamos  sus  valores  booleanos
correspondientes."""

# Código:
e_1 = False
e_2 = True
e_3 = False

c_1 = False
c_2 = True
c_3 = True

# Explicación:
"""Representamos estos valores booleanos en una tabla de  resultados.  En  cada  fila,  añadimos  el
nombre de la variable y, a su derecha, el valor  booleano  correspondiente.  Para  crear  la  tabla,
utilizamos el mismo formato de la tabla de verdad. Esto se logra organizando los datos  en  filas  y
columnas, delimitadas con los signos (|) y (-).

La tabla de resultados es la siguiente:     

|----------|-------|----------|-------|
| Variable | Valor | Variable | Valor |
|----------|-------|----------|-------|
| e_1      | False | c_1      | False |
| e_2      | True  | c_2      | True  |
| e_3      | False | c_3      | True  |
|----------|-------|----------|-------|"""

# Explicación:
"""Definimos una variable llamada "evaluacion_final" y le asignamos el resultado de  una  evaluación
lógica compleja que contiene los operadores lógicos, las variables de la tabla de resultados  y  los
valores literales (True) y (False). Creamos la evaluación lógica siguiendo los parámetros  indicados
en el enunciado, usando paréntesis para agrupar los valores  dentro  de  las  subexpresiones  y  las
subexpresiones dentro de la evaluación lógica.

Además, definimos otra variable llamada "orientacion_final" y le asignamos el resultado de la  misma
evaluación lógica, intercambiando los nombres de las variables por su valor booleano correspondiente
en la tabla. De esta forma, facilitamos la descomposición y el análisis posterior de  la  evaluación
lógica."""

# Código:
evaluacion_final = ((e_1) and (c_1)) or ((e_2) or (c_2)) and not ((e_3) or (c_3)) and not ((True) and (False))

orientacion_final = ((False) and (False)) or ((True) or (True)) and not ((False) or (True)) and not ((True) and (False))

# Explicación:
"""Para realizar el análisis y descomposición de la evaluación lógica como comentario en formato  de
tabla, primero descomponemos la evaluación en subexpresiones y evaluamos cada una de  ellas  paso  a
paso. Ya que hemos intercambiado los nombres de las variables por su  valor  correspondiente  en  la
tabla, realizamos la descomposición y el análisis de la evaluación guiándonos por la tabla de verdad
y por la variable "orientacion_final" de la siguiente manera:

orientacion_final = ((False) and (False)) or ((True) or (True)) and not ((False) or (True)) and not ((True) and (False))
-----------------------------------------(1)--------------------(1)-------------------------(2)-------------------------

|------|--------------------------|-----------|----------------|-------------------|
| Paso | Subexpresión             | Resultado | Operador usado | Operador sin usar |
|------|--------------------------|-----------|----------------|-------------------|
| 1º   | ((False) and (False))    | False     | and            | or  (1)           |
| 2º   | ((True) or (True))       | True      | or             | and (1)           |
| 3º   | not ((False) or (True))  | False     | not y or       | and (2)           |
| 4º   | not ((True) and (False)) | True      | not y and      |                   |
|------|--------------------------|-----------|----------------|-------------------|"""

# Explicación:
"""Tomamos los cuatro resultados booleanos obtenidos en la tabla anterior. Empezando por arriba, los
combinamos con los operadores sin usar respetando la precedencia lógica de la expresión original. En
cada caso, colocamos el operador correspondiente entre los dos valores y encerramos cada valor entre
paréntesis.

|------|--------------------|-----------|----------------|-------------------|
| Paso | Subexpresión       | Resultado | Operador usado | Operador sin usar |
|------|--------------------|-----------|----------------|-------------------|
| 5º   | (True) and (False) | False     | and (1)        | or  (1) and (2)   |
| 6º   | (False) and (True) | False     | and (2)        | or  (1)           |
|------|--------------------|-----------|----------------|-------------------|"""

# Explicación:
"""Finalmente, combinamos los resultados de las dos últimas subexpresiones colocando el operador sin
usar entre los dos valores y encerrando estos entre paréntesis. Esto produce el resultado  final  de
la evaluación, el cual es: (False)

|------|--------------------|-----------|----------------|-------------------|
| Paso | Subexpresión       | Resultado | Operador usado | Operador sin usar |
|------|--------------------|-----------|----------------|-------------------|
| 7º   | (False) or (False) | False     | or  (1)        |                   |
|------|--------------------|-----------|----------------|-------------------|"""

# Nota Muy Importante:
"""El orden de precedencia de los operadores lógicos dentro de su categoría es: (not, and y or).  En
este caso, la evaluación se realiza de manera secuencial, priorizando siempre los  paréntesis  ()  y
luego la precedencia de los operadores lógicos. Esto demuestra cómo el  uso  de  paréntesis  permite
controlar el orden de evaluación y la precedencia de los operadores  lógicos,  ya  sea  con  valores
booleanos o cualquier otro tipo de dato.

En realidad, en la expresión, el operador "or" se evalúa al final debido a su precedencia  más  baja
respecto al operador "and". Representamos las subexpresiones de izquierda  a  derecha  para  que  el
lector pueda seguir mejor la lógica de la evaluación,  pero  el  orden  real  de  evaluación  es  el
siguiente:

Después del paso 4º, la expresión queda como: (False) or (True) and (False) and (True). En  el  paso
5º evaluamos la primera operación con "and": (True) and (False), obteniendo (False). En el  paso  6º
evaluamos la siguiente operación con "and": (False) and (True), obteniendo nuevamente (False). En el
paso 7º evaluamos con el operador "or" el valor (False) reservado  de  la  izquierda  con  el  valor
obtenido anteriormente, quedando (False) or (False) = (False).

En este código, usamos  los  términos  "evaluación  lógica"  o  "evaluación  lógica  compleja"  para
referirnos al proceso global de evaluación, y también como sinónimo de "expresión lógica". Por  otro
lado, cuando decimos "subexpresión", nos referimos a una "subevaluación" o "evaluación" más pequeña.
Por lo tanto, los términos "evaluación" y "expresión" son intercambiables, pero  debe  quedar  claro
que realizamos una evaluación lógica que se expresa a través de estas subexpresiones  para  producir
un resultado final.

Además, el uso de paréntesis no solo afecta el orden de precedencia y evaluación, sino  que  también
mejora la legibilidad del código, haciendo más claras las  intenciones  del  programador.  Por  esta
razón, tanto en la "evaluación final" como en el apartado de la tabla  "subexpresiones",  encerramos
cada valor y subexpresión entre paréntesis. De este modo, cuando realizamos la  evaluación  interna,
el resultado obtenido también  queda  encerrado  entre  paréntesis,  lo  que  facilita  su  correcta
evaluación en el siguiente paso. El uso de paréntesis es, por tanto, una  herramienta  valiosa  para
clarificar la lógica del código.

Por último, es importante recordar que el operador "not" siempre debe estar fuera de los paréntesis,
incluso si aparece después de un "and" o un "or", ya que invierte el valor de la expresión situada a
su derecha antes de evaluarla. Tras realizar la negación, el flujo  de  ejecución  continúa  con  el
operador "and" u "or" que lo rodee. Aunque las combinaciones "and not" y  "or  not"  puedan  parecer
ilógicas, son válidas y bastante comunes en programación."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
