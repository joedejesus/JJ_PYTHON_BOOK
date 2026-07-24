# Enunciado:
"""Define  dos  variables  "a"  y  "b".  Asígnales  los  valores   booleanos   (True)   y   (False),
respectivamente. Luego, realiza tres evaluaciones lógicas utilizando las variables "a" y  "b"  junto
con los operadores "and", "or" y "not" por separado. En cada  caso,  asigna  el  resultado  de  cada
evaluación a una variable con un nombre abreviado y usa la función "print()" para imprimir los  tres
valores de las evaluaciones concatenados con un mensaje descriptivo.

A continuación, define dos variables "c" y "d". Asígnales  una  expresión  aritmética  compleja  que
incluya al menos dos operadores aritméticos,  respectivamente.  Luego,  realiza  tres  comparaciones
utilizando las variables "c" y "d" junto con los operadores (==), (!=) y (>) por separado.  En  cada
caso, asigna el resultado de cada comparación a una variable  con  un  nombre  abreviado  y  usa  la
función "print()" para imprimir los  valores  de  las  comparaciones  concatenados  con  un  mensaje
descriptivo. En todos los casos, usa paréntesis cuando sea necesario y sigue la sintaxis correcta de
Python."""

# Ejercicio_1_operadores_logicos.py

# Explicación:
"""Definimos dos variables llamadas "a" y "b", y  les  asignamos  los  valores  booleanos  (True)  y
(False), respectivamente. Luego, realizamos tres evaluaciones lógicas utilizando las variables "a" y
"b", que contienen los valores booleanos, junto con los operadores lógicos "and", "or" y  "not"  por
separado.

En los dos primeros casos, colocamos el operador correspondiente "and" y "or" entre los dos valores,
los cuales encerramos entre paréntesis. Para el tercer caso, colocamos el operador "not"  antes  del
valor que queremos negar, encerrando este entre paréntesis. Asignamos el valor de cada evaluación  a
una variable con un nombre abreviado, en este  caso  "e_1",  "e_2"  y  "e_3",  respectivamente.  Por
último, usamos la función "print()" para imprimir los valores de las tres evaluaciones  concatenados
con un mensaje descriptivo. Los resultados son (False), (True) y (False), respectivamente."""

# Código:
a = True
b = False

e_1 = (a) and (b)
e_2 = (a) or (b)
e_3 = not (a)

print("El resultado de las tres evaluaciones es:", e_1, e_2, e_3)

# Explicación:
"""Definimos dos variables llamadas "c" y "d" y  les  asignamos  el  resultado  de  dos  operaciones
aritméticas, respectivamente. En cada caso,  utilizamos  varios  operadores  aritméticos  además  de
paréntesis para encerrar las subexpresiones y asegurarnos de que se realicen en el  orden  correcto.
Luego, realizamos tres comparaciones utilizando las variables "c" y "d", que contienen  los  valores
numéricos, junto con los operadores comparativos (==), (!=) y (>) por separado.

Colocamos el operador correspondiente entre los dos valores  y  encerramos  cada  comparación  entre
paréntesis. Asignamos el valor de cada comparación a una variable con un nombre abreviado,  en  este
caso "c_1", "c_2" y "c_3", respectivamente. Por último, usamos la función  "print()"  para  imprimir
los valores de las tres comparaciones concatenados con un mensaje descriptivo.  Los  resultados  son
(False), (True) y (True), respectivamente."""

# Código:
c = (10 + 5) + (3 ** 9) / 2
d = (8 * 2) - (4 ** 2) + 10

c_1 = (c == d)
c_2 = (c != d)
c_3 = (c > d)

print("El resultado de las tres comparaciones es:", c_1, c_2, c_3)

# Nota Importante:
"""Es crucial no confundir el concepto de "evaluación" con el concepto de "comparación". El  primero
se utiliza para los operadores lógicos y el segundo para los comparativos, aunque en ambos casos  se
obtiene un resultado booleano mediante una evaluación, ya sea lógica o comparativa."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ───────────────────────────────────────────────────────────