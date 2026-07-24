# Enunciado:
"""Escribe un programa  que  gestione  tareas  almacenadas  en  un  diccionario,  donde  cada  clave
represente una tarea y cada valor sea otro diccionario anidado con sus detalles.  El  programa  debe
permitir agregar tareas, mostrar la lista completa, completarlas, modificarlas y eliminar una  tarea
específica de forma interactiva. Además, se debe utilizar la biblioteca  "json"  para  formatear  la
salida de las tareas de manera legible."""

# Examen_a_diccionarios.py

# Importar la biblioteca "json" para formatear la salida de las tareas.
import json

# Diccionario general de tareas.
diccionario_general = {
    "comprar": {
        "descripcion": "Hacer la compra",
        "estado": "Pendiente",
        "fecha limite": "2027-10-01"
    },
    "estudiar": {
        "descripcion": "Estudiar Python",
        "estado": "Pendiente",
        "fecha limite": "2027-10-02"
    },
    "limpiar": {
        "descripcion": "Limpiar la casa",
        "estado": "Pendiente",
        "fecha limite": "2027-10-03"
    },
}

# Entradas según el diccionario de mensajes.
def lanzar_imputs(mensaje):
    lanzar = {
        1: "Escribe el nombre de la tarea: ",
        2: "Escribe la descripción de la tarea: ",
        3: "Escribe el estado de la tarea (Pendiente/Completada): ",
        4: "Escribe la fecha límite de la tarea (YYYY-MM-DD): ",
    }
    return input(lanzar.get(mensaje, "El input no es válido"))

# Agrega una tarea.
def agregar_tarea(diccionario_general, clave, descripcion, estado, fecha_limite):
    diccionario_general[clave] = {
        "descripcion": descripcion,
        "estado": estado,
        "fecha limite": fecha_limite
    }
    print(f"Tarea '{clave}' agregada con éxito.")

# Muestra las tareas.
def mostrar_tareas(diccionario_general):
    if (diccionario_general):
        for c, v in diccionario_general.items():
            print(json.dumps({c: v}, indent=4))
    else:
        print("No hay tareas disponibles.")

# Completa una tarea.
def completar_tarea(diccionario_general, clave):
    if (clave in diccionario_general):
        diccionario_general[clave]["estado"] = "Completada"
        print(f"Tarea '{clave}' marcada como completada.")
    else:
        print(f"Tarea '{clave}' no encontrada.")

# Modifica una tarea.
def modificar_tarea(diccionario_general, clave, descripcion, estado, fecha_limite):
    if (clave in diccionario_general):
        diccionario_general[clave]["descripcion"] = descripcion
        diccionario_general[clave]["estado"] = estado
        diccionario_general[clave]["fecha limite"] = fecha_limite
        print(f"Tarea '{clave}' modificada con éxito.")
    else:
        print(f"Tarea '{clave}' no encontrada.")

# Elimina una tarea.
def eliminar_una_tarea_especifica(diccionario_general, clave):
    if (clave in diccionario_general):
        del diccionario_general[clave]
        print(f"Tarea '{clave}' eliminada con éxito.")
    else:
        print("No hay tareas para eliminar.")

# Función principal.
def main():
    diccionario = diccionario_general

    while True:
        print("\nGestión de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Modificar tarea")
        print("5. Eliminar una tarea específica")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if (opcion == "1"):
            v_clave = lanzar_imputs(1)
            v_descripcion = lanzar_imputs(2)
            v_estado = lanzar_imputs(3)
            v_fecha_limite = lanzar_imputs(4)
            agregar_tarea(diccionario, v_clave, v_descripcion, v_estado, v_fecha_limite)

        elif (opcion == "2"):
            mostrar_tareas(diccionario)

        elif (opcion == "3"):
            for c in diccionario.keys():
                print(c)
            v_clave = lanzar_imputs(1)
            completar_tarea(diccionario, v_clave)

        elif (opcion == "4"):
            for c in diccionario.keys():
                print(c)
            v_clave = lanzar_imputs(1)
            v_descripcion = lanzar_imputs(2)
            v_estado = lanzar_imputs(3)
            v_fecha_limite = lanzar_imputs(4)
            modificar_tarea(diccionario, v_clave, v_descripcion, v_estado, v_fecha_limite)

        elif (opcion == "5"):
            for c in diccionario.keys():
                print(c)
            v_clave = lanzar_imputs(1)
            eliminar_una_tarea_especifica(diccionario, v_clave)

        elif (opcion == "6"):
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

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