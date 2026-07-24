# Enunciado:
"""El método ".find()" en Python se utiliza para buscar la primera aparición de un  subtexto  dentro
de una cadena de texto. Este método devuelve un número entero que representa el índice de la primera
coincidencia encontrada, o "-1" si el subtexto no se encuentra en la cadena.

Este método evalúa la cadena completa o una subcadena especificada por los índices de inicio y  fin,
devolviendo el índice de la primera aparición  del  subtexto  en  esa  sección.  Este  método  puede
aplicarse a cualquier objeto de tipo texto en Python, ya sea una variable, una cadena literal  o  el
resultado de una función que devuelva un texto. Además, este método no modifica la cadena  original,
ya que las cadenas en Python son inmutables.

El método ".find()" toma un subtexto como argumento obligatorio  y  dos  argumentos  opcionales:  el
índice de inicio y el índice de fin. Si no se especifican los índices, se evalúa toda la cadena.  El
primer argumento debe ser una cadena de texto que represente el subtexto que se desea buscar, ya sea
en forma de variable, cadena literal o resultado de una función que devuelva un texto. El segundo  y
el tercer argumento deben ser números enteros que indiquen el índice de inicio y el índice  de  fin,
respectivamente.

Además, si el índice de inicio es mayor que el índice de fin, el método devolverá "-1",  ya  que  no
hay coincidencias en una subcadena vacía. Por otro lado, es  posible  utilizar  solo  el  índice  de
inicio. Si se especifica solo el índice de inicio, el método buscará el subtexto  desde  ese  índice
hasta el final de la cadena. Sin embargo, no es posible utilizar solo el  índice  de  fin  de  forma
posicional, ya que, para ello, también debe indicarse el índice de inicio o,  si  se  desea  evaluar
toda la cadena, deben omitirse ambos índices.

Por último, el método ".find()" es una herramienta sencilla y eficiente  para  buscar  subtextos  en
cadenas de texto en Python, lo que lo hace útil  para  realizar  análisis  rápidos  de  texto,  como
localizar palabras, caracteres o patrones específicos dentro de una cadena."""

# Ejemplo_4_metodo_find.py

# Explicación:
"""Definimos una variable llamada "texto" y le asignamos una cadena de texto que contiene una frase.
Esta cadena de texto se utilizará para demostrar el funcionamiento del método ".find()".

A continuación, definimos una nueva variable llamada "indice" y le asignamos el resultado de aplicar
el método ".find()" a la variable "texto" con tres argumentos: el subtexto  "texto",  el  índice  de
inicio 0 y el índice de fin 60. Para ello, escribimos el nombre de la variable  seguido  del  nombre
del método ".find()" y, dentro de los paréntesis, pasamos el subtexto como primer argumento en forma
de cadena entre comillas, el índice de inicio como segundo argumento en forma de número entero y  el
índice de fin como tercer argumento en forma de número entero, separados por comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar el índice de  la  primera  aparición  del
subtexto "texto" en la cadena hasta el índice 60.

De esta forma, hemos localizado la primera aparición del subtexto "texto" en la  cadena,  obteniendo
un número que indica el índice de la coincidencia encontrada. En este caso, el resultado será 11, ya
que el subtexto "texto" aparece por primera vez en el índice 11 de la cadena."""

# Código:
texto = "Esto es un texto que contiene la palabra texto varias veces."
indice = texto.find("texto", 0, 60)
print(f"El subtexto 'texto' aparece por primera vez en el índice {indice} de la cadena hasta el índice 60.")

# Nota Importante:
"""Es fundamental tener en cuenta que el método ".find()" es sensible a mayúsculas y minúsculas, por
lo que "Texto" y "texto" se consideran diferentes. Si se desea realizar una  búsqueda  insensible  a
mayúsculas y minúsculas, es necesario convertir ambas cadenas a un formato consistente utilizando el
método ".lower()" o ".upper()" antes de realizar la comparación.

Además, este método no modifica la cadena original, ya que las cadenas  en  Python  son  inmutables.
Esto significa que siempre genera un número entero como resultado de su aplicación, dejando  intacta
la cadena original, por lo que es recomendable almacenar el resultado de la búsqueda en una variable
para su uso posterior o imprimirlo directamente en la consola para una comprobación rápida.

Por otro lado, hay que tener en cuenta que es posible obtener el índice de  caracteres,  ya  que  un
carácter dentro de una cadena también se considera un subtexto. Por ejemplo, si se busca  el  índice
de la letra "a" en una cadena, el método ".find()" devolverá el índice de la  primera  vez  que  esa
letra aparece, incluso si forma parte de una palabra más grande.

Estos caracteres pueden ser letras, números, espacios  o  cualquier  otro  símbolo  presente  en  la
cadena, lo que permite realizar análisis detallados de su composición, como localizar espacios  para
determinar el inicio de palabras o buscar caracteres específicos para analizar su posición.

Por último, el método ".find()" es ideal para análisis rápidos, pero no es adecuado  para  búsquedas
más complejas dentro de una cadena. En esos casos, deben considerarse otros  métodos  o  expresiones
regulares para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
