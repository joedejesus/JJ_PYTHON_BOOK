# Enunciado:
"""Escribe un programa que simule un sistema de cálculo para una tienda. El programa debe  solicitar
al usuario el precio del producto, la cantidad comprada y el porcentaje de descuento  aplicado.  Con
estos datos, calcula el total sin descuento, el importe descontado y el precio final a pagar.

Después, evalúa si el precio final es  mayor,  igual  o  menor  que  100  utilizando  operadores  de
comparación y muestra el mensaje correspondiente.

Por último, emplea operadores lógicos para comprobar si el descuento es mayor del 20% y la  cantidad
supera las 5 unidades, indicando si se trata de una compra grande con descuento notable o una compra
normal."""

# Examen_operadores.py

# Solicitud de datos.
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad comprada: "))
descuento = float(input("Descuento aplicado (%): "))

# Cálculos principales.
total_sin_descuento = (precio * cantidad)
importe_descuento = (total_sin_descuento * (descuento / 100))
precio_final = (total_sin_descuento - importe_descuento)

# Resultados principales.
print("\n--- Resultados ---")
print(f"Total sin descuento: {total_sin_descuento}")
print(f"Importe descontado: {importe_descuento}")
print(f"Precio final: {precio_final}")

# Comparación del precio final.
if (precio_final > 100):
    print("El precio final es mayor que 100.")
elif (precio_final == 100):
    print("El precio final es exactamente 100.")
else:
    print("El precio final es menor que 100.")

# Evaluación lógica.
if (descuento > 20) and (cantidad > 5):
    print("Compra grande con descuento notable.")
else:
    print("Compra normal.")

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────