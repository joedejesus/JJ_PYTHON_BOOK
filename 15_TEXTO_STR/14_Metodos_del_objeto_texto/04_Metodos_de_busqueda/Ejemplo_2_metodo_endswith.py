# Enunciado:
"""El método ".endswith()" en Python se utiliza para verificar si una cadena de texto termina con un
sufijo específico. Este método devuelve un valor booleano: "True" si la cadena termina con el sufijo
especificado y "False" en caso contrario.

Este método evalúa si el sufijo indicado coincide exactamente con el final de la  cadena  o  con  el
final de una subcadena especificada por los índices de inicio  y  fin,  y  devuelve  "True"  si  hay
coincidencia exacta.

Este método se aplica a una cadena de texto y devuelve un valor booleano que indica si dicha  cadena
termina con el sufijo especificado como argumento. Este método se puede aplicar a  cualquier  objeto
de tipo texto, incluyendo variables que contengan texto o el  resultado  de  otras  operaciones  que
generen texto. Además, no modifica la cadena original, ya que las cadenas en Python son  inmutables.
Esto significa que siempre genera un valor booleano como resultado de su aplicación y  deja  intacta
la cadena original.

El método ".endswith()" puede recibir uno, dos o tres argumentos. El primero es  el  sufijo  que  se
desea verificar y es obligatorio. El segundo argumento es un índice de inicio  opcional  que  indica
desde qué posición de la cadena se debe realizar la verificación del sufijo. El tercer argumento  es
un índice de fin opcional  que  indica  hasta  qué  posición  de  la  cadena  se  debe  realizar  la
verificación del sufijo.

El primer argumento puede ser una cadena de texto literal, una variable que contenga texto o incluso
el resultado de una operación que genere texto. El segundo argumento debe ser un número  entero  que
representa el índice de inicio desde el cual se desea realizar la verificación del sufijo. El tercer
argumento debe ser un número entero que representa el índice de fin hasta el cual se desea  realizar
la verificación del sufijo.

Además, es importante destacar que, si se proporciona el argumento  de  inicio,  no  es  obligatorio
proporcionar también el argumento de fin.  Si  solo  se  proporciona  el  argumento  de  inicio,  la
verificación se realiza desde esa posición hasta el final de la cadena.  Si  se  proporcionan  ambos
argumentos, la verificación se realiza desde el índice de inicio hasta el índice de fin,  excluyendo
este último.

Este método es útil para realizar validaciones rápidas en cadenas de texto,  como  verificar  si  un
archivo tiene una extensión específica, si una "URL" termina con un dominio particular o si un texto
cumple con un  formato  esperado.  Además,  no  realiza  validaciones  insensibles  a  mayúsculas  y
minúsculas, ya que la comparación es sensible a ellas. Si se necesita una comparación  insensible  a
mayúsculas, se debe convertir la cadena y el sufijo a minúsculas o a mayúsculas  antes  de  usar  el
método.

Por último, el método ".endswith()" es una herramienta sencilla y eficiente para validar el final de
cadenas de texto en Python."""

# Ejemplo_2_metodo_endswith.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene una frase.
Esta cadena de texto se utilizará para demostrar el funcionamiento del método ".endswith()".

A continuación, definimos  una  nueva  variable  llamada  "termina_con_sufijo"  y  le  asignamos  el
resultado de aplicar el método ".endswith()" a la variable "texto" con tres  argumentos:  el  sufijo
"cadena.", el índice de inicio 0 y el índice de fin 56.  Para  ello,  escribimos  el  nombre  de  la
variable seguido del método ".endswith()" y, dentro de los paréntesis, pasamos el sufijo como primer
argumento en forma de cadena entre comillas, el índice de inicio como segundo argumento en forma  de
número entero y el índice de fin como tercer argumento en forma  de  número  entero,  separados  por
comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar  si  la  cadena  termina  con  el  sufijo
"cadena." hasta el índice 56.

De esta forma, verificamos si la cadena termina con la  palabra  "cadena."  hasta  el  índice  56  y
obtenemos un resultado booleano que indica si la condición se cumple o no.

En este caso, el resultado será "True", ya que la cadena de texto termina con  el  sufijo  "cadena."
hasta el índice 56. Cuando decimos hasta el índice 56,  nos  referimos  a  que  la  verificación  se
realiza desde el inicio de la cadena hasta el índice 56, excluyendo este último,  lo  que  significa
que se evalúa si el sufijo "cadena." coincide con el final de  la  subcadena  especificada  por  los
índices de inicio y fin.

Esta cadena tiene un total de 56 caracteres, por lo que el índice 56  corresponde  al  final  de  la
cadena, mientras que el último carácter está en el índice 55 y es  el  punto  final  después  de  la
palabra "cadena". Por lo tanto, la verificación del  sufijo  se  realiza  correctamente  y  devuelve
"True"."""

# Código:
texto = "Ejemplo de texto para verificar un sufijo en una cadena."
termina_con_sufijo = texto.endswith("cadena.", 0, 56)
print(f"¿La cadena termina con el sufijo 'cadena.' hasta el índice 56? {termina_con_sufijo}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".endswith()" es sensible a mayúsculas y minúsculas,
por lo que "Cadena." y "cadena." se consideran diferentes. Si se  desea  realizar  una  verificación
insensible a mayúsculas y minúsculas, es necesario convertir ambas cadenas a un formato  consistente
utilizando los métodos ".lower()" o ".upper()" antes de realizar la comparación.

Además, este método no modifica la cadena original, ya que las cadenas  en  Python  son  inmutables.
Esto significa que siempre genera un valor booleano como resultado de su aplicación y  deja  intacta
la cadena original.

En cuanto a los índices de inicio y fin, si el índice de inicio es mayor que el índice  de  fin,  no
obtendremos un error, sino que el método evaluará la subcadena resultante, que puede  ser  vacía,  y
verificará si coincide con el sufijo. Por lo tanto, el resultado dependerá de si el sufijo  coincide
con la subcadena vacía o no. Si el índice de inicio es igual al índice de fin, tampoco  se  obtendrá
un error, ya que el método evaluará la subcadena vacía y  verificará  si  coincide  con  el  sufijo,
devolviendo "True" si el sufijo también es una cadena vacía.

El resultado de la verificación debe almacenarse en una variable si se desea utilizar posteriormente
en el código, o puede imprimirse directamente en la consola para una validación rápida.

Por último, el método ".endswith()" es ideal para validaciones rápidas, pero  no  es  adecuado  para
búsquedas más complejas dentro de una cadena. En esos casos, se deben considerar otros métodos, como
".find()" o las expresiones regulares, para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
