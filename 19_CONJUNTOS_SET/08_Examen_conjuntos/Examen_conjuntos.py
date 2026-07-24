# Enunciado:
"""Escribe un programa que gestione un sistema bibliotecario con dos sucursales  representadas  como
conjuntos dentro de una función. El programa debe permitir lo siguiente mediante el uso de funciones
para cada operación:

- Consultar los libros comunes entre ambas sucursales.
- Encontrar los libros únicos por sucursal.
- Encontrar los libros únicos en ambas sucursales.
- Obtener la lista total de libros del sistema.
- Verificar si una sucursal es subconjunto de la otra.
- Agregar un nuevo libro a ambas sucursales.
- Salir del programa.

Cada operación debe realizarse utilizando métodos propios de los conjuntos en Python."""

# Examen_conjuntos.py

# Sucursales representadas como conjuntos.
def sucursal():
    s1 = {"El arte de la guerra", "El viaje de Chihiro", "Cien años de soledad", "Ciencia ocultista", "El principito"}
    s2 = {"El arte de la guerra", "Cien años de soledad", "El principito", "El señor de los anillos", "Harry Potter"}
    return (s1, s2)

# Libros en común.
def consultar_libros_comunes(s1, s2):
    return s1.intersection(s2)

# Libros únicos de cada sucursal.
def encontrar_libros_unicos_en_cada_sucursal(s1, s2):
    return (s1.difference(s2), s2.difference(s1))

# Libros exclusivos de ambas sucursales.
def encontrar_libros_unicos_en_ambas_sucursales(s1, s2):
    return s1.symmetric_difference(s2)

# Unión de las sucursales.
def combinar_sucursales(s1, s2):
    return s1.union(s2)

# Verificación de subconjuntos.
def verificar_subconjunto(s1, s2):
    return (s1.issubset(s2), s2.issubset(s1))

# Agregar un libro.
def agregar_libro_a_ambas_sucursales(s1, s2, libro):
    if (libro not in s1) and (libro not in s2):
        s1.add(libro)
        s2.add(libro)
        print(f"El libro '{libro}' ha sido añadido a ambas sucursales.")
    else:
        print(f"El libro '{libro}' ya existe en una de las sucursales.")
    return (s1, s2)

# Menú principal.
def main():
    while True:
        print("\nSistema bibliotecario")
        print("1. Libros comunes")
        print("2. Libros únicos por sucursal")
        print("3. Libros únicos en ambas sucursales")
        print("4. Libros totales del sistema")
        print("5. Verificar subconjuntos")
        print("6. Añadir libro a ambas sucursales")
        print("7. Salir")

        opcion = input("Ingrese su opción: ")
        a, b = sucursal()

        if (opcion == "1"):
            print("Libros comunes:", consultar_libros_comunes(a, b))
        
        elif (opcion == "2"):
            unicos_a, unicos_b = encontrar_libros_unicos_en_cada_sucursal(a, b)
            print("Únicos sucursal 1:", unicos_a)
            print("Únicos sucursal 2:", unicos_b)

        elif (opcion == "3"):
            print("Únicos en ambas sucursales:", encontrar_libros_unicos_en_ambas_sucursales(a, b))

        elif (opcion == "4"):
            print("Libros del sistema:", combinar_sucursales(a, b))

        elif (opcion == "5"):
            sub_a, sub_b = verificar_subconjunto(a, b)
            print(f"Sucursal 1 {'sí' if sub_a else 'no'} es subconjunto de la sucursal 2.")
            print(f"Sucursal 2 {'sí' if sub_b else 'no'} es subconjunto de la sucursal 1.")

        elif (opcion == "6"):
            libro = input("Ingrese el nombre del libro a añadir: ")
            a, b = agregar_libro_a_ambas_sucursales(a, b, libro)
            print("Sucursal 1:", a)
            print("Sucursal 2:", b)

        elif (opcion == "7"):
            print("Saliendo del sistema bibliotecario.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Llamada principal.
main()

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────