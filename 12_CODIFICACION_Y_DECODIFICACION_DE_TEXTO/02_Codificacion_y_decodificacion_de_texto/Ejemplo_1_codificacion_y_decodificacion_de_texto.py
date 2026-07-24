# Enunciado:
"""La codificación es el proceso de convertir caracteres y cadenas de texto  en  una  representación
numérica que las computadoras pueden entender mediante tablas de códigos  como  "UTF-8"  o  "ASCII".
"UTF-8" es un estándar ampliamente utilizado que puede representar  caracteres  de  casi  todos  los
idiomas, incluidos símbolos especiales y emojis, lo que lo hace ideal  para  aplicaciones  globales.
Por otro lado, "ASCII" es más limitado, ya que  solo  cubre  caracteres  básicos  del  inglés,  como
letras, números y algunos símbolos.  La  decodificación  realiza  el  proceso  inverso,  traduciendo
representaciones numéricas en caracteres legibles.

Es crucial elegir la codificación adecuada según la compatibilidad y los requisitos del proyecto, ya
que una codificación incorrecta puede provocar errores o pérdida de datos. Las funciones  "ord()"  y
"chr()" son herramientas fundamentales en Python para  convertir  entre  caracteres  y  sus  valores
numéricos en "Unicode", facilitando la manipulación del texto a nivel de código.

Además, existen métodos como ".encode()" y ".decode()" que  permiten  convertir  entre  texto  y  su
representación en bytes. Estos métodos son esenciales para aplicaciones que requieren compatibilidad
con múltiples idiomas, sistemas y plataformas, asegurando que los datos textuales  se  transmitan  y
almacenen correctamente."""

# Ejemplo_1_codificacion_y_decodificacion_de_texto.py

# Nota Muy Importante:
"""Python incluye métodos como ".encode()" y ".decode()" para la codificación  y  decodificación  de
texto, permitiendo convertir entre texto y  bytes.  Estos  métodos  son  especialmente  útiles  para
manejar datos que necesitan ser transmitidos o almacenados en formatos binarios,  como  en  redes  o
archivos. Aunque estos conceptos forman parte de la  codificación  y  decodificación  de  texto,  se
consideran un tema más avanzado que requiere comprender el concepto de bytes y su  relación  con  el
texto para lograr una correcta asimilación. Por lo tanto, se explicarán en  detalle  en  la  sección
correspondiente a bytes.

Sin embargo, en esta sección se explicará la conversión entre texto y puntos de código mediante  las
funciones "ord()" y "chr()", que son fundamentales para entender la representación de los caracteres
en "Unicode". Estas funciones permiten explorar cómo  Python  maneja  internamente  los  caracteres,
proporcionando una base sólida para trabajar con codificaciones más avanzadas en el futuro.

Por último, es importante aclarar que un punto de código es  un  número  entero  que  representa  un
carácter específico en el estándar "Unicode". Por lo tanto, "ord()" devuelve el punto de  código  de
un carácter dado, mientras que "chr()" devuelve el carácter correspondiente a  un  punto  de  código
determinado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
