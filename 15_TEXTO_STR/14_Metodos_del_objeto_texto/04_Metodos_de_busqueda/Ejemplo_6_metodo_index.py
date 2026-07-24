# Enunciado:
"""El método ".index()" en Python se utiliza para encontrar la posición de la primera  aparición  de
un subtexto en una cadena de texto. Este método devuelve un número entero que representa  el  índice
de la primera coincidencia encontrada.

Si el subtexto no se encuentra en la cadena, el método genera una  excepción  "ValueError".  Por  lo
tanto, es importante manejar esta excepción si no se está seguro de que el subtexto esté presente en
la cadena.

Este método evalúa la cadena completa o una subcadena especificada por los índices de inicio y  fin,
devolviendo el índice de la primera aparición  del  subtexto  en  esa  sección.  Este  método  puede
aplicarse a cualquier objeto de tipo texto en Python, ya sea una variable, una cadena literal  o  el
resultado de una función que devuelva un texto. Además, este método no modifica la cadena  original,
ya que las cadenas en Python son inmutables.

El método ".index()" toma un subtexto como argumento obligatorio y  dos  argumentos  opcionales:  el
índice de inicio y el índice de fin. Si no se especifican los índices, se evalúa toda la cadena.  El
primer argumento debe ser una cadena de texto que represente el subtexto que se desea buscar, ya sea
en forma de variable, de cadena literal o incluso como el resultado de una función que  devuelva  un
texto. El segundo y el tercer argumento deben ser números enteros que indiquen el índice de inicio y
el índice de fin, respectivamente.

Además, si el índice de inicio es mayor que el índice de fin, el método no encontrará  coincidencias
en esa subcadena. Por otro lado, es posible utilizar solo el índice de inicio. Si se especifica solo
el índice de inicio, el método buscará el subtexto desde ese índice hasta el final de la cadena. Sin
embargo, no es posible pasar únicamente el índice de fin como argumento  posicional,  ya  que  antes
debe indicarse el índice de inicio; a menos que se quiera evaluar toda la cadena, en  cuyo  caso  se
omiten ambos índices.

Es importante destacar que la diferencia entre el método ".index()" y el método ".find()" es que  el
primero genera una excepción si el subtexto no se encuentra, mientras que el segundo  devuelve  "-1"
en ese caso. Ambos métodos funcionan de manera similar para localizar la  posición  de  un  subtexto
dentro de una cadena de texto en Python, pero es importante elegir  el  método  adecuado  según  las
necesidades del programa y manejar las posibles excepciones de forma adecuada para evitar errores en
la ejecución del código.

Por último, el método ".index()" es una herramienta útil para localizar la posición de  un  subtexto
dentro de una cadena de texto en Python, pero requiere precaución para manejar posibles  excepciones
si el subtexto no está presente."""

# Ejemplo_6_metodo_index.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene una frase.
Esta cadena de texto se utilizará para demostrar el funcionamiento del método ".index()".

A continuación, definimos una nueva variable llamada "posicion"  y  le  asignamos  el  resultado  de
aplicar el método ".index()" a la variable "texto" con tres  argumentos:  el  subtexto  "texto",  el
índice de inicio 0 y el índice de fin 60. Para ello, escribimos el nombre de la variable seguido del
nombre del método ".index()" y, dentro de los paréntesis, pasamos el subtexto como primer  argumento
en forma de cadena entre comillas, el índice de inicio como segundo argumento  en  forma  de  número
entero y el índice de fin como tercer argumento en forma de número entero, separados por comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar la posición de la primera  aparición  del
subtexto "texto" en la cadena hasta el índice 60.

De esta forma, hemos localizado la posición del subtexto "texto" en la cadena, obteniendo un  número
que indica el índice de la primera coincidencia encontrada. En este caso, el resultado será  11,  ya
que el subtexto "texto" aparece por primera vez en el índice 11 de la cadena."""

# Código:
texto = "Esto es un texto que contiene la palabra texto varias veces."
posicion = texto.index("texto", 0, 60)
print(f"El subtexto 'texto' aparece por primera vez en el índice {posicion} de la cadena hasta el índice 60.")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".index()" es sensible a  mayúsculas  y  minúsculas,
por lo que "Texto" y "texto" se consideran diferentes. Si se desea realizar una búsqueda  insensible
a mayúsculas y minúsculas, es necesario convertir ambas cadenas a un formato consistente  utilizando
el método ".lower()" o ".upper()" antes de realizar la comparación.

Además, este método no modifica la cadena original, ya que las cadenas  en  Python  son  inmutables.
Esto significa que devuelve un número entero como resultado de su  aplicación,  dejando  intacta  la
cadena original.

Si el subtexto no se encuentra en la cadena, el método genera una  excepción  "ValueError".  Por  lo
tanto, es importante manejar esta excepción si no se está seguro de que el subtexto esté presente en
la cadena. En este caso, se podría utilizar un bloque "try-except"  para  capturar  la  excepción  y
manejarla de manera adecuada, como mostrar un mensaje de error o realizar una acción alternativa.

Sin embargo, si se desea evitar la generación de excepciones, se puede utilizar el método ".find()",
que devuelve "-1" en caso de no encontrar el subtexto, lo que permite manejar la situación de manera
más sencilla sin necesidad de capturar excepciones.

Por último, el método ".index()" es ideal para localizar la posición de  un  subtexto,  pero  no  es
adecuado para realizar búsquedas más complejas dentro  de  una  cadena.  En  esos  casos,  se  deben
considerar otros métodos o expresiones regulares para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
