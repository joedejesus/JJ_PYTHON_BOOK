# Enunciado:
"""Las secuencias de escape en Python son caracteres especiales que permiten representar  caracteres
no imprimibles o caracteres con un significado  especial  dentro  de  una  cadena  de  texto.  Estas
secuencias comienzan con una barra invertida (\), seguida de un  carácter  que  indica  el  tipo  de
secuencia de escape. Por ejemplo, (\n) representa un salto de línea, mientras que  (\t)  se  utiliza
para insertar una tabulación horizontal.
   
El uso de las secuencias de escape es esencial para incluir caracteres que, de  otro  modo,  podrían
causar errores de sintaxis o comportamientos inesperados. Por ejemplo, para incluir comillas  dentro
de una cadena delimitada por comillas, se  utilizan  las  secuencias  (\')  o  (\").  Además,  estas
secuencias son útiles para dar formato a cadenas  de  texto,  como  al  insertar  saltos  de  línea,
tabulaciones o caracteres especiales.        
       
Sin embargo, un mal uso de las secuencias  de  escape  puede  llevar  a  errores  de  sintaxis  o  a
resultados inesperados, especialmente si se olvida escapar un carácter especial o si se utiliza  una
secuencia de escape incorrecta. Por ejemplo, si se intenta incluir una barra invertida sin escaparla
correctamente, Python podría interpretar la letra siguiente como parte de una secuencia  de  escape,
lo que podría resultar en un error o en un comportamiento no deseado.
                
Cuando usamos el término "escapar", nos referimos a la acción de utilizar una  secuencia  de  escape
para representar un carácter especial dentro de una cadena de texto.
           
Las secuencias de escape más comunes en Python son:"""

# \n  -> Salto de línea.
# \t  -> Tabulación horizontal.
# \v  -> Tabulación vertical.
# \\  -> Barra invertida literal.
# \'  -> Comilla simple literal.
# \"  -> Comilla doble literal.
# \r  -> Retorno de carro.
# \b  -> Retroceso.
# \f  -> Avance de página.

# Ejemplo_secuencias_de_escape.py

# Explicación:
"""Definimos varias variables, cada una con un nombre descriptivo que indica la secuencia de  escape
que se utiliza en la cadena de texto que contiene, y les asignamos, en  cada  caso,  una  cadena  de
texto que incluye la secuencia de escape correspondiente. Para ello, utilizamos la  barra  invertida
(\) seguida del carácter que forma la secuencia de escape, sin espacios entre ellos, para que Python
pueda interpretar correctamente la secuencia de escape dentro de la cadena de texto.

En los casos del salto de línea (\n), la tabulación horizontal (\t) y la tabulación  vertical  (\v),
no separamos el texto con espacios en el punto donde  aplicamos  la  secuencia  de  escape,  ya  que
utilizamos dicha secuencia como separador entre las partes del texto que queremos mostrar.

En los casos de la barra invertida literal (\\), la comilla simple literal (\') o la  comilla  doble
literal (\"), utilizamos la secuencia de escape para incluir  caracteres  especiales  dentro  de  la
cadena de texto sin que Python los interprete como parte de la sintaxis del código.

En los casos del retorno de carro (\r) y el retroceso (\b), colocamos  la  secuencia  de  escape  en
medio del texto, lo que permite modificar la forma en que  se  muestra  al  imprimirlo,  ya  que  el
retorno de carro sobrescribe el texto anterior a la secuencia de escape, mientras que  el  retroceso
elimina el carácter anterior a ella.

Por último, en el caso del avance de página (\f), utilizamos la secuencia de escape para simular  un
salto de página, lo que puede ser útil para organizar la salida de texto  en  la  consola  o  en  un
archivo.

Además, en cada caso utilizamos la función  "print()"  para  mostrar  el  valor  de  cada  variable,
acompañado de un mensaje descriptivo en formato  "f-string",  que  indica  la  secuencia  de  escape
aplicada. De esta forma, podemos observar el efecto de  cada  secuencia  de  escape  en  cada  texto
impreso en la consola."""

# Código:
salto_de_linea = "Hola\nMundo"
print(f"Salto de línea: {salto_de_linea}")

tabulacion_horizontal = "Columna1\tColumna2"
print(f"Tabulación horizontal: {tabulacion_horizontal}")

tabulacion_vertical = "Texto1\vTexto2\vTexto3"
print(f"Tabulación vertical: {tabulacion_vertical}")

barra_invertida_literal = "C:\\Users\\joede"
print(f"Barra invertida literal: {barra_invertida_literal}")

comilla_simple_literal = 'It\'s a beautiful day'
print(f"Comilla simple literal: {comilla_simple_literal}")

comilla_doble_literal = "Ella dijo: \"Hola\""
print(f"Comilla doble literal: {comilla_doble_literal}")

retorno_de_carro = "Primera línea\rSegunda línea"
print(f"Retorno de carro: {retorno_de_carro}")

retroceso = "Hola\bMundo"
print(f"Retroceso: {retroceso}")

avance_de_pagina = "Primera pagina\fSegunda pagina"
print(f"Avance de página: {avance_de_pagina}")

# Nota Importante:
"""Es importante tener en cuenta que las secuencias de escape solo funcionan dentro  de  cadenas  de
texto, ya que su propósito es modificar o interpretar ciertos caracteres de manera especial.  Si  se
desea incluir una barra invertida literal (\) en una cadena, se debe usar una doble barra  invertida
(\\), lo que asegura que Python no la interprete como el inicio de una secuencia de escape.

Alternativamente, se puede utilizar una cadena sin formato, "raw string", añadiendo el  prefijo  "r"
antes de la cadena. Esto resulta especialmente útil cuando  se  trabaja  con  rutas  de  archivos  o
expresiones regulares, ya que permite incluir caracteres especiales sin necesidad  de  escaparlos  y
mantiene el texto tal como se escribe.

Por último, es importante tener  en  cuenta  que,  si  se  ejecuta  este  código,  obtendremos  tres
advertencias en la consola del tipo "SyntaxWarning: invalid escape sequence". Esto se debe a que, al
explicar el código, se han incluido secuencias de escape en el texto sin  escaparlas  correctamente,
lo que hace que Python interprete ciertas partes del texto  como  secuencias  de  escape  inválidas.
Estas secuencias aparecen en el texto explicativo y forman parte de literales de cadena no asignados
a variables, lo que provoca la advertencia. Sin embargo, esta advertencia no afecta la ejecución del
código, ya que las secuencias de escape se han utilizado correctamente  dentro  de  las  cadenas  de
texto asignadas a las variables."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
