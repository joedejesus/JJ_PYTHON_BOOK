# Enunciado:
"""Escribe un programa que solicite un texto al usuario  y  lo  convierta  en  bytes  utilizando  la
codificación "UTF-8". Muestra  la  secuencia  de  bytes  y  su  representación  hexadecimal.  Luego,
decodifica los bytes para reconstruir el  texto  original  y  verifica  si  coincide  con  el  texto
ingresado.

Por último, solicita un carácter y muestra su código "Unicode" y su representación en "UTF-8", tanto
en bytes como en formato hexadecimal."""

# Examen_codificacion_y_decodificacion_de_texto.py

# Solicitud de texto.
texto = input("Introduce un texto: ")

# Codificación UTF-8.
bytes_utf8 = texto.encode("utf-8")

# Mostrar codificación.
print("\n--- Codificación ---")
print("Bytes UTF-8:", bytes_utf8)
print("Hexadecimal:", bytes_utf8.hex())

# Decodificación.
texto_decodificado = bytes_utf8.decode("utf-8")

# Mostrar decodificación.
print("\n--- Decodificación ---")
print("Texto decodificado:", texto_decodificado)

# Verificación.
if (texto == texto_decodificado):
    print("La decodificación coincide con el texto original.")
else:
    print("La decodificación NO coincide con el texto original.")

# Solicitud de carácter.
caracter = input("\nIntroduce un carácter para analizar: ")

# Información del carácter.
codigo_unicode = ord(caracter)
bytes_caracter = caracter.encode("utf-8")

# Mostrar información del carácter.
print("\n--- Información del carácter ---")
print(f"Carácter: {caracter}")
print(f"Código Unicode (entero): {codigo_unicode}")
print(f"UTF-8 en bytes: {bytes_caracter}")
print(f"UTF-8 en hexadecimal: {bytes_caracter.hex()}")

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────