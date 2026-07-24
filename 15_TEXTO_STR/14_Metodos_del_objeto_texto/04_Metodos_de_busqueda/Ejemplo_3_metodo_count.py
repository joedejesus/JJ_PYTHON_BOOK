# Enunciado:
"""El método ".count()" en Python se utiliza para contar el número de veces que un subtexto  aparece
en una cadena de texto. Este método  devuelve  un  número  entero  que  representa  la  cantidad  de
coincidencias encontradas.

Este método evalúa la cadena completa o una subcadena especificada por los índices de inicio y  fin,
y devuelve el número de veces que el subtexto aparece en esa sección. Este método puede aplicarse  a
cualquier objeto de tipo texto en Python, ya sea una variable, una cadena literal o el resultado  de
una función que devuelva un texto. Además, este método no modifica la cadena original,  ya  que  las
cadenas en Python son inmutables.

El método ".count()" toma un subtexto como argumento obligatorio y  dos  argumentos  opcionales:  el
índice de inicio y el índice de fin. Si no se especifican los índices, se evalúa toda la cadena.  El
primer argumento debe ser una cadena de texto que represente el subtexto que  se  desea  contar.  El
segundo y el tercer argumento deben ser números enteros que indican  el  índice  de  inicio  y  fin,
respectivamente.

Además, si el índice de inicio es mayor que el índice de fin, el método devolverá 0, ya que  no  hay
coincidencias en una subcadena vacía. Por otro lado, es posible utilizar solo el índice  de  inicio.
Si se especifica solo el índice de inicio, el método contará las ocurrencias del subtexto desde  ese
índice hasta el final de la cadena. Sin embargo, no es posible utilizar solo el  índice  de  fin  de
forma posicional, ya que el método requiere un índice de inicio para funcionar correctamente. Si  se
quiere evaluar toda la cadena, se omiten ambos índices.

Por último, el método ".count()" es una herramienta sencilla y eficiente para contar ocurrencias  de
subtextos en cadenas de texto en Python, lo que lo hace  útil  para  realizar  análisis  rápidos  de
texto, como contar palabras, caracteres o patrones específicos dentro de una cadena."""

# Ejemplo_3_metodo_count.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene una frase.
Esta cadena de texto se utilizará para demostrar el funcionamiento del método ".count()".

A continuación, definimos una nueva variable llamada "ocurrencias" y le asignamos  el  resultado  de
aplicar el método ".count()" a la variable "texto" con tres  argumentos:  el  subtexto  "texto",  el
índice de inicio 0 y el índice de fin 92. Para ello, escribimos el nombre de la variable seguido del
nombre del método ".count()", y dentro de los paréntesis, pasamos el subtexto como primer  argumento
en forma de cadena entre comillas, el índice de inicio como segundo argumento  en  forma  de  número
entero y el índice de fin como tercer argumento en forma de número entero, separados por comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola acompañado de un
mensaje descriptivo en formato "f-string" para indicar cuántas veces aparece el subtexto "texto"  en
la cadena hasta antes del índice 92.

De esta forma, hemos contado las ocurrencias del subtexto "texto" en la cadena, obteniendo un número
que indica la cantidad de coincidencias encontradas. En este caso, el resultado será 2,  ya  que  el
subtexto "texto" aparece dos veces en la cadena antes del índice 92."""

# Código:
texto = "Ejemplo de texto para contar el número de veces que aparece la palabra texto en esta cadena."
ocurrencias = texto.count("texto", 0, 92)
print(f"El subtexto 'texto' aparece {ocurrencias} veces en la cadena hasta el índice 92.")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".count()" es sensible a  mayúsculas  y  minúsculas,
por lo que "Texto" y "texto" se consideran diferentes. Si se desea realizar una búsqueda  insensible
a mayúsculas y minúsculas, es necesario convertir ambas cadenas a un formato consistente  utilizando
el método ".lower()" o ".upper()" antes de realizar la comparación.

Además, este método no modifica la cadena original, ya que las cadenas  en  Python  son  inmutables.
Esto significa que siempre genera un número entero como resultado de su aplicación, dejando  intacta
la cadena original, por lo que es recomendable almacenar el resultado de la búsqueda en una variable
para su posterior uso o imprimirlo directamente en la consola para una comprobación rápida.

Por otro lado, hay que tener en cuenta que es posible evaluar el número de  caracteres,  ya  que  un
carácter dentro de una cadena también se considera un subtexto. Por ejemplo, si se cuenta el  número
de veces que aparece la letra "a" en una cadena, el método ".count()" devolverá el número  de  veces
que esa letra aparece, incluso si es parte de una palabra más grande.

Estos caracteres pueden ser letras, números, espacios  o  cualquier  otro  símbolo  presente  en  la
cadena, lo que permite realizar análisis detallados de la composición  de  la  cadena,  como  contar
espacios para determinar el número de palabras o contar  caracteres  específicos  para  análisis  de
frecuencia.

Por último, el método ".count()" es ideal para análisis rápidos, pero no es adecuado para  búsquedas
más complejas dentro de una cadena. En esos casos, se deben considerar otros métodos como  ".find()"
o expresiones regulares para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
