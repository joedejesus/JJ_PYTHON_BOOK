# Enunciado:
"""La fusión de textos es una técnica fundamental en la manipulación de cadenas de texto en  Python.
Permite combinar múltiples cadenas en una sola, lo que  resulta  útil  en  una  amplia  variedad  de
aplicaciones, como la creación de mensajes, la generación de informes y la construcción de rutas  de
archivos. Además, es una herramienta esencial para el procesamiento de datos,  ya  que  facilita  la
integración de información proveniente de diferentes fuentes y su presentación de forma coherente  y
estructurada.

Esta técnica se logra utilizando el operador  de  concatenación  (+)  o  el  método  ".join()",  que
permiten unir cadenas de manera eficiente y flexible. El operador (+) es  ideal  para  combinaciones
simples y rápidas, mientras que el método ".join()" es más eficiente cuando se trabaja con múltiples
cadenas, ya que reduce el consumo de memoria al evitar la creación de múltiples objetos intermedios.


El método ".join()" es útil cuando se tiene una lista de cadenas  que  se  desea  fusionar,  ya  que
permite unir todos los elementos de la lista en una sola cadena de  manera  eficiente.  Este  método
toma una secuencia de cadenas como argumento y devuelve una nueva cadena que es la concatenación  de
las cadenas de la secuencia, separadas por el separador  especificado  antes  del  método,  de  esta
forma: "separador".join(lista_de_cadenas). El separador puede ser cualquier cadena, como un espacio,
una coma o incluso una cadena vacía, dependiendo de cómo se desee dar formato al resultado final.

Además, con esta técnica es posible combinar cadenas literales con variables que contienen texto, lo
que facilita la creación de mensajes dinámicos y personalizados. Esto hace que la fusión  de  textos
sea una habilidad clave para cualquier programador que trabaje con datos textuales."""

# Ejemplo_fusion_de_textos.py

# Explicación:
"""Definimos dos variables llamadas "texto_1" y "texto_2", y les  asignamos  las  cadenas  de  texto
"Hola, " y "¿cómo estás?", respectivamente. Estas cadenas representan dos partes de un  mensaje  que
queremos fusionar para formar un mensaje completo.

Luego definimos una nueva variable llamada "texto_fusionado" y  le  asignamos  el  resultado  de  la
fusión de "texto_1" y "texto_2" utilizando el operador de concatenación (+).  Para  ello,  colocamos
ambas variables en el orden deseado de fusión, entre paréntesis para dejar  clara  la  operación,  y
separadas por el operador de concatenación (+).

De esta forma, las subcadenas "Hola, " y "¿cómo estás?" contenidas  en  las  variables  "texto_1"  y
"texto_2" se combinan  para  formar  una  nueva  cadena  que  contiene  el  mensaje  completo.  Esta
combinación se realiza en el orden en que aparecen las variables, por lo  que  el  resultado  de  la
fusión será "Hola, ¿cómo estás?".

Por último, utilizamos la función "print()" para mostrar el resultado de la fusión  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" que indica que se trata del resultado  de
la fusión de los textos."""

# Código:
texto_1 = "Hola, "
texto_2 = "¿cómo estás?"

texto_fusionado = (texto_1 + texto_2)
print(f"Este es el resultado de la fusión de los textos: {texto_fusionado}")

# Nota Importante:
"""Es importante destacar que la fusión de textos no modifica las cadenas originales, sino que  crea
una nueva cadena que contiene la combinación de las cadenas originales.  Esto  se  debe  a  que  las
cadenas en Python son inmutables, lo que significa que no pueden modificarse después de su creación.
Por lo tanto, cada vez que se fusionan cadenas, se genera una nueva cadena que contiene el resultado
de la fusión, mientras que las cadenas originales permanecen sin cambios.

Esta característica garantiza la seguridad y la consistencia  de  los  datos,  ya  que  las  cadenas
originales no se ven afectadas por operaciones posteriores. Sin embargo, también es importante tener
en cuenta que la creación de nuevas cadenas puede tener un  impacto  en  el  rendimiento  cuando  se
trabaja con grandes volúmenes de datos, por lo que es recomendable utilizar métodos eficientes  como
".join()" en estos casos.

El uso de paréntesis es opcional en este caso, pero ayuda a mejorar la  legibilidad  del  código  al
indicar claramente que se está realizando una operación de fusión de textos. Además, el orden de las
variables es importante, ya que determina el resultado final de la fusión. Si se invierte  el  orden
de las variables, el resultado sería diferente, por lo que es  fundamental  prestar  atención  a  la
secuencia en la que se combinan las cadenas para obtener el resultado deseado.

Por último, cabe destacar que, en realidad, lo que estamos haciendo es  concatenar  las  cadenas  de
texto con ayuda del operador  de  concatenación  (+),  pero  utilizamos  el  término  "fusión"  para
describir el proceso de combinar las cadenas de texto en una sola, ya que este  término  se  utiliza
comúnmente para referirse a este proceso en un contexto más amplio y descriptivo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
