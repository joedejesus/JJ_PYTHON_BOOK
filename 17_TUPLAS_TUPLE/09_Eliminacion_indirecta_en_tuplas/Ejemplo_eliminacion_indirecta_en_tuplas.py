# Enunciado:
"""La eliminación indirecta en tuplas  se  refiere  a  la  posibilidad  de  crear  una  nueva  tupla
excluyendo ciertos elementos de la original mediante técnicas como el rebanado o "slicing". Dado que
las tuplas son inmutables, no se pueden modificar directamente. Sin  embargo,  se  puede  crear  una
nueva tupla a partir de la original que contenga solo los elementos deseados, lo que se conoce  como
eliminación indirecta.

Este enfoque es útil cuando se necesita trabajar con una versión modificada de una tupla sin alterar
la original. La tupla original permanece intacta y  se  genera  una  nueva  tupla  con  los  cambios
aplicados.

Por último, este proceso puede ser práctico para gestionar la inmutabilidad de las tuplas en Python,
pero debe utilizarse con precaución en situaciones en las que el rendimiento  sea  crítico,  ya  que
implica operaciones adicionales para crear nuevas tuplas."""

# Ejemplo_eliminacion_indirecta_en_tuplas.py

# Explicación:
"""Definimos una variable llamada "tupla" y le asignamos una tupla de números enteros (1, 2,  3,  4,
5). Esta tupla se utilizará para demostrar el proceso de eliminación indirecta.

Además, definimos una nueva variable llamada "nueva_tupla"  y  le  asignamos  el  resultado  de  una
operación de rebanado o "slicing" que crea una nueva tupla excluyendo el tercer elemento de la tupla
original. La operación de rebanado se realiza de la siguiente manera:

En primer lugar, hacemos referencia a la variable "tupla" y utilizamos  el  operador  de  indexación
"[]" con el rango de índices [:2]. Esto indica que queremos incluir los elementos desde el inicio de
la tupla hasta el índice 2, sin incluir dicho índice. De esta forma, hemos creado una  subtupla  que
contiene los primeros dos elementos de la tupla original, en este caso, los números 1 y 2.

En segundo lugar, hacemos referencia a la variable "tupla" y utilizamos el  operador  de  indexación
"[]" con el rango de índices [3:]. Esto indica que queremos incluir los elementos desde el índice 3,
incluyéndolo, hasta el final de la tupla. De esta forma, hemos creado una subtupla que contiene  los
elementos a partir del índice 3 hasta el final de la tupla original, en este caso, los números  4  y
5.

Utilizamos el operador aritmético (+) para concatenar las dos subtuplas  resultantes  del  rebanado,
encerrando la operación entre paréntesis () para asegurar que se realice correctamente.

Por último, utilizamos la función "print()" para mostrar en la consola  el  resultado  de  la  nueva
tupla, que corresponde a la tupla original con  el  tercer  elemento  eliminado,  acompañado  de  un
mensaje descriptivo en formato "f-string" que indica que se trata del resultado  de  la  eliminación
indirecta. El resultado mostrará la nueva tupla con el tercer elemento eliminado,  mientras  que  la
tupla original permanecerá sin cambios."""

# Código:
tupla = (1, 2, 3, 4, 5)

nueva_tupla = (tupla[:2] + tupla[3:])
print(f"Este es el resultado de la eliminación indirecta: {nueva_tupla}")

# Nota Importante:
"""Es importante destacar que este proceso no modifica la tupla original, sino que  crea  una  nueva
tupla con los cambios deseados. Esto significa que la tupla original permanece  inalterada,  lo  que
garantiza la integridad de los datos originales. Sin embargo, este método puede ser ineficiente para
tuplas grandes, ya que implica la creación de nuevas tuplas, lo que puede aumentar el uso de memoria
y el tiempo de ejecución.

El término "eliminación indirecta" se refiere a la idea de que estamos eliminando  elementos  de  la
tupla mediante la creación de una nueva tupla, en lugar de modificar la tupla directamente, debido a
su naturaleza inmutable.

Por lo tanto, se recomienda usar este enfoque solo cuando  sea  realmente  necesario  y  no  existan
alternativas más eficientes. En general, es mejor diseñar  el  código  de  manera  que  no  requiera
eliminaciones indirectas y, de esta forma, desarrollar un código más limpio, mantenible y eficiente.

Para obtener un resultado similar, se podría crear una lista a partir de la tupla original, eliminar
los elementos deseados de la lista con la instrucción "del" o con  el  método  ".remove()"  y  luego
convertirla nuevamente en una tupla. Alternativamente, se  podría  utilizar  la  función  "filter()"
junto con una función lambda para crear una nueva tupla que excluya ciertos elementos, lo que  puede
ser más eficiente en algunos casos.

Por último, comprender las limitaciones y ventajas de este enfoque es clave  para  tomar  decisiones
informadas al trabajar con tuplas en Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
