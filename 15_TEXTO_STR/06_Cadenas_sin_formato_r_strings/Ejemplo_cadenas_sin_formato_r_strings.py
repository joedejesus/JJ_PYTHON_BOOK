# Enunciado:
"""Las cadenas sin formato, también conocidas como "raw strings" o "r-strings" en  Python,  son  una
forma de representar cadenas de texto en la que los  caracteres  de  escape  no  se  procesan.  Esto
significa que secuencias de escape como el salto de línea (\n) o la tabulación (\t)  se  interpretan
literalmente como texto, en lugar de convertirse en sus correspondientes caracteres especiales.

Esto quiere decir que, al utilizar una cadena sin formato, cualquier carácter incluido en la  cadena
se interpreta tal cual, sin modificaciones ni interpretaciones  adicionales,  y  las  secuencias  de
escape se tratan como texto literal, por lo que no producen su efecto habitual.

Para crear una cadena sin formato, se antepone una letra "r" minúscula o "R" mayúscula al inicio  de
la cadena, indicando al intérprete que trate todos sus caracteres de manera  literal.  Esto  asegura
que cualquier carácter incluido en la cadena  sea  interpretado  tal  cual,  sin  modificaciones  ni
interpretaciones adicionales.

Esto resulta especialmente útil en situaciones en las que  se  requiere  trabajar  con  cadenas  que
contienen múltiples caracteres de escape, como rutas de archivos o  expresiones  regulares,  ya  que
evita errores y hace que el código sea más legible y fácil de mantener.

Por ejemplo, al trabajar con rutas de archivos en sistemas operativos como Windows, donde las  rutas
contienen barras invertidas (\), las cadenas sin formato eliminan la  necesidad  de  duplicar  estas
barras para evitar que se interpreten como caracteres de escape. De igual forma, en las  expresiones
regulares, donde los patrones suelen  incluir  múltiples  caracteres  especiales,  las  cadenas  sin
formato simplifican la escritura y la lectura del código al eliminar la necesidad  de  duplicar  las
barras invertidas, lo que facilita la comprensión y reduce errores.

Por último, es importante saber que una expresión regular es una secuencia de caracteres que  define
un patrón de búsqueda, utilizado para encontrar coincidencias en cadenas de  texto.  Esta  expresión
puede incluir caracteres literales, metacaracteres y cuantificadores para especificar el  patrón  de
búsqueda. Por ejemplo, la expresión regular "\d{3}-\d{2}-\d{4}" se utiliza para  buscar  números  de
seguro social en el formato "XXX-XX-XXXX", donde "\d" representa un dígito y "{n}" indica que  dicho
dígito debe aparecer "n" veces."""

# Ejemplo_cadenas_sin_formato_r_strings.py

# Explicación:
"""Definimos varias variables, cada una con un nombre descriptivo que indica el tipo de  cadena  sin
formato que almacena, y les asignamos diferentes cadenas  sin  formato  utilizando  la  sintaxis  de
"r-string". Para ello, anteponemos la letra "r" al inicio de  cada  cadena  y  la  encerramos  entre
comillas, lo que indica que se trata de una cadena sin formato.

En el primer caso, la variable "cadena_sin_formato_con_caracteres_especiales"  almacena  una  cadena
sin formato que incluye secuencias como salto de línea (\n), tabulación (\t) y una  barra  invertida
seguida de una comilla doble (\"). Al imprimir esta variable, se muestra la  cadena  tal  cual,  sin
interpretar dichas secuencias, lo que produce una salida literal que incluye esos caracteres.

En el segundo caso, la variable "cadena_sin_formato_con_expresion_regular" almacena una  cadena  sin
formato que representa un patrón de expresión regular para un número de seguro  social  con  formato
"XXX-XX-XXXX". Al imprimir esta variable, se muestra el patrón tal cual, sin interpretar las  barras
invertidas como caracteres de escape, lo que facilita su lectura y comprensión.

En el tercer caso, la variable  "cadena_sin_formato_con_ruta_de_archivo"  almacena  una  cadena  sin
formato que representa una ruta de archivo  en  un  sistema  operativo  Windows.  Al  imprimir  esta
variable, se muestra la ruta tal cual, sin interpretar las  barras  invertidas  como  caracteres  de
escape, lo que facilita la lectura y la comprensión de la ruta del archivo.

Por último, en cada caso utilizamos la función "print()" para mostrar el contenido de cada  variable
en la consola, acompañado de un mensaje descriptivo en formato "f-string" para indicar  el  tipo  de
cadena sin formato que se está mostrando."""

# Código:
cadena_sin_formato_con_caracteres_especiales = r"@@\n##\t€€\""
print(f"r-string con caracteres especiales: {cadena_sin_formato_con_caracteres_especiales}")

cadena_sin_formato_con_expresion_regular = r"\d{3}-\d{2}-\d{4}"
print(f"r-string con expresión regular: {cadena_sin_formato_con_expresion_regular}")

cadena_sin_formato_con_ruta_de_archivo = r"C:\Users\Usuario\Documents\Archivo.txt"
print(f"r-string con ruta de archivo: {cadena_sin_formato_con_ruta_de_archivo}")

# Nota Importante:
"""Es importante tener en cuenta que las cadenas sin formato son útiles cuando se trabaja con  rutas
de archivos, expresiones regulares u otros casos en los que los caracteres de escape  pueden  causar
problemas. Por ejemplo, al trabajar con rutas de archivos en sistemas operativos como Windows, donde
las rutas contienen barras invertidas (\), las cadenas sin formato  evitan  que  estas  barras  sean
interpretadas como caracteres de escape. Esto es particularmente relevante en contextos en  los  que
las rutas deben manipularse o  procesarse  dinámicamente,  reduciendo  la  probabilidad  de  errores
relacionados con caracteres de escape mal interpretados.

De igual forma, en las expresiones regulares, donde los patrones suelen incluir múltiples caracteres
especiales, las cadenas sin formato simplifican la escritura y la lectura del código al eliminar  la
necesidad de duplicar las barras invertidas. Esto no solo mejora la legibilidad del código, sino que
también facilita su mantenimiento a largo plazo, especialmente en proyectos grandes o colaborativos.

Por último, es importante tener en  cuenta  que,  si  se  ejecuta  este  código,  se  obtendrán  dos
advertencias en la consola del tipo "SyntaxWarning: invalid escape sequence". Esto se debe a que, al
explicar el código, se han incluido secuencias de escape en el texto sin  escaparlas  correctamente,
lo que hace que Python interprete ciertas partes del texto como secuencias  de  escape  no  válidas.
Estas secuencias de escape aparecen en el texto explicativo con otro color, pero no están dentro  de
una cadena de texto asignada a una variable, lo  que  provoca  la  advertencia.  Sin  embargo,  esta
advertencia no afecta la ejecución del código, ya que las secuencias  de  escape  se  han  utilizado
correctamente dentro de las cadenas de texto asignadas a las variables."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
