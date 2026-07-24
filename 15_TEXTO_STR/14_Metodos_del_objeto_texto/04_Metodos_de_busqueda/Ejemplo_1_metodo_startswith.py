# Enunciado:
"""El método ".startswith()" en Python se utiliza para verificar si una cadena de texto comienza con
un prefijo específico. Este método devuelve un valor booleano: "True" si la cadena comienza  con  el
prefijo especificado y "False" en caso contrario.

Este método evalúa si el prefijo indicado coincide exactamente con el inicio de la cadena o  con  el
inicio de una subcadena especificada por los índices de inicio y fin, devolviendo "True"  si  existe
una coincidencia exacta.

Este método se aplica sobre una cadena de texto y devuelve un valor booleano que indica si la cadena
comienza con el prefijo especificado como argumento. Este método se puede aplicar a cualquier objeto
de tipo texto, incluyendo variables que contengan texto o el  resultado  de  otras  operaciones  que
generen texto. Además, no modifica la cadena original, ya que las cadenas en Python son  inmutables.
Esto significa que siempre genera un valor booleano como resultado de su aplicación, dejando intacta
la cadena original.

El método ".startswith()" puede recibir uno, dos o tres argumentos. El primero es el prefijo que  se
desea verificar y es obligatorio. El segundo argumento es un índice de inicio  opcional  que  indica
desde qué posición de la cadena se debe realizar la verificación del prefijo. El tercer argumento es
un índice de fin opcional  que  indica  hasta  qué  posición  de  la  cadena  se  debe  realizar  la
verificación del prefijo.

El primer argumento puede ser una cadena de texto literal, una variable que contenga texto o incluso
el resultado de una operación que genere texto. El segundo argumento debe ser un número  entero  que
representa el índice de inicio desde el cual se desea  realizar  la  verificación  del  prefijo.  El
tercer argumento debe ser un número entero que representa el índice de fin hasta el  cual  se  desea
realizar la verificación del prefijo.

Además, es importante destacar que, si se proporciona el argumento  de  inicio,  no  es  obligatorio
proporcionar también el argumento de fin.  Si  solo  se  proporciona  el  argumento  de  inicio,  la
verificación se realiza desde esa posición hasta el final de la cadena.  Si  se  proporcionan  ambos
argumentos, la verificación se realiza desde el índice de inicio hasta el índice de fin,  excluyendo
este último.

Este método es útil para realizar validaciones rápidas en cadenas de texto,  como  verificar  si  un
texto tiene un prefijo específico, si una "URL" comienza con un esquema particular  o  si  un  texto
cumple con un formato  esperado.  Además,  no  realiza  comparaciones  insensibles  a  mayúsculas  y
minúsculas, ya que la comparación es sensible a estas. Si se necesita una comparación  insensible  a
mayúsculas y minúsculas, se debe convertir la cadena y el prefijo a minúsculas o mayúsculas antes de
usar el método.

Por último, el método ".startswith()" es una herramienta sencilla y eficiente para validar el inicio
de cadenas de texto en Python."""

# Ejemplo_1_metodo_startswith.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene una frase.
Esta cadena de texto se utilizará para demostrar el funcionamiento del método ".startswith()".

A continuación, definimos una nueva  variable  llamada  "comienza_con_prefijo"  y  le  asignamos  el
resultado de aplicar el método ".startswith()" a la variable "texto" con tres argumentos: el prefijo
"Ejemplo", el índice de inicio 0 y el índice de fin  7.  Para  ello,  escribimos  el  nombre  de  la
variable seguido del nombre del método ".startswith()" y,  dentro  de  los  paréntesis,  pasamos  el
prefijo como primer argumento en forma de cadena entre comillas, el índice de  inicio  como  segundo
argumento en forma de número entero y el índice de fin como tercer  argumento  en  forma  de  número
entero, separados por comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar si la  cadena  comienza  con  el  prefijo
"Ejemplo" hasta el índice 7.

De esta forma, hemos verificado si la cadena comienza con la palabra "Ejemplo" hasta  el  índice  7,
obteniendo un resultado booleano que indica si la condición se cumple o no.

En este caso, el resultado será "True", ya que la cadena de texto comienza con el prefijo  "Ejemplo"
hasta el índice 7. Cuando decimos hasta el índice 7, nos referimos a que la verificación se  realiza
desde el inicio de la cadena hasta el índice 7, excluyendo este último,  lo  que  significa  que  se
evalúa si el prefijo "Ejemplo" coincide con el inicio de la subcadena especificada por  los  índices
de inicio y fin.

Esta cadena tiene un total de 57 caracteres, pero solo evaluamos  los  primeros  7  caracteres  para
verificar si coinciden con el prefijo especificado. Por lo tanto, la  verificación  del  prefijo  se
realiza correctamente y devuelve "True"."""

# Código:
texto = "Ejemplo de texto para verificar un prefijo en una cadena."
comienza_con_prefijo = texto.startswith("Ejemplo", 0, 7)
print(f"¿La cadena comienza con el prefijo 'Ejemplo' hasta el índice 7? {comienza_con_prefijo}")

# Nota Muy Importante:
"""Es fundamental tener en  cuenta  que  el  método  ".startswith()"  es  sensible  a  mayúsculas  y
minúsculas, por lo que "ejemplo" y "Ejemplo" se consideran diferentes.  Si  se  desea  realizar  una
verificación insensible a mayúsculas y minúsculas, es necesario convertir ambas cadenas a un formato
consistente utilizando el método ".lower()" o ".upper()" antes de realizar la comparación.

Además, este método no modifica la cadena original, ya que las cadenas  en  Python  son  inmutables.
Esto significa que siempre genera un valor booleano como resultado de su aplicación, dejando intacta
la cadena original.

En cuanto al índice de inicio y fin, si el índice de inicio es  mayor  que  el  índice  de  fin,  no
obtendremos un error, sino que el método evaluará la subcadena resultante, que puede  ser  vacía,  y
verificará si coincide con el prefijo. Por lo  tanto,  el  resultado  dependerá  de  si  el  prefijo
coincide con la subcadena vacía o no. Si el índice de inicio es igual al índice de fin,  tampoco  se
obtendrá un error, ya que el método evaluará la subcadena vacía y  verificará  si  coincide  con  el
prefijo, devolviendo "True" si el prefijo también es una cadena vacía.

Por otro lado, el resultado de la  verificación  debe  almacenarse  en  una  variable  si  se  desea
utilizarlo posteriormente en el código, o puede imprimirse  directamente  en  la  consola  para  una
validación rápida.

Por último, el método ".startswith()" es ideal para validaciones rápidas, pero no es  adecuado  para
búsquedas más complejas dentro de una cadena. En esos casos, se deben considerar otros métodos, como
".find()" o las expresiones regulares, para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
