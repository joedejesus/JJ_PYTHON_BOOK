# Enunciado:
"""El método ".index()" en Python se utiliza para encontrar la posición de la primera  aparición  de
un elemento en una lista. Este método devuelve un número entero  que  representa  el  índice  de  la
primera coincidencia encontrada.

El método ".index()" evalúa la lista completa o una sublista especificada por los índices de  inicio
y fin, y devuelve el índice de la primera aparición del elemento en esa sección. Si el  elemento  no
se encuentra en la lista, el método genera una excepción "ValueError". Por lo tanto,  es  importante
manejar esta excepción si no se tiene la seguridad de que el elemento esté presente en la lista.

El método ".index()" puede aplicarse a cualquier  objeto  de  tipo  lista  en  Python,  como  listas
literales, variables que contienen listas o incluso resultados  de  otras  operaciones  que  generan
listas. Este método no modifica la lista original y devuelve un valor que representa la posición del
elemento encontrado, el cual se almacena en la variable asignada al resultado de la  aplicación  del
método.

El método ".index()" toma un elemento como argumento obligatorio y  dos  argumentos  opcionales:  el
índice de inicio y el índice de fin. Si no se especifican los índices, se evalúa toda la lista.

El primer argumento debe ser el elemento que se desea buscar, y puede pasarse al método  ya  sea  en
forma de variable, como valor literal o incluso como el resultado de una función.  Este  valor  debe
coincidir exactamente con el tipo de dato presente en la lista, respetando la sintaxis y el formato,
ya que, de lo  contrario,  el  método  no  encontrará  la  coincidencia  y  generará  una  excepción
"ValueError".

El segundo argumento y el tercer argumento deben ser números enteros que indican el índice de inicio
y de fin, respectivamente. Si el índice de inicio es mayor que el índice  de  fin,  la  búsqueda  se
realiza sobre una sublista vacía y, al no encontrarse coincidencias, el método genera una  excepción
"ValueError".

Por otro lado, es posible utilizar solo el índice de inicio. Si se  especifica  solo  el  índice  de
inicio, el método buscará el elemento desde ese índice hasta el final de la lista. Sin  embargo,  no
es posible utilizar solo el índice de fin, ya que el  método  requiere  un  índice  de  inicio  para
funcionar correctamente, a menos que se quiera evaluar toda la lista; en ese caso, se  omiten  ambos
índices.

Por último, el método ".index()" es una herramienta útil para localizar la posición de  un  elemento
dentro de una lista en Python, pero requiere  precaución  al  manejar  posibles  excepciones  si  el
elemento no está presente."""

# Ejemplo_1_metodo_index.py

# Explicación:
"""Definimos una variable llamada "lista" y le asignamos una lista que  contiene  varios  elementos.
Esta lista se utilizará para demostrar el funcionamiento del método ".index()".

A continuación, definimos una nueva variable llamada "posicion"  y  le  asignamos  el  resultado  de
aplicar el método ".index()" a la variable "lista" con tres  argumentos:  el  elemento  "texto",  el
índice de inicio 0 y el índice de fin 8. Para ello, escribimos el nombre de la variable seguido  del
nombre del método ".index()" y, dentro de los paréntesis, pasamos el elemento como primer argumento,
el índice de inicio como segundo argumento en forma de número entero y el índice de fin como  tercer
argumento, también en forma de número entero, separados por comas.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string", para indicar la posición de la primera  aparición  del
elemento "texto" en la lista dentro del rango evaluado, que llega hasta el índice 8 sin incluirlo.

De esta forma, hemos localizado la posición del  elemento  "texto"  en  la  lista  sin  modificarla,
obteniendo un número que indica el índice de la primera coincidencia encontrada. En  este  caso,  el
resultado será 3, ya que el elemento "texto" aparece por primera vez en el índice 3 de la lista."""

# Código:
lista = [1, 2, 3, "texto", 5, 6, "texto", 8, 9]

posicion = lista.index("texto", 0, 8)
print(f"El elemento 'texto' aparece por primera vez en el índice {posicion} de la lista.")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".index()" distingue entre mayúsculas  y  minúsculas
en el caso de las cadenas dentro de la lista, por lo que "Texto" y "texto" se consideran diferentes.
Además, el elemento que se busca debe coincidir exactamente con el  tipo  de  dato  presente  en  la
lista, respetando la sintaxis y el formato, ya que, de lo contrario,  el  método  no  encontrará  la
coincidencia y generará una excepción "ValueError".

Este método no modifica la lista original y  devuelve  un  valor  que  representa  la  posición  del
elemento encontrado, el cual se almacena en la variable asignada al resultado de la  aplicación  del
método. Esto significa que siempre genera un número entero como resultado de su aplicación,  dejando
intacta la lista original.

Si el elemento no se encuentra en la lista, el método genera  una  excepción  "ValueError".  Por  lo
tanto, es importante manejar esta excepción si no se tiene la seguridad  de  que  el  elemento  esté
presente en la lista. En este caso, se podría utilizar  un  bloque  "try-except"  para  capturar  la
excepción y manejarla de manera adecuada, como mostrar un mensaje de error  o  realizar  una  acción
alternativa.

Además, este método solo devuelve la posición de la primera aparición del elemento en la lista,  por
lo que, si el elemento aparece múltiples veces, solo se obtendrá el índice de la primera  ocurrencia
contando desde la posición de inicio especificada o, por defecto, desde el inicio de la lista. Si se
desea obtener todas las posiciones de un elemento que aparece en la lista varias  veces,  se  deberá
utilizar un bucle o una comprensión de listas para recorrer la lista  y  almacenar  los  índices  de
todas las apariciones del elemento.

Por último, el método ".index()" es ideal para localizar la posición de  un  elemento,  pero  no  es
adecuado para realizar búsquedas más complejas  dentro  de  una  lista.  En  esos  casos,  se  deben
considerar otros métodos o estructuras de datos para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
