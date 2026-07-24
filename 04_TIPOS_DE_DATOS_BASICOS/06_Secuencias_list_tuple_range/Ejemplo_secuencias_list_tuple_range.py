# Enunciado:
"""Las secuencias en Python son estructuras ordenadas que almacenan  una  serie  de  elementos.  Las
listas (list) son dinámicas y mutables, ideales para almacenar datos que pueden cambiar  durante  la
ejecución del programa. Por  otro  lado,  las  tuplas  (tuple)  son  similares  a  las  listas  pero
inmutables, lo que las hace útiles para guardar información que no debe modificarse.

Finalmente, los rangos (range) generan secuencias de números y  se  utilizan  comúnmente  en  bucles
"for". Cada una de estas secuencias corresponde a un tipo de dato en Python y tiene  características
y métodos específicos, explicados en las secciones correspondientes."""

# Ejemplo_secuencias_list_tuple_range.py

# Explicación:
"""Asignamos una lista de números del 1 al 5 a una variable llamada "lista". Colocamos los elementos
dentro de la lista entre corchetes [] y los separamos con comas. Finalmente, imprimimos el valor  de
la variable "lista" en pantalla usando la función "print()"."""

# Código:
lista = [1, 2, 3, 4, 5]
print(lista)

# Explicación:
"""Asignamos una tupla de números del 1 al 5 a una variable llamada "tupla". Colocamos los elementos
dentro de la tupla entre paréntesis () y los separamos con comas. Finalmente, imprimimos el valor de
la variable "tupla" en pantalla usando la función "print()"."""

# Código:
tupla = (1, 2, 3, 4, 5)
print(tupla)

# Explicación:
"""Asignamos un rango de números del 1 al 5 a una variable llamada "rango". Colocamos los  elementos
dentro del rango entre paréntesis () y usamos el constructor "range()" para  crearlo.  Definimos  el
rango con un número inicial "1" y un número final "6", donde este último no  se  incluye.  El  rango
contiene todos los números enteros desde  el  número  inicial  hasta  el  número  final  menos  uno.
Finalmente, imprimimos el valor de la variable "rango" en pantalla usando la función "print()"."""

# Código:
rango = range(1, 6)
print(rango)

# Nota Muy Importante:
"""Al imprimir el rango, no se apreciará gráficamente la exclusión del  último  número,  ya  que  el
rango no imprime los números, sino que genera una secuencia de números enteros.  Esto  se  verá  con
claridad cuando se itere sobre el rango en su sección correspondiente. Además, es  fundamental  usar
el constructor "range()" para crear rangos; de lo  contrario,  estaríamos  creando  una  tupla.  Sin
embargo, para crear listas y tuplas no es necesario usar  su  constructor  correspondiente,  ya  que
Python puede inferir automáticamente el tipo de dato.

Cada una de estas secuencias tiene características, métodos y sintaxis específicos, explicados en la
sección correspondiente a cada tipo de dato. Los constructores  se  explicarán  con  detalle  en  la
sección correspondiente a "Constructores de objetos"."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
