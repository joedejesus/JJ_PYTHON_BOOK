# Enunciado:
"""Crea una función llamada "suma_lista()" que  reciba  como  parámetro  obligatorio  una  lista  de
números y retorne la suma de sus elementos. Dentro de  esta  función,  define  una  función  anidada
llamada "suma_elementos()" que realice la suma de los elementos de la  lista,  la  almacene  en  una
variable y retorne dicho  valor.  La  función  "suma_lista()"  debe  llamar  a  la  función  anidada
"suma_elementos()" y retornar su resultado con la instrucción "return".

La función "suma_elementos()" será responsable de  realizar  la  operación  de  suma,  mientras  que
"suma_lista()" actuará como un contenedor que delega esta tarea a la función interna. La  lógica  de
suma debe estar completamente encapsulada dentro de la función  anidada,  evitando  que  se  exponga
innecesariamente al resto del programa y asegurando que la suma se realice de  manera  controlada  y
segura.  Además,  la  lista  debe  ser  pasada  como  parámetro   a   "suma_lista()"   y   luego   a
"suma_elementos()" para garantizar la independencia y reutilización de ambas funciones."""

# Ejercicio_funciones_anidadas.py

# Explicación:
"""Definimos una función llamada "suma_lista()"  que  recibe  un  parámetro  llamado  "lista".  Este
parámetro se utilizará para realizar una operación de suma dentro  de  la  función  interna  y  será
sustituido por la lista que se le pase a la función externa al llamarla. Para  ello,  utilizamos  la
palabra clave "def" seguida del nombre de la función,  en  este  caso  "suma_lista()",  seguida  del
nombre del parámetro "lista" entre paréntesis (), y terminamos con dos puntos (:)  para  indicar  el
inicio del bloque de código asociado a la función.

Dentro de la función "suma_lista()", definimos otra función llamada "suma_elementos()" que recibe el
mismo parámetro "lista". Este parámetro se utilizará para realizar una operación de suma  dentro  de
esta función y será sustituido por la lista que se le pase al llamarla. Esta  función  interna  será
responsable de iterar sobre la lista, realizar la suma de los elementos y retornar el resultado.  La
definición de la función interna se realiza dentro del bloque de código de la  función  externa  con
una indentación de cuatro espacios para indicar que es una función anidada.

A continuación, definimos una variable llamada "contenedor" y le asignamos el valor  inicial  de  0.
Esta variable almacena la suma acumulada de los elementos de la lista durante  las  iteraciones  del
bucle "for".

Utilizamos un bucle "for" para iterar sobre cada elemento de la  lista.  Para  ello,  escribimos  la
palabra clave "for", seguida de la variable "i", que representa el valor  de  cada  elemento  de  la
lista en cada iteración, seguida del operador "in" para indicar dónde queremos  que  se  realice  la
iteración y el nombre de la secuencia sobre  la  que  queremos  iterar,  en  este  caso  "lista".  A
continuación, escribimos dos puntos (:) para indicar el final de la expresión y el inicio del bloque
de código asociado al bucle "for". Colocamos estas dos líneas  de  código  con  una  indentación  de
cuatro espacios desde la propia función interna para indicar que forman parte del bloque  de  código
de dicha función y deben ejecutarse siempre que se llame a la función interna.

Dentro del bucle "for", incrementamos el valor de "contenedor" en "i" hasta que se  hayan  recorrido
todos los elementos de la lista. Para ello, utilizamos la expresión de incremento "contenedor += i",
que es una forma concisa de escribir "contenedor = contenedor + i". De esta forma, sumamos el  valor
de cada elemento "i" al valor actual de la variable en cada iteración y asignamos el resultado a  la
misma variable "contenedor". Colocamos esta línea de código con una indentación de  cuatro  espacios
desde el bucle "for" para indicar que forma parte del bloque de código  asociado  al  bucle  y  debe
ejecutarse en cada iteración y siempre que la función interna sea llamada.

Después del bucle "for", y dentro de la función interna, utilizamos  la  instrucción  "return"  para
devolver el valor final de "contenedor" desde la función interna "suma_elementos()". De esta  forma,
cuando se llame a la función interna, se obtendrá el resultado de la suma de  los  elementos  de  la
lista calculado dentro del bucle. Colocamos esta línea de  código  con  una  indentación  de  cuatro
espacios desde la propia función interna para indicar que forma parte del bloque de código de  dicha
función y debe ejecutarse siempre que se llame a la función interna.

Luego, fuera de la función interna pero aún dentro de la función externa "suma_lista()", llamamos  a
la función interna "suma_elementos()" pasando la lista como  argumento  y  retornamos  su  resultado
utilizando la instrucción "return". Para ello, escribimos la  palabra  clave  "return"  seguida  del
nombre de la función interna "suma_elementos()" con el parámetro "lista"  entre  paréntesis  ().  De
esta forma, cuando se llame a la función externa, se ejecutará la función interna y se devolverá  el
resultado de la suma de los  elementos  de  la  lista.  Colocamos  esta  línea  de  código  con  una
indentación de cuatro espacios desde la propia función externa para  indicar  que  forma  parte  del
bloque de código de dicha función y debe ejecutarse siempre que se llame a la función externa.

Por último, fuera de la función "suma_lista()",  llamamos  a  esta  función  externa  "suma_lista()"
pasando una lista literal de números enteros como argumento, en este caso  "[1,  2,  3,  4,  5]",  y
almacenamos el resultado en la variable "resultado". Para ello, escribimos el nombre de  la  función
externa "suma_lista()" con la lista entre paréntesis () y asignamos el resultado de la llamada a  la
variable "resultado" utilizando el operador  de  asignación  (=).  Luego,  imprimimos  el  valor  de
"resultado"  con  la  ayuda  de  la  función  "print()"  para  verificar  que  la  función  funciona
correctamente."""

# Código:
def suma_lista(lista):
    def suma_elementos(lista):
        contenedor = 0
        for i in lista:
            contenedor += i
        return contenedor

    return suma_elementos(lista)

resultado = suma_lista([1, 2, 3, 4, 5])
print(f"El resultado de la suma es: {resultado}")

# Nota Importante:
"""Es necesario que la función anidada "suma_elementos()" reciba un parámetro porque es una  función
definida dentro de "suma_lista()" y necesita saber sobre qué  lista  operar.  Esto  asegura  que  la
función sea reutilizable y no dependa de variables externas, lo que mejora la claridad, la seguridad
y la predictibilidad del código. Al recibir la lista como parámetro, se garantiza que cada llamada a
"suma_lista()" sea completamente independiente y no tenga efectos secundarios no deseados.

En este caso, no podemos definir la  variable  "contenedor"  fuera  de  la  función  interna  porque
queremos que cada vez que  se  llame  a  la  función  externa,  la  suma  comience  desde  cero.  Si
definiéramos la variable fuera de la función interna, su valor podría  acumularse  entre  diferentes
llamadas a la función externa, lo que generaría resultados incorrectos.

Además, encapsular la lógica de suma dentro de "suma_elementos()" asegura que la función interna  no
dependa de variables externas, lo que refuerza la  independencia  y  modularidad  del  código.  Este
diseño modular y encapsulado es una buena práctica en programación, ya que facilita la  comprensión,
el mantenimiento y la reutilización del código. Al mantener las responsabilidades  de  cada  función
bien definidas y evitar dependencias innecesarias, se logra un código más robusto, legible  y  fácil
de depurar."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
