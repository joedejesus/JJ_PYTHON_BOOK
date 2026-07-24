# Enunciado:
"""El método ".format_map()" en Python se utiliza para formatear cadenas de texto de manera flexible
y eficiente. Este método es similar al método ".format()".  Sin  embargo,  en  lugar  de  pasar  los
valores como argumentos posicionales o nombrados, este método utiliza un diccionario como  argumento
para proporcionar los valores que se insertarán en los marcadores de posición definidos entre llaves
{} dentro de la cadena de texto.

El método ".format_map()" toma una cadena de texto y sustituye cada marcador de posición {}  por  el
valor correspondiente proporcionado como argumento. Este valor está  asociado  a  una  clave  en  el
diccionario pasado como argumento al método. El resultado es una nueva cadena de  texto  en  la  que
cada marcador de posición ha sido reemplazado por el valor especificado. Esto permite crear  cadenas
dinámicas y personalizadas de manera sencilla, ya que se pueden combinar texto estático con  valores
variables de forma clara y legible.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, una variable que contenga texto o incluso como resultado de una expresión que  devuelva  un
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve una nueva cadena con los cambios realizados. Si se desea conservar
el resultado de la transformación, es necesario asignarlo a una nueva variable o usarlo directamente
en una operación posterior.

Este método toma un único argumento, el cual es un diccionario que contiene las claves y los valores
que se utilizarán para reemplazar los marcadores de posición en la cadena de texto. Cada marcador de
posición debe coincidir con una clave en el diccionario pasado como argumento  al  método  para  que
este pueda realizar la sustitución  correctamente.  Además,  este  diccionario  puede  pasarse  como
argumento en forma de variable o directamente como un diccionario literal dentro de  los  paréntesis
del método.

Además, el diccionario pasado como argumento debe contener claves que coincidan exactamente con  los
nombres de los marcadores de posición en la cadena de texto y los valores asociados  a  esas  claves
serán los que se insertarán en la cadena resultante para cada marcador de posición  correspondiente.
Si falta alguna clave requerida, se generará un error. Por otro lado,  si  el  diccionario  contiene
claves adicionales que no se utilizan en la cadena, estas serán ignoradas.

El método ".format_map()"  es  especialmente  útil  cuando  se  trabaja  con  datos  almacenados  en
diccionarios, ya que permite acceder directamente a los valores  sin  necesidad  de  descomponer  el
diccionario en argumentos individuales. Esto lo convierte en una herramienta poderosa  para  generar
salidas de texto personalizadas y bien formateadas.

Por último, el método ".format_map()" es una herramienta versátil y eficaz para formatear cadenas de
texto en Python utilizando diccionarios. Su capacidad  para  manejar  valores  dinámicos  y  aplicar
formatos personalizados lo convierte en una opción preferida para tareas que requieren la generación
de texto dinámico y bien estructurado."""

# Ejemplo_3_metodo_format_map.py

# Explicación:
"""Definimos una variable llamada "plantilla" y le asignamos una cadena de texto  que  contiene  dos
marcadores de posición {nombre} y {edad} para indicar dónde se insertarán los valores dinámicos.  En
este caso, la cadena de texto es un saludo que incluye un marcador para el nombre  y  otro  para  la
edad de una persona. Esta cadena de texto se utilizará para demostrar el funcionamiento  del  método
".format_map()".

A continuación, definimos una variable llamada "diccionario" y le asignamos un diccionario  con  dos
pares clave-valor, donde la clave "nombre" tiene el valor "Joe" y la clave "edad" tiene el valor 34.
Para ello creamos un diccionario  utilizando  llaves  {}  y  dentro  de  ellas  definimos  cada  par
clave-valor, separando la clave del valor con dos puntos y cada par con una coma. En este  caso,  la
clave "nombre" es una cadena de texto y su valor es también una cadena de  texto,  mientras  que  la
clave "edad" es una cadena de texto y su valor es un número entero. Este  diccionario  se  utilizará
como argumento del método.

Luego, definimos una nueva variable llamada "resultado" y le asignamos el resultado  de  aplicar  el
método ".format_map()" a la variable "plantilla" con un  argumento,  en  este  caso  el  diccionario
"diccionario". Para ello, escribimos el nombre de la variable "plantilla"  seguido  del  nombre  del
método ".format_map()" y dentro de los paréntesis del método  colocamos  la  variable  "diccionario"
como argumento.

De esta forma, el método ".format_map()" reemplazará el marcador de posición {nombre} por  el  valor
asociado a la clave "nombre" en el diccionario y  el  marcador  de  posición  {edad}  con  el  valor
asociado a la clave "edad" también en el diccionario, lo que generará  una  nueva  cadena  de  texto
almacenada en la variable "resultado".

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" que indica que se trata del  resultado  de  aplicar  el
método ".format_map()" al texto contenido en la variable "plantilla" utilizando un diccionario  como
argumento.

De esta forma, hemos combinado texto estático con valores dinámicos almacenados en  un  diccionario,
demostrando la flexibilidad y la potencia del método ".format_map()"."""

# Código:
plantilla = "Hola, mi nombre es {nombre} y tengo {edad} años."
diccionario = {"nombre": "Joe", "edad": 34}
resultado = plantilla.format_map(diccionario)
print(f"Aplicamos el método al texto: {plantilla} El resultado es: {resultado}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".format_map()" no modifica la cadena  original,  ya
que las cadenas en Python son inmutables. Esto significa que siempre se genera una nueva cadena como
resultado de su aplicación, dejando intacta la cadena original. Este comportamiento es especialmente
útil cuando se trabaja con datos que no deben  ser  alterados  directamente,  ya  que  garantiza  la
integridad del texto original.

Si se desea almacenar el resultado del método ".format_map()", es necesario asignarlo  a  una  nueva
variable o sobrescribir la variable original. De lo contrario, el resultado de la transformación  se
perderá.

Es importante asegurarse de que el diccionario pasado  como  argumento  contenga  todas  las  claves
necesarias para los marcadores de posición en la cadena de texto. Si falta alguna clave, se generará
un error. Además, las claves deben ser cadenas de texto válidas y únicas dentro  del  diccionario  y
deben coincidir exactamente con los nombres de los marcadores de posición en la cadena de texto para
que el método funcione correctamente.

En cuanto a los valores asociados a las claves en el diccionario, estos pueden ser de cualquier tipo
de dato, ya sea en forma literal, contenidos en variables o incluso como resultados de  expresiones.
Además, no es necesario convertir estos  valores  a  texto  ya  que  el  método  ".format_map()"  se
encargará de convertirlos a texto de manera automática durante el proceso de formateo.

El método ".format_map()" es capaz de manejar valores de diferentes tipos y convertirlos a texto  de
manera automática, lo que facilita la creación de cadenas de texto complejas  y  personalizadas  sin
necesidad de realizar conversiones manuales.

Es importante notar que este método es muy versátil, ya que es posible definir un diccionario con un
número extenso de claves y valores y luego utilizarlo para formatear diferentes cadenas de texto, lo
que permite reutilizar  el  mismo  conjunto  de  datos  para  generar  múltiples  salidas  de  texto
personalizadas de manera eficiente.

Por último, el método ".format_map()"  es  una  herramienta  útil  y  versátil,  pero  su  uso  debe
considerarse cuidadosamente en contextos donde se requiere un control preciso sobre el  formato  del
texto o para ciertos idiomas o contextos donde las reglas de presentación son más complejas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
