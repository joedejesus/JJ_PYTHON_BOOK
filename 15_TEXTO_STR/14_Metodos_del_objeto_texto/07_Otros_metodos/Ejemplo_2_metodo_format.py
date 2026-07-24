# Enunciado:
"""El método ".format()" en Python se utiliza para formatear cadenas de texto de manera  flexible  y
eficiente. Este método permite insertar valores en una cadena  de  texto  utilizando  marcadores  de
posición definidos con llaves {}. Los valores que se insertarán se especifican como  argumentos  del
método y se transfieren a los marcadores de posición correspondientes dentro de la cadena de texto.

El método ".format()" toma una cadena de texto y sustituye cada marcador de posición {} por el valor
correspondiente proporcionado como argumento. El resultado es una nueva cadena de texto  donde  cada
marcador de posición ha sido reemplazado por el  valor  especificado.  Esto  permite  crear  cadenas
dinámicas y personalizadas de manera sencilla, ya que se pueden combinar texto estático con  valores
variables de forma clara y legible.

Este método puede aplicarse a cualquier objeto de tipo texto en Python, ya sea en  forma  de  cadena
literal, a una variable que contenga texto o incluso como resultado de una  expresión  que  devuelva
texto. Además, este método no modifica la  cadena  original,  ya  que  las  cadenas  en  Python  son
inmutables. En su lugar, devuelve una nueva cadena con los cambios realizados. Si se desea conservar
el resultado de la transformación, es necesario asignarlo a una nueva variable o usarlo directamente
en una operación posterior.

El método toma tantos argumentos como marcadores de posición {}  se  hayan  definido  en  la  cadena
original, y estos argumentos pueden ser de cualquier tipo de dato, como  cadenas,  números,  listas,
diccionarios, objetos personalizados, entre otros. Además, estos argumentos pueden pasarse en  forma
de valores literales, variables o incluso expresiones. Si no se proporcionan suficientes  argumentos
para cubrir todos los  marcadores  de  posición,  se  generará  un  error.  Por  otro  lado,  si  se
proporcionan más argumentos de los necesarios, los argumentos adicionales serán ignorados.

El método ".format()" puede utilizarse con argumentos posicionales o con argumentos  nombrados.  Los
argumentos posicionales se insertan en el  orden  en  que  aparecen,  mientras  que  los  argumentos
nombrados se identifican mediante claves. Esto proporciona flexibilidad para organizar y  reutilizar
los valores en la cadena de texto.

Además, en el caso de los argumentos posicionales, los marcadores de posición se definen  dentro  de
la cadena como llaves vacías {}, y los valores que se  insertarán  se  especifican  como  argumentos
posicionales en  el  método  de  esta  forma:  ".format(a,  b,  c,  ...)".  Estos  argumentos  serán
transferidos a los marcadores de posición en el orden en que se  definieron,  es  decir,  el  primer
argumento se insertará en el primer marcador  de  posición,  el  segundo  argumento  en  el  segundo
marcador de posición, y así sucesivamente.

En el caso de los argumentos nombrados, los marcadores de posición se definen dentro  de  la  cadena
como llaves con una clave específica {clave}, y los valores que se insertarán  se  especifican  como
argumentos nombrados en el método de esta  forma:  ".format(clave=valor)".  Estos  argumentos  serán
transferidos a los marcadores de posición  correspondientes  según  las  claves  definidas,  lo  que
permite una mayor flexibilidad y claridad en la organización de la cadena de texto.

El método ".format()" es especialmente útil para crear cadenas dinámicas, ya  que  permite  combinar
texto con valores variables de manera sencilla. Además, ofrece opciones avanzadas para dar formato a
los valores, como especificar el ancho, la alineación, el relleno y el  formato  numérico.  Esto  lo
convierte en  una  herramienta  poderosa  para  generar  salidas  de  texto  personalizadas  y  bien
formateadas.

Por último, el método ".format()" es una herramienta versátil y poderosa para formatear  cadenas  de
texto en Python. Su capacidad para manejar valores dinámicos y aplicar  formatos  personalizados  lo
convierte en una opción preferida para tareas que requieren la generación de texto dinámico  y  bien
estructurado."""

# Ejemplo_2_metodo_format.py

# Explicación:
"""Definimos una variable llamada "plantilla" y le asignamos una cadena de texto  que  contiene  dos
marcadores de posición {} para indicar dónde se insertarán los valores dinámicos. En este  caso,  la
cadena de texto es un saludo que incluye un marcador para el nombre y  otro  para  la  edad  de  una
persona. Esta cadena de texto se utilizará para demostrar el funcionamiento del método ".format()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".format()" a la variable "plantilla" con dos argumentos posicionales: "Joe" y 34.
Para ello, escribimos el nombre de la variable "plantilla" seguido del método ".format()" y,  dentro
de los paréntesis, colocamos los valores que  queremos  insertar  en  los  marcadores  de  posición,
separados por comas y respetando la sintaxis de cada tipo de dato:  comillas  para  las  cadenas  de
texto y sin comillas para los números.

De esta forma, el método ".format()" reemplazará el primer marcador de posición {} por el valor  del
argumento "Joe" y el segundo marcador de posición {} por el valor del argumento  34,  generando  una
nueva cadena de texto almacenada en la variable "resultado".

Por último, utilizamos la función "print()" para mostrar el resultado en la consola acompañado de un
mensaje descriptivo en formato "f-string" que indica que se trata del resultado de aplicar el método
".format()" al texto contenido en la variable "plantilla" utilizando argumentos posicionales.

De esta forma, hemos combinado texto estático con valores dinámicos, demostrando la  flexibilidad  y
la potencia del método ".format()".

Además, realizamos el mismo proceso, pero utilizando un argumento nombrado, para lo  cual  definimos
una nueva variable llamada "plantilla_2" y le asignamos una cadena de texto que contiene un marcador
de posición con la clave {clave}. Luego, definimos una nueva variable  llamada  "resultado_2"  y  le
asignamos el resultado de aplicar el método ".format()" a la variable "plantilla_2" con un argumento
nombrado, en este caso: (clave=3.14159).

Por último, utilizamos la función "print()" para mostrar el resultado en la consola acompañado de un
mensaje descriptivo en formato "f-string" que indica que se trata del resultado de aplicar el método
".format()" al texto contenido en la variable "plantilla_2" utilizando argumentos nombrados. En este
caso, el método ".format()" reemplazará el marcador de posición  {clave}  por  el  valor  "3.14159",
generando una nueva cadena de texto que se asignará a la variable "resultado_2"."""

# Código:
plantilla = "Hola, mi nombre es {} y tengo {} años."
resultado = plantilla.format("Joe", 34)
print(f"Este es el resultado de aplicar el método con argumentos posicionales: {resultado}")

plantilla_2 = "El valor de pi es aproximadamente {clave}."
resultado_2 = plantilla_2.format(clave=3.14159)
print(f"Este es el resultado de aplicar el método con argumentos nombrados: {resultado_2}")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".format()" no modifica la cadena original,  ya  que
las cadenas en Python son inmutables. Esto significa que siempre se genera  una  nueva  cadena  como
resultado de su aplicación, dejando intacta la cadena original. Este comportamiento es especialmente
útil cuando se trabaja con datos que no deben alterarse directamente, ya que garantiza la integridad
del texto original.

Si se desea almacenar el resultado del método  ".format()",  es  necesario  asignarlo  a  una  nueva
variable o sobrescribir la variable original. De lo contrario, el resultado de la transformación  se
perderá.

Es importante saber que, en una misma cadena de texto, se pueden utilizar argumentos posicionales  y
argumentos nombrados, siempre que los marcadores de posición estén definidos correctamente.

En cuanto a las claves, estas pueden ser cualquier cadena de texto válida, pero no  pueden  contener
espacios ni caracteres especiales, y deben comenzar con una letra  o  un  guion  bajo.  Además,  las
claves deben ser únicas dentro de la misma cadena de texto para evitar conflictos  y  garantizar  la
correcta sustitución de los valores pasados como argumentos nombrados.

En cuanto a los valores asignados a los argumentos nombrados, estos pueden ser de cualquier tipo  de
dato, como cadenas, números, listas, diccionarios, objetos personalizados,  entre  otros,  y  pueden
pasarse en forma de valores literales, variables o expresiones. Sin embargo, es importante tener  en
cuenta  que  el  formato  de  los  valores  debe  ser  compatible  con  el  marcador   de   posición
correspondiente; es decir, si el marcador de  posición  espera  un  número,  el  valor  asignado  al
argumento nombrado debe ser un número.

El método ".format()" es capaz de manejar valores de diferentes tipos  y  convertirlos  a  texto  de
manera automática, lo que facilita la creación de cadenas de texto complejas  y  personalizadas  sin
necesidad de realizar conversiones manuales.

Además, el método ".format()" ofrece opciones avanzadas para personalizar el formato de los valores,
como especificar el ancho, la alineación, el relleno y el formato numérico. Esto lo convierte en una
herramienta poderosa para generar salidas de texto personalizadas y bien formateadas.

Por último, el método ".format()" es una herramienta útil y versátil, pero su uso debe  considerarse
cuidadosamente en contextos donde se requiere un control preciso sobre el formato  del  texto  o  en
ciertos idiomas o contextos donde las reglas de presentación son más complejas."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
