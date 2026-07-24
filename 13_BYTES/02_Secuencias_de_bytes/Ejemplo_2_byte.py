# Enunciado:
"""Un "byte" es  una  unidad  de  información  digital  compuesta  por  una  secuencia  de  8  bits.
Independientemente del sistema numérico en el que se represente, un "byte" siempre contiene 8  bits,
ya sea en binario, decimal, hexadecimal u octal.  Esto  significa  que  un  "byte"  puede  almacenar
valores que van desde 0 hasta 255 en el  sistema  decimal,  lo  que  equivale  a  256  combinaciones
posibles o, lo que es lo mismo, (2**8) combinaciones.

Un "byte" puede representarse en varios sistemas numéricos: en binario, de 00000000 a  11111111;  en
decimal, de 0 a 255; en hexadecimal, de 00 a FF; y en octal, de 000 a  377.  Estas  representaciones
son fundamentales en informática porque permiten codificar  caracteres,  colores,  instrucciones  de
máquina o cualquier tipo de dato  representable  digitalmente.  Por  ejemplo,  en  el  caso  de  los
caracteres, cada uno puede representarse mediante un valor  único  dentro  de  este  rango,  lo  que
facilita su almacenamiento y manipulación en sistemas digitales.  Así,  el  "byte"  es  esencial  en
informática para representar caracteres, almacenar datos y realizar operaciones de cómputo.

Para representar correctamente los "bytes" en Python, se debe usar el constructor "bytes()", el cual
espera un iterable de enteros y devuelve un objeto de tipo "bytes". Cada entero dentro del  iterable
debe estar en el rango de 0 a 255 y puede definirse utilizando los prefijos: "0b" para binario,  sin
prefijo para decimal, "0x" para hexadecimal y "0o" para octal. Estos números en diferentes  sistemas
numéricos deben encerrarse  dentro  de  una  lista,  ya  que  el  constructor  "bytes()"  no  acepta
directamente valores individuales no iterables. Esto es fundamental para que el  programa  construya
correctamente el objeto "bytes". De lo contrario, estaríamos representando un  número  en  distintos
sistemas numéricos y no un objeto de tipo "bytes", lo que puede llevar a errores o malentendidos  en
el manejo de datos digitales.

La forma más común de representar un "byte" es mediante  el  sistema  hexadecimal,  ya  que  es  más
compacto y fácil de leer en comparación con el binario. Sin embargo, es importante destacar  que  la
representación de un "byte" no cambia su valor ni su función, sino que simplemente ofrece diferentes
formas de visualizarlo y entenderlo. Cada sistema numérico tiene sus propias ventajas y desventajas,
y la elección de uno u otro dependerá  del  contexto  y  de  las  necesidades  específicas  de  cada
situación. Por ejemplo, el binario es fundamental para entender cómo funcionan los  circuitos  y  la
lógica digital, mientras que el hexadecimal es más conveniente para representar  grandes  cantidades
de datos de manera compacta y legible.

Además, la salida predeterminada de un objeto de tipo "bytes" en Python es en  formato  hexadecimal,
lo que significa que, aunque se defina utilizando cualquiera de los sistemas numéricos  mencionados,
la representación visual en la consola será siempre hexadecimal. Esto  se  debe  a  que  el  formato
hexadecimal es más compacto  y  legible  para  los  seres  humanos,  y  se  utiliza  ampliamente  en
programación y depuración para representar datos binarios de manera más clara.

Por último, es importante saber que el prefijo "0x", correspondiente al sistema hexadecimal,  no  se
mostrará en la consola al imprimir un objeto de tipo "bytes". Esto se debe a que Python utiliza  una
representación estándar para los objetos "bytes". Esta representación muestra los valores en formato
hexadecimal, pero sin incluir el prefijo "0x". Cuando  se  imprime  un  objeto  "bytes",  Python  lo
representa como una cadena prefijada con la letra "b" para indicar que es un objeto de tipo "bytes".
Los valores individuales dentro del objeto se muestran precedidos por una barra invertida seguida de
la letra "x" para indicar que son valores hexadecimales. Esto garantiza una representación  estándar
y consistente."""

# Ejemplo_2_byte.py

# Explicación:
"""Definimos  varias  variables  con  un  nombre  descriptivo  para  cada   byte   en   su   formato
correspondiente. En cada caso, les asignamos un valor que representa el mismo byte, pero  utilizando
diferentes sistemas numéricos. Para ello, en cada caso utilizamos el constructor "bytes()"  con  una
lista en su interior, "bytes([...])", que contiene un solo número, el cual representa el byte en  el
formato correspondiente.

En cada caso, dentro de la lista escribimos el número  utilizando  el  formato  adecuado  para  cada
sistema numérico: para el  binario,  utilizamos  el  prefijo  "0b";  para  el  decimal,  simplemente
escribimos el número sin prefijo; para el hexadecimal, utilizamos el prefijo "0x"; y para el  octal,
utilizamos el prefijo "0o".

En este caso, "0b11001010" representa el byte en formato binario, "202" representa el mismo byte  en
formato decimal, "0xca" representa el mismo byte en formato  hexadecimal  y  "0o312"  representa  el
mismo byte en formato octal. Todos estos valores representan el mismo byte  en  diferentes  sistemas
numéricos y están dentro del rango permitido (0-255) para ser convertidos a bytes por el constructor
"bytes()". Además, todos corresponden al mismo valor hexadecimal: "CA".

Por último, en cada caso utilizamos la función "print()" para mostrar los resultados en la  consola,
acompañados de un mensaje descriptivo en formato "f-string", que indica el sistema  numérico  en  el
que se ha definido cada byte, junto con su representación correspondiente.

En todos los casos, la salida será en formato hexadecimal, ya que el constructor "bytes()" convierte
el valor en un objeto de tipo "bytes" y Python  lo  muestra  en  su  formato  estándar.  Además,  se
imprimirá el prefijo "b" para indicar que es un objeto de tipo "bytes" y,  al  tratarse  de  valores
individuales dentro de un objeto "bytes", se mostrarán precedidos por una barra invertida seguida de
la letra "x". Python utiliza la barra invertida y  la  letra  "x"  como  prefijo  para  los  valores
hexadecimales individuales dentro de los objetos "bytes", con el  fin  de  diferenciarlos  de  otros
tipos de datos."""

# Código:
byte_binario = bytes([0b11001010])
print(f"Este es un byte en formato binario: {byte_binario}")

byte_decimal = bytes([202])
print(f"Este es un byte en formato decimal: {byte_decimal}")

byte_hexadecimal = bytes([0xca])
print(f"Este es un byte en formato hexadecimal: {byte_hexadecimal}")

byte_octal = bytes([0o312])
print(f"Este es un byte en formato octal: {byte_octal}")

# Nota Muy Importante:
"""Es crucial representar cada "byte" tal y como se muestra aquí, ya que, de lo contrario, podríamos
estar representando un número en diferentes sistemas numéricos y no un objeto de tipo  "bytes".  Por
ejemplo, si no utilizamos el constructor "bytes()" con un iterable,  el  programa  interpretará  los
valores como enteros simples y no como "bytes".  Esto  puede  generar  confusión,  especialmente  al
trabajar con datos binarios o al realizar operaciones que dependen de la representación en "bytes".

Además, es importante recordar que los "bytes"  son  inmutables,  lo  que  significa  que,  una  vez
creados, no pueden modificarse.  Si  se  necesita  una  versión  mutable,  se  puede  usar  el  tipo
"bytearray", que permite modificar los valores después de su creación. Esto los  hace  ideales  para
representar datos que no deben  cambiar,  como  claves  criptográficas,  datos  de  red  o  archivos
binarios.

Aunque el constructor "bytes()" espera un iterable de enteros, es posible pasarle valores  numéricos
escritos en el formato deseado, ya que Python los interpretará como enteros y luego los convertirá a
"bytes", siempre y cuando cada número esté dentro del rango permitido (0-255) y  se  defina  con  el
prefijo  correspondiente.  Por  lo  tanto,  es  fundamental  asegurarse  de  que  cada  valor   esté
correctamente definido y de que se utilicen las herramientas adecuadas para su manipulación; en este
caso, el constructor "bytes()" y el prefijo correspondiente.

Por último, aunque los valores se definan con diferentes prefijos, la salida siempre será en formato
hexadecimal dentro del objeto "bytes", ya que Python convierte  la  entrada  a  enteros  y  luego  a
"bytes". Por ello, el formato de entrada no afecta a la salida,  siempre  y  cuando  el  valor  esté
dentro del rango permitido (0-255). Si se desea incluir explícitamente el prefijo "0x" en la salida,
es posible convertir los valores individuales dentro del  objeto  "bytes"  en  cadenas  con  formato
hexadecimal utilizando el constructor "hex()" o una comprensión de lista."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
