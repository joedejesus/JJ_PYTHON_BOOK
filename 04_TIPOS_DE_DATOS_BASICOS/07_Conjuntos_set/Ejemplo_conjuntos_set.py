# Enunciado:
"""Los conjuntos (set) en Python son estructuras de datos  desordenadas  y  mutables,  ideales  para
almacenar elementos únicos, es decir, no duplicados. Esto significa que dentro de un  set  no  puede
haber elementos repetidos. Son desordenados porque no tienen un índice,  por  lo  que  no  se  puede
acceder a sus elementos mediante posiciones específicas.

Los conjuntos son ideales para operaciones de pertenencia, eliminación de duplicados  y  operaciones
matemáticas como uniones, intersecciones y diferencias, entre otras. Este tipo de  dato  corresponde
al tipo (set) en Python.

Cabe destacar que existe una variante llamada "frozenset", que es un conjunto congelado, el cual  es
inmutable y se utiliza cuando se requiere un conjunto que no cambie a lo largo del tiempo.  Este  se
crea comúnmente a partir de un set mediante el constructor "frozenset()"."""

# Ejemplo_conjuntos_set.py

# Explicación:
"""Asignamos un conjunto de números del 1 al 5 a una  variable  llamada  "conjunto".  Colocamos  los
elementos dentro del conjunto entre llaves {} y los separamos con comas. Finalmente,  imprimimos  el
valor de la variable "conjunto" en pantalla mediante la función "print()"."""

# Código:
conjunto = {1, 2, 3, 4, 5}
print(conjunto)

# Explicación:
"""Definimos una variable llamada "conjunto_frozenset_1" y usamos el constructor "frozenset()"  para
crear un conjunto congelado a  partir  de  la  variable  "conjunto",  pasándola  como  argumento  al
constructor "frozenset()" y guardando el resultado en la variable "conjunto_frozenset_1".

Esto significa que "conjunto_frozenset_1" será inmutable, es decir, no se podrán agregar ni eliminar
elementos de él una vez creado. Contendrá los mismos elementos que el conjunto original. Finalmente,
imprimimos  el  valor  de  la  variable  "conjunto_frozenset_1"  en  pantalla  mediante  la  función
"print()"."""

# Código:
conjunto_frozenset_1 = frozenset(conjunto)
print(conjunto_frozenset_1)

# Explicación:
"""Definimos una variable llamada "conjunto_frozenset_2" y usamos el constructor "frozenset()"  para
crear un conjunto congelado a partir  de  un  conjunto  de  números,  pasándolo  como  argumento  al
constructor "frozenset()" y guardando el resultado en la variable "conjunto_frozenset_2".

Esto significa que "conjunto_frozenset_2" será inmutable, es decir, no se podrán agregar ni eliminar
elementos  de  él   una   vez   creado.   Finalmente,   imprimimos   el   valor   de   la   variable
"conjunto_frozenset_2" en pantalla mediante la función "print()"."""

# Código:
conjunto_frozenset_2 = frozenset({7, 8, 9, 10})
print(conjunto_frozenset_2)

# Nota Importante:
"""Los métodos y operaciones para trabajar con conjuntos (set) y conjuntos congelados (frozenset) se
explicarán con detalle en la sección correspondiente a "Conjuntos (set)"."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────