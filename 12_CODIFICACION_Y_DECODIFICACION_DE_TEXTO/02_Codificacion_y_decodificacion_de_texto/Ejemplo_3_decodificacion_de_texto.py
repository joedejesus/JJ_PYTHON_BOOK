# Enunciado:
"""La función "chr()" es una función incorporada en Python que se  utiliza  para  convertir  valores
numéricos en sus caracteres correspondientes según la codificación "Unicode"; es decir, para obtener
caracteres a partir de sus valores numéricos. Esta función toma un único número entero y devuelve el
carácter correspondiente en "Unicode".

Es decir, convierte un número en su carácter equivalente dentro del estándar "Unicode",  que  es  un
sistema universal para representar caracteres de prácticamente todos los idiomas. La función "chr()"
es especialmente útil para manipular cadenas, realizar operaciones  de  decodificación  de  datos  y
convertir  entre  diferentes  formatos  de   datos,   asegurando   compatibilidad   con   estándares
internacionales."""

# Ejemplo_3_decodificacion_de_texto.py

# Explicación:
"""Definimos una variable llamada "lista_numeros" y le asignamos una lista de  valores  enteros,  en
este  caso:  [104,  111,  108,  97].  Cada  número  de  esta  lista  se  convertirá  a  su  carácter
correspondiente en Unicode utilizando la función "chr()".

Utilizamos un bucle "for" para iterar sobre cada  elemento  de  la  lista  de  números.  Para  ello,
escribimos la palabra clave "for", seguida de la variable "i", que representa cada  elemento  de  la
secuencia en cada iteración y que definimos en este momento, seguida del operador "in" para  indicar
dónde queremos que se realice la iteración y el nombre de la secuencia sobre la que queremos iterar,
en este caso "lista_numeros". A continuación, escribimos dos puntos (:) para indicar el final de  la
expresión y el inicio del bloque de código asociado al bucle "for".

Dentro del bucle "for", definimos una variable llamada "valor_unicode" y le asignamos  el  resultado
de aplicar la función "chr()" a la variable "i" en cada iteración del bucle. Para  ello,  utilizamos
la expresión "chr(i)", que obtiene el carácter Unicode correspondiente al número "i" y lo  asigna  a
la variable "valor_unicode" en cada iteración del bucle. De esta forma, en cada iteración del bucle,
"valor_unicode" contendrá el carácter correspondiente al número "i", lo que permite decodificar cada
número de la lista en su representación de carácter en Unicode. Colocamos esta línea de  código  con
una indentación de cuatro espacios desde el margen izquierdo,  para  indicar  que  forma  parte  del
bloque de código asociado al bucle "for" y debe ejecutarse en cada iteración del bucle.

Por último, dentro del bucle "for", utilizamos la función "print()" para mostrar los valores  "i"  y
"valor_unicode" en cada iteración, al ejecutar el código, acompañados de un mensaje descriptivo que
indica que el número "i" corresponde a un carácter específico en Unicode. De esta forma, se  muestra
el valor sin convertir en cada iteración, "i", acompañado de su carácter correspondiente en Unicode,
"valor_unicode", lo que permite visualizar la relación entre los números y sus  representaciones  de
carácter en el sistema Unicode. Colocamos esta  línea  de  código  con  una  indentación  de  cuatro
espacios desde el margen izquierdo, para indicar que forma parte del bloque de  código  asociado  al
bucle "for" y debe ejecutarse en cada iteración del bucle."""

# Código:
lista_numeros = [104, 111, 108, 97]

for i in lista_numeros:
    valor_unicode = chr(i)
    print(f"El número decimal {i} corresponde al carácter '{valor_unicode}' en Unicode.")

# Nota Importante:
"""Es importante destacar que la función "chr()" opera directamente sobre números enteros y devuelve
el carácter "Unicode" en formato de carácter, lo que la hace ideal  para  tareas  que  requieren  la
conversión precisa de números a sus representaciones de carácter. Aunque  es  posible  trabajar  con
bytes usando esta función, no es lo más común ni recomendable, ya que los bytes representan datos en
un nivel más bajo y suelen requerir un manejo más específico. Para este fin se recomienda  usar  los
métodos de codificación y decodificación de cadenas,  como  ".encode()"  y  ".decode()",  que  están
diseñados para manejar la conversión entre caracteres y bytes de manera más eficiente y segura."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
