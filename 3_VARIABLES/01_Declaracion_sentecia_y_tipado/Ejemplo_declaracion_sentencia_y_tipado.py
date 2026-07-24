# Enunciado:
"""Una declaración introduce una variable, como "x". Una sentencia puede  asignar  un  valor  a  esa
variable usando el operador de asignación (=), por ejemplo, "x = 5". Finalmente, el tipado asocia un
tipo de dato al valor asignado. Por ejemplo, si encerramos el valor entre corchetes, como  en  "x  =
[5]", la variable "x" pasa a contener una lista. En Python, las variables tienen tipado dinámico, lo
que significa que no es necesario declarar explícitamente el tipo de dato de una  variable,  ya  que
este queda determinado por el valor o conjunto de valores que le asignamos."""

# Ejemplo_declaracion_sentencia_y_tipado.py

# Explicación:
"""Definimos una variable llamada "x" (declaración) y le asignamos el valor 5 usando el operador  de
asignación (sentencia). Luego, encerramos el valor entre corchetes, [5], para que  la  variable  "x"
pase a contener una lista (tipado). Esto significa que "x" ahora es una lista que contiene un  único
elemento: el número 5. Finalmente, aplicamos la función "type()" a la variable "x" y encerramos  esa
llamada dentro de la función "print()" para  verificar  el  tipo  de  dato  de  la  variable  "x"  e
imprimirlo en la consola."""

# Código:
x = 5           # Declaración y sentencia.
x = [5]         # Tipado.
print(type(x))  # Verificación e impresión del tipo de dato de la variable "x".

# Nota Importante:
"""Es importante destacar que, al asignar un valor a una variable, de  forma  directa  o  indirecta,
determinamos su tipo de dato. Es decir, el tipo de dato del valor asignado será el tipo de dato  que
adopte la variable. En Python, una sentencia puede usarse para asignar  valores  a  variables,  pero
también para ejecutar funciones o dar instrucciones. Es  importante  no  confundir  estos  conceptos
generales con el concepto específico que se explica en este código, que es la asignación directa  de
un valor a una variable."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
