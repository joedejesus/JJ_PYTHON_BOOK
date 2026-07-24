# Enunciado:
"""El método ".index()" en Python se utiliza para encontrar la posición de la primera  aparición  de
un elemento en una tupla. Este método devuelve un número entero  que  representa  el  índice  de  la
primera coincidencia encontrada.

Este método evalúa la tupla completa o una subtupla especificada por los índices de inicio y fin,  y
devuelve el índice de la primera aparición del elemento  en  esa  sección.  Si  el  elemento  no  se
encuentra en la tupla, el método genera una excepción "ValueError".  Por  lo  tanto,  es  importante
manejar esta excepción si no se está seguro de que el elemento esté presente en la tupla.

El método ".index()" puede aplicarse a cualquier  objeto  de  tipo  tupla  en  Python,  como  tuplas
literales, variables que contienen tuplas o incluso resultados  de  otras  operaciones  que  generan
tuplas. Este método no modifica la tupla original, ya que las tuplas son inmutables, y  devuelve  un
valor que representa la posición del elemento  encontrado,  el  cual  se  almacena  en  la  variable
asignada al resultado de la aplicación del método.

El método ".index()" toma un elemento como argumento obligatorio y  dos  argumentos  opcionales:  el
índice de inicio y el índice de fin. Si no se especifican estos índices, se evalúa toda la tupla.

El primer argumento debe ser el elemento que se desea buscar y puede pasarse al  método  ya  sea  en
forma de variable, de valor literal o incluso como el resultado de  una  función.  Este  valor  debe
coincidir exactamente con el tipo de dato presente en la tupla, respetando la sintaxis y el formato,
ya que, de lo  contrario,  el  método  no  encontrará  la  coincidencia  y  generará  una  excepción
"ValueError".

El segundo y el tercer argumento deben ser números enteros que indican el índice de inicio y  el  de
fin, respectivamente. Si el índice de inicio es mayor que el índice de fin, la búsqueda se realizará
sobre una subtupla vacía y, si no hay coincidencias, el método generará una excepción "ValueError".

Por otro lado, es posible utilizar solo el índice de inicio. Si se  especifica  solo  el  índice  de
inicio, el método buscará el elemento desde ese índice hasta el final de la tupla. Sin  embargo,  no
es posible utilizar solo el índice de fin de forma posicional, ya que el método requiere  un  índice
de inicio para funcionar correctamente, a menos que se quiera evaluar toda la tupla; en ese caso, se
omiten ambos índices.

Por último, el método ".index()" es una herramienta útil para localizar la posición de  un  elemento
dentro de una tupla en Python, pero requiere precaución para  manejar  posibles  excepciones  si  el
elemento no está presente."""

# Ejemplo_metodo_index.py

# Explicación:
"""Definimos una variable llamada "tupla" y le asignamos una tupla que  contiene  varios  elementos.
Esta tupla se utilizará para demostrar el funcionamiento del método ".index()".

A continuación, definimos una nueva variable llamada "posicion"  y  le  asignamos  el  resultado  de
aplicar el método ".index()" a la variable "tupla" con tres  argumentos:  el  elemento  "texto",  el
índice de inicio 0 y el índice de fin 8. Para ello, escribimos el nombre de la variable seguido  del
nombre del método ".index()" y, dentro de los paréntesis, pasamos el elemento como primer argumento,
el índice de inicio como segundo argumento en forma de número entero y el índice de fin como  tercer
argumento en forma de número entero, separados por comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar la posición de la primera  aparición  del
elemento "texto" en la tupla hasta el índice 8.

De esta forma, hemos localizado la posición del elemento "texto" en la tupla, obteniendo  un  número
que indica el índice de la primera coincidencia encontrada. En este caso, el resultado  será  3,  ya
que el elemento "texto" aparece por primera vez en el índice 3 de la tupla."""

# Código:
tupla = (1, 2, 3, "texto", 5, 6, "texto", 8, 9)

posicion = tupla.index("texto", 0, 8)
print(f"El elemento 'texto' aparece por primera vez en el índice {posicion} de la tupla.")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".index()" es sensible a mayúsculas y minúsculas  en
el caso de las cadenas dentro de la tupla, por lo que "Texto" y "texto"  se  consideran  diferentes.
Además, el elemento que se busca debe coincidir exactamente con el  tipo  de  dato  presente  en  la
tupla, respetando la sintaxis y el formato, ya que, de lo contrario,  el  método  no  encontrará  la
coincidencia y generará una excepción "ValueError".

Este método no modifica la tupla original, ya que las tuplas son inmutables, y devuelve un valor que
representa la posición del elemento encontrado, el cual se  almacena  en  la  variable  asignada  al
resultado de la aplicación del método. Esto significa que  siempre  genera  un  número  entero  como
resultado de su aplicación, dejando intacta la tupla original.

Si el elemento no se encuentra en la tupla, el método genera  una  excepción  "ValueError".  Por  lo
tanto, es importante manejar esta excepción si no se está seguro de que el elemento esté presente en
la tupla. En este caso, se podría utilizar un bloque  "try-except"  para  capturar  la  excepción  y
manejarla de manera adecuada, como mostrar un mensaje de error o realizar una acción alternativa.

Además, este método solo devuelve la posición de la primera aparición del elemento en la tupla,  por
lo que, si el elemento aparece múltiples veces, solo se obtendrá el índice de la primera  ocurrencia
contando desde la posición de inicio especificada o, por defecto, desde el inicio de la tupla. Si se
desea obtener todas las posiciones de un elemento que aparece en la tupla varias veces,  se  deberán
utilizar otros métodos compatibles con tuplas o estructuras de datos como  listas  para  lograr  ese
resultado de manera más eficiente.

Por último, el método ".index()" es ideal para localizar la posición de  un  elemento,  pero  no  es
adecuado para realizar búsquedas más complejas  dentro  de  una  tupla.  En  esos  casos,  se  deben
considerar otros métodos o estructuras de datos para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────