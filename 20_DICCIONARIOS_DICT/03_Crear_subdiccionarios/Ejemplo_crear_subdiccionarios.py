# Enunciado:
"""La creación de subdiccionarios es una técnica fundamental en la manipulación de  diccionarios  en
Python. Permite extraer partes específicas de un diccionario original, lo que resulta  útil  en  una
amplia variedad de aplicaciones, como el procesamiento de datos, la limpieza  de  información  y  la
generación de informes.

Esta técnica se logra seleccionando claves específicas del diccionario original  para  construir  un
nuevo diccionario que contenga únicamente los  pares  clave-valor  deseados.  A  diferencia  de  las
listas, los diccionarios no utilizan índices numéricos para acceder a sus elementos, sino claves.

Por ello, la extracción de subdiccionarios se realiza seleccionando explícitamente las claves que se
desean incluir. Además, esta funcionalidad es compatible con cualquier tipo de clave  inmutable,  lo
que facilita la organización y el filtrado de la información dentro de un diccionario."""

# Ejemplo_crear_subdiccionarios.py

# Explicación:
"""Definimos una variable llamada "diccionario" y le asignamos un diccionario con varios  elementos.
Este  diccionario  se  utilizará  para  crear  subdiccionarios  mediante  la  selección  de   claves
específicas.

A continuación, definimos una variable llamada "sub_diccionario" y le asignamos un nuevo diccionario
creado a partir de las claves "a", "b" y "c". Para ello, utilizamos una comprensión  de  diccionario
que recorre las claves seleccionadas y extrae sus valores del diccionario original. De  esta  forma,
se obtiene un subdiccionario que contiene únicamente los pares clave-valor correspondientes a dichas
claves.

Por  último,  utilizamos  la  función  "print()"  para  mostrar  en  la  consola  el  resultado  del
subdiccionario creado, acompañado de un mensaje descriptivo en formato  "f-string"  que  indica  qué
elementos contiene el subdiccionario."""

# Código:
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

sub_diccionario = {clave: diccionario[clave] for clave in ["a", "b", "c"]}
print(f"Subdiccionario que contiene las claves 'a', 'b' y 'c': {sub_diccionario}")

# Nota Importante:
"""En Python, los diccionarios almacenan sus elementos en pares clave-valor, y las claves deben  ser
inmutables. A diferencia de las listas, los diccionarios no utilizan índices numéricos para  acceder
a sus elementos, por lo que no es posible aplicar slicing directamente sobre ellos. Sin embargo,  es
posible convertir sus claves en una lista y aplicar slicing sobre dicha lista  para  seleccionar  un
rango de claves y construir un subdiccionario a partir de estas.

Al crear subdiccionarios, es importante recordar que las claves seleccionadas deben  existir  en  el
diccionario original; de lo contrario, se  producirá  un  error  al  intentar  acceder  a  un  valor
inexistente. Por ello, es recomendable verificar la existencia de las claves o utilizar métodos  más
seguros, como ".get()", cuando sea necesario.

Es importante destacar que los diccionarios pueden utilizar cualquier tipo de objeto inmutable  como
clave. Esto añade una capa adicional de flexibilidad al trabajar con diccionarios, ya que se  pueden
seleccionar claves de forma dinámica según las necesidades del programa.

Por último, es fundamental tener en cuenta  que  los  diccionarios  son  objetos  mutables,  lo  que
significa que sus elementos pueden agregarse, eliminarse o modificarse después de su  creación.  Sin
embargo, al crear subdiccionarios mediante comprensiones o  mediante  la  selección  de  claves,  se
generan nuevos diccionarios independientes, lo que permite trabajar con copias parciales sin alterar
el diccionario original. Esto hace que la técnica de creación de subdiccionarios sea robusta y fácil
de usar para manipular diccionarios en Python."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────