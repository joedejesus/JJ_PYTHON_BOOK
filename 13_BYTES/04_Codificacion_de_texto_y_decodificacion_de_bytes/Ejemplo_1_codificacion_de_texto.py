# Enunciado:
"""La codificación de texto es el proceso de convertir una cadena de texto en una secuencia de bytes
utilizando una codificación específica. El método ".encode()" convierte cada carácter de una  cadena
de texto en su representación en bytes mediante una codificación específica, como  "UTF-8",  que  se
utiliza de forma predeterminada. Este proceso es  fundamental  para  la  manipulación  de  datos  en
sistemas informáticos, ya que permite transformar el texto legible por  los  seres  humanos  en  una
secuencia de bytes que las computadoras pueden procesar y almacenar.

Es posible especificar  otra  codificación,  como  "ASCII",  dentro  del  método  ".encode()".  Cada
codificación tiene su propia tabla de códigos, que define cómo  se  representan  los  caracteres  en
formato  binario.  Por  ejemplo,  "UTF-8"  es  una  codificación  ampliamente  utilizada  que  puede
representar todos los caracteres del estándar "Unicode", mientras que "ASCII" es más limitada y solo
incluye los caracteres básicos del inglés.

Por último, la codificación "UTF-8" es especialmente útil porque es compatible con una  amplia  gama
de sistemas y plataformas, lo que la convierte en una opción predeterminada en muchos contextos. Por
otro lado, "ASCII", aunque es más simple, puede ser suficiente para aplicaciones  que  solo  manejen
texto en inglés. El método ".encode()"  es  esencial  para  garantizar  la  interoperabilidad  entre
sistemas, la correcta interpretación de los datos en diferentes  contextos  y  evitar  problemas  de
incompatibilidad o pérdida de información."""

# Ejemplo_1_codificacion_de_texto.py

# Explicación:
"""Definimos una variable llamada "cadena_texto" y le asignamos una cadena de texto; en  este  caso:
"Hola". Luego, utilizamos el método ".encode()" para convertir esa cadena de texto en una  secuencia
de bytes utilizando la codificación "UTF-8".  Para  ello,  aplicamos  el  método  ".encode()"  a  la
variable "cadena_texto", especificando "utf-8"  como  argumento,  y  asignamos  el  resultado  a  la
variable "secuencia_bytes_texto".

En este caso,  el  argumento  "utf-8"  no  sería  necesario,  ya  que  "UTF-8"  es  la  codificación
predeterminada, pero se incluye para ilustrar cómo se puede especificar  una  codificación  concreta
cuando sea necesario. La codificación especificada debe ir  entre  comillas;  de  lo  contrario,  se
generará un error.

Por último, utilizamos la  función  "print()"  para  mostrar  en  la  consola  el  resultado  de  la
codificación, acompañado de un mensaje descriptivo en formato "f-string" para indicar que  se  trata
de la cadena de texto codificada.

De esta forma, obtenemos el resultado de la codificación de la cadena de texto en formato de  bytes,
que se muestra en la consola como una secuencia de  caracteres  legibles,  pero  que,  en  realidad,
representa la codificación de cada carácter según la tabla de códigos de "UTF-8".  Este  proceso  es
fundamental para la manipulación de datos en sistemas informáticos, ya que permite transformar texto
legible por humanos en una secuencia de bytes que las computadoras pueden procesar y almacenar."""

# Código:
cadena_texto = "Hola"
secuencia_bytes_texto = cadena_texto.encode("utf-8")
print(f"Este es el resultado de codificar la cadena de texto: {secuencia_bytes_texto}")

# Nota Muy Importante:
"""En este caso, obtenemos en la consola una secuencia de bytes representada en formato de  texto  y
precedida por la letra "b". Aunque visualicemos los caracteres en formato legible, debemos  recordar
que estamos trabajando con bytes en formato binario. Esto significa que, internamente, cada carácter
está representado por un conjunto de bits según la codificación utilizada. Las computadoras procesan
estos caracteres como secuencias de bytes, lo cual es esencial para  comprender  la  codificación  y
decodificación de datos.

Este entendimiento es crucial para evitar errores al manipular datos  entre  diferentes  sistemas  o
aplicaciones, especialmente cuando se trabaja con archivos, redes o bases  de  datos  que  requieren
formatos específicos de codificación. Por ejemplo,  un  carácter  que  no  esté  soportado  por  una
codificación  específica  puede  generar  errores  o  pérdida  de  información  si  no   se   maneja
adecuadamente.

Por último, es importante tener en cuenta que el método ".encode()" no modifica la cadena  de  texto
original, sino que devuelve una nueva representación en formato de bytes."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
