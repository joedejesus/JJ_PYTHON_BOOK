# Enunciado:
"""La concatenación es el proceso de unir dos o más cadenas de texto en una sola, y  constituye  una
operación esencial en programación. Permite construir mensajes  dinámicos,  combinar  variables  con
texto  y  generar  salidas  personalizadas.  En  Python,  las  formas  más   comunes   de   realizar
concatenaciones son mediante el operador (+) y el uso de comas (,) dentro de la función "print()".

El operador (+) permite unir cadenas de texto de manera explícita, pero  tiene  como  requisito  que
todos los elementos involucrados sean del tipo (str). Si se intenta concatenar una cadena  de  texto
con otro tipo de dato, como un número o un valor booleano, es necesario convertir  previamente  esos
datos al tipo (str) utilizando el constructor "str()". De lo contrario,  se  generará  un  error  de
tipo.

Por otro lado, la función "print()" con  comas  (,)  ofrece  una  forma  más  flexible  de  combinar
diferentes tipos de datos, ya que realiza automáticamente la conversión de estos a cadenas de  texto
al momento de imprimirlos. Esto resulta especialmente útil para mostrar mensajes rápidamente, aunque
no modifica ni almacena las cadenas de texto originales, ya que su propósito es únicamente presentar
la información en la salida estándar.

Es importante destacar que el operador (+) crea una nueva cadena de texto cada vez que  se  utiliza,
lo que puede resultar ineficiente en procesos que requieren muchas concatenaciones debido al consumo
de memoria y al tiempo de procesamiento.

Por último, las comas (,) en la función "print()" no generan  nuevas  cadenas  de  texto,  sino  que
simplemente presentan los elementos juntos en la salida,  lo  que  las  hace  ideales  para  mostrar
información de manera temporal y eficiente."""

# Ejemplo_concatenacion.py

# Explicación:
"""Definimos varias variables llamadas "nombre", "apellido", "edad" y "altura" con diferentes  tipos
de datos y les asignamos valores  específicos,  coherentes  con  su  tipo,  los  cuales  representan
información personal de un individuo.

A continuación, definimos una variable llamada "concatenacion_1" y  le  asignamos  el  resultado  de
concatenar las variables "nombre" y "apellido" utilizando el operador (+). Para ello, escribimos  el
nombre de la variable "nombre", seguido del operador (+), seguido de un espacio entre comillas  para
separar el nombre del apellido, seguido del operador (+) y, finalmente, el  nombre  de  la  variable
"apellido". De esta forma, obtenemos una nueva cadena que combina el nombre y  el  apellido  con  un
espacio entre ellos. Por último, utilizamos la función "print()" para mostrar  el  resultado  de  la
concatenación, acompañado de un mensaje concatenado que indica que se  trata  de  una  concatenación
usando el operador (+).

Definimos otra variable llamada "concatenacion_2" y le asignamos  el  resultado  de  concatenar  las
variables "nombre" y "altura" con dos cadenas que describen la altura  de  la  persona.  Para  ello,
escribimos el nombre de la variable "nombre", seguido del operador (+), seguido de la cadena "  mide
", seguido del operador (+), luego el resultado de convertir la  variable  "altura"  al  tipo  (str)
utilizando el constructor "str()", seguido del operador (+) y, finalmente,  la  cadena  "  metros.".
Esto nos permite crear una nueva cadena que combina el nombre de la persona con su altura en metros.
Por último, utilizamos  la  función  "print()"  para  mostrar  el  resultado  de  la  concatenación,
acompañado de un mensaje concatenado que indica que se trata de una concatenación usando el operador
(+) con conversión explícita.

Por último, utilizamos la función "print()" con comas (,) para  mostrar  el  nombre,  la  edad,  dos
cadenas y un mensaje indicando que se trata de una concatenación usando comas  (,)  con  la  función
"print()". Para ello, escribimos la función "print()", seguida de una cadena que indica que se trata
de una concatenación usando comas (,) con la función "print()", luego una coma (,),  seguida  de  la
variable "nombre", luego una coma (,), seguida de la cadena "tiene", luego otra coma (,), seguida de
la variable "edad", y, finalmente, otra coma (,) seguida de la  cadena  "años.".  Esto  nos  permite
mostrar el nombre de la persona junto con su edad y un mensaje descriptivo sin necesidad de realizar
conversiones explícitas, ya que la función "print()" se encarga  de  convertir  automáticamente  los
datos a cadenas de texto al momento de imprimirlos."""

# Código:
nombre = "Joe"
apellido = "Férnandez"
edad = 34
altura = 1.68

concatenacion_1 = nombre + " " + apellido
print("Concatenación usando el operador (+):", concatenacion_1)

concatenacion_2 = nombre + " mide " + str(altura) + " metros."
print("Concatenación usando el operador (+) con conversión explícita:", concatenacion_2)

print("Concatenación usando comas (,) con la función print():",nombre, "tiene", edad, "años.")

# Nota Muy Importante:
"""El operador (+) es una herramienta poderosa para construir nuevas cadenas de texto, pero  su  uso
requiere que todos los datos que no sean de tipo (str) se conviertan previamente al tipo (str). Esto
asegura que no se produzcan errores durante la concatenación y que el resultado sea  una  cadena  de
texto válida.

La función "print()" con comas (,) es una alternativa práctica para combinar  y  mostrar  diferentes
tipos de datos sin necesidad de realizar conversiones explícitas. Sin embargo, es  importante  tener
en cuenta que esta técnica no une los datos de forma permanente, ya que su propósito  es  únicamente
presentar la información en la salida estándar.

Es fundamental recordar que el uso de comas (,) fuera de la función "print()" no genera  una  cadena
de texto, sino una tupla, lo cual no es adecuado para concatenar texto. Por esta razón, el  operador
(+) sigue siendo la opción preferida cuando se necesita unir cadenas de texto de manera  efectiva  y
permanente.

Además, se debe tener cuidado al combinar el operador (+) con las comas (,) en la función "print()",
ya que el operador (+) se utiliza para concatenar cadenas de texto, mientras que las  comas  (,)  se
utilizan para separar diferentes elementos  en  la  función  "print()".  Si  no  se  comprende  esta
diferencia, se podrían generar errores de  sintaxis  o  resultados  inesperados.  Por  ello,  no  se
recomienda mezclar estas dos técnicas en la misma línea de código, ya que puede llevar a confusión y
dificultar la lectura del código.

Es importante mencionar que el operador (+) puede resultar ineficiente en situaciones en las que  se
realizan múltiples concatenaciones, ya que cada operación crea una nueva cadena de texto en memoria.
En estos casos, se recomienda considerar  otras  técnicas,  como  el  uso  de  listas  y  el  método
".join()", para mejorar el rendimiento y la eficiencia en la manipulación de cadenas de texto.

Por último, es preciso encerrar cada cadena de texto individual entre comillas simples o dobles para
que el intérprete de Python las reconozca como  cadenas  de  texto  válidas.  De  lo  contrario,  se
generará un error de sintaxis, ya que el intérprete no podrá identificar correctamente  las  cadenas
de texto. Además, se  recomienda  utilizar  espacios  para  que  la  salida  sea  legible  y  clara,
especialmente cuando se concatenan varias cadenas de texto."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
