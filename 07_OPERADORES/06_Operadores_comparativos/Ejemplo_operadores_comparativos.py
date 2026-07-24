# Enunciado:
"""Los operadores comparativos en Python son  herramientas  esenciales  que  permiten  comparar  dos
valores y obtener  un  resultado  booleano:  True  o  False.  Los  operadores  son:  igualdad  (==),
desigualdad (!=), mayor que (>), menor que (<), mayor o igual que (>=) y menor o igual que (<=).

Es fundamental no confundir el operador de igualdad (==) con el operador de asignación  simple  (=).
El primero se usa para "comparar" valores, mientras que el segundo  se  utiliza  para  "asignar"  un
valor a una variable.

Estos operadores evalúan relaciones entre valores siempre que la comparación tenga sentido lógico  y
los tipos de datos sean compatibles. Se pueden comparar números, cadenas de texto,  listas,  tuplas,
entre otros. Los resultados de estas comparaciones controlan el flujo del programa y permiten  tomar
decisiones basadas en las condiciones evaluadas.

Los operadores comparativos son esenciales en la programación porque establecen condiciones  lógicas
y permiten realizar evaluaciones. Además, son clave en la toma de decisiones del  programa,  ya  que
controlan el flujo en estructuras como "if",  "while"  o  "for".  También  se  pueden  combinar  con
operadores lógicos como "and", "or" y "not"  para  crear  evaluaciones  más  complejas  y  precisas,
enriqueciendo la lógica y la toma de decisiones en los programas."""

# Ejemplo_operadores_comparativos.py

# Explicación:
"""Definimos dos variables globales "a" y  "b"  y  les  asignamos  los  valores  enteros  10  y  20,
respectivamente. Luego, usamos los diferentes operadores comparativos  para  realizar  comparaciones
entre los valores contenidos en ambas variables, situando  el  respectivo  operador  entre  ellas  y
encerrando cada expresión entre paréntesis.

A continuación, asignamos cada expresión a una variable con un nombre que describe el  propósito  de
la comparación. Por  último,  usamos  la  función  "print()"  para  mostrar  el  resultado  de  cada
comparación en la consola, acompañado de un mensaje descriptivo. Cada comparación devuelve un  valor
booleano que indica si la condición es verdadera (True) o falsa (False)."""

# Código:
a = 10
b = 20

igualdad = (a == b)
print("El resultado de la comparación \"igualdad\" entre a y b es:", igualdad)

desigualdad = (a != b)
print("El resultado de la comparación \"desigualdad\" entre a y b es:", desigualdad)

mayor_que = (a > b)
print("El resultado de la comparación \"mayor que\" entre a y b es:", mayor_que)

menor_que = (a < b)
print("El resultado de la comparación \"menor que\" entre a y b es:", menor_que)

mayor_o_igual = (a >= b)
print("El resultado de la comparación \"mayor o igual que\" entre a y b es:", mayor_o_igual)

menor_o_igual = (a <= b)
print("El resultado de la comparación \"menor o igual que\" entre a y b es:", menor_o_igual)

# Nota Muy Importante:
"""Los operadores de igualdad (==)  y  desigualdad  (!=)  son  versátiles  y  se  pueden  aplicar  a
prácticamente cualquier tipo de dato: cadenas de texto, valores booleanos, listas, tuplas,  números,
e incluso objetos personalizados. Sin embargo, es fundamental recordar que no todos  los  operadores
son intercambiables. Por ejemplo, el operador "menor que" (<) puede no  tener  sentido  al  comparar
estructuras como listas o tuplas, ya que su comportamiento depende del contexto y de  la  definición
de los objetos.

Por ello, es crucial entender cómo y cuándo usar cada operador para evitar errores lógicos y  lograr
un código más robusto. Además, es aconsejable asegurarse de que  los  valores  involucrados  en  las
comparaciones sean compatibles y usar paréntesis para agrupar expresiones y mejorar  la  legibilidad
del código.

Los operadores comparativos siguen la jerarquía de operadores en Python.  Dentro  de  su  categoría,
todos los operadores tienen la misma precedencia, lo que significa que se  evaluarán  con  el  mismo
nivel de prioridad.

El orden de evaluación estará determinado  por  la  jerarquía  de  operadores  en  el  caso  de  los
operadores con diferente precedencia, por la asociatividad en el caso de  los  operadores  de  igual
precedencia y por el uso de paréntesis, con  el  que  podemos  forzar  el  orden  de  precedencia  y
evaluación. En este caso, la asociatividad es de izquierda a derecha.

Por último, es importante destacar que estos operadores tienen una prioridad inferior a  la  de  los
operadores aritméticos. Esto significa que, en una expresión compuesta, las operaciones  aritméticas
se evaluarán antes que las comparaciones, a menos que se utilicen paréntesis para modificar el orden
de precedencia y evaluación, tema que se verá con detalle al estudiar los operadores lógicos."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
