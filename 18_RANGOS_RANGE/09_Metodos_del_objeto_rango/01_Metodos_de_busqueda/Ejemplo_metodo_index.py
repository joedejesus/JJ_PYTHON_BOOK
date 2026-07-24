# Enunciado:
"""El método ".index()" en Python se utiliza para encontrar la posición de la primera  aparición  de
un elemento en una secuencia, como listas o tuplas. En el caso de los objetos de  tipo  rango,  este
método está disponible desde Python 3.3 y devuelve un número entero que representa el índice  de  la
coincidencia encontrada.

En los rangos, el método evalúa la secuencia generada y devuelve  el  índice  de  la  aparición  del
elemento buscado. Si el elemento no se  encuentra  en  el  rango,  el  método  genera  la  excepción
"ValueError". Por lo tanto, es importante manejar esta excepción si no se tiene la seguridad de  que
el elemento esté presente en el rango.

El método ".index()" puede aplicarse a cualquier objeto de tipo rango, ya sea un rango literal,  una
variable que contenga un rango o el resultado de una operación que genere un rango. Este  método  no
modifica el rango original, ya que los rangos son inmutables, y devuelve un valor que representa  la
posición del elemento encontrado, el cual se almacena en la variable asignada  al  resultado  de  la
aplicación del método.

En el caso de los rangos, el método ".index()" toma un único argumento obligatorio: el elemento  que
se desea buscar dentro del rango. A diferencia de lo que ocurre  con  listas  o  tuplas,  el  método
".index()" en rangos no acepta argumentos adicionales para especificar un rango de búsqueda  (inicio
y fin); solo acepta el elemento a buscar.

Además, este argumento debe ser el elemento que se desea buscar y puede pasarse al método  en  forma
de variable, de valor literal o incluso como resultado de una función. Este valor debe  corresponder
con un valor que pueda encontrarse dentro del rango; de lo contrario, el  método  no  encontrará  la
coincidencia y generará la excepción "ValueError".

Es importante tener en cuenta que los rangos solo pueden contener números enteros,  por  lo  que  el
elemento a buscar debe corresponder a un  valor  entero  para  que  el  método  ".index()"  funcione
correctamente. Si se intenta buscar un elemento de otro tipo, como una cadena o  un  número  decimal
que no coincida con un valor del rango, el método  no  encontrará  la  coincidencia  y  generará  la
excepción "ValueError".

Por último, el método ".index()" es una herramienta útil para localizar la posición de  un  elemento
dentro de un rango en Python, pero requiere precaución  para  manejar  posibles  excepciones  si  el
elemento no está presente."""

# Ejemplo_metodo_index.py

# Explicación:
"""Definimos una variable llamada "rango" y le asignamos  un  rango  que  genera  una  secuencia  de
números del 1 al 9. Este rango se utilizará para demostrar el funcionamiento del método ".index()".

A continuación, definimos una nueva variable llamada "posicion"  y  le  asignamos  el  resultado  de
aplicar el método ".index()" a la variable "rango" con un  argumento:  el  elemento  4.  Para  ello,
escribimos el nombre de la variable seguido del método  ".index()"  y,  dentro  de  los  paréntesis,
pasamos el elemento como argumento.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" que indica la posición en la que aparece el elemento  4
en el rango.

De esta forma, hemos localizado la posición del elemento 4 en el rango,  obteniendo  un  número  que
indica el índice de la coincidencia encontrada. En este  caso,  el  resultado  será  3,  ya  que  el
elemento 4 aparece en el índice 3 del rango."""

# Código:
rango = range(1, 10)

posicion = rango.index(4)
print(f"El elemento 4 aparece por primera vez en el índice {posicion} del rango.")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".index()" requiere que el  elemento  que  se  busca
corresponda a un valor  presente  en  el  rango;  de  lo  contrario,  el  método  no  encontrará  la
coincidencia y generará la excepción "ValueError".

Este método no modifica el rango original, ya que los rangos son inmutables, y devuelve un valor que
representa la posición del elemento encontrado, el cual se  almacena  en  la  variable  asignada  al
resultado de la aplicación del método. Esto significa que  siempre  genera  un  número  entero  como
resultado de su aplicación, dejando intacto el rango original.

Si el elemento no se encuentra en el rango, el método  genera  la  excepción  "ValueError".  Por  lo
tanto, es importante manejar esta excepción si no se tiene la seguridad  de  que  el  elemento  esté
presente en el rango. En este caso, se podría utilizar  un  bloque  "try-except"  para  capturar  la
excepción y manejarla de manera adecuada, como mostrar un mensaje de error  o  realizar  una  acción
alternativa.

Es importante destacar que, si se utilizan rangos con pasos, los elementos omitidos por el  paso  no
se incluirán en el rango, por lo que no podrán ser encontrados por el método ".index()". Si se busca
un elemento que no está presente en el rango, se generará una excepción de tipo "ValueError".

Por ejemplo, si se tiene un rango definido como "range(0, 11, 2)" y se intenta encontrar la posición
del elemento "5" utilizando el método ".index()", se generará un error de tipo "ValueError",  porque
el elemento "5" no forma parte del rango generado.

Además, en los objetos de tipo rango, cada elemento es único dentro de la secuencia generada, por lo
que el método ".index()" siempre devolverá la posición de ese único elemento si existe. Si se  desea
obtener todas las posiciones de un elemento en una secuencia, esto solo tendría sentido en listas  o
tuplas, donde puede haber elementos repetidos.

En un solo objeto rango no puede haber elementos duplicados, ya  que  cada  valor  es  único  en  la
secuencia generada. Sin embargo, si se fusionan dos o más rangos concatenando sus secuencias, sí  es
posible obtener una secuencia con elementos duplicados y, en ese caso, el método ".index()" aplicado
a la secuencia resultante devolverá la posición de la primera aparición del elemento repetido.

Por último, el método ".index()" es ideal para localizar la posición de  un  elemento,  pero  no  es
adecuado para realizar búsquedas más  complejas  dentro  de  un  rango.  En  esos  casos,  se  deben
considerar otros métodos o estructuras de datos para lograr el resultado deseado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────