# Enunciado:
"""El sistema numérico decimal en Python es un sistema de numeración basado en diez dígitos,  del  0
al 9, que se utiliza para representar números en base 10. Este sistema es el más común  en  la  vida
cotidiana  y  se  emplea  ampliamente  en  aplicaciones  informáticas  debido  a  su  simplicidad  y
familiaridad. En Python, los  números  decimales  se  representan  directamente,  sin  necesidad  de
prefijos ni notaciones especiales. Por ejemplo, el número decimal "4" se  escribe  simplemente  como
"4". Esto hace  que  trabajar  con  números  decimales  sea  intuitivo  y  accesible,  incluso  para
principiantes en programación.

En el sistema decimal, cada dígito representa un valor entre 0 y 9, y las posiciones de los  dígitos
tienen un peso basado en potencias de 10, lo que lo hace  especialmente  adecuado  para  representar
datos de manera intuitiva y familiar en la vida cotidiana.

El número de dígitos en un número decimal determina su  valor,  y  estos  dígitos  se  organizan  en
potencias de 10, donde el dígito más a la derecha representa "10**0", el siguiente  a  la  izquierda
representa "10**1", y así sucesivamente. Esto significa que cada dígito en un número  decimal  tiene
un valor específico, dependiendo de su posición, lo que permite representar cualquier número decimal
utilizando solo los dígitos del 0 al 9. Por ejemplo, el número decimal "100" se interpreta como:  
(1 * 10**2) + (0 * 10**1) + (0 * 10**0), lo que equivale a: (1 * 100) + (0 * 10) + (0 * 1), resultando
en el valor decimal 100.

Python proporciona herramientas integradas para realizar conversiones entre sistemas numéricos.  Por
ejemplo, los constructores "bin()", "hex()" y "oct()" permiten convertir  números  decimales  a  sus
equivalentes en los sistemas binario, hexadecimal y octal, respectivamente. Asimismo, el constructor
"int()" permite convertir números de otros sistemas numéricos al sistema decimal. Estas  capacidades
son esenciales para desarrollar programas que interactúan con hardware, protocolos de comunicación o
sistemas de bajo nivel, donde las conversiones  entre  sistemas  numéricos  son  fundamentales  para
garantizar la interoperabilidad y el correcto funcionamiento de los sistemas.

Por último, comprender  el  sistema  decimal  es  crucial  para  abordar  temas  avanzados  como  la
programación y el análisis de  datos,  y  la  resolución  de  problemas  matemáticos.  Además,  este
conocimiento es indispensable para trabajar con datos en la mayoría de los contextos informáticos  y
científicos. Dominar el sistema decimal también proporciona una  base  sólida  para  entender  otros
sistemas numéricos, como el binario o el hexadecimal, y su aplicación  en  diferentes  áreas  de  la
tecnología y la ciencia."""

# Ejemplo_sistema_numerico_decimal.py

# Explicación:
"""Definimos una variable llamada "numero_decimal" y le asignamos el valor "100", que representa  el
número 100 en el sistema decimal. Para ello, simplemente  escribimos  el  número  sin  necesidad  de
prefijos especiales. Luego, utilizamos la función "print()" para mostrar el  número  decimal  en  la
consola acompañado de un mensaje descriptivo en formato "f-string". En este caso, el número  decimal
se mostrará en formato decimal por defecto, ya que Python interpreta automáticamente el número  como
decimal al imprimirlo o usarlo en operaciones si no se especifica lo contrario.

A continuación, realizamos conversiones a otros  sistemas  numéricos  utilizando  los  constructores
"bin()", "hex()" y "oct()",  respectivamente.  Para  ello,  en  cada  caso  encerramos  la  variable
"numero_decimal", que contiene  el  número  decimal  dentro  del  constructor  correspondiente  para
realizar la conversión, asignamos el resultado a una variable diferente para cada sistema numérico y
luego utilizamos la función "print()" para mostrar los resultados en la consola  acompañados  de  un
mensaje descriptivo en formato "f-string". Esto nos permite observar cómo  se  representa  el  mismo
número en diferentes sistemas numéricos, lo cual es útil para comprender las relaciones entre  ellos
y trabajar con datos en diferentes formatos.

En este caso, no es necesario utilizar el constructor "int()" para convertir el número decimal, como
sí ocurre con otros sistemas numéricos, ya que partimos de un número decimal y este  se  muestra  en
formato decimal por defecto. De esta forma cubrimos todos los casos  posibles  de  conversión  entre
sistemas numéricos partiendo de un número decimal, lo que es esencial para  trabajar  con  datos  en
diferentes formatos y realizar cálculos y transformaciones entre ellos de manera eficiente."""

# Código:
numero_decimal = 100
print(f"Número decimal (salida decimal por defecto): {numero_decimal}")

conversion_binario = bin(numero_decimal)
print(f"Número binario: {conversion_binario}")

conversion_hexadecimal = hex(numero_decimal)
print(f"Número hexadecimal: {conversion_hexadecimal}")

conversion_octal = oct(numero_decimal)
print(f"Número octal: {conversion_octal}")

# Nota Importante:
"""En Python, los  números  enteros  escritos  en  base  decimal  son  la  forma  predeterminada  de
representar este tipo de valores, lo  que  significa  que  no  es  necesario  realizar  conversiones
explícitas para trabajar con ellos. Esto simplifica  el  desarrollo  y  mejora  la  legibilidad  del
código, permitiendo a los programadores centrarse en la lógica del problema en lugar de  preocuparse
por detalles técnicos innecesarios. Este  comportamiento  predeterminado  también  permite  realizar
operaciones matemáticas y lógicas de manera eficiente, lo que resulta en un código más limpio, fácil
de mantener y menos propenso a errores.

Este enfoque es especialmente útil en aplicaciones que requieren cálculos matemáticos precisos, como
el análisis financiero, la ingeniería y la ciencia de datos. Por ejemplo, en el  ámbito  financiero,
la capacidad de realizar cálculos exactos con números en  representación  decimal  es  crucial  para
garantizar  la  precisión  de  los  resultados,  evitar  errores  en  transacciones  y  cumplir  con
regulaciones estrictas. En ingeniería, trabajar con números  decimales  permite  modelar  y  simular
sistemas físicos con precisión, lo que es esencial para diseñar y optimizar soluciones técnicas.  En
la ciencia de datos, los números decimales son  indispensables  para  analizar  y  procesar  grandes
volúmenes de datos de manera eficiente y precisa, asegurando que los resultados  sean  confiables  y
reproducibles.

Por último, el comportamiento predeterminado  de  Python  refuerza  su  posición  como  un  lenguaje
versátil y poderoso para una amplia variedad de aplicaciones.  Su  capacidad  para  manejar  números
decimales de forma  intuitiva  y  eficiente  lo  convierte  en  una  herramienta  ideal  tanto  para
principiantes como para  desarrolladores  experimentados  que  trabajan  en  proyectos  complejos  y
exigentes."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
