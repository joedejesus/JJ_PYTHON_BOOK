# Enunciado:
"""La fusión de listas es una técnica fundamental en la manipulación de  datos  en  Python.  Permite
combinar múltiples listas en una sola, lo que resulta útil en una amplia variedad  de  aplicaciones,
como la agregación de datos, la creación de estructuras de datos más complejas y la organización  de
la información. Además, es una herramienta esencial para el procesamiento de datos, ya que  facilita
la integración de contenidos  provenientes  de  diferentes  fuentes  y  su  presentación  de  manera
coherente y estructurada.

Esta técnica se logra utilizando el operador (+), que permite unir  listas  de  manera  eficiente  y
flexible. El operador (+) es ideal para combinaciones simples y rápidas,  aunque  puede  generar  un
mayor consumo de memoria, ya que de esta forma se crean nuevas listas cada vez que  se  realiza  una
fusión, en lugar de modificar las listas existentes.

Sin embargo, esta característica también garantiza que las listas originales  permanezcan  intactas,
lo que puede ser beneficioso para evitar efectos secundarios no deseados y mantener la integridad de
los datos originales, teniendo en cuenta que las listas en Python son objetos mutables.

Por último, con esta técnica es posible combinar listas que contengan diferentes tipos de datos,  ya
sea por medio de variables o  directamente  con  listas  literales,  lo  que  proporciona  una  gran
flexibilidad para la manipulación de datos y la creación de estructuras dinámicas. Esto nos  permite
adaptar nuestras soluciones a las necesidades específicas de cada caso, combinando diferentes  tipos
de datos y estructuras de manera eficiente y eficaz, lo que es fundamental  para  el  desarrollo  de
programas robustos y versátiles en Python."""

# Ejemplo_fusion_de_listas.py

# Explicación:
"""Definimos dos variables llamadas "lista_1" y "lista_2", y les asignamos las listas [1,  2,  3]  y
[4, 5, 6], respectivamente. Estas listas representan dos conjuntos de datos  que  queremos  fusionar
para formar una lista combinada que contenga todos los elementos de  ambas  listas,  además  de  los
elementos de una lista literal adicional.

A continuación, definimos una nueva variable llamada "lista_fusionada" y le asignamos  el  resultado
de la fusión de "lista_1", "lista_2" y la lista literal "[7, 8, 9]" utilizando el operador (+). Para
ello, colocamos ambas variables y la lista literal en el orden deseado de fusión,  entre  paréntesis
para mejorar la legibilidad y separadas por el operador (+).

De esta forma, las listas [1, 2, 3] y [4, 5, 6], contenidas en las variables "lista_1" y  "lista_2",
junto con la lista literal "[7, 8, 9]", se combinan para formar una nueva lista que  contiene  todos
los elementos. Esta combinación se realiza en el orden en que aparecen  las  variables  y  la  lista
literal, por lo que el resultado de la fusión será la lista [1, 2, 3, 4, 5, 6, 7, 8, 9].

Por último, utilizamos la función "print()" para mostrar el resultado de la fusión  en  la  consola,
acompañado de un mensaje descriptivo en formato "f-string" que indica que se trata del resultado  de
la fusión de las listas."""

# Código:
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_fusionada = (lista_1 + lista_2 + [7, 8, 9])
print(f"Este es el resultado de la fusión de las listas: {lista_fusionada}")

# Nota Importante:
"""Es importante destacar que la fusión de listas no modifica las listas originales, sino  que  crea
una nueva lista que contiene la combinación de las listas originales. Esto se debe a que, aunque las
listas en Python son objetos mutables, el operador (+) genera una nueva lista en lugar de  modificar
las existentes. Por lo tanto, cada vez que se  fusionan  listas,  se  genera  una  nueva  lista  que
contiene el resultado de la fusión, mientras que las listas originales permanecen sin cambios.

Esta característica garantiza la seguridad y la  consistencia  de  los  datos,  ya  que  las  listas
originales no se ven afectadas por operaciones posteriores. Sin embargo, también es importante tener
en cuenta que la creación de nuevas listas puede tener  un  impacto  en  el  rendimiento  cuando  se
trabaja con grandes volúmenes de datos, por lo que es  recomendable  utilizar  métodos  alternativos
como ".extend()" si se busca modificar una lista existente y optimizar el uso de memoria.

El método ".extend()" permite agregar los elementos de una lista a otra sin crear una  nueva  lista,
lo que puede ser más eficiente en términos de memoria y rendimiento cuando se  trabaja  con  grandes
volúmenes de datos. Sin embargo, el operador (+)  es  más  adecuado  para  combinaciones  simples  y
rápidas, especialmente cuando se desea mantener las listas originales  sin  modificaciones.  Por  lo
tanto, la elección entre el operador (+) y el método ".extend()" dependerá del contexto específico y
de las necesidades del programa, teniendo en cuenta las ventajas y desventajas de cada enfoque  para
lograr la fusión de listas de manera eficiente y eficaz.

Por otro lado, el uso de paréntesis en este caso no es necesario y no  tiene  ningún  efecto  en  la
operación, pero puede ayudar a mejorar la legibilidad del código al indicar claramente que  se  está
realizando una operación de fusión de listas. Además, el orden de las listas es importante,  ya  que
determina el resultado final de la fusión. Si se invierte el orden de las listas, el resultado  será
diferente, por lo que es fundamental prestar atención a la secuencia  en  la  que  se  combinan  las
listas para obtener el resultado deseado.

Por último, cabe destacar que, en realidad, lo que estamos haciendo es  concatenar  las  listas  con
ayuda del operador (+), pero utilizamos el término "fusión" para describir el  proceso  de  combinar
las listas en una sola, ya que este término se utiliza comúnmente para referirse a este  proceso  en
un contexto más amplio y descriptivo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
