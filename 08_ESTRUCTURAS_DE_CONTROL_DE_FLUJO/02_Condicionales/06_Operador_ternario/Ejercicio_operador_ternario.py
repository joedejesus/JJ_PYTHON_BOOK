# Enunciado:
"""Desarrolla un programa para calcular el precio final de una entrada de cine según el precio base,
el descuento aplicado y la edad del comprador. Primero, muestra un mensaje coherente  de  bienvenida
al usuario. Luego, define una variable llamada "precio_base" y asígnale el  precio  estándar  de  la
entrada, que es 100€.

Utiliza la función "input()" para solicitar al usuario su edad y asigna el  valor  ingresado  a  una
variable llamada "opcion_usuario". El contenido dentro de la función "input()" debe ser  un  mensaje
formateado con una "f-string" que incluya el precio base de la entrada  almacenado  en  la  variable
"precio_base". Además, convierte la entrada al tipo  de  dato  adecuado  utilizando  el  constructor
correspondiente. La entrada del usuario debe estar definida en la posición correcta del código.

Luego, utiliza el operador ternario para aplicar un descuento del 20% si  la  persona  es  mayor  de
edad, es decir (18 años o más) y un descuento del 50% si la persona es  menor  de  edad.  Guarda  el
resultado en una nueva variable llamada "precio_final". Para realizar el cálculo, ten en  cuenta  la
siguiente fórmula: precio_final = precio_base * (1 - (descuento)).

A continuación, calcula el porcentaje de descuento aplicado  y  guárdalo  en  una  variable  llamada
"descuento". Para ello, utiliza una operación aritmética que reste el precio final al precio base  y
exprese el resultado en porcentaje. La fórmula para el porcentaje es: porcentaje = (x *  100  /  z),
donde "x" es la parte y "z" es el todo.

Por último, muestra al usuario el porcentaje de descuento aplicado y el precio final de  la  entrada
utilizando una "f-string" para formatear la salida. Además, haz que el programa imprima  un  mensaje
de despedida al usuario."""

# Ejercicio_operador_ternario.py

# Explicación:
"""Mostramos un mensaje de bienvenida al usuario utilizando la función "print()".  Luego,  definimos
una variable llamada "precio_base" y le asignamos el precio estándar de la entrada, que es 100.

Utilizamos la función "input()" para solicitar al usuario que ingrese su edad. Para ello,  definimos
una variable llamada "opcion_usuario", escribimos la palabra clave "input" seguida de paréntesis (),
y dentro de estos incluimos un mensaje que contiene la información que se espera del usuario, además
del precio base de la entrada almacenado en la variable "precio_base". Colocamos la letra "f"  antes
de las comillas para indicar que es una "f-string".

Como la función "input()" devuelve un valor de tipo string (str), utilizamos el constructor  "int()"
para convertir esa entrada en un número entero,  encerrando  la  función  "input()"  dentro  de  los
paréntesis del constructor "int()", el cual colocamos justo antes de la función "input()".  De  esta
forma, obtenemos un valor de tipo entero  (int)  almacenado  en  la  variable  "opcion_usuario"  que
podremos utilizar en el operador ternario para calcular el descuento según la edad  introducida  por
el usuario. Además, colocamos la entrada del usuario en  la  posición  correcta  del  código,  justo
después de definir la variable "precio_base" y antes de utilizar el operador ternario para  calcular
el precio final con el descuento aplicado.

Luego, utilizamos el operador ternario para aplicar un descuento del 20% si la persona es  mayor  de
edad y del 50% si es menor de edad. Para ello, definimos una variable llamada "precio_final" seguida
de la expresión entre paréntesis (), que consta de la variable  "precio_base"  multiplicada  por  
(1 menos el operador ternario).

El operador ternario se compone de: el valor que se devuelve si la condición es verdadera (0.2),  el
condicional "if", la condición (opcion_usuario >= 18), el condicional "else" y, por último, el valor
a devolver si la condición es falsa (0.5). Encerramos el operador ternario entre paréntesis ()  para
asegurarnos de que se evalúe correctamente dentro de la  expresión  y  separarlo  del  resto  de  la  
expresión.

El valor devuelto por el operador ternario (0.2 o 0.5), el cual depende del valor introducido por el
usuario y almacenado en la variable "opcion_usuario", se resta a "1" y el  resultado  se  multiplica
por el precio base "100", produciendo el resultado del precio final con el  descuento  aplicado,  el
cual se almacena en la variable "precio_final". De esta forma, aplicamos la fórmula: precio_final  =
precio_base * (1 - (descuento)), siendo el descuento el operador ternario.

A continuación, calculamos el porcentaje de descuento aplicado. Para ello utilizamos  una  expresión
aritmética asignada a  la  variable  "descuento",  que  se  compone  de:  la  parte  (precio_base  -
precio_final), multiplicada por "100" y  dividida  entre  el  todo  (precio_base).  De  esta  forma,
obtenemos el porcentaje de descuento aplicado al precio base utilizando la fórmula porcentaje = (x *
100 / z), donde "x" es la parte (precio_base  -  precio_final)  y  "z"  es  el  todo  (precio_base).
Utilizamos paréntesis para separar debidamente las diferentes partes de la expresión  y  asegurarnos
de que se evalúe correctamente.

Por último, utilizamos una "f-string" para mostrar al usuario el porcentaje de descuento aplicado  y
el precio final de la entrada. Para ello, utilizamos la función "print()" seguida de paréntesis  (),
dentro de los cuales incluimos una "f-string" que contiene  el  mensaje  a  mostrar.  Dentro  de  la
"f-string", utilizamos llaves {} para insertar las variables  "descuento"  y  "precio_final"  en  el
mensaje, mostrando así el porcentaje de descuento aplicado y el precio final de la entrada.  Además,
hacemos que el programa imprima un mensaje de despedida al usuario. Para ello, utilizamos nuevamente
la función "print()" que contiene el mensaje a mostrar."""

# Código:
print("¡Bienvenido al sistema de venta de entradas de cine!")

precio_base = 100

opcion_usuario = int(input(f"El precio de la entrada es: {precio_base} €. Ingresa tu edad para calcular el precio final: "))

precio_final = precio_base * (1 - (0.2 if opcion_usuario >= 18 else 0.5))
descuento = ((precio_base - precio_final) * 100 / precio_base)

print(f"Has recibido un descuento del {descuento}%. El precio final de la entrada es: {precio_final} €.")
print("¡Gracias por tu compra! ¡Disfruta de la película!")

# Nota Importante:
"""En el contexto del operador  ternario,  cuando  vemos  varios  operadores  ternarios  anidados  o
encadenados es señal del uso de este operador de forma anidada. En  este  caso,  los  paréntesis  se
utilizan para agrupar y separar las diferentes partes de la expresión,  asegurando  que  se  evalúen
correctamente y manteniendo la claridad del código, por lo que en  este  caso  no  se  trata  de  un
operador ternario anidado, algo que se debe evitar para no complicar la lectura del código.

Los valores "0.2" y "0.5" representan el porcentaje de  descuento  en  forma  decimal  (20%  y  50%,
respectivamente). Al restar estos valores de 1 (que representa el 100% del precio),  se  obtiene  la
fracción del precio que el cliente debe pagar después de  aplicar  el  descuento.  Este  cálculo  se
realiza de manera eficiente y compacta gracias al uso del operador ternario, lo que permite mantener
el código limpio y legible.

Para el porcentaje, se utiliza la fórmula:  descuento  =  ((precio_base  -  precio_final)  *  100  /
precio_base). Esta fórmula toma la diferencia entre el precio base y el precio final,  la  convierte
en un porcentaje  y  la  almacena  en  la  variable  "descuento".  Este  cálculo  es  esencial  para
proporcionar al usuario información clara sobre el ahorro obtenido en su compra.

Por último, el operador ternario en Python es una  forma  concisa  y  legible  de  tomar  decisiones
simples en una sola línea de código. Sin embargo, para  condiciones  más  complejas,  se  recomienda
utilizar estructuras condicionales tradicionales "if...elif...else" para mantener la claridad  y  la
legibilidad del código. En este caso, el operador ternario es ideal debido a la  simplicidad  de  la
lógica involucrada."""

# ════════════════════════════════════════════════════════════
#  Código corregido, revisado y optimizado por el autor.
#  Autor: Joe De Jesús Fernández Diniz.
# ────────────────────────────────────────────────────────────
