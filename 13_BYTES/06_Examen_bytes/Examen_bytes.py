# Enunciado:
"""Escribe un programa que solicite un texto al usuario y lo convierta en  bytes  mediante  "UTF-8".
Luego, genera una segunda versión codificada en "ASCII". Muestra ambas secuencias de bytes,  compara
sus tamaños y determina cuál ocupa más espacio.

A continuación, decodifica ambas versiones y verifica si la versión en "ASCII" coincide con el texto
original; si no coincide, indica qué caracteres no pudieron  representarse.  Por  último,  crea  una
lista con los valores numéricos de cada byte en "UTF-8" y muestra el valor máximo, el  mínimo  y  la
media en la consola."""

# Examen_bytes.py

# Solicitud del texto.
texto = input("Introduce un texto: ")

# Codificación en UTF-8.
bytes_utf8 = texto.encode("utf-8")

# Codificación en ASCII.
bytes_ascii = texto.encode("ascii", errors="replace")

# Muestra de las codificaciones.
print("\n--- Codificaciones ---")
print("UTF-8:", bytes_utf8)
print("ASCII:", bytes_ascii)

# Comparación de tamaños.
print("\n--- Comparación de tamaños ---")
print(f"Tamaño UTF-8: {len(bytes_utf8)} bytes")
print(f"Tamaño ASCII: {len(bytes_ascii)} bytes")

# Determinación de cuál ocupa más espacio.
if (len(bytes_utf8) > len(bytes_ascii)):
    print("UTF-8 ocupa más espacio.")
elif (len(bytes_utf8) < len(bytes_ascii)):
    print("ASCII ocupa más espacio (inusual).")
else:
    print("Ambas codificaciones ocupan lo mismo.")

# Decodificación.
texto_utf8 = bytes_utf8.decode("utf-8")
texto_ascii = bytes_ascii.decode("ascii")

# Resultados de la decodificación.
print("\n--- Decodificación ---")
print("Texto desde UTF-8:", texto_utf8)
print("Texto desde ASCII:", texto_ascii)

# Verificación.
if (texto == texto_ascii):
    print("El texto ASCII coincide con el original.")
else:
    print("El texto ASCII NO coincide con el original.")
    print("Caracteres no representables fueron reemplazados por '?'.")

# Análisis de los bytes en UTF-8.
valores_bytes = list(bytes_utf8)

print("\n--- Análisis de bytes UTF-8 ---")
print("Valores numéricos:", valores_bytes)
print("Valor máximo:", max(valores_bytes))
print("Valor mínimo:", min(valores_bytes))
print("Media:", sum(valores_bytes) / len(valores_bytes))

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────