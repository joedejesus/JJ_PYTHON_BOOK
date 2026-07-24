# Enunciado:
"""Define una función llamada "saludar()" que reciba un parámetro llamado "persona".  Dentro  de  la
función, utiliza la instrucción "print()" para mostrar  un  mensaje  en  formato  "f-string"  en  la
consola al llamarla. Elmensaje debe incluir el valor del parámetro, el cual será sustituido  por  el
argumento pasado al llamar a la función.

Por último, llama a la función con tu propio nombre como argumento para personalizar el  mensaje  de
saludo que se imprimirá en la consola."""

# Ejercicio_declarar_y_llamar_funciones.py

# Explicación:
"""Definimos una función llamada  "saludar()"  que  recibe  un  parámetro  llamado  "persona".  Este
parámetro se utilizará para personalizar el mensaje de saludo que se imprimirá en la consola y  será
sustituido por el valor que se pase a la función al llamarla. Para ello, utilizamos la palabra clave
"def", seguida del nombre de la función, en este  caso  "saludar()",  y  del  nombre  del  parámetro
"persona" entre paréntesis. Terminamos con dos puntos (:) para  indicar  el  inicio  del  bloque  de
código asociado a la función.

Dentro de la función, utilizamos la instrucción "print()" para mostrar un mensaje en la  consola  en
formato "f-string", el cual incluye el parámetro "persona" dentro  del  saludo.  El  valor  de  este
parámetro será sustituido por el argumento pasado al llamar a la función, el cual  será  de  nuestra
elección. Colocamos esta instrucción  con  una  indentación  de  cuatro  espacios  desde  el  margen
izquierdo para indicar que forma parte del cuerpo de la función y debe  ejecutarse  siempre  que  la
función sea llamada.

Por último, llamamos a la función "saludar()" con el argumento correspondiente, en este caso nuestro
nombre "Joe", para ejecutar el código asociado dentro de ella. Para llamar a la función, simplemente
escribimos su  nombre  seguido  de  paréntesis  con  el  argumento  correspondiente,  en  este  caso
"saludar("Joe")". Escribimos el argumento entre comillas dobles para indicar que  se  trata  de  una
cadena de texto (str) y, de esta forma, hacer que los tipos de datos sean compatibles. Esta  llamada
indica al intérprete que debe ejecutar el bloque de código asociado a la función, mostrando  así  el
mensaje de saludo con nuestro nombre en la consola gracias a la instrucción "print()".

Repetimos el proceso de llamada dos veces más para  ilustrar  que  la  función  puede  llamarse  con
diferentes argumentos tantas veces como sea necesario y generar  saludos  personalizados  para  cada
caso sin necesidad de  redefinir  la  función.  Colocamos  todas  las  llamadas  a  la  función  sin
indentación, ya que se encuentran en el nivel principal del código y no forman parte de ninguna otra
estructura."""

# Código:
def saludar(persona):
    print(f"¡Hola, {persona}! ¡Bienvenido/a!")

saludar("Joe")
saludar("Ana")
saludar("Luis")

# Nota Muy Importante:
"""Es fundamental que el tipo de dato del argumento pasado al llamar a la función  coincida  con  el
tipo de dato esperado por el parámetro definido en la función. En este caso, el parámetro  "persona"
está diseñado para recibir cadenas de texto (strings), por lo que  los  argumentos  "Joe",  "Ana"  y
"Luis" son apropiados. Si se intenta pasar un tipo de dato diferente, como un número  entero  o  una
lista, se producirá un resultado no deseado o un error. Por ello, es esencial asegurarse de que  los
tipos de datos sean compatibles para evitar problemas durante la ejecución del código.

Además, es importante recordar que Python es un lenguaje de tipado dinámico, lo que significa que no
se especifica el tipo de dato de los parámetros al definir la función, pero  el  tipo  de  dato  del
argumento pasado debe ser coherente con el uso que se le dará dentro de la función.

Si la función requiere un parámetro,  es  obligatorio  pasarle  un  argumento  al  llamarla.  De  lo
contrario, se generará un error de tipo "TypeError", indicando que la función requiere un argumento.
En situaciones en las que no se disponga de un valor válido para pasar como argumento, se puede usar
el valor nulo "None" como una alternativa temporal. Esto  permite  que  el  código  se  ejecute  sin
interrupciones, aunque es importante manejar adecuadamente este  caso  dentro  de  la  función  para
evitar errores adicionales.

Por ejemplo, se puede incluir una validación dentro de la función para verificar  si  el  valor  del
parámetro es "None" y actuar en consecuencia. Esto se logra mediante estructuras condicionales  como
"if", que permiten evaluar el valor del parámetro y ejecutar un bloque de código alternativo en caso
de que sea necesario.

Los argumentos deben pasarse en el mismo orden en que los parámetros fueron definidos en la función,
ya que Python asigna los valores de los argumentos a los parámetros en función de su  posición.  Sin
embargo,  también  es  posible  usar  argumentos  nombrados  (keyword  arguments)  para  especificar
explícitamente qué valor corresponde a cada parámetro, lo  que  permite  alterar  el  orden  de  los
argumentos al llamar a la función. Esto puede ser útil para mejorar  la  legibilidad  del  código  o
cuando se trabaja con funciones que tienen muchos parámetros. Los argumentos nombrados  también  son
útiles para evitar errores relacionados con el orden de los argumentos, especialmente  en  funciones
con parámetros opcionales o predeterminados.

Es muy importante respetar la sintaxis al pasar argumentos a una función. Por ejemplo,  las  cadenas
de texto (str) deben estar entre comillas simples o dobles, mientras que los números enteros (int) o
flotantes (float) no deben llevar comillas. Asimismo, al definir  los  parámetros  de  una  función,
estos deben estar separados por comas si hay más de uno y deben escribirse dentro de los  paréntesis
que siguen al nombre de la función. Es una buena práctica usar nombres descriptivos y en minúsculas,
separados por guiones bajos si es necesario, siguiendo las convenciones de estilo de Python (PEP 8).
Esto facilita la comprensión del código  y  reduce  la  probabilidad  de  errores  al  trabajar  con
funciones más complejas.

Por último, es útil saber que es posible usar variables como argumentos al  llamar  a  una  función,
siempre y cuando dichas variables hayan sido definidas previamente en el código y contengan un valor
del tipo de dato esperado. Esto permite reutilizar valores ya definidos y hace que el código sea más
dinámico y flexible. Además, estas variables pueden contener cualquier valor válido en Python,  como
cadenas, números, listas o diccionarios, entre otros, siempre que sean compatibles con el uso que se
les dará dentro de la función. Esto hace que las funciones sean  herramientas  muy  versátiles  para
estructurar y reutilizar código en diferentes contextos.

También es importante considerar que las variables utilizadas como argumentos no  se  ven  afectadas
por los cambios realizados dentro de la función, a menos que se  trate  de  objetos  mutables,  como
listas o diccionarios, en cuyo caso los cambios realizados dentro de la  función  pueden  reflejarse
fuera de ella. Esto se debe al comportamiento de paso por referencia compartida en  Python,  que  es
importante comprender para evitar resultados inesperados al trabajar con funciones."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
