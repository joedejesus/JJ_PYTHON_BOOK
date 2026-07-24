# Enunciado:
"""Escribe un programa que utilice una función encargada de mostrar mensajes de entrada al usuario a
través de un diccionario interno. La función debe recibir una clave y devolver el  mensaje  asociado
para ser utilizado en la función "input()".  Si  la  clave  no  existe,  debe  devolver  un  mensaje
predeterminado.

Usa esta función para implementar un gestor de libros mediante tuplas. Cada libro debe representarse
como una tupla de tres elementos: título, autor y año de  publicación.  El  programa  debe  permitir
agregar libros, mostrarlos, buscarlos por autor y borrarlos por título mediante un menú  interactivo
en consola."""

# Examen_tuplas.py

# Función para mostrar los mensajes de entrada al usuario.
def lanzar_inputs(mensaje):
    diccionario = {
        "opcion": "Seleccione una opción (1-5): ",
        "titulo": "Ingrese el título del libro: ",
        "autor": "Ingrese el autor del libro: ",
        "año": "Ingrese el año de publicación del libro: ",
        "buscar": "Ingrese el nombre del autor para buscar libros: ",
        "borrar": "Ingrese el título del libro a borrar: "
    }
    return input(diccionario.get(mensaje, "Opción no válida."))

# Crear una tupla con los datos de un libro.
def datos_libro(titulo, autor, año):
    datos = (titulo, autor, año)
    return datos

# Agregar un libro a la biblioteca.
def agregar_libro(biblioteca, datos):
    biblioteca.append(datos)
    print(f"\nLibro '{datos[0]}' agregado exitosamente.")

# Mostrar todos los libros.
def mostrar_libros(biblioteca):
    if (not biblioteca):
        print("No hay libros registrados.")
    else:
        print("\nLista de Libros:")
        for libro in biblioteca:
            print(f"Título: {libro[0]}, Autor: {libro[1]}, Año de Publicación: {libro[2]}")

# Buscar libros por autor.
def buscar_libros_por_autor(biblioteca, autor):
    libros_encontrados = [libro for libro in biblioteca if libro[1] == autor]
    
    if (not libros_encontrados):
        print(f"No hay libros del autor '{autor}'.")
    else:
        print(f"\nLibros del autor '{autor}':")
        for libro in libros_encontrados:
            print(f"Título: {libro[0]}, Año de Publicación: {libro[2]}")

# Borrar un libro por título.
def borrar_libro_por_titulo(biblioteca, titulo):
    for libro in biblioteca:
        if (libro[0] == titulo):
            biblioteca.remove(libro)
            print(f"\nLibro '{titulo}' borrado exitosamente.")
            return
    print(f"\nNo se encontró el libro '{titulo}'.")

# Función principal.
def main():
    biblioteca = []

    while True:
        print("\nGestor de Libros")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Buscar libros por autor")
        print("4. Borrar libro por título")
        print("5. Salir")

        opcion = lanzar_inputs("opcion")

        if (opcion == "1"):
            titulo = lanzar_inputs("titulo")
            autor = lanzar_inputs("autor")
            año = lanzar_inputs("año")

            nuevo_libro = datos_libro(titulo, autor, año)
            agregar_libro(biblioteca, nuevo_libro)

        elif (opcion == "2"):
            mostrar_libros(biblioteca)

        elif (opcion == "3"):
            autor_buscar = lanzar_inputs("buscar")
            buscar_libros_por_autor(biblioteca, autor_buscar)

        elif (opcion == "4"):
            titulo_borrar = lanzar_inputs("borrar")
            borrar_libro_por_titulo(biblioteca, titulo_borrar)

        elif (opcion == "5"):
            print("Saliendo del programa. ¡Hasta luego!")
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