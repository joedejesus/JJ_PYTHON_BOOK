# Enunciado:
"""El tipo de dato texto (str) es esencial en Python para representar información textual. Se define
como una secuencia de caracteres delimitada por comillas simples (' ') o dobles (" "). Puede incluir
letras, números, símbolos, espacios y otros caracteres especiales. Python  utiliza  la  codificación
"Unicode", lo que permite trabajar con caracteres de diferentes idiomas y sistemas de escritura.

Es importante destacar que el tipo de dato (str), derivado de "string" (cadena  de  caracteres),  es
inmutable. Esto significa que, una vez creado, no puede modificarse. Sin embargo,  permite  realizar
operaciones como concatenar, buscar  y  extraer  subcadenas,  entre  otras.  También  es  importante
distinguir entre "texto", que denota contenido extenso o complejo, y "cadena", que hace referencia a
secuencias breves de caracteres."""

# Ejemplo_texto_str.py

# Explicación:
"""Definimos varias variables y asignamos a cada una un texto en  forma  de  cadena,  cada  una  con
diferentes características. Encerramos cada texto entre comillas dobles (" ")  para  definirlo  como
una cadena de caracteres. Finalmente, imprimimos el valor de cada variable con la función  "print()"
para observar el resultado.

En el caso de la variable "texto_6", concatenamos el texto que  contiene  con  el  contenido  de  la
variable "texto_1". Utilizamos el operador (+) para unir ambos textos. El resultado es un texto  que
incluye el contenido de ambas variables."""

# Código:
texto_1 = "Hola, soy un texto en Python."
print(texto_1)

texto_2 = "Hola, soy un texto en Python con números: 1234567890"
print(texto_2)

texto_3 = "Hola, soy un texto en Python con símbolos: !@#$%^&*()_+"
print(texto_3)

texto_4 = "Hola, soy un texto en Python con tabulaciones y saltos de línea: \n\t\"\\\""
print(texto_4)

texto_5 = "Hola, soy un texto en Python con caracteres especiales: \n\t\"\\\""
print(texto_5)

texto_6 = "Hola, soy un texto en Python concatenado con una variable y un salto de línea: \n" + texto_1
print(texto_6)

# Nota Importante:
"""Explicamos la concatenación detalladamente en la sección correspondiente a "Texto (str)". También
explicamos las secuencias de escape y los diferentes caracteres especiales, como el salto  de  línea
(\n), la tabulación (\t), las comillas dobles (\") y las comillas simples (\'), así como el  uso  de
la barra invertida doble (\\) para incluir comillas dobles y simples dentro de un texto,  además  de
otros caracteres especiales."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────