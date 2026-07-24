# Enunciado:
"""Escribe un programa que permita convertir un número decimal a binario, octal o hexadecimal, según
la opción seleccionada por el usuario mediante un menú en consola. El  programa  debe  solicitar  la
opción, recibir el número decimal y mostrar el resultado de la conversión correspondiente."""

# Examen_a_sistemas_numericos.py

# Menú principal.
def opcion_menu_usuario():
    print("Bienvenido al programa de conversión de sistemas numéricos")
    print("1. Decimal a binario")
    print("2. Decimal a octal")
    print("3. Decimal a hexadecimal")
    print("4. Salir")

# Mostrar el menú inicial.
opcion_menu_usuario()

# Conversión a binario.
def decimal_a_binario(decimal):
    return bin(decimal)

# Conversión a octal.
def decimal_a_octal(decimal):
    return oct(decimal)

# Conversión a hexadecimal.
def decimal_a_hexadecimal(decimal):
    return hex(decimal)

# Solicitud de la opción y del número decimal.
def input_usuario():
    a = int(input("Ingresa la opción que deseas realizar: "))
    b = int(input("Ingresa el número decimal que deseas convertir: "))
    return a, b

# Bucle principal.
while True:
    opcion, numero = input_usuario()

    if (opcion == 4):
        print("Gracias por utilizar el programa")
        break
    elif (opcion == 1):
        print(f"Resultado (Decimal a binario): {decimal_a_binario(numero)}")
    elif (opcion == 2):
        print(f"Resultado (Decimal a octal): {decimal_a_octal(numero)}")
    elif (opcion == 3):
        print(f"Resultado (Decimal a hexadecimal): {decimal_a_hexadecimal(numero)}")
    else:
        print("Opción inválida")

    opcion_menu_usuario()

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────