# Enunciado:
"""Los condicionales "if...else" en Python son estructuras de control de flujo  que  permiten  tomar
decisiones en un programa. Se utilizan para ejecutar un bloque de código si una condición se  evalúa
como verdadera y otro bloque si la condición es falsa.

La estructura básica consiste en escribir la palabra clave "if" seguida  de  una  condición.  Si  la
condición es verdadera, se ejecuta el bloque de código asociado  con  el  condicional  "if".  Si  es
falsa, se ejecuta el bloque de código asociado con el condicional "else". Ambos bloques deben  estar
correctamente indentados.

En términos semánticos, "if numero > 0: ... else: ..." se traduce como "si el número es mayor que 0,
haz esto; de lo contrario, haz aquello".

Además, podemos utilizar los condicionales "if...else" para evaluar una amplia  variedad  de  casos.
Por ejemplo, se puede verificar si un número es positivo, negativo o cero, o evaluar condiciones más
complejas  combinando  múltiples  operadores  ya  sean  aritméticos,   comparativos,   lógicos,   de
pertenencia, de identidad o utilizando índices para acceder  a  elementos  de  colecciones,  lo  que
permite construir expresiones más complejas.

Es importante destacar que el bloque "else" abarca todos los casos que no cumplen con  la  condición
"if". Por lo tanto, "else" no necesita una condición  para  evaluarse.  Además,  la  indentación  es
crucial en Python, ya que define los bloques de código.

Por último, es importante destacar que es posible  anidar  múltiples  estructuras  "if...else"  para
manejar casos más específicos, pero esto puede dificultar la lectura del código. En estos casos,  se
recomienda usar "elif" para simplificar la lógica y mejorar la legibilidad, lo que  se  verá  en  la
siguiente sección."""

# Ejemplo_condicionales_if_else.py

# Explicación:
"""Definimos una variable llamada "numero" y le asignamos el valor entero -5. Luego,  utilizamos  el
condicional "if" para verificar si la variable "numero" es mayor que 0.  Para  ello,  escribimos  la
palabra clave "if" seguida de la condición entre paréntesis y  terminada  con  dos  puntos  (:).  La
condición se compone de la variable "numero", el operador mayor que (>) y el valor 0.

Si la condición se cumple (si el número es mayor que  0),  se  imprime  un  mensaje  en  la  consola
utilizando la función "print()", el cual corresponde al bloque de código asociado con el condicional
"if" que colocamos justo debajo y con una indentación de cuatro espacios.

A continuación, utilizamos el condicional "else" para manejar el caso en que la condición  del  "if"
no se cumpla. Para ello, escribimos la palabra clave "else" seguida de dos puntos (:).

Si la condición "if" no se cumple (si el número es menor o igual que 0), se imprime un mensaje en la
consola utilizando la función "print()", el cual corresponde al bloque de  código  asociado  con  el
condicional "else" que colocamos justo debajo y con una indentación de cuatro espacios.

Por último, después del bloque "if...else", se imprime otro mensaje que indica el fin del  programa,
el cual se imprimirá siempre, independientemente de si la condición se cumple  o  no,  ya  que  está
fuera del bloque "if...else". En este caso, se imprimirá "El número es negativo", ya que la variable
"numero" tiene un valor de -5, el cual es menor que 0 y, por tanto, negativo."""

# Código:
numero = -5

if (numero > 0):
    print("El número es positivo")
else:
    print("El número es negativo")

print("Fin del programa")

# Nota Importante:
"""En Python, las condiciones no se limitan a valores booleanos. Cualquier valor puede evaluarse  en
un contexto condicional, donde valores como listas vacías, cadenas vacías y el número 0  se  evalúan
como falsos,  mientras  que  otros  valores  se  evalúan  como  verdaderos.  Esto  permite  escribir
condiciones más dinámicas y flexibles, como verificar si una lista tiene elementos  simplemente  con
"if lista:". Este comportamiento hace que  las  estructuras  condicionales  sean  más  adaptables  a
diferentes tipos de datos y escenarios.

Es importante seguir buenas prácticas al  trabajar  con  estructuras  condicionales.  Evitar  anidar
demasiados bloques "if...else" ayuda a mantener el código legible y fácil de  entender.  Además,  es
recomendable usar comentarios para explicar condiciones complejas y priorizar el uso  de  "elif"  en
lugar de múltiples bloques "if" independientes.

Esto no solo mejora la eficiencia del código, sino que también facilita su comprensión por parte  de
otros desarrolladores.

Por último, la indentación es un aspecto crucial en Python, ya que define los bloques de código. Una
mala indentación puede generar errores de sintaxis  o  comportamientos  inesperados.  Por  ello,  es
fundamental asegurarse de que los bloques "if" y "else" estén correctamente  alineados.  Además,  es
buena práctica estructurar el código de manera que sea fácil de  leer  y  seguir,  especialmente  en
programas que incluyen múltiples condiciones o lógica compleja."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
