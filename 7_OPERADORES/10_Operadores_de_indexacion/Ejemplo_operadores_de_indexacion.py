# Enunciado:
"""Los operadores de indexación  en  Python  son  herramientas  que  permiten  acceder  a  elementos
específicos o subconjuntos de elementos  dentro  de  colecciones  como  listas,  tuplas,  cadenas  y
diccionarios. Estos operadores son fundamentales para manipular y extraer datos de manera eficiente.

Los operadores de indexación son: [index], [start:stop], [start:stop:step] y [key]. Cada  uno  tiene
un propósito específico:

1. [index]: Permite acceder a un elemento específico en una  colección  utilizando  su  índice.  Los
  índices comienzan en 0 para el primer elemento y pueden  ser  negativos  para  acceder  desde  el
  final.

2. [start:stop]: Permite obtener un subconjunto de elementos desde el índice  "start"  hasta  "stop"
  (sin incluir este último).

3. [start:stop:step]: Permite obtener un subconjunto de elementos desde "start"  hasta  "stop"  (sin
  incluir este último) con un paso definido por "step", lo  que  permite  saltar  elementos  en  el
  subconjunto.

4. [key]: Permite acceder al valor asociado a una clave específica en un diccionario.

Es importante destacar que estos operadores  no  modifican  las  colecciones  originales,  sino  que
generan nuevos objetos o permiten acceder a los datos según sea necesario. Además, el  uso  adecuado
de estos operadores contribuye a escribir código más claro y eficiente.

Estos operadores son aplicables a colecciones ordenadas, como  listas,  tuplas  y  cadenas,  ya  que
permiten acceder a elementos en posiciones específicas utilizando índices.

Por último,  dominar  los  operadores  de  indexación  permite  realizar  operaciones  complejas  de
manipulación de datos, lo que resulta útil en estructuras de control como  bucles  y  condicionales,
así como en otros contextos donde se requiere trabajar  con  colecciones  de  datos.  Además,  estos
operadores son esenciales para aprovechar al máximo las capacidades de las  colecciones  en  Python,
facilitando el acceso y la manipulación de datos de manera precisa y eficiente."""

# Ejemplo_operadores_de_indexacion.py

# Explicación:
"""Definimos una variable llamada lista  y  le  asignamos  una  lista  de  números  enteros.  Luego,
realizamos operaciones de acceso a elementos individuales y subconjuntos de elementos sobre la lista
utilizando los operadores de indexación."""

# Código:
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Explicación:
"""Accedemos a elementos individuales. En el primer caso, accedemos al primer elemento de  la  lista
haciendo referencia a la lista y colocando entre corchetes el índice correspondiente, en  este  caso
[0], que corresponde al primer elemento. En el segundo caso, accedemos  al  último  elemento  de  la
lista haciendo referencia a la lista y colocando entre corchetes el índice correspondiente, en  este
caso [-1], que corresponde al último  elemento.  En  ambos  casos,  asignamos  el  resultado  de  la
operación a una variable e imprimimos el resultado utilizando la función "print()"."""

# Código:
elemento_1 = lista[0]
elemento_2 = lista[-1]
print("Elemento 1:", elemento_1)
print("Elemento 2:", elemento_2)

# Explicación:
"""Accedemos a subconjuntos de elementos. En el primer caso, accedemos a los elementos del índice  1
al  4  de  la  lista  haciendo  referencia  a  la  lista  y  colocando  entre  corchetes  el  índice
correspondiente, en este caso [1:5], que corresponde a los elementos  del  índice  1  al  4.  En  el
segundo caso, accedemos a los elementos en índices pares de la lista haciendo referencia a la  lista
y colocando entre corchetes el índice correspondiente, en este caso [::2],  que  corresponde  a  los
elementos en índices pares. En ambos casos, asignamos el resultado de la operación a una variable  e
imprimimos el resultado utilizando la función "print()"."""

# Código:
subconjunto_1 = lista[1:5]
subconjunto_2 = lista[::2]
print("Subconjunto 1:", subconjunto_1)
print("Subconjunto 2:", subconjunto_2)

# Explicación:
"""Accedemos a un subconjunto con paso desde un rango específico. Para ello, definimos una variable,
hacemos referencia a la lista y colocamos entre corchetes el índice correspondiente,  en  este  caso
[1:8:3], que corresponde a los elementos del índice 1 al 7,  avanzando  de  3  en  3.  Asignamos  el
resultado  de  la  operación  a  la  variable  e  imprimimos  el  resultado  utilizando  la  función
"print()"."""

# Código:
subconjunto_3 = lista[1:8:3]
print("Subconjunto 3:", subconjunto_3)

# Explicación:
"""Accedemos a un elemento mediante un índice negativo. Para ello, definimos una  variable,  hacemos
referencia a la lista y colocamos entre corchetes el índice correspondiente, en este caso [-3],  que
corresponde al tercer elemento desde el final. Asignamos el resultado de la operación a la  variable
e imprimimos el resultado utilizando la función "print()"."""

# Código:
elemento_negativo = lista[-3]
print("Elemento negativo:", elemento_negativo)

# Explicación:
"""Accedemos a un subconjunto desde el inicio hasta un índice específico. Para ello,  definimos  una
variable, hacemos referencia a la lista y colocamos entre corchetes el  índice  correspondiente,  en
este caso [:4], que corresponde a los elementos desde el inicio hasta  el  índice  3.  Asignamos  el
resultado  de  la  operación  a  la  variable  e  imprimimos  el  resultado  utilizando  la  función
"print()"."""

# Código:
subconjunto_inicio = lista[:4]
print("Subconjunto desde el inicio hasta el índice 3:", subconjunto_inicio)

# Explicación:
"""Accedemos a un subconjunto desde un índice específico hasta el final. Para  ello,  definimos  una
variable, hacemos referencia a la lista y colocamos entre corchetes el  índice  correspondiente,  en
este caso [5:], que corresponde a los elementos desde el índice  5  hasta  el  final.  Asignamos  el
resultado  de  la  operación  a  la  variable  e  imprimimos  el  resultado  utilizando  la  función
"print()"."""

# Código:
subconjunto_final = lista[5:]
print("Subconjunto desde el índice 5 hasta el final:", subconjunto_final)

# Explicación:
"""Accedemos a una lista con paso negativo  (inversión  de  la  lista).  Para  ello,  definimos  una
variable, hacemos referencia a la lista y colocamos entre corchetes el  índice  correspondiente,  en
este caso [::-1], que corresponde a todos los elementos de la lista en orden inverso.  Asignamos  el
resultado  de  la  operación  a  la  variable  e  imprimimos  el  resultado  utilizando  la  función
"print()"."""

# Código:
conjunto_invertido = lista[::-1]
print("Conjunto con paso negativo (inversión de la lista):", conjunto_invertido)

# Explicación:
"""Accedemos a un subconjunto con paso negativo desde un rango específico. Para ello, definimos  una
variable, hacemos referencia a la lista y colocamos entre corchetes el  índice  correspondiente,  en
este caso [7:2:-1], que corresponde a los elementos desde el índice 7 hasta el 3 en  orden  inverso.
Asignamos el resultado de la operación a la variable e imprimimos el resultado utilizando la función
"print()"."""

# Código:
subconjunto_invertido = lista[7:2:-1]
print("Subconjunto con paso negativo desde un rango específico:", subconjunto_invertido)

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con claves y  valores.
Accedemos a un elemento del diccionario. Para ello, definimos una variable,  hacemos  referencia  al
diccionario y  colocamos  entre  corchetes  la  clave  correspondiente,  en  este  caso  ["a"],  que
corresponde al valor asociado a la clave "a". Asignamos el resultado de la operación a la variable e
imprimimos el resultado utilizando la función "print()"."""

# Código:
diccionario = {"a": 1, "b": 2, "c": 3}
valor_clave_a = diccionario["a"]
print("Valor asociado a la clave 'a':", valor_clave_a)

# Explicación:
"""Definimos una variable llamada "cadena" y le asignamos  una  cadena  de  texto.  Accedemos  a  un
subconjunto de la cadena. Para ello, definimos una  variable,  hacemos  referencia  a  la  cadena  y
colocamos entre corchetes el índice correspondiente, en este  caso  [1:4],  que  corresponde  a  los
caracteres desde el índice 1 al 3. Asignamos el resultado de la operación a la variable e imprimimos
el resultado utilizando la función "print()".

A continuación, invertimos la subcadena. Para ello, definimos otra variable, hacemos referencia a la
subcadena y  colocamos  entre  corchetes  el  índice  correspondiente,  en  este  caso  [::-1],  que
corresponde a todos los elementos de la subcadena en orden inverso. Asignamos  el  resultado  de  la
operación a la variable e imprimimos el resultado utilizando la función "print()"."""

# Código:
cadena = "Python"
subcadena = cadena[1:4]
subcadena_invertida = subcadena[::-1]
print("Subcadena:", subcadena)
print("Subcadena invertida:", subcadena_invertida)

# Nota Importante:
"""Los índices negativos en Python permiten acceder a elementos desde  el  final  de  la  colección.
Cuando utilizamos rangos de acceso con índices negativos, el comportamiento es  similar  al  de  los
índices positivos, pero contando desde el final de la colección.

Además, se pueden omitir el índice de inicio, el índice de parada o ambos. Si se omite el índice  de
inicio, Python asume que se comienza desde el principio de la colección. Si se omite  el  índice  de
parada, Python asume que se continúa hasta el final de la colección. Si ambos índices se omiten,  se
accede a todos los elementos de la colección.

El orden de los parámetros en la notación [start:stop:step] no se puede alterar. El paso es opcional
en un rango ascendente y, si  no  se  especifica,  Python  asume  un  valor  de  1.  En  los  rangos
descendentes, el paso es obligatorio, ya que, de no especificarlo, Python asumirá un  paso  positivo
de 1 y no obtendremos el resultado esperado.

Para obtener elementos en un orden ascendente, el índice de inicio debe ser menor que el  índice  de
parada, y el paso debe ser positivo. Para obtener elementos en un orden descendente,  el  índice  de
inicio debe ser mayor que el índice de parada, y el paso debe ser negativo. El valor del paso indica
cuántos elementos se deben saltar en cada iteración.

Los operadores de indexación siguen la jerarquía de operadores en Python. Dentro  de  su  categoría,
todos los operadores tienen la misma precedencia, lo que significa que se evalúan en el mismo  nivel
de prioridad. El orden de evaluación está determinado por la jerarquía de operadores en el  caso  de
operadores con diferente precedencia, por la asociatividad en el caso de  los  operadores  de  igual
precedencia y por el uso de paréntesis, con los  que  podemos  forzar  el  orden  de  precedencia  y
evaluación. En este caso, la asociatividad es de izquierda a derecha.

Cabe destacar que los operadores de indexación tienen la segunda  precedencia  más  alta  entre  los
operadores en Python, solo superados por los paréntesis.

Aspectos adicionales importantes:

- Si el índice de inicio o de parada excede los límites de  la  colección,  Python  no  generará  un
  error, sino que ajustará automáticamente el rango para que se mantenga dentro de los límites válidos.

- Los índices negativos son especialmente útiles  para  acceder  a  los  últimos  elementos  de  una
  colección sin necesidad de conocer su longitud.

- Cuando se utiliza un paso negativo, el índice de inicio debe ser mayor que  el  índice  de  parada
  para evitar obtener resultados vacíos.

- La notación de rebanado (slicing) no modifica la colección original; en su lugar, genera una nueva
  colección que contiene los elementos seleccionados.

- Es posible combinar índices positivos y negativos en una  misma  operación  de  rebanado,  lo  que
  permite una mayor flexibilidad al trabajar con colecciones.

- En cadenas de texto, cada carácter se trata como un elemento individual, lo  que  permite  aplicar
  las mismas reglas de indexación y rebanado que en listas y tuplas.

- El índice correspondiente al parámetro stop nunca se incluye en el resultado de  la  operación  de
  rebanado."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
