# Enunciado:
"""La construcción de tipos de datos es el proceso mediante el cual se crean y definen los tipos  de
datos básicos en un lenguaje de  programación  para  almacenarlos  en  variables.  Este  proceso  es
fundamental en el desarrollo de software, ya que manipular información de manera  efectiva  requiere
comprender cómo se representan, organizan y gestionan los diferentes tipos de datos.

Para ello, se utilizan constructores que permiten definir variables capaces de almacenar valores  de
distintos tipos o clases. Los constructores permiten instanciar o crear objetos de estas clases,  es
decir, crear instancias u objetos concretos de tipos de datos específicos.

En Python, los  tipos  de  datos  básicos  incluyen  números  enteros,  números  flotantes,  números
complejos, booleanos, cadenas de texto, listas, tuplas, rangos, conjuntos,  conjuntos  inmutables  y
diccionarios. Cada uno de estos tipos tiene su propio constructor: "int()", "float()",  "complex()",
"bool()",  "str()",   "list()",   "tuple()",   "range()",   "set()",   "frozenset()"   y   "dict()",
respectivamente.

Además, cada tipo de dato básico tiene sus  propias  características  y  usos  específicos,  lo  que
permite elegir la estructura más adecuada para  almacenar  y  manipular  la  información  según  las
necesidades del programa. Estos tipos de datos básicos  son  esenciales  para  realizar  operaciones
matemáticas, manipular texto y controlar el flujo de un programa, entre otras tareas comunes  de  la
programación."""

# Ejemplo_construccion_de_tipos_de_datos_basicos.py

# Explicación:
"""Definimos varias variables, cada una con un nombre que representa el tipo de dato  que  almacena.
En cada caso, asignamos un valor específico a la variable. Esto se logra utilizando  el  constructor
correspondiente para cada tipo de dato, pasándole el valor como  argumento  entre  paréntesis  ()  y
siguiendo la sintaxis de Python para cada tipo de dato.

Por último, imprimimos el  valor  de  cada  variable  en  consola  usando  la  función  "print()"  y
concatenamos un mensaje descriptivo para identificar el tipo de dato que se está mostrando."""

# Código:
numero_entero = int(42)
print("Número entero:", numero_entero)

numero_flotante = float(3.14)
print("Número flotante:", numero_flotante)

numero_complejo = complex(2 + 3j)
print("Número complejo:", numero_complejo)

booleano = bool(True)
print("Booleano:", booleano)

texto = str("Hola, mundo")
print("Texto:", texto)

lista = list([1, 2, 3])
print("Lista:", lista)

tupla = tuple((4, 5, 6))
print("Tupla:", tupla)

rango = range(10)
print("Rango:", rango)

conjunto = set({1, 2, 3})
print("Conjunto:", conjunto)

Conjunto_inmutable = frozenset({4, 5, 6})
print("Conjunto inmutable:", Conjunto_inmutable)

diccionario = dict({"clave": "valor"})
print("Diccionario:", diccionario)

# Nota Importante:
"""En este caso, usamos los constructores de tipos de datos básicos  para  mostrar  cómo  se  pueden
crear variables que almacenan los diferentes tipos de datos  básicos  en  Python.  Sin  embargo,  es
importante destacar que en Python no es  necesario  usar  estos  constructores  explícitamente  para
definir variables, ya que Python es un lenguaje de tipado dinámico.

Esto significa que no es necesario especificar explícitamente  el  tipo  de  dato  al  declarar  una
variable, porque el intérprete de Python infiere el tipo de  dato  automáticamente  según  el  valor
asignado a la variable. Esto proporciona una mayor flexibilidad en  la  programación,  pero  también
requiere que los programadores sean cuidadosos al manejar los tipos de  datos  para  evitar  errores
inesperados durante la ejecución del código."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
