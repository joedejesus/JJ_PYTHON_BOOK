# Enunciado:
"""Escribe un programa que solicite al usuario una serie de valores separados por comas. Cada  valor
puede representar un número entero, un número decimal, un  valor  booleano  escrito  como  "True"  o
"False", o un texto.

El programa debe analizar cada elemento y determinar su  tipo:  entero  si  contiene  solo  dígitos,
decimal si contiene un único punto y cumple las reglas numéricas, booleano si coincide con "true"  o
"false" sin importar las mayúsculas o minúsculas, y texto en cualquier otro caso.

Una vez convertidos los valores, guarda los resultados en una lista llamada "convertidos"  y  genera
otra lista llamada "tipos" que almacene el tipo real de cada elemento.

Por último, muestra cuántos elementos de cada  tipo  se  han  detectado,  proporcionando  un  conteo
detallado de enteros, decimales, valores booleanos y cadenas de texto."""

# Examen_manejo_de_tipos_de_datos_basicos.py

# Solicitud de entrada.
entrada = input("Introduce valores separados por comas: ")

# Separación y limpieza.
elementos = [e.strip() for e in entrada.split(",")]

# Lista de valores convertidos.
convertidos = []

# Conversión de cada elemento.
for elem in elementos:
    elem_lower = elem.lower()

    if (elem_lower == "true"):
        convertidos.append(True)
    elif (elem_lower == "false"):
        convertidos.append(False)
    elif (elem.isdigit()):
        convertidos.append(int(elem))
    elif (elem.count(".") == 1):
        parte1, parte2 = elem.split(".")
        if (parte1.isdigit()) and (parte2.isdigit()):
            convertidos.append(float(elem))
        else:
            convertidos.append(elem)
    else:
        convertidos.append(elem)

# Lista de tipos.
tipos = [type(v) for v in convertidos]

# Conteo por tipo.
conteo = {
    "int": sum(isinstance(v, int) for v in convertidos),
    "float": sum(isinstance(v, float) for v in convertidos),
    "bool": sum(isinstance(v, bool) for v in convertidos),
    "str": sum(isinstance(v, str) for v in convertidos)
}

# Resultados.
print("\n--- Resultados ---")
print("Valores convertidos:", convertidos)
print("Tipos detectados:", tipos)
print("Conteo por tipo:", conteo)

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────