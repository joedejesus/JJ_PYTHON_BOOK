# Enunciado:
"""Crea un diccionario complejo donde cada clave principal sea el nombre de una persona y  su  valor
sea otro diccionario que contenga la edad, la ciudad de residencia y el país de  cada  persona  como
claves internas. Asigna valores representativos  a  esas  claves.  Finalmente,  utiliza  la  función
"print()" para mostrar el diccionario en la consola."""

# Ejercicio_diccionarios_dict.py

# Explicación:
"""Definimos una  variable  llamada  "diccionario"  que  contiene  tres  diccionarios  anidados  con
información de varias personas. Cada clave del diccionario principal es el nombre de una  persona  y
su valor es otro diccionario {} que contiene la edad, la ciudad y  el  país  de  residencia  de  esa
persona como claves internas, con sus valores correspondientes.

Esto se logra asignando un diccionario {} como valor a  cada  una  de  las  claves  del  diccionario
principal, usando dos puntos (:). Los diccionarios internos se encierran entre llaves y  se  separan
entre sí por comas. Cada par clave-valor dentro de ellos se separa  por  comas  del  siguiente  par,
utilizando dos puntos (:) entre la clave y su valor.

Cada  clave  interna  representa  un  atributo  (edad,  ciudad,  país)  y  su  valor  es   el   dato
correspondiente. En  todo  momento  se  sigue  la  sintaxis  adecuada  para  cada  par  clave-valor,
dependiendo del tipo de dato del valor. Finalmente, imprimimos el valor de la variable "diccionario"
usando la función "print()" para mostrar el contenido del diccionario complejo en la consola."""

# Código:
diccionario = {
    "joe": {
        "edad": 33,
        "ciudad": "Asturias",
        "pais": "España"
    },
    "oscar": {
        "edad": 30,
        "ciudad": "Barcelona",
        "pais": "España"
    },
    "manuel": {
        "edad": 35,
        "ciudad": "Valencia",
        "pais": "España"
    },
}
print(diccionario)

# Nota Muy Importante:
"""Recuerda la sintaxis correcta de los diccionarios y presta atención a las comas que separan  cada
diccionario interno, ya que estos corresponden  a  un  "valor"  del  diccionario  principal.  Separa
correctamente cada par clave-valor dentro de ellos con comas. Recuerda que para las claves externas,
así como para el cierre del diccionario anidado, se utiliza una tabulación desde el margen izquierdo
como separación. Para las claves internas, se utiliza una tabulación como separación desde el margen
donde empieza la clave externa."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
