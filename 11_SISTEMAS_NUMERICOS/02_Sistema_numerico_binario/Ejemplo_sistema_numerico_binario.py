# Enunciado:
"""El sistema numérico binario en Python es un sistema de numeración que utiliza solo dos dígitos, 0
y 1, para representar números. En Python, los números binarios se representan con el  prefijo  "0b",
seguido de una secuencia de dígitos binarios, los cuales pueden ser 0 o 1. Por  ejemplo,  el  número
binario "0b100" representa el número decimal 4. Estos números son fundamentales en  la  computación,
ya que constituyen la base del sistema binario utilizado por las máquinas para procesar y  almacenar
información. En el sistema binario, cada dígito representa un valor entre 0 y 1, y las posiciones de
los dígitos tienen un peso basado en potencias de 2, lo que  lo  hace  especialmente  adecuado  para
representar datos a nivel de bits y bytes.

El número de dígitos en un número binario determina su  valor,  y  estos  dígitos  se  organizan  en
potencias de 2, donde el dígito más a la derecha representa "2**0", el  siguiente  a  la  izquierda,
"2**1", y así sucesivamente. Esto significa que cada dígito en un  número  binario  tiene  un  valor
específico, dependiendo de  su  posición,  lo  que  permite  representar  cualquier  número  decimal
utilizando solo los dígitos 0 y 1. Por ejemplo, el número binario "0b100" se interpreta como:  
(1  * 2**2) + (0 * 2**1) + (0 * 2**0), lo que equivale a: (1 * 4) + (0 * 2) + (0 * 1),  resultando en  
el valor decimal 4.

Estos números son esenciales para trabajar con datos a nivel de bits y bytes, lo que es crucial para
la programación de bajo nivel, la manipulación  de  datos  y  la  optimización  del  rendimiento  en
sistemas informáticos. Además, el sistema binario es ampliamente utilizado en la informática  debido
a su compatibilidad con los circuitos electrónicos, que operan en estados de encendido (1) y apagado
(0). Esto lo convierte en la base de la lógica digital y de los sistemas computacionales modernos.

En Python, trabajar  con  números  binarios  es  sencillo  y  eficiente,  lo  que  permite  realizar
operaciones matemáticas y lógicas con facilidad. Además, estos números pueden  convertirse  a  otros
sistemas numéricos, como el decimal, hexadecimal u  octal,  utilizando  los  constructores  "int()",
"hex()" y "oct()", respectivamente. Del mismo modo, también es posible convertir  números  de  otros
sistemas numéricos a binario utilizando el constructor "bin()".

Por último, esto permite realizar cálculos y transformaciones entre diferentes  sistemas  numéricos,
lo cual es esencial para el desarrollo de programas y aplicaciones informáticas que interactúan  con
hardware o protocolos de comunicación. Comprender este sistema es crucial  para  abordar  temas  más
avanzados, como la arquitectura de computadoras, el diseño de sistemas operativos y la  programación
de bajo nivel. Asimismo, el conocimiento del sistema binario es indispensable para entender cómo los
datos son representados, almacenados y procesados en los sistemas digitales."""

# Ejemplo_sistema_numerico_binario.py

# Explicación:
"""Definimos una variable llamada "numero_binario" y le asignamos el valor "0b100",  que  representa
el número 4 en el sistema decimal. Para ello, utilizamos el prefijo "0b" para indicar que  se  trata
de un número binario, seguido de los dígitos binarios correspondientes, en este caso  "100".  Luego,
utilizamos la función "print()" para mostrar el número binario  en  la  consola,  acompañado  de  un
mensaje descriptivo en formato "f-string". En este caso, el número binario se  mostrará  en  formato
decimal por defecto, ya que  Python  convierte  automáticamente  el  número  binario  a  decimal  al
imprimirlo o usarlo en operaciones, si no se especifica lo contrario.

A continuación, realizamos conversiones a otros  sistemas  numéricos  utilizando  los  constructores
"int()", "hex()" y "oct()",  respectivamente.  Para  ello,  en  cada  caso  encerramos  la  variable
"numero_binario", que contiene el  número  binario,  dentro  del  constructor  correspondiente  para
realizar la conversión, asignamos el resultado a una variable diferente para cada sistema numérico y
luego utilizamos la función "print()" para mostrar los resultados en la consola, acompañados  de  un
mensaje descriptivo en formato "f-string". Esto nos permite observar cómo  se  representa  el  mismo
número en diferentes sistemas numéricos, lo cual es útil para comprender las relaciones entre  ellos
y trabajar con datos en diferentes formatos.

En el segundo caso, utilizamos el constructor "bin()" para  obtener  su  representación  en  formato
binario explícito, lo que nos permite mostrar el número binario con su prefijo "0b"  y  los  dígitos
binarios correspondientes.

Por último, en el tercer caso, aunque utilizamos el constructor "int()"  para  convertir  el  número
binario, realmente no es necesario, ya que el número binario  se  muestra  en  formato  decimal  por
defecto. Sin embargo, esto nos permite enfatizar que el número binario se interpreta como  un  valor
decimal en las operaciones y al imprimirlo, lo que es importante para entender  cómo  Python  maneja
los números binarios y su relación con otros sistemas numéricos.

Además, de esta forma, cubrimos todos los casos posibles  de  conversión  entre  sistemas  numéricos
partiendo de un número binario, lo que es esencial para trabajar con datos en diferentes formatos  y
realizar cálculos y transformaciones entre ellos de manera eficiente."""

# Código:
numero_binario = 0b100
print(f"Número binario (salida decimal por defecto): {numero_binario}")

conversion_binario = bin(numero_binario)
print(f"Número binario (conversión explícita): {conversion_binario}")

conversion_decimal = int(numero_binario)
print(f"Número decimal: {conversion_decimal}")

conversion_hexadecimal = hex(numero_binario)
print(f"Número hexadecimal: {conversion_hexadecimal}")

conversion_octal = oct(numero_binario)
print(f"Número octal: {conversion_octal}")

# Nota Importante:
"""Siempre que no se indique el prefijo "bin", "hex"  u  "oct",  el  resultado  se  mostrará  en  su
representación decimal por defecto. Esto significa  que,  aunque  el  número  se  haya  definido  en
binario, hexadecimal u octal, Python convertirá automáticamente su valor a decimal al  imprimirlo  o
utilizarlo en operaciones, si no se indica explícitamente el sistema numérico original ni se utiliza
un constructor para la conversión. Este comportamiento es útil para garantizar  la  consistencia  en
los cálculos y la interoperabilidad entre diferentes sistemas numéricos.

Este enfoque nos permite  trabajar  con  diferentes  sistemas  numéricos  sin  preocuparnos  por  la
conversión manual, lo que simplifica el desarrollo y mejora la legibilidad del código. Además,  este
comportamiento predeterminado de Python permite  realizar  operaciones  matemáticas  y  lógicas  sin
necesidad de preocuparse por el sistema numérico original, ya que siempre  se  trabaja  con  valores
decimales en las operaciones.

Esto resulta especialmente útil en aplicaciones que  requieren  interoperabilidad  entre  diferentes
sistemas numéricos, como la criptografía, el  análisis  de  datos  y  la  programación  de  sistemas
embebidos. Por ejemplo, en el ámbito de la criptografía, la capacidad de  convertir  entre  sistemas
numéricos es crucial para implementar algoritmos de cifrado y descifrado. En el análisis  de  datos,
trabajar con diferentes representaciones numéricas puede facilitar la optimización de cálculos y  la
representación de la información.

Por último, en la programación de sistemas embebidos, la interoperabilidad entre sistemas  numéricos
permite la comunicación eficiente entre hardware y software, asegurando un rendimiento óptimo y  una
correcta interpretación de los datos."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
