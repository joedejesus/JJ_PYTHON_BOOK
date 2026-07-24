# Lista_de_la_jerarquia_de_los_operadores.py

# Código:
lista_de_la_jerarquia_de_los_operadores = [

    "1º:",   # Paréntesis (). "Mayor precedencia".
    "2º:",   # Operadores de indexación y segmentación ([], [:]). "Misma precedencia".
    "3º:",   # Exponenciación (**). "Precedencia específica".
    "4º:",   # Operadores unarios (+, -, ~). "Misma precedencia".
    "5º:",   # Operadores aritméticos (*, /, //, %, +, -). "Precedencia específica".
    "6º:",   # Desplazamientos de bits (<<, >>). "Misma precedencia".
    "7º:",   # Operadores a nivel de bits (&, ^, |). "Precedencia específica".
    "8º:",   # Operadores de comparación (==, !=, >, <, >=, <=). "Misma precedencia".
    "9º:",   # Operadores de pertenencia (in, not in) e identidad (is, is not). "Misma precedencia".
    "10º:",  # Operadores lógicos (not, and, or). "Precedencia específica".
    "11º:",  # Operadores de asignación (=, +=, -=, *=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=). "Misma precedencia".
]

# Nota Muy Importante:
"""Esta lista muestra la jerarquía de los operadores en Python, ordenados de mayor a menor precedencia.

Dentro de cada categoría, los operadores pueden tener:
- Precedencia específica: El orden de evaluación está definido explícitamente.
- Misma precedencia: El orden de evaluación depende de la regla de asociatividad.

Reglas importantes:
1. Precedencia específica dentro de una categoría:
   - Los operadores se evalúan en el orden indicado en la lista, de mayor a menor precedencia.
   - Ejemplo: En los operadores aritméticos, la multiplicación (*) tiene mayor precedencia que la suma (+).

2. Asociatividad para operadores con la misma precedencia
   - Determina el orden de evaluación dentro de una categoría.
   - Solo se aplica a operadores con la misma precedencia.
   - Puede ser de izquierda a derecha o de derecha a izquierda.
   - Ejemplos:
     - La exponenciación (**) se evalúa de derecha a izquierda.
     - La mayoría de los operadores aritméticos (+, -,  *,  /,  etc.) se evalúan de izquierda a derecha.

3. Combinación de operadores de diferentes categorías:
   - Se respeta el orden jerárquico establecido en la lista.
   - Si el orden no es claro o puede generar ambigüedades, se recomienda usar paréntesis explícitos.
     

4. Uso de paréntesis ():
   - Tienen la mayor precedencia y se utilizan para agrupar expresiones.
   - Permiten alterar tanto el orden de precedencia como el de evaluación.

Diferencia entre precedencia y evaluación:
- Orden de precedencia: Determina qué operador se evalúa primero según la jerarquía.
- Orden de evaluación: Determina en qué orden se evalúan los operandos y operadores.

El orden de evaluación no siempre coincide con el  orden  de  precedencia,  ya  que  depende  de  la
jerarquía, la asociatividad y el uso de paréntesis. Por lo tanto, para garantizar el  comportamiento
deseado, es recomendable usar paréntesis explícitos."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
