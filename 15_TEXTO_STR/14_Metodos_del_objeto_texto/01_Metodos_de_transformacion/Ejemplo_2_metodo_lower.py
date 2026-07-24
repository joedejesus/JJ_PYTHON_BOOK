# Enunciado:
"""El método ".lower()" en Python es un método de texto que convierte una cadena  de  caracteres  en
minúsculas.  Este  método  es  útil  cuando  se  necesita  estandarizar  el  formato  de  un  texto,
especialmente en contextos en los que se  requiere  comparar  cadenas  de  texto  sin  importar  las
diferencias entre mayúsculas y minúsculas. Por ejemplo, puede emplearse en  validaciones  de  datos,
búsquedas de texto o en el procesamiento de información textual.

Al aplicar este método, se genera una nueva cadena con todas las letras en minúsculas, mientras  que
los caracteres no alfabéticos permanecen sin cambios. Además, este método no requiere  argumentos  y
puede aplicarse a cualquier objeto de tipo texto, ya sea literal o almacenado en  una  variable,  lo
que proporciona una forma directa de transformar el texto a un formato uniforme, lo que facilita  su
manipulación y análisis posterior.

Por último, el método ".lower()" es particularmente valioso en tareas de limpieza y normalización de
datos, ya que permite que las comparaciones entre cadenas sean consistentes,  independientemente  de
cómo se hayan ingresado los datos. Además, su implementación es sencilla  y  eficiente,  lo  que  lo
convierte en una herramienta esencial para el manejo de textos en Python."""

# Ejemplo_2_metodo_lower.py

# Explicación:
"""Definimos una variable llamada "texto"  y  le  asignamos  una  cadena  de  texto  con  todos  sus
caracteres en mayúsculas. Esta cadena será utilizada para demostrar  el  funcionamiento  del  método
".lower()".

Definimos una nueva variable llamada "texto_minuscula_1" y le asignamos el resultado de  aplicar  el
método ".lower()" a la variable "texto". Para ello, escribimos el nombre de la variable seguido  del
nombre del método ".lower()". En este caso, el método no recibe argumentos adicionales, por  lo  que
los paréntesis se dejan vacíos.

Luego, utilizamos la función "print()" para mostrar el resultado en la  consola,  acompañado  de  un
mensaje descriptivo en formato "f-string" para indicar que se trata  del  resultado  de  aplicar  el
método al texto contenido en la variable "texto".

A continuación, definimos una variable llamada "texto_minuscula_2" y le asignamos  el  resultado  de
aplicar el método ".lower()" a la cadena literal "PYTHON ES GENIAL". Para ello, escribimos la cadena
literal entre comillas, seguida del nombre del método ".lower()". En este caso, el método no  recibe
argumentos adicionales, por lo que los paréntesis se dejan vacíos.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" para indicar que se trata del resultado de  aplicar  el
método a la cadena literal "PYTHON ES GENIAL"."""

# Código:
texto = "HOLA MUNDO"

texto_minuscula_1 = texto.lower()
print(f"Resultado de aplicar el método a '{texto}': {texto_minuscula_1}")

texto_minuscula_2 = "PYTHON ES GENIAL".lower()
print(f"Resultado de aplicar el método a 'PYTHON ES GENIAL': {texto_minuscula_2}")
      
# Nota Importante:
"""Es importante destacar que el método ".lower()" no modifica la cadena original, sino que devuelve
una ueva cadena con todas las letras convertidas a minúsculas. Esto significa que la cadena original
permanece intacta, lo cual es útil para preservar los  datos  originales  mientras  se  trabaja  con
versiones transformadas. Si se desea  guardar  el  resultado  de  la  transformación,  es  necesario
asignarlo a una nueva variable o sobrescribir la variable original, ya  que  el  método  no  realiza
cambios en la cadena original.

Además, este método solo afecta a los caracteres alfabéticos y deja  inalterados  los  números,  los
espacios y caracteres especiales. Esto permite que el método sea versátil y aplicable en una  amplia
variedad de contextos, desde la normalización de datos hasta la preparación de texto  para  análisis
más complejos.

Otro aspecto relevante es que, al  ser  un  método  no  destructivo,  puede  utilizarse  en  cadenas
inmutables sin riesgo  de  alterar  su  contenido  original.  Esto  resulta  especialmente  útil  en
aplicaciones donde la integridad de los datos es crucial, como en el análisis de  grandes  volúmenes
de información textual o en sistemas  que  requieren  mantener  un  registro  exacto  de  los  datos
ingresados.

Por último, cabe mencionar que este método es ampliamente soportado en todas las versiones  modernas
de Python, lo  que  garantiza  su  compatibilidad  y  facilidad  de  uso  en  diversos  entornos  de
desarrollo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
