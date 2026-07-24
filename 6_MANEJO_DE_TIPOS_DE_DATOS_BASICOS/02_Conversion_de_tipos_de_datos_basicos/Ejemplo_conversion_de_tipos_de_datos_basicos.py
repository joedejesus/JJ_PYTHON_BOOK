# Enunciado:
"""La conversión de tipos (casting) en Python es el proceso mediante el cual se transforma  un  tipo
de dato en otro. Este mecanismo se aplica tanto a tipos primitivos (enteros,  flotantes,  complejos,
booleanos y cadenas) como  a  tipos  compuestos,  que  pueden  ser  mutables  (listas,  conjuntos  y
diccionarios) o inmutables (tuplas y frozensets).

Se utiliza para modificar el  tipo  de  dato  almacenado  en  una  variable  de  forma  explícita  y
controlada, especialmente cuando se necesita cumplir los requisitos de  una  función  o  método  que
exige un tipo de dato específico. Al realizar el casting, se obtiene una  nueva  representación  del
valor original ajustada al tipo de dato deseado, lo cual permite ejecutar operaciones que,  de  otro
modo, podrían causar errores o comportamientos inesperados."""

# Ejemplo_conversion_de_tipos_de_datos_basicos.py

# Explicación:
"""Definimos una variable llamada "numero_1" y le asignamos un valor de tipo  entero  (int).  Luego,
convertimos el número entero en una cadena de texto aplicando el constructor "str()" a  la  variable
que contiene el número. Finalmente, guardamos el resultado en una nueva variable llamada  "cadena_1"
y usamos la función "print()" para mostrar el valor de la variable en la consola."""

# Código:
numero_1 = 108
cadena_1 = str(numero_1)
print(cadena_1)

# Explicación:
"""Definimos una variable llamada "cadena_2" y le asignamos un valor de tipo cadena de texto  (str).
Luego, convertimos la cadena de texto en un número entero aplicando  el  constructor  "int()"  a  la
variable que contiene la cadena de texto. Finalmente, guardamos el resultado en una  nueva  variable
llamada "numero_2" y usamos la función "print()"  para  mostrar  el  valor  de  la  variable  en  la
consola."""

# Código:
cadena_2 = "108"
numero_2 = int(cadena_2)
print(numero_2)

# Explicación:
"""Aplicamos el constructor "list()" a la variable que contiene  la  cadena  de  texto.  Finalmente,
encerramos la llamada al constructor "list()"  dentro  de  la  función  "print()"  para  mostrar  el
resultado en la consola sin necesidad de crear una variable intermedia. Esto convierte cada carácter
de la cadena en un elemento de una lista."""

# Código:
print(list(cadena_2))

# Nota Importante:
"""Es importante tener en cuenta que algunas conversiones pueden no ser posibles  o  pueden  generar
errores si los datos no son compatibles.  Por  ejemplo,  si  intentamos  convertir  una  cadena  que
contiene texto no numérico a un entero, como "int("hola")", Python lanzará un "ValueError" porque no
puede realizar la conversión. Por lo tanto, debemos asegurarnos de que los  datos  sean  compatibles
antes de realizar una conversión de tipo."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────