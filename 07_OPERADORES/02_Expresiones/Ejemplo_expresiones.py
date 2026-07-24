# Enunciado:
"""En Python, las expresiones son combinaciones de valores, variables, operadores o funciones que se
evalúan para producir un resultado. Este resultado puede ser numérico,  booleano,  texto  o  incluso
fragmentos extraídos mediante indexación. Las expresiones son fundamentales para realizar  cálculos,
comparaciones y manipular datos.

Además de las expresiones fundamentales  que  emplean  operadores  aritméticos,  de  asignación,  de
comparación, lógicos, de pertenencia, de identidad y de indexación, existen otras expresiones,  como
las concatenaciones con comas o con el signo de suma (+), las interpolaciones con "f-strings"  o  el
desempaquetado de listas y tuplas, entre otras. Aunque  no  siempre  se  consideran  en  el  sentido
matemático o lógico estricto, estas también son expresiones válidas en Python."""

# Ejemplo_expresiones.py

# Explicación:
"""Definimos dos variables globales, "a" y "b", y les asignamos valores enteros.  También  definimos
una variable llamada "lista", a la que asignamos una secuencia numérica en forma  de  lista.  Luego,
creamos varias expresiones usando las variables globales definidas, en las que se combinan valores y
uno o más operadores.

En cada caso, encerramos la expresión entre paréntesis y guardamos el resultado en una variable  con
un nombre descriptivo. Finalmente, usamos la función "print()" para mostrar  el  resultado  de  cada
expresión, acompañado de un mensaje que describe su tipo y su representación."""

# Código:
a = 15
b = 4

lista = [1, 2, 3, 4, 5]

suma = (a + b)
print("Suma =", suma)

a %= (2)
print("Módulo (15 % 2) =", a)

comparacion = (a > b)
print("Comparación (a > b) =", comparacion)

comparacion_logica = ((a > 0) and (b > 0))
print("Comparación lógica ((a > 0) and (b > 0)) =", comparacion_logica)

verificacion_de_pertenencia = (3 in lista)
print("Verificación de pertenencia (3 in lista) =", verificacion_de_pertenencia)

verificacion_de_identidad = (a is not b)
print("Verificación de identidad (a is not b) =", verificacion_de_identidad)

indexacion = lista[2:]
print("Indexación (lista[2:]) =", indexacion)

# Nota Importante:
"""Es fundamental respetar la jerarquía de los operadores, su sintaxis y  el  uso  correcto  de  los
paréntesis para evitar errores en los resultados. Las expresiones en Python  no  se  limitan  a  los
operadores aritméticos, sino que también abarcan operadores de asignación, de comparación,  lógicos,
de pertenencia, de identidad y de indexación.

Además, las expresiones condicionales, entre otras, también  forman  parte  de  las  expresiones  en
Python, ya que  permiten  evaluar  condiciones  y  devolver  valores  en  función  de  ellas.  Estas
herramientas ofrecen una forma compacta  y  elegante  de  escribir  código,  aunque,  por  su  mayor
complejidad, se abordan en sus respectivas secciones.

Cada operación se asocia a un tipo  específico  de  operador,  y  cada  expresión  realiza  acciones
distintas,  como  suma,  módulo,  comparación,  comparación  lógica,  verificación  de  pertenencia,
verificación de identidad e indexación. Al evaluarse, las expresiones devuelven un  valor  según  el
tipo de operación realizada."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
