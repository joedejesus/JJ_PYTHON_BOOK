# Enunciado:
"""Este "script" muestra cómo analizar y manipular un diccionario extenso, anidado y desconocido. El
estudiante debe realizar las siguientes tareas:

1. Explorar la estructura del diccionario imprimiendo las claves y los tipos de valores.
2. Extraer subconjuntos anidados utilizando el método ".get()" y mostrarlos en un formato legible.
3. Agregar nuevos pares "clave-valor" utilizando el método ".update()".
4. Modificar valores existentes, incluidas claves anidadas y elementos dentro de listas anidadas.

Además, el estudiante debe imaginar que no tiene acceso visual al diccionario y que debe  analizarlo
y manipularlo únicamente a través de código. De esta  forma,  podremos  simular  cómo  trabajar  con
estructuras complejas contenidas en variables  sin  acceso  visual  a  ellas,  mediante  el  uso  de
operaciones de manipulación de diccionarios y listas anidadas."""

# Examen_b_diccionarios.py

# Importar el módulo "json" para mostrar los diccionarios de forma legible.
import json

# Diccionario principal.
citroen_c15 = {
    "fabricante": "Citroen",
    "modelo": "C15",
    "año": 1995,
    "estilo_carrocería": "Furgoneta",
    "tipo_de_conduccion": "Diésel",
    "autonomía": "Depósito de 55 litros con autonomía aproximada de 730 a 800 km, según carga y consumo",
    "aceleración": "0-100 km/h en aproximadamente 18 segundos",
    "velocidad_máxima": "135 km/h",
    "capacidad_batería": "Batería de 12 V para arranque y sistemas eléctricos básicos",
    "tiempo_de_carga": "No aplica; repostaje en pocos minutos",
    "interior": {
        "capacidad_asientos": 2,
        "pantalla": "Panel de instrumentos analógico sin pantalla central",
        "sistema_de_sonido": "Radio básica con dos altavoces",
        "control_de_clima": "Ventilación y calefacción manual",
        "conectividad": "Sin conectividad integrada",
    },
    "características_de_seguridad": [
        "Frenos delanteros de disco",
        "Cinturones de seguridad delanteros",
        "Retrovisores exteriores",
        "Luces antiniebla traseras",
        "Puertas traseras con cierre mecánico",
        "Estructura reforzada para carga ligera",
        "Sin airbags de serie"
    ],
    "precio": {
        "inicial": "$4,500",
        "variacion": True
    }
}

# Mostrar las claves y los tipos de los valores.
def ver_tipos_de_valores(diccionario):
    for clave, valor in diccionario.items():
        print(f"Clave: {clave}, Tipo de valor: {type(valor)}")

# Llamar a la función para mostrar las claves y los tipos de valores del diccionario.
ver_tipos_de_valores(citroen_c15)

# Extraer subconjuntos anidados.
def extraer_sub_conjuntos():
    interior = citroen_c15.get("interior")
    print("\nInterior:")
    print(json.dumps(interior, indent=2))

    seguridad = citroen_c15.get("características_de_seguridad")
    print("\nCaracterísticas de seguridad:")
    print(json.dumps(seguridad, indent=2))

    precio = citroen_c15.get("precio")
    print("\nPrecio:")
    print(json.dumps(precio, indent=2))
    return interior, seguridad, precio

# Llamar a la función para extraer y mostrar los subconjuntos.
extraer_sub_conjuntos()

# Modificar el diccionario anidado.
def modificar_interior(diccionario):
    diccionario["interior"].update({"pantalla": "Pantalla multimedia de 7 pulgadas instalada como mejora"})
    print("\nInterior modificado:")
    print(json.dumps(diccionario["interior"], indent=2))
    return diccionario["interior"]

# Llamar a la función para modificar el diccionario anidado.
modificar_interior(citroen_c15)

# Modificar la lista anidada.
def modificar_seguridad(diccionario):
    diccionario["características_de_seguridad"][6] = "Airbag del conductor instalado como mejora"
    print("\nCaracterísticas de seguridad modificadas:")
    print(json.dumps(diccionario["características_de_seguridad"], indent=2))
    return diccionario["características_de_seguridad"]

# Llamar a la función para modificar la lista anidada.
modificar_seguridad(citroen_c15)

# Modificar el diccionario de precios.
def modificar_precio(diccionario):
    diccionario["precio"].update({"inicial": "$4,800"})
    print("\nPrecio modificado:")
    print(json.dumps(diccionario["precio"], indent=2))
    return diccionario["precio"]

# Llamar a la función para modificar el diccionario de precios.
modificar_precio(citroen_c15)

# Nota Importante:
"""Este examen requiere que el estudiante consulte la biblioteca de Python para comprender y aplicar
correctamente los conceptos necesarios. No puede resolverse únicamente con lo visto en el  tema;  es
necesario investigar, analizar y relacionar información para completar el ejercicio."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────