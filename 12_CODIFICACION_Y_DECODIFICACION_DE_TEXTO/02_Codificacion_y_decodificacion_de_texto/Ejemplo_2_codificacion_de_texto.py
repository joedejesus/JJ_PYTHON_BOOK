# Enunciado:
"""La función "ord()" es una función incorporada en Python que se utiliza para convertir  caracteres
en sus representaciones numéricas correspondientes según  el  estándar  "Unicode",  es  decir,  para
codificar caracteres. Esta función toma un único carácter y devuelve su valor entero correspondiente
en "Unicode", el cual se representa en el sistema decimal.

Es decir, convierte un carácter en su equivalente numérico dentro del estándar "Unicode", que es  un
sistema universal para representar caracteres de prácticamente todos los idiomas. La función "ord()"
es especialmente útil para manipular cadenas,  realizar  operaciones  de  codificación  de  datos  y
convertir entre diferentes formatos de datos,  lo  que  asegura  la  compatibilidad  con  estándares
internacionales."""

# Ejemplo_2_codificacion_de_texto.py

# Explicación:
"""Definimos una variable llamada "cadena_texto" y le asignamos una cadena de texto, en  este  caso:
"hola". Cada carácter de esta cadena se convertirá en su valor decimal  correspondiente  en  Unicode
utilizando la función "ord()".

Utilizamos un bucle "for" para iterar sobre  cada  elemento  de  la  cadena  de  texto.  Para  ello,
escribimos la palabra clave "for", seguida de la variable "i", que representa cada  elemento  de  la
secuencia y que definimos en este  momento,  seguida  del  operador  "in"  para  indicar  sobre  qué
secuencia  queremos  realizar  la  iteración  y  el  nombre  de  dicha  secuencia,  en   este   caso
"cadena_texto". A continuación, escribimos dos puntos (:) para indicar el final de la expresión y el
inicio del bloque de código asociado al bucle "for".

Dentro del bucle "for", definimos una variable llamada "valor_unicode" y le asignamos  el  resultado
de aplicar la función "ord()" a la variable "i" en cada iteración del bucle. Para  ello,  utilizamos
la expresión "ord(i)", que calcula el valor Unicode decimal del  carácter  "i"  y  lo  asigna  a  la
variable "valor_unicode" en cada iteración del bucle. De esta forma, en cada  iteración  del  bucle,
"valor_unicode" contendrá el valor decimal correspondiente al carácter "i", lo que permite codificar
cada carácter de la cadena de texto en su representación numérica en Unicode. Colocamos  esta  línea
de código con una indentación de cuatro espacios desde el margen izquierdo para  indicar  que  forma
parte del bloque de código asociado al bucle "for" y debe ejecutarse en cada iteración del bucle.

Por último, dentro del bucle "for", utilizamos la función "print()" para mostrar los valores  "i"  y
"valor_unicode" en cada iteración al ejecutar el código, acompañados de un mensaje descriptivo  que
indica que el carácter "i" corresponde a un número decimal específico en Unicode. De esta forma,  se
muestra en cada iteración el carácter "i" acompañado de su valor decimal correspondiente en Unicode,
almacenado en "valor_unicode", lo que permite visualizar la relación  entre  los  caracteres  y  sus
representaciones numéricas en el sistema Unicode. Colocamos esta línea de código con una indentación
de cuatro espacios desde el margen izquierdo para indicar que  forma  parte  del  bloque  de  código
asociado al bucle "for" y debe ejecutarse en cada iteración del bucle."""     

# Código:
cadena_texto = "hola"

for i in cadena_texto:
    valor_unicode = ord(i)
    print(f"El carácter '{i}' corresponde al número decimal {valor_unicode} en Unicode.")

# Nota Importante:
"""Es importante destacar que la función "ord()" opera directamente sobre caracteres individuales  y
devuelve su valor "Unicode" en formato decimal, lo que la hace ideal para tareas  que  requieren  la
conversión precisa de caracteres a sus representaciones numéricas.

Aunque es posible trabajar con bytes en contextos relacionados con esta función, no es lo más  común
ni recomendable, ya que los bytes representan datos en un nivel más bajo y suelen requerir un manejo
más específico. Para este fin, se recomienda usar los métodos de codificación  y  decodificación  de
cadenas, como ".encode()" y ".decode()", que están  diseñados  para  realizar  la  conversión  entre
caracteres y bytes de manera más eficiente y segura."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
