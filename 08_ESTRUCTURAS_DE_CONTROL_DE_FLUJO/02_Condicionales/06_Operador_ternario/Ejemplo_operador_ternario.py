# Enunciado:
"""El operador ternario en Python, también conocido  como  "expresión  condicional",  es  una  forma
abreviada de escribir una estructura "if...else" simple. Introducido en la versión  2.5  de  Python,
este operador permite evaluar una condición y devolver un valor dependiendo de si  la  condición  es
verdadera o falsa, todo en una sola línea de código.

Su  sintaxis  es:  x  =  <valor/expresión  si  la  condición  es  verdadera>  if  <condición>   else
<valor/expresión si la condición es falsa>.  El  valor  puede  ser  cualquier  literal,  variable  o
expresión válida en Python. Si el valor es una expresión, se evalúa y retorna su resultado; si es un
valor literal o variable, se retorna tal cual.

El operador ternario evalúa primero la condición y  luego  selecciona  uno  de  los  dos  valores  o
expresiones, siguiendo un orden de evaluación de izquierda a  derecha  y  devolviendo  el  resultado
correspondiente. Este operador resulta especialmente útil para simplificar el código, haciéndolo más
legible y compacto, siempre que la lógica sea sencilla. Por ejemplo, si queremos determinar un valor
en función de una  condición,  podemos  usar  este  operador  en  lugar  de  un  bloque  "if...else"
tradicional.

Por último, el operador ternario es ideal para casos en los que se necesita una  decisión  rápida  y
directa. Sin embargo, es importante no abusar de él en situaciones donde la legibilidad pueda  verse
comprometida, como en condiciones complejas o anidadas.  En  tales  casos,  es  preferible  utilizar
estructuras condicionales tradicionales para mantener la claridad del código. Además, este  operador
puede utilizarse dentro de funciones como "print()" o en cadenas "f-strings"  para  generar  salidas
formateadas, lo que añade versatilidad a su uso en diferentes contextos de programación."""

# Ejemplo_operador_ternario.py     

# Explicación:
"""Definimos una variable llamada "edad" y le asignamos un valor numérico, en este caso  20.  Luego,
utilizamos el operador ternario para evaluar si la edad es mayor o igual a 18. Para ello,  definimos
una variable llamada "operador_ternario" y le asignamos una expresión con  operador  ternario  entre
paréntesis (), que consta de: el valor a devolver si la  condición  es  verdadera  ("Eres  mayor  de
edad"), el condicional "if", la condición (edad >= 18), el condicional  "else"  y,  por  último,  el
valor a devolver si la condición es falsa ("Eres menor de edad"). Por último, imprimimos el valor de
la variable utilizando la función "print()", acompañado de un mensaje que contiene el  resultado  de
la evaluación.

También mostramos cómo usar el operador ternario directamente dentro de  una  función  "print()"  en
formato "f-string" para generar una salida formateada sin necesidad de almacenar el resultado en una
variable.

Para ello, utilizamos la función "print()" en formato "f-string" que contiene el  operador  ternario
en su interior. El operador ternario consta de las mismas  partes:  el  valor  si  la  condición  es
verdadera, el condicional "if", la condición, el condicional "else" y, por último, el  valor  si  la
condición es falsa.

Además, incluimos la "f" al principio de la cadena para indicar que es  una  "f-string"  y  de  esta
forma permitir la evaluación de expresiones  dentro  de  la  cadena.  En  este  caso,  no  se  están
utilizando llaves {}  porque  la  expresión  condicional  ocupa  toda  la  cadena  y  esta  se  pasa
directamente como argumento a la función "print()".

En los dos casos, la salida en consola será el  valor  asociado  al  condicional  "if",  ya  que  la
condición (edad >= 18) se cumple. En este caso, el valor es "Eres mayor de edad"."""

# Código:
edad = 20

operador_ternario = ("Eres mayor de edad" if edad >= 18 else "Eres menor de edad")
print("Este es el resultado de la evaluación con el operador ternario:", operador_ternario)

print(f"Eres mayor de edad" if edad >= 18 else "Eres menor de edad")

# Nota Importante:     
"""El operador ternario en Python evalúa la condición y, a continuación, selecciona el  valor  o  la
expresión correspondiente si la condición es verdadera o, en caso contrario, el valor o la expresión
correspondiente si es falsa.  Esto  significa  que  solo  se  evalúa  una  de  las  dos  expresiones
resultantes. Esto es similar al cortocircuito en operaciones lógicas y también ocurre en estructuras
condicionales tradicionales. Esto puede ser útil para evitar  cálculos  innecesarios  o  errores  en
expresiones no evaluadas.

Las expresiones dentro del operador ternario pueden  ser  cualquier  tipo  de  expresión  válida  en
Python, incluyendo llamadas  a  funciones,  operaciones  matemáticas  o  incluso  otras  expresiones
condicionales. Sin embargo, es importante asegurarse  de  que  las  expresiones  sean  claras  y  no
demasiado complejas para mantener la legibilidad del código.

Además, el uso de "f-strings" permite incluir variables y expresiones directamente dentro de cadenas
de texto, facilitando la creación de mensajes dinámicos, aunque en este  caso  no  es  estrictamente
necesario utilizar una "f-string", ya  que  el  operador  ternario  se  evalúa  como  una  expresión
independiente y bastaría con una simple instrucción "print()".

Por último, es importante tener en cuenta que el operador ternario no admite el uso del  condicional
"elif", ya que está diseñado para manejar únicamente una  condición  con  dos  posibles  resultados.
Aunque el operador ternario es útil para simplificar el código en casos de lógica  sencilla,  no  se
recomienda su uso en condiciones complejas o anidadas, ya que puede dificultar  la  legibilidad  del
código. En estos casos, es preferible utilizar estructuras tradicionales como "if...else"."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
