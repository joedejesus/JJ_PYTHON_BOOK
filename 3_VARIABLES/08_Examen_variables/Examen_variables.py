# Enunciado:
"""Escribe un programa que gestione la información básica de un personaje de  videojuego  utilizando
variables. El programa debe solicitar al usuario el nombre del personaje, su nivel  como  un  número
entero, sus puntos de vida como un número decimal y su estado vital mediante los  valores  "True"  o
"False".

Cada  entrada  debe  convertirse  a  su  tipo  correspondiente,  y  el  estado  debe   interpretarse
correctamente sin importar cómo lo escriba el usuario. Si la entrada del estado  no  es  válida,  el
programa debe mostrar un mensaje de error y asumir que el personaje está muerto. Una  vez  obtenidos
los valores, calcula el poder total multiplicando el nivel por los puntos de vida y muestra toda  la
información en la consola utilizando la funcion "print()" en formato "f-strings"."""

# Examen_variables.py

# Solicitud de datos al usuario.
nombre_personaje = input("Nombre del personaje (texto): ")
nivel_personaje = int(input("Nivel del personaje (entero): "))
puntos_vida = float(input("Puntos de vida (float): "))
estado_vivo = input("¿Está vivo? (True/False): ")

# Procesamiento del estado vital.
if (estado_vivo.lower() == "true"):
    estado_vivo = True
elif (estado_vivo.lower() == "false"):
    estado_vivo = False
else:
    print("Entrada de estado no válida. Se asumirá que el personaje está muerto.")
    estado_vivo = False

# Cálculo del poder total.
poder_total = (nivel_personaje * puntos_vida)

# Salida de resultados.
print("\n--- Información del personaje ---")
print(f"Nombre: {nombre_personaje}")
print(f"Nivel: {nivel_personaje}")
print(f"Puntos de vida: {puntos_vida}")
print(f"Estado: {estado_vivo}")
print(f"Poder total: {poder_total}")

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────