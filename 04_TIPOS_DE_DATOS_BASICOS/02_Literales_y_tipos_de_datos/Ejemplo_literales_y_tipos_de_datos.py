# Enunciado:
"""Los literales y los tipos de datos en Python  son  elementos  esenciales  para  trabajar  con  el
lenguaje. Los literales representan valores concretos que se escriben  directamente,  como  números,
cadenas de texto, valores booleanos, estructuras vacías como set() para conjuntos, [] para listas  y
() para tuplas, y secuencias de escape, como saltos de línea y tabulaciones, entre otros.

Los tipos de datos agrupan los literales en forma de objetos de una  clase  específica,  como  (int,
float, complex, bool, str, list, tuple, set, frozenset, range,  dict,  NoneType,  bytes,  bytearray,
memoryview). Cada objeto creado en Python tiene un tipo de dato  asociado,  pertenece  a  una  clase
específica y contiene literales que representan valores concretos."""

# Ejemplo_literales_y_tipos_de_datos.py

# Código:
10  # Este literal representa un valor numérico entero.

"Programación"  # Este literal representa una cadena de texto.

False  # Este literal representa un valor booleano.

entero = int(10)  # Este tipo de dato es un objeto de la clase (int).

booleano = bool(False)  # Este tipo de dato es un objeto de la clase (bool). 

texto = str("Programación")  # Este tipo de dato es un objeto de la clase (str).
          
lista = list([1, 2, 3])  # Este tipo de dato es un objeto de la clase (list).

tupla = tuple((1, 2, 3))  # Este tipo de dato es un objeto de la clase (tuple).

conjunto = set({1, 2, 3})  # Este tipo de dato es un objeto de la clase (set).

rango = range(1, 4)  # Este tipo de dato es un objeto de la clase (range).

diccionario = dict({"clave": "valor"})  # Este tipo de dato es un objeto de la clase (dict).

nulo = None  # Este tipo de dato es un objeto de la clase (NoneType).

# Nota Muy Importante:
"""En estos ejemplos se usan los constructores de cada tipo de dato para crear objetos específicos y
mostrar cómo se asocian los literales con los tipos de datos. Python  asocia  los  literales  a  los
tipos dedatos automáticamente, por lo que no es necesario especificar el tipo de dato  al  crear  un
literal.

Lo mismo ocurre con los tipos de datos, ya que, al crear un objeto  de  cualquier  tipo,  Python  lo
asocia automáticamente con su clase o tipo de dato correspondiente. Aunque no  es  obligatorio  usar
los constructores explícitamente, en algunos casos es una buena práctica hacerlo para mayor claridad
en el código."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────