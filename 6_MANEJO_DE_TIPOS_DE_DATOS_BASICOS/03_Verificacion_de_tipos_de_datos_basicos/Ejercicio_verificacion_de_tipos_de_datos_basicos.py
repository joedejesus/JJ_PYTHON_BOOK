# Enunciado:
"""Usa la función "type()" para verificar cada tipo de dato visto hasta ahora."""

# Ejercicio_verificacion_de_tipos_de_datos_basicos.py

# Explicación:
"""Definimos varias variables, cada una con un nombre representativo del tipo de dato que almacenan.
Luego, les asignamos un valor que corresponde a cada tipo de  dato  básico.  Después,  aplicamos  la
función "type()" a cada una de las variables definidas para verificar su tipo  de  dato,  encerrando
cada llamada a la función "type()" dentro de la función "print()" para imprimir el resultado  en  la
consola.

En este caso, no guardamos el resultado en una variable adicional porque solo queremos  imprimir  el
tipo de dato que contiene cada variable. Finalmente, ejecutamos el código para mostrar el  resultado
en la consola. En cada caso, el resultado será la clase del objeto almacenado en la variable."""

# Código:
entero = 5
print(type(entero))  # <class 'int'>

flotante = 5.0
print(type(flotante))  # <class 'float'>

complejo = (5 + 5j)
print(type(complejo))  # <class 'complex'>

booleano = False
print(type(booleano))  # <class 'bool'>

texto = "Adiós Mundo"
print(type(texto))  # <class 'str'>

lista = [1, 2, 3, 4, 5]
print(type(lista))  # <class 'list'>

tupla = (1, 2, 3, 4, 5)
print(type(tupla))  # <class 'tuple'>

rango = range(6)
print(type(rango))  # <class 'range'>

conjunto = {1, 2, 3, 4, 5}
print(type(conjunto))  # <class 'set'>

conjunto_inmutable = frozenset({1, 2, 3, 4, 5})
print(type(conjunto_inmutable))  # <class 'frozenset'>

diccionario = {"nombre": "Joe", "edad": 33}
print(type(diccionario))  # <class 'dict'>

nulo = None
print(type(nulo))  # <class 'NoneType'>

# Nota Muy Importante:
"""Independientemente del sistema numérico (binario, decimal, hexadecimal u octal) que  evalúes  con
la función "type()" en Python, el resultado será siempre <class 'int'>. Sin embargo, si  evalúas  un
número de punto flotante, el resultado será <class 'float'>, y si evalúas  un  número  complejo,  el
resultado será <class 'complex'>.

Esto ocurre porque Python interpreta los números como  enteros,  flotantes  o  complejos,  según  su
formato. En la categoría de enteros (int) se incluyen los números enteros, independientemente de  su
representación en los diferentes sistemas numéricos (binario, decimal, hexadecimal u octal).

Por otro lado, si evalúas datos de tipo byte  con  la  función  "type()"  en  Python,  el  resultado
dependerá del contexto: Si evalúas una secuencia de bytes, obtendrás <class 'bytes'>; si evalúas  un
bytearray,  obtendrás  <class  'bytearray'>;  y  si  evalúas   un   memoryview,   obtendrás   <class
'memoryview'>.

Sin embargo, si evalúas un solo byte en formato binario, decimal,  hexadecimal  u  octal,  obtendrás
<class 'int'>,  ya  que  Python  los  interpreta  como  números  enteros  independientemente  de  su
representación en  los  diferentes  sistemas  numéricos.  Los  aspectos  relacionados  con  sistemas
numéricos y bytes se explicarán en sus secciones correspondientes."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────