# Enunciado:
"""La verificación de tipos de datos en Python es el proceso que permite comprobar el tipo  de  dato
almacenado en una variable. Esto es especialmente  útil  al  trabajar  con  datos  dinámicos  o  con
entradas externas. Garantiza que los datos sean  del  tipo  correcto  para  ejecutar  una  operación
específica, evitando errores que pueden surgir al aplicar métodos o funciones inadecuadas.

Dado que Python es un lenguaje de tipado dinámico, no siempre  es  evidente  el  tipo  de  dato  que
contiene una variable. Por ello, conocer su tipo es clave para mantener la fiabilidad del  código  y
facilitar su mantenimiento.

Para realizar esta verificación, usamos la función "type()", que recibe la variable como parámetro y
devuelve su tipo, por ejemplo "<class 'str'>", en forma de un objeto de la clase "type".  Incorporar
estas comprobaciones en el flujo de trabajo permite detectar inconsistencias  de  forma  temprana  y
mejora la robustez del código."""

# Ejemplo_verificacion_de_tipos_de_datos_basicos.py

# Explicación:
"""Definimos una variable llamada "texto" y le  asignamos  el  valor  "Hola".  Luego,  aplicamos  la
función "type()" a la variable para verificar el tipo de dato que contiene y guardamos el  resultado
en la variable "tipo_de_dato". Finalmente, imprimimos el resultado de la verificación utilizando  la
función "print()". El resultado será <class 'str'>."""

# Código:
texto = "Hola"
tipo_de_dato = type(texto)  # Aplicamos la función "type()" a la variable.
print(tipo_de_dato)         # Muestra <class 'str'>.

# Explicación:
"""Verificamos el tipo de dato  en  una  sola  línea.  Para  ello,  aplicamos  la  función  "type()"
directamente a la variable que queremos verificar, encerrando  la  llamada  a  la  función  "type()"
dentro de la función "print()". Finalmente, imprimimos el resultado. Esto permite verificar el  tipo
de dato sin necesidad de almacenarlo en una variable adicional."""

# Código:
print(type(texto))  # Muestra <class 'str'>.

# Nota Muy Importante:
"""La verificación del tipo de dato se puede realizar en una sola línea siempre que no sea necesario
almacenar el resultado en una  variable  adicional.  Si  se  requiere  almacenar  el  resultado,  es
recomendable usar una variable para guardar el tipo de dato, como se hizo en el primer ejemplo.

Aunque aquí hablamos de "tipo de dato", al usar la función "type()" obtenemos la "clase"  a  la  que
pertenece el objeto. De ahí la salida <class 'str'>. En Python, las clases son una forma de  definir
tipos de datos personalizados. Por lo tanto, los términos "tipo de dato" y "clase" se usan de manera
intercambiable en este contexto. Explicamos las clases con detalle en la  sección  de  "Programación
Orientada a Objetos"."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
