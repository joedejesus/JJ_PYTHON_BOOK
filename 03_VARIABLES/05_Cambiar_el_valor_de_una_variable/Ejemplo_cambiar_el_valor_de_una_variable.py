# Enunciado:
"""Cambiar el valor de una variable en Python es sencillo. Solo necesitas asignar un nuevo  valor  a
la variable existente. Esto reemplaza el valor anterior de  la  variable  por  el  nuevo  valor  que
asignes. Si asignas un valor de un tipo de dato diferente, también cambiará el tipo de  dato  de  la
variable. Esto es útil para actualizar el valor de una  variable  en  tu  programa.  Además,  puedes
modificar el tipo de dato de la variable al asignarle un nuevo valor de un tipo de dato distinto."""

# Ejemplo_cambiar_el_valor_de_una_variable.py

# Explicación:
"""Definimos una variable llamada "x", le asignamos el valor 5 y  mostramos  su  valor  mediante  la
función "print()"."""

# Código:
x = 5  # (int)
print(x)

# Explicación:
"""Asignamos un nuevo valor a la variable "x", cambiándolo a 10, y mostramos su nuevo valor mediante
la función "print()"."""

# Código:
x = 10  # (int)
print(x)

# Explicación:
"""Asignamos un nuevo valor a la variable "x", cambiándolo a "15". Esto también modifica su tipo  de
dato a cadena de texto (str) porque el valor está entre comillas. Mostramos el  nuevo  valor  de  la
variable "x" mediante la función "print()". Luego, mostramos su tipo de dato  aplicando  la  función
"type()" a la variable "x". Encerramos la llamada  a  la  función  "type()"  dentro  de  la  función
"print()" para mostrar el tipo de dato de la variable. Ahora el tipo de  dato  es  cadena  de  texto
(str) y no entero (int), como antes."""

# Código:
x = "15"  # (str)
print(x)
print(type(x))  # Verificamos el tipo de dato de la variable "x".

# Nota Muy Importante:
"""Ten en cuenta que, al asignar un nuevo valor a una variable, el valor anterior se pierde. En este
caso, el valor 5 se pierde al asignar el nuevo valor 10 a la variable "x". De igual manera, el valor
10 se pierde al asignar el nuevo valor "15" a la misma variable. A partir  de  la  última  línea  de
código, siempre que mostremos la variable "x", obtendremos el valor "15" y  su  tipo  de  dato  será
cadena de texto (str). Esto ocurre porque, en Python, las variables son  referencias  a  objetos  en
memoria. Al cambiar el valor de una variable, se crea una nueva referencia  a  un  nuevo  objeto  en
memoria, mientras que el objeto anterior queda sin referencia y, eventualmente, será recolectado por
el recolector de basura de Python si no hay otras referencias a él.

Por lo tanto, es importante tener cuidado al cambiar el valor de una  variable,  ya  que  no  podrás
recuperar el valor anterior, a menos que lo hayas guardado previamente en otra variable o  en  algún
otro lugar. Esto se demuestra en el ejercicio correspondiente a esta lección."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────