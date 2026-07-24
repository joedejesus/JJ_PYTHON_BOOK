# Enunciado:
"""El sistema numérico octal en Python es un sistema de numeración basado en 8 dígitos, que  incluye
los números del 0 al 7. En Python, los números octales se  representan  mediante  el  prefijo  "0o",
seguido de los dígitos octales. Por ejemplo, el número octal  "0o144"  equivale  al  número  decimal
"100". Este sistema es menos común que el sistema decimal o el hexadecimal, pero sigue  siendo  útil
en ciertos contextos, como la  representación  de  permisos  en  sistemas  de  archivos  Unix  y  en
aplicaciones específicas de programación de bajo nivel.

En el sistema octal, cada dígito representa un valor entre 0 y 7, y las posiciones  de  los  dígitos
tienen un peso basado en potencias de 8, lo que lo  hace  especialmente  adecuado  para  representar
datos de forma compacta y legible en ciertos entornos.

El número de dígitos en un número octal  determina  su  valor,  y  estos  dígitos  se  organizan  en
potencias de 8, donde el dígito más a la derecha representa "8**0",  el  siguiente  a  la  izquierda
representa "8**1", y así sucesivamente. Esto significa que cada dígito en un número octal  tiene  un
valor específico según su posición, lo que permite representar cualquier número  decimal  utilizando
solo los dígitos del 0 al 7. Por ejemplo, el número octal "0o144" se interpreta como: (1 *  8**2)  +
(4 * 8**1) + (4 * 8**0), lo que equivale a: (1 * 64) + (4 * 8) + (4 * 1), dando  como  resultado  el
valor decimal 100.

Python proporciona herramientas integradas, como los constructores "bin()", "int()" y "hex()",  para
realizar conversiones entre sistemas numéricos. Del mismo modo, también es posible convertir números
de otros sistemas  numéricos  a  octal  mediante  el  constructor  "oct()".  Estas  capacidades  son
esenciales para trabajar con datos en diferentes formatos y garantizar  la  interoperabilidad  entre
sistemas. Además, el uso de estas herramientas permite  a  los  programadores  realizar  operaciones
matemáticas y lógicas de manera eficiente, asegurando que los datos se manipulen con precisión.

Por último, el sistema octal tiene aplicaciones  prácticas  en  diversos  campos.  Por  ejemplo,  en
sistemas de archivos Unix, cada dígito octal representa un conjunto de permisos para el propietario,
el grupo y otros usuarios. Esto permite una representación compacta y precisa de las configuraciones
de seguridad. Asimismo, en el ámbito de las redes y los sistemas  embebidos,  el  sistema  octal  se
utiliza para representar datos binarios de forma más legible y compacta, optimizando  el  espacio  y
mejorando la claridad en la interpretación de los datos. Estas características hacen que el  sistema
octal sea una herramienta indispensable para los desarrolladores que trabajan en contextos donde  la
eficiencia y la precisión son críticas, como la programación de bajo nivel y  la  administración  de
sistemas."""

# Ejemplo_sistema_numerico_octal.py

# Explicación:
"""Definimos una variable llamada "numero_octal" y le asignamos el valor "0o144", que representa  el
número 100 en el sistema decimal. Para ello, utilizamos el prefijo "0o" para indicar que se trata de
un número octal, seguido de los  dígitos  octales  correspondientes,  en  este  caso  "144".  Luego,
utilizamos la función "print()" para mostrar el número octal en la consola, acompañado de un mensaje
descriptivo en formato "f-string". En este caso, el número octal se mostrará en formato decimal  por
defecto, ya que Python lo  convierte  automáticamente  a  decimal  al  imprimirlo  o  al  usarlo  en
operaciones, si no se especifica lo contrario.

A continuación, realizamos conversiones a otros  sistemas  numéricos  utilizando  los  constructores
"bin()", "int()" y  "hex()",  respectivamente.  Para  ello,  en  cada  caso  colocamos  la  variable
"numero_octal", que contiene el número octal, dentro del constructor correspondiente  para  realizar
la conversión. Asignamos el resultado a una variable diferente para cada sistema  numérico  y  luego
utilizamos la función "print()" para mostrar los resultados en la consola, acompañados de un mensaje
descriptivo en formato "f-string". Esto nos permite observar cómo se representa el mismo  número  en
diferentes sistemas numéricos, lo cual es útil para comprender las relaciones entre ellos y trabajar
con datos en distintos formatos.

En el segundo caso, utilizamos el constructor "oct()" para obtener su  representación  explícita  en
formato octal, lo que nos permite mostrar el número con  su  prefijo  "0o"  y  los  dígitos  octales
correspondientes.

En el cuarto caso, aunque  utilizamos  el  constructor  "int()"  para  convertir  el  número  octal,
realmente no es necesario, ya que este se muestra en formato decimal por defecto. Sin embargo,  esto
nos permite enfatizar que el número octal se interpreta como un valor decimal en las  operaciones  y
al imprimirlo, lo que es importante para entender cómo  Python  maneja  los  números  octales  y  su
relación con otros sistemas numéricos.

Además, de esta forma cubrimos todos los casos  posibles  de  conversión  entre  sistemas  numéricos
partiendo de un número octal, lo que es esencial para trabajar con datos en  diferentes  formatos  y
realizar cálculos y transformaciones entre ellos de manera eficiente."""

# Código:
numero_octal = 0o144
print(f"Número octal (salida decimal por defecto): {numero_octal}")

conversion_octal = oct(numero_octal)
print(f"Número octal (conversión explícita): {conversion_octal}")

conversion_binario = bin(numero_octal)
print(f"Número binario: {conversion_binario}")

conversion_decimal = int(numero_octal)
print(f"Número decimal: {conversion_decimal}")

conversion_hexadecimal = hex(numero_octal)
print(f"Número hexadecimal: {conversion_hexadecimal}")

# Nota Importante:
"""En Python, los números octales son una herramienta poderosa para representar datos de bajo nivel,
como permisos en sistemas de archivos Unix  y  valores  en  protocolos  de  red.  Su  representación
compacta y legibilidad los hace ideales para estas aplicaciones. Además, las herramientas integradas
de Python permiten realizar conversiones  entre  sistemas  numéricos  de  manera  sencilla,  lo  que
facilita el desarrollo y mejora la legibilidad del código.

Este enfoque es especialmente útil en aplicaciones que  requieren  manipulación  de  datos  de  bajo
nivel, como el desarrollo de sistemas embebidos  o  protocolos  de  comunicación.  Por  ejemplo,  en
sistemas Unix, los permisos de archivos y directorios se representan comúnmente en formato octal, lo
que permite a los administradores de sistemas definir configuraciones de seguridad de manera precisa
y eficiente. Asimismo, en el ámbito de  las  redes,  el  sistema  octal  puede  ser  utilizado  para
representar datos binarios de forma más compacta, lo que  resulta  en  una  mejor  optimización  del
espacio y una mayor claridad en la interpretación de los datos.

Por último, estas características hacen que el sistema octal sea una herramienta indispensable  para
los desarrolladores que trabajan en contextos donde la  eficiencia  y  la  precisión  son  críticas.
Además, su uso fomenta la interoperabilidad entre sistemas y asegura que los datos sean  manipulados
con exactitud,  lo  que  es  esencial  en  entornos  donde  la  confiabilidad  y  la  seguridad  son
primordiales."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
