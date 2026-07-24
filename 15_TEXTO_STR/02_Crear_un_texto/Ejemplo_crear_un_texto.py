# Enunciado:
"""La forma más común de crear un texto en Python es utilizando comillas simples ('  ')  o  comillas
dobles (" "). Ambas formas son válidas y  se  pueden  usar  indistintamente,  aunque  es  importante
mantener la consistencia en su uso dentro de un mismo proyecto.

Esto hace que el código sea más legible y menos propenso a errores. Además, el uso adecuado  de  las
comillas facilita la colaboración en los proyectos, ya que mantiene un estándar claro para todos los
desarrolladores involucrados."""

# Ejemplo_crear_un_texto.py

# Explicación:
"""Definimos una variable llamada "texto_1" y le asignamos el valor 'Hola mundo' utilizando comillas
simples. Luego, definimos otra variable llamada "texto_2" y le asignamos el mismo  valor  utilizando
comillas dobles. Finalmente, utilizamos la función "print()" para mostrar los textos en la  consola,
acompañados de un mensaje en formato "f-string" que indica el tipo de comillas utilizadas para  cada
texto. En este caso, en ninguna de las salidas de la consola se mostrarán las comillas,  ya  que  el
texto en Python se representa sin ellas, a  menos  que  se  incluyan  explícitamente  en  el  propio
texto."""

# Código:
texto_1 = 'Hola mundo'
print(f"Este es el texto con comillas simples: {texto_1}")

texto_2 = "Hola mundo"
print(f"Este es el texto con comillas dobles: {texto_2}")

# Nota Importante:
"""Es recomendable mantener la consistencia en el uso de comillas dentro de un mismo proyecto.  Esto
significa elegir un estilo predominante, ya sea de comillas simples o dobles, y mantenerlo  en  todo
el código. Si el texto contiene una comilla simple, como en el caso de una contracción (por ejemplo,
"I'm"), es mejor usar comillas dobles para evitar errores de sintaxis.

De igual forma, si el texto contiene comillas dobles, como en una cita  textual  (por  ejemplo,  'Él
dijo: "Hola"'), es preferible usar comillas simples. Este enfoque no solo previene errores, sino que
también mejora la claridad y la legibilidad del código."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
