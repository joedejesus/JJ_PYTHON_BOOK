# Enunciado:
"""Esta guía reúne los términos y conceptos  fundamentales  de  Python,  acompañados  de  una  breve
definición y una explicación clara. Su propósito es servir como referencia rápida para quienes están
comenzando a aprender Python o desean repasar conceptos esenciales del lenguaje. Está organizada  de
forma sencilla y pedagógica para facilitar la comprensión y el estudio."""

# Ejemplo_guia_de_terminos.py

# Código:
Guia_de_terminos_en_Python = [

    # ------------------------------
    # Conceptos básicos del lenguaje
    # ------------------------------
    "Variable",              # Espacio en memoria donde se almacena un valor.
    "Tipo de dato",          # Clasificación del valor (int, float, str, etc.).
    "Identificador",         # Nombre asignado a variables, funciones o clases.
    "Asignación",            # Proceso de dar un valor a una variable con "=".
    "Expresión",             # Combinación de valores y operadores que produce un resultado.
    "Sentencia",             # Instrucción ejecutable en Python.

    # ------------------------------
    # Tipos de datos primitivos
    # ------------------------------
    "int",                   # Números enteros.
    "float",                 # Números decimales.
    "complex",               # Números complejos (a + bj).
    "bool",                  # Valores booleanos: True o False.
    "str",                   # Cadenas de texto.

    # ------------------------------
    # Tipos de datos compuestos
    # ------------------------------
    "list",                  # Colección ordenada y mutable.
    "tuple",                 # Colección ordenada e inmutable.
    "set",                   # Colección no ordenada y sin duplicados.
    "frozenset",             # Versión inmutable de un set.
    "dict",                  # Colección de pares clave-valor.

    # ------------------------------
    # Estructuras de control
    # ------------------------------
    "if",                    # Condición simple.
    "elif",                  # Condición adicional.
    "else",                  # Bloque alternativo.
    "for",                   # Bucle para iterar sobre secuencias.
    "while",                 # Bucle que se ejecuta mientras se cumpla una condición.
    "break",                 # Rompe un bucle.
    "continue",              # Salta a la siguiente iteración.
    "pass",                  # Instrucción vacía (marcador de posición).

    # ------------------------------
    # Funciones y programación
    # ------------------------------
    "def",                   # Define una función.
    "return",                # Devuelve un valor desde una función.
    "lambda",                # Función anónima de una sola línea.
    "argumento",             # Valor que se pasa a una función.
    "parámetro",             # Nombre definido en una función para recibir un valor.
    "scope",                 # Alcance de una variable.
    "namespace",             # Espacio donde viven los nombres definidos.     
    
    # ------------------------------
    # Manejo de errores
    # ------------------------------
    "try",                   # Bloque para intentar ejecutar código.
    "except",                # Captura excepciones.
    "finally",               # Código que se ejecuta siempre.
    "raise",                 # Lanza una excepción manualmente.
    "Exception",             # Clase base de las excepciones.

    # ------------------------------
    # Programación orientada a objetos
    # ------------------------------
    "class",                 # Define una clase.
    "object",                # Objeto creado a partir de una clase.
    "atributo",              # Variable dentro de una clase.
    "método",                # Función dentro de una clase.
    "self",                  # Referencia a la instancia actual.
    "herencia",              # Capacidad de extender clases.
    "polimorfismo",          # Uso de una misma interfaz con comportamientos distintos.
    "encapsulamiento",       # Control de acceso a atributos.

    # ------------------------------
    # Módulos y paquetes
    # ------------------------------
    "import",                # Importa un módulo.
    "from",                  # Importa partes específicas.
    "as",                    # Alias.
    "module",                # Archivo .py con código reutilizable.
    "package",               # Carpeta que contiene módulos.

    # ------------------------------
    # Funciones incorporadas importantes
    # ------------------------------
    "print()",               # Muestra información.
    "len()",                 # Longitud de un objeto.
    "type()",                # Tipo de un valor.
    "id()",                  # Identificador único en memoria.
    "input()",               # Entrada por consola.
    "range()",               # Secuencia numérica.
    "enumerate()",           # Índice y valor.
    "zip()",                 # Combina secuencias.
    "map()",                 # Aplica una función.
    "filter()",              # Filtra elementos.
    "sum()",                 # Suma.
    "min()",                 # Mínimo.
    "max()",                 # Máximo.
    "sorted()",              # Ordena.
    "reversed()",            # Iterador invertido.

    # ------------------------------
    # Conceptos avanzados
    # ------------------------------
    "iterable",              # Objeto que puede recorrerse.
    "iterador",              # Produce valores uno a uno.
    "comprehension",         # Sintaxis compacta para colecciones.
    "decorador",             # Función que modifica otra función.
    "generador",             # Produce valores con yield.
    "yield",                 # Devuelve un valor sin terminar la función.
    "context manager",       # Controla recursos con "with".
    "with",                  # Manejo seguro de recursos.
    "namedtuple",            # Tupla con campos nombrados.
    "dataclass",             # Clase optimizada para datos.

    # ------------------------------
    # Memoria y comportamiento
    # ------------------------------
    "mutabilidad",           # Capacidad de cambiar su contenido.
    "inmutabilidad",         # Propiedad de no poder modificarse.
    "referencia",            # Ubicación donde vive un objeto.
    "identidad",             # Identificador único de un objeto.
    "copia superficial",     # Comparte objetos internos.
    "copia profunda",        # Copia independiente.

    # ------------------------------
    # Jerga común en programación
    # ------------------------------
    "asignar",               # Dar un valor a una variable.
    "devolver",              # Retornar un valor desde una función.
    "invocar",               # Llamar a una función o método.
    "instanciar",            # Crear un objeto desde una clase.
    "iterar",                # Recorrer los elementos.
    "parsear",               # Interpretar o convertir datos.
    "castear",               # Convertir tipos de datos.
    "debuggear",             # Buscar y corregir errores.
    "loggear",               # Registrar información.
    "refactorizar",          # Mejorar código sin cambiar su comportamiento.
    "ejecutar",              # Correr un programa.
    "mutar",                 # Modificar un objeto mutable.
    "desempaquetar",         # Extraer valores de una secuencia.
    "slicing",               # Obtener una porción de una secuencia.
    "mergear",               # Combinar estructuras de datos.
    "crashear",              # Cuando un programa falla.
    "levantar excepción",    # Lanzar un error manualmente.
    "manejar errores",       # Controlar excepciones.
    "shadowing",             # Una variable oculta otra con el mismo nombre.
    "optimizar",             # Mejorar eficiencia.
    "overhead",              # Coste adicional de una operación.
    "lazy evaluation",       # Evaluación diferida.
    "pipeline",              # Encadenar operaciones.
    "API",                   # Interfaz para comunicar sistemas entre sí.
    "endpoint",              # Punto de acceso de una API.
]

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
