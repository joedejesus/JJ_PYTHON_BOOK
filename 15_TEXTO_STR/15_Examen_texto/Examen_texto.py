# Enunciado:
"""Escribe un programa que defina una función que reciba un texto como argumento y realice  diversas
operaciones sobre él: contar caracteres, reemplazar palabras, buscar posiciones,  eliminar  espacios
al principio y al final, dividirlo en palabras y verificar cómo comienza el texto. Estas operaciones
deben realizarse con la ayuda de los métodos del objeto texto. Por último, llama a la función con un
texto de tu elección y muestra los resultados de cada operación en la consola."""

# Examen_texto.py

# Función para procesar el texto.
def procesar_texto(texto):

    # Longitud del texto.
    print(f"Longitud del texto: {len(texto)} caracteres")

    # Reemplazo de una palabra del texto.
    reemplazar = texto.replace("Python", "C++")
    print(f"Texto modificado:\n{reemplazar}")

    # Búsqueda de una palabra en el texto.
    posicion = texto.find("desafiante")
    if (posicion != -1):
        print(f"La palabra 'desafiante' comienza en la posición {posicion}")
    else:
        print("La palabra 'desafiante' no se encuentra en el texto")

    # Eliminación de espacios.
    espacios = texto.strip()
    print(f"Texto sin espacios al principio y al final:\n{espacios}")

    # División del texto en palabras.
    dividir = texto.split()
    print(f"Lista de palabras:\n{dividir}")

    # Verificación del inicio del texto.
    if (texto.startswith("Este")):
        print("El texto comienza con la palabra Este")
    else:
        print("El texto no comienza con la palabra Este")

# Texto de ejemplo.
texto_ejemplo = "Este es un texto de ejemplo. Python es un lenguaje de programación desafiante y poderoso."

# Llamada a la función.
procesar_texto(texto_ejemplo)

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────