# Enunciado:
"""NoneType es un tipo de dato en Python que representa la ausencia de valor. Se utiliza cuando  una
variable no contiene ningún valor asignado o cuando  se  le  asigna  explícitamente  el  valor  nulo
"None". Es común en funciones, donde "None" puede devolverse para indicar que no  hay  un  resultado
específico.

Esto  permite  controlar  mejor  el  flujo  del  programa  y  asegura  que  la  función  se  ejecute
correctamente, incluso si no se le pasa un valor explícito, evitando errores de ejecución.  Es  útil
para manejar errores y desarrollar funciones más flexibles y robustas."""

# Ejemplo_nonetype.py

# Explicación:
"""Definimos una variable llamada "tipo" y le asignamos el valor "None". Luego, aplicamos la función
"type()" a la variable "tipo" para verificar su tipo de dato y guardamos el resultado en la variable
"verificamos". Finalmente, imprimimos el valor de la variable "verificamos"  utilizando  la  función
"print()" para ver el resultado en la consola. El resultado será <class 'NoneType'>."""

# Código:
tipo = None               # Asignamos el valor "None" a la variable "tipo".
verificamos = type(tipo)  # Aplicamos la función "type()" a la variable "tipo" para verificar su tipo de dato.
print(verificamos)        # Imprimimos el resultado de la verificación en la consola.

# Nota Importante:
"""Uno de los usos más comunes de "None" en Python es definir una variable sin  asignarle  un  valor
específico. Esto resulta especialmente útil  cuando  una  función  espera  recibir  un  parámetro  o
argumento que podría no estar disponible. En esos casos, usamos "None" para  asignar  explícitamente
un valor nulo, lo que permite que la función y el programa se ejecuten sin errores.

Esto garantiza que la función se ejecute correctamente,  incluso  si  no  se  proporciona  un  valor
explícito, y  evita  posibles  errores  de  ejecución.  Recuerda  que  "None"  se  escribe  con  "N"
mayúscula."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────