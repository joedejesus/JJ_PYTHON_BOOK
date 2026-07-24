# Enunciado:
"""El método ".get()" en Python se utiliza para acceder al valor asociado a una clave dentro  de  un
diccionario. Este método devuelve el valor correspondiente a la clave especificada  sin  generar  un
error si la clave no existe, lo que lo convierte en una herramienta segura y flexible para acceder a
datos almacenados en diccionarios.

El método ".get()" busca la clave indicada en el diccionario y devuelve el valor asociado a ella. Si
la clave no se encuentra en el diccionario, el  método  devuelve  "None"  por  defecto  o  un  valor
alternativo si se especifica como segundo argumento. Esto evita errores de tipo "KeyError",  que  sí
ocurren cuando se intenta acceder a una clave inexistente mediante el operador de indexación [].

Este método puede aplicarse a cualquier objeto de tipo  diccionario  en  Python,  como  diccionarios
literales, variables que contienen diccionarios  o  incluso  resultados  de  otras  operaciones  que
generan diccionarios. Este método no modifica el  diccionario  original  y  devuelve  un  valor  que
representa el contenido asociado a la clave buscada, el cual se almacena en la variable asignada  al
resultado de la aplicación del método.

El método ".get()" toma un argumento obligatorio, que  es  la  clave  que  se  desea  buscar,  y  un
argumento opcional, que es el valor por defecto que se devolverá si la clave no  existe.  Si  no  se
especifica este segundo argumento, el método devolverá "None" cuando la clave no esté presente en el
diccionario.

El primer argumento debe ser la clave que se desea buscar, y puede pasarse al método ya sea en forma
de variable, de valor literal o incluso como resultado de una función.  Este  valor  debe  coincidir
exactamente con la clave presente en el diccionario, respetando la sintaxis y el formato, ya que, de
lo contrario, el método no encontrará coincidencia y devolverá el valor por defecto.

Por último, el método ".get()" es una herramienta útil para acceder de manera segura a  los  valores
de un diccionario en Python, evitando errores y permitiendo especificar valores alternativos  cuando
la clave no está presente."""

# Ejemplo_1_metodo_get.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario  que  contiene  varios
pares clave-valor. Este diccionario  se  utilizará  para  demostrar  el  funcionamiento  del  método
".get()".

A continuación, definimos una nueva variable llamada "resultado" y  le  asignamos  el  resultado  de
aplicar el método ".get()" a la variable "diccionario" con dos argumentos: la clave "c" y  el  valor
por defecto "Clave no encontrada". Para ello, escribimos el nombre de la variable seguido del nombre
del método ".get()" y, dentro de los paréntesis, pasamos la clave como primer argumento y  el  valor
por defecto como segundo argumento, separados por una coma.

Por último, utilizamos la función "print()" para mostrar el resultado en la consola,  acompañado  de
un mensaje descriptivo en formato "f-string" para indicar el valor asociado a  la  clave  "c"  o  el
valor por defecto si la clave no existe.

De esta forma, hemos accedido al valor asociado a la clave "c" en el  diccionario  sin  modificarlo,
obteniendo un resultado seguro incluso si la clave no estuviera presente."""

# Código:
diccionario = {"a": 1, "b": 2, "c": "texto", "d": 4}

resultado = diccionario.get("c", "Clave no encontrada")
print(f"El valor asociado a la clave 'c' es: {resultado}")

# Nota Muy Importante:
"""Es fundamental tener en cuenta que el método ".get()" no genera errores si la clave no existe  en
el diccionario. En su lugar, devuelve "None" o el valor por defecto especificado. Esto lo  convierte
en una alternativa segura al operador de indexación [], que sí genera un error "KeyError" cuando  la
clave no está presente.

Este método no modifica el diccionario original y devuelve un  valor  que  representa  el  contenido
asociado a la clave buscada, el cual se  almacena  en  la  variable  asignada  al  resultado  de  la
aplicación del método. Esto significa que siempre devuelve un valor, ya sea el encontrado o el valor
por defecto.

Si la clave no se encuentra en el diccionario y no se especifica un valor  por  defecto,  el  método
devolverá "None". Por lo tanto, es recomendable utilizar  un  valor  alternativo  cuando  se  deseen
evitar resultados poco claros o cuando se necesite un mensaje más comprensible para el usuario.

Además, este método solo devuelve el valor asociado a una clave  específica.  Si  se  desea  obtener
múltiples valores o realizar búsquedas más complejas dentro del  diccionario,  se  deberán  utilizar
otros métodos como ".keys()", ".values()" o ".items()", o incluso estructuras de control como bucles
o comprensiones.

Por último, el método ".get()" es ideal para acceder a valores de manera  segura,  especialmente  en
situaciones en las que no se tiene certeza de que la clave esté presente en el diccionario, evitando
errores y permitiendo un manejo más robusto de los datos."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ───────────────────────────────────────────────────────────