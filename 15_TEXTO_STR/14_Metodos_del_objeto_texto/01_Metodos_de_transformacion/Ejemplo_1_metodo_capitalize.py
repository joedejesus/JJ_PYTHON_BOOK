# Enunciado:
"""El método ".capitalize()" en Python se utiliza para convertir el primer carácter de una cadena  a
mayúscula y el resto de los caracteres a minúscula. Este método es útil para dar formato al texto de
manera consistente, especialmente cuando se desea que solo la primera letra de una palabra  o  frase
esté en mayúscula.

Este método puede ser aplicado a cualquier cadena de texto (str) y devuelve una nueva cadena con  el
formato deseado. Es importante destacar que el método no modifica la cadena  original,  ya  que  las
cadenas en Python son inmutables. En su lugar, genera una nueva cadena con los cambios aplicados.

Además, si el primer carácter de la cadena no es una letra, no se  realizará  ninguna  conversión  a
mayúscula para ese carácter específico, pero el resto de los caracteres se convertirán a  minúscula.
Esto incluye caracteres especiales, números o espacios en blanco al inicio de la cadena, los  cuales
permanecerán intactos.

El método ".capitalize()" no recibe  argumentos  adicionales  y  se  puede  aplicar  directamente  a
cualquier cadena, ya sea en forma de variable o como  una  cadena  literal.  Dado  que  este  método
devuelve una nueva cadena, es necesario asignar el resultado a una variable si se desea  conservarlo
para su uso posterior.

Por último, este método es  especialmente  útil  en  situaciones  donde  se  desea  estandarizar  la
apariencia de los datos textuales, como en  nombres  propios,  títulos  de  libros,  encabezados  de
secciones o cualquier otro tipo de texto donde se prefiera un formato específico.  Sin  embargo,  es
importante tener en cuenta que este método no es adecuado para casos donde se  requiere  capitalizar
cada palabra de una frase, ya que solo afecta el primer carácter de la cadena completa. Esto lo hace
especialmente útil en tareas de limpieza y normalización de  datos  textuales,  donde  se  busca  un
formato uniforme y estandarizado."""

# Ejemplo_1_metodo_capitalize.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos la  cadena  de  texto  "hOLA  MUNDO".  Esta
cadena será utilizada para demostrar el funcionamiento del método ".capitalize()".

Definimos una nueva variable llamada "texto_capitalizado_1" y le asignamos el resultado  de  aplicar
el método ".capitalize()" a la variable "texto". Para ello, escribimos  el  nombre  de  la  variable
seguido del nombre del método  ".capitalize()".  En  este  caso,  el  método  no  recibe  argumentos
adicionales, por lo que los paréntesis se dejan vacíos.

Luego utilizamos la función "print()" para mostrar el resultado  en  la  consola  acompañado  de  un
mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado  de  aplicar  el
método al texto original contenido en la variable "texto".

A continuación, definimos una variable llamada "texto_capitalizado_2" y le asignamos el resultado de
aplicar el método ".capitalize()" a la cadena literal "aDIOS MUNDO". Para ello, escribimos la cadena
literal encerrada entre comillas, seguida del nombre del método ".capitalize()". En  este  caso,  el
método no recibe argumentos adicionales, por lo que los paréntesis se dejan vacíos.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola acompañado de un
mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado  de  aplicar  el
método a la cadena literal "aDIOS MUNDO"."""

# Código:
texto = "hOLA MUNDO"

texto_capitalizado_1 = texto.capitalize()
print(f"Este es el resultado de aplicar el método a '{texto}': {texto_capitalizado_1}")

texto_capitalizado_2 = "aDIOS MUNDO".capitalize()
print(f"Este es el resultado de aplicar el método a 'aDIOS MUNDO': {texto_capitalizado_2}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".capitalize()" no afecta los caracteres  especiales
ni los números que puedan estar al inicio de la cadena. Por ejemplo,  si  tenemos  una  cadena  como
"123python", al aplicar el método ".capitalize()", el resultado será "123python", sin modificaciones
en los números. Asimismo, si la cadena  contiene  caracteres  especiales  como  "¡hola  MUNDO!",  el
resultado será "¡Hola mundo!", respetando los caracteres especiales y ajustando las letras según las
reglas mencionadas.

Además, si la cadena contiene caracteres en mayúscula  después  del  primer  carácter,  estos  serán
convertidos a minúscula. Por ejemplo, al aplicar ".capitalize()" a la cadena "PYTHON ES GENIAL",  el
resultado será "Python es genial". Por lo tanto, este método es ideal para casos donde  se  requiere
un formato de tipo "Título" en una frase o palabra, pero no es  adecuado  para  mantener  mayúsculas
específicas en otras partes del texto o para capitalizar múltiples palabras en una cadena.

Por último, es importante recordar  que  este  método  genera  una  nueva  cadena  con  los  cambios
aplicados, dejando intacta la cadena original. Esta es una característica inherente de  las  cadenas
en Python, ya que son inmutables. Por lo tanto, si se desea conservar  el  resultado,  es  necesario
asignarlo a una nueva variable o sobrescribir la  existente.  Este  comportamiento  asegura  que  el
método  sea  seguro  de  usar  en  contextos  donde  la  cadena  original  no  debe   ser   alterada
directamente."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
