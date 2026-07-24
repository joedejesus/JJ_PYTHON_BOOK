# Enunciado:
"""Crea un programa que asigne el valor 10 a la variable "x"; luego, multiplique "x" por 5, reste  3
a "x", divida "x" entre 2, calcule el residuo de la división de "x" entre 4, eleve  "x"  al  cubo  y
calcule la división entera de "x" entre 5. Utiliza los operadores de asignación y,  finalmente,  usa
la función "print()" para mostrar el resultado en la consola, concatenado con un mensaje descriptivo
para ilustrar la salida. El resultado debe ser el número 8.0."""

# Ejercicio_operadores_de_asignacion.py

# Explicación:
"""Definimos una variable llamada "x" y le asignamos el valor  10  con  el  operador  de  asignación
simple (=). A continuación, utilizamos varios operadores de asignación para realizar las  siguientes
operaciones matemáticas sobre "x":

Multiplicamos "x" por 5 (x *= 5). Restamos 3 a "x" (x -=  3).  Dividimos  "x"  entre  2  (x  /=  2).
Calculamos el residuo de la división de "x" entre 4 (x %= 4). Elevamos "x"  al  cubo  (x  **=  3)  y
calculamos la división entera de "x" entre 5 (x //= 5).

Finalmente, usamos la función "print()" para mostrar el resultado final tras realizar las  múltiples
operaciones sobre la variable "x".  Acompañamos  el  resultado  con  un  mensaje  descriptivo.  Cada
operador de asignación realiza  una  operación  y  actualiza  el  valor  de  "x"  con  el  resultado
obtenido."""

# Código:
x = 10   # Asignamos el valor 10 a la variable "x".
x *= 5   # Resultado parcial: 50
x -= 3   # Resultado parcial: 47
x /= 2   # Resultado parcial: 23.5
x %= 4   # Resultado parcial: 3.5
x **= 3  # Resultado parcial: 42.875
x //= 5  # Resultado final: 8.0

print("El resultado de toda la operación es =", x)

# Nota Importante:
"""Es importante saber que con cada asignación se almacena el nuevo resultado en la variable. Por lo
tanto, no es necesario crear una nueva variable para almacenar el resultado de  cada  operación.  En
este caso, la variable "x" se actualiza con el resultado de cada operación. Al final  del  programa,
"x" contiene el resultado final después de realizar todas las operaciones.

Cabe destacar que el resultado anterior se pierde con cada actualización, por lo que hay que tenerlo
presente, ya que no se puede acceder a  los  resultados  intermedios  una  vez  que  se  realiza  la
siguiente operación. Esto demuestra cómo es posible cambiar el valor de una variable  en  tiempo  de
ejecución."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
