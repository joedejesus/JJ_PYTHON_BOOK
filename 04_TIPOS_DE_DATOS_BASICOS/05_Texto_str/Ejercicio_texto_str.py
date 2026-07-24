# Enunciado:
"""Define dos variables: una de tipo texto (str) llamada  "nombre"  y  otra  de  tipo  entero  (int)
llamada "edad". Asigna los valores "Joe" y 33, respectivamente. Luego, utiliza la función  "print()"
para concatenar el texto y las variables, y muestra un mensaje de saludo que incluya el nombre y  la
edad como una cadena de texto coherente."""

# Ejercicio_texto_str.py

# Explicación:
"""Definimos dos variables: una de tipo texto (str) llamada "nombre" y otra  de  tipo  entero  (int)
llamada "edad". Asignamos los valores "Joe" y 33,  respectivamente.  Posteriormente,  imprimimos  un
mensaje de saludo utilizando la función "print()"  que  incluye  las  variables  "nombre"  y  "edad"
concatenadas con las cadenas "Hola", "tienes" y "años".

Utilizamos el signo de suma (+) para concatenar las variables y el texto, colocando cada  cadena  de
texto entre comillas dobles. Además, convertimos la variable "edad" a  cadena  de  texto  usando  el
constructor "str()", porque el operador (+) no puede concatenar un número entero con una  cadena  de
texto, ya que son tipos de datos diferentes. El resultado será: Hola Joe, tienes 33 años."""
   
# Código:
nombre = "Joe"
edad = 33

print("Hola " + nombre + ", tienes " + str(edad) + " años.")

# Nota Muy Importante:
"""Dado que la variable "edad" tiene un valor de tipo entero (int), necesitas convertirla  a  cadena
(str) usando el constructor "str()" para poder concatenarla. De lo contrario, se generará  un  error
de tipo de dato.

Este aspecto se aborda en la sección  correspondiente  a  "Texto  (str)".  Es  importante  notar  la
separación entre las comillas y el texto que encierran para que la salida sea  legible  y  correcta.
Además, debemos seguir las normas de sintaxis del idioma español, ya que este mensaje será  mostrado
al lector o usuario (código externo). El formato correcto a seguir en este caso  es:  ("cadena  "  +
variable + ", cadena " + variable + "cadena.")."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
