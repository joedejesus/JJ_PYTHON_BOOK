# Enunciado:
"""Escribe un programa que utilice una función encargada de mostrar mensajes de entrada al usuario a
través de un diccionario interno. La función debe recibir una clave y devolver el  mensaje  asociado
para ser utilizado en la función "input()".  Si  la  clave  no  existe,  debe  devolver  un  mensaje
predeterminado.

Usa esta función para implementar un "CRUD" de  usuarios:  agregar,  mostrar,  actualizar  y  borrar
usuarios de una lista. El programa debe funcionar mediante un menú interactivo en la consola."""

# Examen_listas.py

# Función para mostrar mensajes de entrada al usuario.
def lanzar_inputs(mensajes):
    diccionario = {
        "agregar":    "Ingrese el nombre del usuario: ",
        "actualizar": "Ingrese el nombre del usuario a actualizar: ",
        "nuevo":      "Ingrese el nuevo nombre (o presione Enter para mantener el actual): ",
        "borrar":     "Ingrese el nombre del usuario a borrar: ",
        "opcion":     "Seleccione una opción (1-5): ",
    }
    return input(diccionario.get(mensajes, "Entrada no válida"))

# Agregar usuario.
def agregar_usuario(lista_usuarios):
    nombre = lanzar_inputs("agregar")
    lista_usuarios.append(nombre)
    print(f"\nUsuario '{nombre}' agregado exitosamente.")

# Mostrar usuarios.
def mostrar_usuarios(lista_usuarios):
    if (not lista_usuarios):
        print("No hay usuarios registrados.")
    else:
        print(lista_usuarios)

# Actualizar usuario.
def actualizar_usuario(lista_usuarios):
    nombre_a_actualizar = lanzar_inputs("actualizar")

    if (nombre_a_actualizar in lista_usuarios):
        nuevo_nombre = lanzar_inputs("nuevo")
        if nuevo_nombre:
            lista_usuarios[lista_usuarios.index(nombre_a_actualizar)] = nuevo_nombre
        print(f"\nUsuario '{nombre_a_actualizar}' actualizado exitosamente.")
    else:
        print(f"No se encontró el usuario '{nombre_a_actualizar}'.")

# Borrar usuario.
def borrar_usuario(lista_usuarios):
    nombre_a_borrar = lanzar_inputs("borrar")

    if (nombre_a_borrar in lista_usuarios):
        lista_usuarios.remove(nombre_a_borrar)
        print(f"\nUsuario '{nombre_a_borrar}' borrado exitosamente.")
    else:
        print(f"No se encontró el usuario '{nombre_a_borrar}'.")

# Función principal.
def main():
    lista_usuarios = []

    while True:
        print("\nCRUD de Usuarios")
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Actualizar usuario")
        print("4. Borrar usuario")
        print("5. Salir")

        opcion = lanzar_inputs("opcion")

        if (opcion == "5"):
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif (opcion == "1"):
            agregar_usuario(lista_usuarios)
        elif (opcion == "2"):
            mostrar_usuarios(lista_usuarios)
        elif (opcion == "3"):
            actualizar_usuario(lista_usuarios)
        elif (opcion == "4"):
            borrar_usuario(lista_usuarios)
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