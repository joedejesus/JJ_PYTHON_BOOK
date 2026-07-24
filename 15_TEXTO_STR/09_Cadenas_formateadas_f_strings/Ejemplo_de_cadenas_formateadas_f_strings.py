# Enunciado:
"""Las cadenas formateadas, también conocidas  como  "f-strings"  en  Python,  son  una  herramienta
poderosa y flexible para  crear  cadenas  de  texto  dinámicas.  Introducidas  en  Python  3.6,  las
"f-strings" permiten incluir expresiones de  Python  directamente  dentro  de  una  cadena,  lo  que
facilita la interpolación de variables y la evaluación de expresiones en tiempo de ejecución.

La sintaxis de las "f-strings" es la siguiente:  (f"texto  {expresion}  texto").  Donde  "texto"  es
cualquier texto que se desee incluir en la cadena y "expresion" es  cualquier  expresión  válida  en
Python que se quiera evaluar e incluir en la cadena.  El  conjunto  del  texto  y  las  expresiones,
después de la letra "f", debe estar  entre  comillas,  ya  sean  simples  ('  ')  o  dobles  ("  "),
dependiendo de las necesidades del texto. En cuanto a las expresiones, estas deben estar  encerradas
entre llaves {} para indicar que se trata de una expresión que será evaluada e incluida en la cadena
formateada.

Si estas cadenas formateadas se asignan  a  una  variable,  es  recomendable  usar  paréntesis  para
encerrar la cadena completa, lo que ayuda a mejorar la legibilidad del código. Esto es especialmente
útil cuando la cadena es larga o contiene múltiples expresiones.  Si  se  utilizan  con  la  función
"print()", no es necesario usar paréntesis adicionales a los de la función para encerrar la  cadena,
aunque también pueden usarse.

Las expresiones encerradas entre llaves {} se evalúan en tiempo  de  ejecución  y  su  resultado  se
convierte en una cadena que se inserta en la posición correspondiente dentro de la "f-string". Estas
expresiones  pueden  ser  variables,  operaciones  matemáticas,  llamadas  a  funciones  o   incluso
expresiones más complejas, lo que las hace extremadamente versátiles y útiles en una amplia variedad
de contextos.

Además, las "f-strings" admiten especificadores de formato que permiten controlar cómo se  presentan
los datos, como el número de decimales en un número flotante o el relleno de espacios en una cadena.
Estos especificadores se colocan después de la expresión dentro de las llaves {}, separados por  dos
puntos (:), y pueden utilizarse para formatear números, fechas, cadenas y otros tipos  de  datos  de
manera precisa y consistente. Esto las convierte en  una  herramienta  ideal  para  generar  salidas
formateadas de manera clara y profesional.

Por último, las "f-strings" se utilizan dentro de la función "print()" para mostrar  información  de
manera clara y concisa, pero también pueden utilizarse para construir  cadenas  formateadas  que  se
asignan a variables, se escriben en archivos o se envían a través de redes,  entre  otros  usos.  En
resumen, las "f-strings" son una herramienta esencial para cualquier programador de Python que desee
escribir código claro, eficiente y fácil de mantener."""

# Ejemplo_de_cadenas_formateadas_f_strings.py

# Explicación:
"""Definimos varias variables llamadas "base", "altura",  "nombre"  y  "valores",  y  les  asignamos
diferentes tipos de datos que representan la base y  la  altura  de  un  triángulo,  el  nombre  del
triángulo y una lista de valores numéricos, respectivamente. Luego, creamos tres mensajes utilizando
"f-strings" para mostrar el área del triángulo, el cuadrado de la suma de los valores y el  promedio
de los valores.

En el primer mensaje, calculamos el área del triángulo utilizando la fórmula "((base * altura) / 2)"
y formateamos el resultado para mostrar  solo  dos  decimales.  Para  ello,  utilizamos  el  formato
"f-string" con la expresión: (f"texto {nombre} texto {base} texto {altura} texto {(base * altura)  /
2:.2f}."). Donde "texto" es el texto que se  desea  mostrar,  "nombre"  se  refiere  al  nombre  del
triángulo, "base" y "altura" son las variables que contienen los valores correspondientes, (/) es el
operador de división, "2" es el número utilizado en la operación para calcular el área y  ":.2f"  es
el especificador de formato que indica que el resultado debe mostrarse con dos decimales.

En el segundo mensaje, calculamos el cuadrado de la  suma  de  los  valores  utilizando  la  función
"sum()" para obtener la suma de los elementos de la lista "valores" y luego elevamos  ese  resultado
al cuadrado utilizando el operador de potencia (**). Para ello, utilizamos el formato "f-string" con
la expresión: (f"texto {valores} texto {(sum(valores))**2}."). Donde "texto"  es  el  texto  que  se
desea mostrar, "valores" se refiere a la lista de valores numéricos, "sum(valores)"  es  la  función
que calcula la suma de los elementos de la lista "valores", (**) es  el  operador  de  potencia  que
indica que se debe elevar al cuadrado el resultado de la suma y 2 es la potencia a la que  se  eleva
dicho resultado.

En el tercer mensaje, calculamos el promedio de los  valores  utilizando  la  función  "sum()"  para
obtener la suma de los elementos de la lista "valores" y luego  dividimos  ese  resultado  entre  la
cantidad de elementos de la lista utilizando la función "len()". Para ello,  utilizamos  el  formato
"f-string" con la expresión: (f"texto {sum(valores) /  len(valores):.2f}.").  Donde  "texto"  es  el
texto que se desea mostrar, "sum(valores)" es la función que calcula la suma de los elementos de  la
lista "valores", (/) es el operador de  división,  "len(valores)"  es  la  función  que  obtiene  la
cantidad de elementos de la lista "valores" y ":.2f" es el especificador de formato que  indica  que
el resultado debe mostrarse con dos decimales.

En cada caso, usamos las llaves {} para incluir las  expresiones  que  se  evaluarán  en  tiempo  de
ejecución y se insertarán en la cadena formateada. Además, utilizamos paréntesis para encerrar  cada
"f-string" asignada a las variables con  el  fin  de  mejorar  la  legibilidad.  También  utilizamos
paréntesis en las operaciones matemáticas cuando es necesario, siguiendo las reglas matemáticas para
asegurar la correcta evaluación de las expresiones.

Por último, en cada caso utilizamos la función "print()" para mostrar el resultado  de  cada  cadena
formateada en la consola, acompañado de un mensaje descriptivo en formato  "f-string"  para  indicar
qué información se está mostrando. En todos los casos, incluimos el mensaje descriptivo dentro de la
función "print()" utilizando la sintaxis básica de las "f-strings" para mostrar dicho mensaje  junto
con el resultado de cada cadena formateada. Esto permite presentar la información de manera clara  y
organizada, facilitando su comprensión."""

# Código:
base = 5
altura = 10
nombre = "Triángulo"
valores = [1, 2, 3, 4, 5]

mensaje_1 = (f"El área del {nombre} con base {base} y altura {altura} es {(base * altura) / 2:.2f}.")
mensaje_2 = (f"El cuadrado de la suma de los valores {valores} es {(sum(valores))**2}.")
mensaje_3 = (f"El promedio de los valores es {sum(valores) / len(valores):.2f}.")

print(f"Este es el mensaje 1: {mensaje_1}")
print(f"Este es el mensaje 2: {mensaje_2}")
print(f"Este es el mensaje 3: {mensaje_3}")

# Nota Importante:
"""Es fundamental tener en cuenta que las "f-strings" solo están disponibles a partir de Python 3.6.
Si se intenta usar esta característica en versiones anteriores,  el  código  generará  un  error  de
sintaxis. Por lo tanto, es importante asegurarse de que el entorno de  desarrollo  esté  configurado
con una versión compatible de Python.

Otro aspecto relevante es que las "f-strings" evalúan las expresiones en tiempo de ejecución, lo que
significa que cualquier error en las expresiones dentro de las llaves {} se reflejará inmediatamente
al ejecutar el código. Esto puede ser útil para  depurar,  pero  también  requiere  precaución  para
evitar errores inesperados.

Además, es posible concatenar varias "f-strings" utilizando el operador (+) o simplemente  colocando
las cadenas formateadas una al lado de la otra, sin necesidad de usar comas (,), lo  que  puede  ser
útil para construir mensajes más complejos de manera clara y organizada.  En  este  caso,  se  puede
encerrar el conjunto de "f-strings" con un solo paréntesis.

Por último,  aunque  las  "f-strings"  son  muy  convenientes,  es  recomendable  no  abusar  de  su
flexibilidad incluyendo expresiones demasiado complejas dentro de las  llaves,  ya  que  esto  puede
dificultar la lectura y el mantenimiento del código. En su lugar, es preferible calcular los valores
complejos por separado, almacenar esos resultados en variables intermedias y luego incluirlos en  la
cadena formateada."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────